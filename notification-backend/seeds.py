from src.app.database import SessionLocal
from src.app.api import manager, schemas


def main():

    try:
        db = SessionLocal()
        # check admin user already exist
        db_user = manager.get_user_by_username(db, "admin")
        # IF admin user does not exist then create user
        if not db_user:
            print("===================== creating default user =============")
            user = schemas.UserCreate(**{
                "username": "admin",
                "fullname": "Admin",
                "password": "admin"
              })
            manager.create_user(db=db, user=user)
            db.commit()
            print("===================== end default user creation =============")
        db.close()
    except Exception as error:
        print("Default user creation failed!")



if __name__ == '__main__':
    main()