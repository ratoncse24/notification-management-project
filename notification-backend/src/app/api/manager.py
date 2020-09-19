from sqlalchemy.orm import Session
from src.app.api import schemas
from src.app.api import models
import bcrypt


def get_user_by_username(db: Session, username: str):
    """
     - Search user by username to User model
    """
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt(10))
    db_user = models.User(username=user.username, password=hashed_password.decode('utf-8'), fullname=user.fullname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_username_password(db: Session, user: schemas.UserAuthenticate):
    db_user_info: models.User = get_user_by_username(db, username=user.username)
    return bcrypt.checkpw(user.password.encode('utf-8'), db_user_info.password.encode('utf-8'))


def create_new_notification(db: Session, notification: schemas.NotificationInfo):
    db_blog = models.Notification(event=notification.event, notification_text=notification.notification_text)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def update_notification(db: Session, notification_id: int, notification: schemas.NotificationBase):
    db_blog = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    db_blog.notification_text = notification.notification_text
    db.commit()
    db.refresh(db_blog)
    return db_blog


def get_notification_by_event(db: Session, event: str):
    return db.query(models.Notification).filter(models.Notification.event == event).first()


def get_all_notifications(db: Session):
    return db.query(models.Notification).all()


def get_notification_by_id(db: Session, notification_id: int):
    return db.query(models.Notification).filter(models.Notification.id == notification_id).first()


def get_notification_by_event(db: Session, event: str):
    return db.query(models.Notification).filter(models.Notification.event == event).first()


def get_notification_by_event_name(db: Session, event: str):
    db_notification = db.query(models.Notification).filter(models.Notification.event == event).first()
    if db_notification:
        return {"notification_text": db_notification.notification_text}
    else:
        return {}

def delete_notification_by_id(db: Session, notification_id: int):
    db.query(models.Notification).filter(models.Notification.id == notification_id).delete()
    db.commit()
    return {"msg": "Notification deleted!"}

