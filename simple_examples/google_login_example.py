from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from starlette.config import Config
from starlette.requests import Request
from starlette.responses import JSONResponse
import os
import set_env

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

'''
oauth.register(
    name='google',
    client_id=config.get('GOOGLE_CLIENT_ID'),
    client_secret=config.get('GOOGLE_CLIENT_SECRET'),
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://localhost:5001/auth',
    client_kwargs={'scope': 'openid profile email'}
)
'''

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

def get_user_info(access_token):


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
        # user = await oauth.google.parse_id_token(token)
        user = token.get('userinfo')
       # user2 = await oauth.google.parse_id_token(request, token)

        # Store user info in the session (you can store more details if needed)
        # request.session['user'] = dict(user)
        print("User = ", user)

        return JSONResponse({"message": "Login successful", "user": user})
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
