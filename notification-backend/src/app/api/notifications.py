from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from src.app.api import schemas, manager
from src.app.api import auth
from src.app.api.auth import authentication_required
from src.app.database import connect_db
from fastapi import APIRouter

router = APIRouter()


@router.post("/api/v1/notification", response_model=schemas.Notification, status_code=status.HTTP_201_CREATED)
async def create_new_notification(notification: schemas.NotificationInfo,
                                  authorize: bool = Depends(authentication_required)
                                  , db: Session = Depends(connect_db)):
    """
    - create new notification
      ENDPOINT: BASE_URL/api/v1/notification/
      REQUEST METHOD: POST
      REQUEST BODY: {
        "event": "event-name",
        "notification_text": "Notification text"
      }
      RESPONSE: {
            "id": 1,
            "event": "event-name",
            "notification_text": "Notification text"
          }
    """
    db_notification = manager.get_notification_by_event(db, event=notification.event)
    if db_notification:
        return manager.update_notification(db=db, notification_id=db_notification.id, notification=notification)
    return manager.create_new_notification(db=db, notification=notification)


@router.get("/api/v1/notification")
async def get_all_notifications(authorize: bool = Depends(authentication_required), db: Session = Depends(connect_db)):
    """
    - list of all notification
      ENDPOINT: BASE_URL/api/v1/notification/
      REQUEST METHOD: GET
      RESPONSE: [
          {
            "id": 1,
            "event": "event-name",
            "notification_text": "Notification text"
          },
          {
            "id": 2,
            "event": "event-name-2",
            "notification_text": "Notification text 2"
          }
        ]
    """
    return manager.get_all_notifications(db=db)


@router.get("/api/v1/notification/{notification_id}")
async def show_notification_by_id(notification_id, authorize: bool = Depends(authentication_required)
                                  , db: Session = Depends(connect_db)):
    """
    - single notification details
      ENDPOINT: BASE_URL/api/v1/notification/<NOTIFICATION ID>/
      REQUEST METHOD: GET
      RESPONSE: {
            "id": 1,
            "event": "event-name",
            "notification_text": "Notification text"
          }
    """
    db_notification = manager.get_notification_by_id(db=db, notification_id=notification_id)
    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification does not exist")
    return db_notification

@router.get("/api/v1/notification/event/{event}")
async def show_notification_by_event(event, db: Session = Depends(connect_db)):
    """
    - single notification details by event
      ENDPOINT: BASE_URL/api/v1/notification/<NOTIFICATION EVENT>/
      REQUEST METHOD: GET
      RESPONSE: {
            "id": 1,
            "event": "event-name",
            "notification_text": "Notification text"
          }
    """
    return manager.get_notification_by_event_name(db=db, event=event)


@router.put("/api/v1/notification/{notification_id}", response_model=schemas.Notification)
async def update_notification_by_id(notification_id: int, notification: schemas.NotificationBase,
                                    authorize: bool = Depends(authentication_required)
                                    , db: Session = Depends(connect_db)):
    """
    - update notification_text value
      ENDPOINT: BASE_URL/api/v1/notification/<NOTIFICATION ID>/
      REQUEST METHOD: PUT
      REQUEST BODY: {
        "notification_text": "update-Notification text"
      }
      RESPONSE: {
            "id": 1,
            "notification_text": "update-Notification text"
          }
    """
    db_notification = manager.get_notification_by_id(db=db, notification_id=notification_id)
    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification does not exist")
    return manager.update_notification(db=db, notification_id=notification_id, notification=notification)


@router.delete("/api/v1/notification/{notification_id}")
async def delete_notification_by_id(notification_id: int, authorize: bool = Depends(authentication_required)
                                    , db: Session = Depends(connect_db)):
    """
    - delete notification
      ENDPOINT: BASE_URL/api/v1/notification/<NOTIFICATION ID>/
      REQUEST METHOD: DELETE
      RESPONSE: {
            "msg": "success",
          }
    """
    db_notification = manager.get_notification_by_id(db=db, notification_id=notification_id)
    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification does not exist")
    return manager.delete_notification_by_id(db=db, notification_id=notification_id)
