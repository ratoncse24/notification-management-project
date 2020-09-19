from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import status
from fastapi import Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from src.app.api import schemas, manager
from src.app.api import auth
from src.app.api.auth import authentication_required
from src.app.database import connect_db
from fastapi import APIRouter

router = APIRouter()


@router.post("/api/v1/user", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
async def create_new_user(user: schemas.UserCreate
                                  , db: Session = Depends(connect_db)):
    """
    - create new user
      ENDPOINT: BASE_URL/api/v1/user/
      REQUEST METHOD: POST
      REQUEST BODY: {
        "username": "admin",
        "password": "admin",
        "fullname": "admin"
      }
      RESPONSE: {
            "username": "admin",
            "password": "admin",
            "fullname": "admin"
          }
    """
    return manager.create_user(db, user)



@router.post("/obtain_token_for_docs", response_model=schemas.Token, summary="Obtain token for docs")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(connect_db)):
    """
    - authentication endpoint for API docs
    - As API docs use form-data to authenticate, we need a seperate api to accept form-data
    """
    return auth.obtain_token(form_data, db)


@router.post("/api/v1/obtain_token", response_model=schemas.Token)
def obtain_token(user: schemas.UserAuthenticate, db: Session = Depends(connect_db)):
    """
    - Authentication endpoint once the authentication done response a JWT token to user
    """
    return auth.obtain_token(user, db)


@router.post("/api/v1/refresh_token", response_model=schemas.AccessToken)
async def refresh_token(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_identity()
    ret = {
        'access_token': AuthJWT.create_access_token(identity=current_user)
    }
    return ret

