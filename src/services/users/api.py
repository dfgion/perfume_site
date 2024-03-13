from typing import Annotated

from fastapi import Depends, HTTPException, Request
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse, RedirectResponse

from authlib.integrations.starlette_client import OAuth, OAuthError

from dependencies import registrate, authenticate_user, create_access_token, create_refresh_token, refresh_jwt_token
from schemas import TokenData, RegistrateUser, RegistratedUser, FormData
from utils.settings import Config


auth_router = APIRouter(prefix='/api/v1', tags=['auth'])

google_oauth = OAuth()
google_oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id='221420112692-igbpfdsl6bsn04v35vr71c1l01bkpkfs.apps.googleusercontent.com',
    client_secret='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',
    client_kwargs={
        'scope': 'email openid profile',
    },
    authorize_state='Oe_Ef1Y38o1KSWM2R-s-Kg'
)

@auth_router.post("/auth/token", response_model=TokenData)
async def login_for_access_token(
    form_data: FormData
):
    user = await authenticate_user(form_data.login, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = Config.JWT_EXP_ACCESS
    access_token = create_access_token(
        data={
            "sub": user.login, 
            "scopes": ['me'], 
            },
        expires_delta=access_token_expires,
    )
    refresh_token_expires = Config.JWT_EXP_REFRESH
    refresh_token = await create_refresh_token(
        data={
                "sub": user.login, 
                "scopes": ['refresh'],
                },
        expires_delta=refresh_token_expires
        )
    return JSONResponse(status_code=201, 
                        content = {
                            'access_token': access_token, 
                            "refresh_token": refresh_token, 
                            "token_type": "bearer"
                        })
    
@auth_router.get('/auth/google/login')
async def google_auth_redirect(request: Request):
    url = request.url_for('google_auth_token')
    return await google_oauth.google.authorize_redirect(request, url)

@auth_router.route('/auth/google/token')
async def google_auth_token(request: Request):
    token = await google_oauth.google.authorize_access_token(request)
    user = token.get('userinfo')
    if user:
        request.session['user'] = dict(user)
    return RedirectResponse(url='/')

@auth_router.post("/registration", response_model=RegistratedUser)
async def registration(
    registrate_user: RegistrateUser
) -> RegistratedUser:
    response = await registrate(registrate_user.login, registrate_user.email, registrate_user.password)
    return response

@auth_router.post("/auth/refresh_token", 
                  response_model=TokenData, 
                  responses={
                      400: {'description': 'Bad request token'}, 
                      401: {'description': 'The access token expired'}, 
                      403: {'description': 'Not enough permissions'}
                      }
                  )
async def refresh_user_token(refresh_data: str):
    refresh_token: TokenData = await refresh_jwt_token(refresh_data)
    return JSONResponse(status_code=200, 
                        content= {
                            'access_token': refresh_token.access_token,
                            'refresh_token': refresh_token.refresh_token,
                            'token_type': refresh_token.token_type
                        })
    

    
    
    
    

