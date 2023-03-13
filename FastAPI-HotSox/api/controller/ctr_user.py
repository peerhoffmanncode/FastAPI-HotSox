from sqlalchemy.orm import Session
from sqlalchemy import exc, or_
from ..database import models, schemas
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from ..authentication.hashing import Hash

from datetime import datetime


##
## Users
##
def show_all_user(db: Session):
    users = db.query(models.User).order_by(models.User.id.desc()).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No users available",
        )
    return users


def show_specific_user(username: str, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the username {username} is not available",
        )
    return user


def create_user(request: schemas.CreateUser, db: Session):
    # hash password before storing it to the db!
    request.password = Hash.encrypt(request.password)

    # check for duplicates
    try:
        # create db object
        new_user = models.User(**request.dict())
        # write to db / commit!
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except exc.IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Already exists! <{e.orig}>",
        )
    return new_user


def edit_user(username: str, request: schemas.EditUser, db: Session):
    current_user = (
        db.query(models.User).filter(models.User.username == username).first()
    )
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the username {username} is not available",
        )

    # check for duplicates
    try:
        db.query(models.User).filter(models.User.username == username).update(
            request.dict()
        )
        db.commit()
        db.refresh(current_user)
    except exc.IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Already exists! <{e.orig}>",
        )
    return current_user


def delete_user(request: schemas.SimplyUser, db: Session):
    user = (
        db.query(models.User)
        .filter(
            models.User.username == request.username, models.User.email == request.email
        )
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the username <{request.username}> and email <{request.email}> is not available!",
        )

    db.query(models.User).filter(
        models.User.username == request.username, models.User.email == request.email
    ).delete()
    db.commit()
    return {"message": "Success! User deleted!"}


##
## Mail
##
def show_all_mails(username: str, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the username <{username}> is not available",
        )
    mails = db.query(models.MessageMail).filter(models.MessageMail.user == user).all()
    if not mails:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No mails available of user <{username}>",
        )

    return mails


##
## Chats
##
def show_all_chats(username: str, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the username <{username}> is not available",
        )
    chats = db.query(models.MessageChat).filter(models.MessageChat.user == user).all()
    if not chats:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No chats available of user <{username}>",
        )

    return chats


def show_specific_chat(username: str, receiver: str, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the username <{username}> is not available",
        )
    other = db.query(models.User).filter(models.User.username == receiver).first()
    if not other:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Receiver with the username <{receiver}> is not available",
        )

    chats = (
        db.query(models.MessageChat)
        .filter(models.MessageChat.user == user, models.MessageChat.other == other)
        .all()
    )
    if not chats:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No chats available between user <{username}> and <{receiver}>",
        )
    return chats
