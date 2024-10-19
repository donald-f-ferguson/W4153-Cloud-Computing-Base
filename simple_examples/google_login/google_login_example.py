import json

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from starlette.config import Config
from starlette.requests import Request
from starlette.responses import JSONResponse, HTMLResponse
import requests
import os

# This is a "hack" to avoid setting environment variables.
# set_env.py is a python file in the local directory that has the
# secret information needed to call the API.
#
# DO NOT ADD THIS FILE TO GITHUB
#
# To see an example of the format, look at sample_set_env.py. You can use this
# example to create your own set_env.py
#
import set_env

from time import sleep

# Load environment variables from a .env file (containing GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET)
# from dotenv import load_dotenv
# load_dotenv("/Users/donald.ferguson/Dropbox/000/000-Columbia-Courses/W4153-Cloud-Computing-Base/simple_examples/.env")

# Initialize FastAPI app
app = FastAPI()

# Secret key for session management
# DFF Changed
# app.add_middleware(SessionMiddleware, secret_key=os.getenv('SECRET_KEY', 'your-secret-key'))

app.add_middleware(SessionMiddleware, secret_key=os.getenv('SECRET_KEY',
                                                           set_env.SECRET_KEY))

# OAuth configuration
# DFF also changed.
# TODO Move back to environment variables.
#
config = Config(environ={
    "GOOGLE_CLIENT_ID": set_env.GOOGLE_CLIENT_ID,
    "GOOGLE_CLIENT_SECRET": set_env.GOOGLE_CLIENT_SECRET
})
oauth = OAuth(config)


google = oauth.register(
    name='google',
    client_id=config.get('GOOGLE_CLIENT_ID'),
    client_secret=config.get('GOOGLE_CLIENT_SECRET'),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
    jwks_uri = "https://www.googleapis.com/oauth2/v3/certs"
)

profile_url = "https://www.googleapis.com/oauth2/v3/userinfo"


def get_response_html(profile):

    name = profile["name"]
    picture = profile["picture"]
    email = profile["email"]

    html = f"""
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Login Result</title>
        </head>
        <body>
        <h1>Login Success!</h1>
        Full name: {name}<br>
        Email: {email}<br>
        <br>
        <a href="{picture}">Profile Picture</a>
        </body>
    </html>
    """

    return html


def get_user_info(access_token):
    auth = "Bearer " + access_token
    headers = {"Authorization": auth}
    rsp = requests.get(profile_url, headers=headers)

    try:
        result = rsp.json()
    except Exception as e:
        print("get_user_info: Exception = ", e)
        result = None

    return result


@app.get('/')
def index():
    return {"message": "Welcome to the FastAPI Google OAuth example"}

@app.get('/login')
async def login(request: Request):
    # Redirect the user to Google's OAuth2 authorization URL
    redirect_uri = 'http://localhost:5001/auth/callback'  # The callback URL
    return await oauth.google.authorize_redirect(request, redirect_uri)

@app.get('/auth/callback')
async def auth(request: Request):
    # Get the token and user info after user authorization
    try:
        token = await oauth.google.authorize_access_token(request)
        access_token = token.get("access_token")

        # user = await oauth.google.parse_id_token(token)
        user = token.get('userinfo')
       # user2 = await oauth.google.parse_id_token(request, token)

        # Store user info in the session (you can store more details if needed)
        # request.session['user'] = dict(user)
        print("User = ", user)

        profile = get_user_info(access_token)
        print("Full profile = \n", json.dumps(profile, indent=2))

        result_html = get_response_html(profile)

        # return JSONResponse({"message": "Login successful", "user profile": profile})
        return HTMLResponse(result_html)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Authentication failed")

@app.get('/logout')
def logout(request: Request):
    # Clear session data
    request.session.clear()
    return RedirectResponse(url='/')

# Protected route for users
@app.get('/users')
async def get_users(request: Request):
    # Check if the user is logged in
    user = request.session.get('user')
    if not user:
        raise HTTPException(status_code=401, detail="You are not logged in")

    # Example response with a protected resource
    return {"message": "Welcome, you are authenticated!", "user": user}

# Run the application
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=5001)
