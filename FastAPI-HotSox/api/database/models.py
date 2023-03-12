from sqlalchemy import (
    ForeignKey,
    Column,
    Integer,
    Float,
    String,
    DateTime,
    Date,
    Boolean,
)
from sqlalchemy.orm import relationship

from .setup import Base

from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(Base):
    __tablename__ = "app_users_user"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String)
    last_login = Column(DateTime)
    is_superuser = Column(Boolean)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    is_staff = Column(Boolean)
    is_active = Column(Boolean)
    date_joined = Column(DateTime)
    info_about = Column(String)
    info_birthday = Column(Date)
    info_gender = Column(Integer)
    location_city = Column(String)
    location_latitude = Column(Float)
    location_longitude = Column(Float)
    notification = Column(Boolean)
    social_instagram = Column(String)
    social_facebook = Column(String)
    social_twitter = Column(String)
    social_spotify = Column(String)

    profile_pictures = relationship("UserProfilePicture", back_populates="user")
    socks = relationship("Sock", back_populates="user")
    user_matches = relationship(
        "UserMatch", back_populates="user", foreign_keys="UserMatch.user_id"
    )
    mail = relationship("MessageMail", back_populates="user")
    chat = relationship(
        "MessageChat", back_populates="user", foreign_keys="MessageChat.user_id"
    )


class UserProfilePicture(Base):
    __tablename__ = "app_users_userprofilepicture"

    id = Column(Integer, primary_key=True, index=True)
    profile_picture = Column(String)
    user_id = Column(Integer, ForeignKey("app_users_user.id"))

    user = relationship("User", back_populates="profile_pictures")


class UserMatch(Base):
    __tablename__ = "app_users_usermatch"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("app_users_user.id"))
    other_id = Column(Integer, ForeignKey("app_users_user.id"))
    unmatched = Column(Boolean)
    chatroom_uuid = Column(UUID(as_uuid=True))

    user = relationship("User", back_populates="user_matches", foreign_keys=[user_id])
    other = relationship("User", back_populates="user_matches", foreign_keys=[other_id])


class Sock(Base):
    __tablename__ = "app_users_sock"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("app_users_user.id"))
    info_joining_date = Column(DateTime)
    info_name = Column(String)
    info_about = Column(String)
    info_color = Column(Integer)
    info_fabric = Column(Integer)
    info_fabric_thickness = Column(Integer)
    info_brand = Column(Integer)
    info_type = Column(Integer)
    info_size = Column(Integer)
    info_age = Column(Integer)
    info_separation_date = Column(Date)
    info_condition = Column(Integer)
    info_holes = Column(Integer)
    info_kilometers = Column(Integer)
    info_inoutdoor = Column(Integer)
    info_washed = Column(Integer)
    info_special = Column(String)

    user = relationship("User", back_populates="socks")
    profile_pictures = relationship("SockProfilePicture", back_populates="sock")
    sock_likes = relationship(
        "SockLike", back_populates="sock", foreign_keys="SockLike.sock_id"
    )


class SockProfilePicture(Base):
    __tablename__ = "app_users_sockprofilepicture"

    id = Column(Integer, primary_key=True, index=True)
    profile_picture = Column(String)
    sock_id = Column(Integer, ForeignKey("app_users_sock.id"))

    sock = relationship("Sock", back_populates="profile_pictures")


class SockLike(Base):
    __tablename__ = "app_users_socklike"

    id = Column(Integer, primary_key=True, index=True)
    sock_id = Column(Integer, ForeignKey("app_users_sock.id"))
    like_id = Column(Integer, ForeignKey("app_users_sock.id"))
    dislike_id = Column(Integer, ForeignKey("app_users_sock.id"))

    sock = relationship("Sock", back_populates="sock_likes", foreign_keys=[sock_id])
    like = relationship("Sock", back_populates="sock_likes", foreign_keys=[like_id])
    dislike = relationship(
        "Sock", back_populates="sock_likes", foreign_keys=[dislike_id]
    )


class MessageMail(Base):
    __tablename__ = "app_users_messagemail"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("app_users_user.id"))
    subject = Column(String)
    content = Column(String)
    sent_date = Column(Date)

    user = relationship("User", back_populates="mail")


class MessageChat(Base):
    __tablename__ = "app_users_messagechat"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("app_users_user.id"))
    other_id = Column(Integer, ForeignKey("app_users_user.id"))
    message = Column(String)
    sent_date = Column(DateTime)
    seen_date = Column(DateTime)

    user = relationship("User", back_populates="chat", foreign_keys=[user_id])
    other = relationship("User", back_populates="chat", foreign_keys=[other_id])
