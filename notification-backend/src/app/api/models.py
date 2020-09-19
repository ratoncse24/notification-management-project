from sqlalchemy import Column, Integer, String

from src.app.database import Base


class User(Base):
    """
    - User table
    - Used for authentication
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    fullname = Column(String)


class Notification(Base):
    """
     - Notification table
     - Used for store notification information
    """
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    event = Column(String, index=True, unique=True)
    notification_text = Column(String, index=True)
