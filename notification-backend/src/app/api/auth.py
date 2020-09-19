from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi_jwt_auth import AuthJWT
from src.app.api import manager

# auth url for docs
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/obtain_token_for_docs")


def authentication_required(token: str = Depends(oauth2_scheme), Authorize: AuthJWT = Depends()):
    """
     - Validate user is authenticate
    """
    Authorize.jwt_required()
    return True

def obtain_token(user, db):
    """
     - Authenticate and generate JWT token using valid username and password
    """
    db_user = manager.get_user_by_username(db, username=user.username)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Username not existed")
    else:
        is_password_correct = manager.check_username_password(db, user)
        if is_password_correct is False:
            raise HTTPException(status_code=400, detail="Password is not correct")
        else:
            access_token = AuthJWT.create_access_token(identity=user.username)
            refresh_token = AuthJWT.create_refresh_token(identity=user.username)
            return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "Bearer"}


def refresh_token(Authorize: AuthJWT = Depends()):
    """
    - Retreive current user using JWT token
    """
    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_identity()
    ret = {
        'access_token': AuthJWT.create_access_token(identity=current_user)
    }
    return current_user



