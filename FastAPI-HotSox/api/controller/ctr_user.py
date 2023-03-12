from sqlalchemy.orm import Session
from ..database import models, schemas
from fastapi import HTTPException, status
from ..authentication.hashing import Hash


def show_all_user(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No users available",
        )
    return users


def show_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} is not available",
        )
    return user


# def create(request: schemas.User, db: Session):
#     new_user = models.User(
#         name=request.name, email=request.email, password=Hash.bcrypt(request.password)
#     )
#     # db.add(new_user)
#     # db.commit()
#     # db.refresh(new_user)
#     return new_user
