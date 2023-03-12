from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..database.setup import get_db
from ..database import models, schemas

from ..authentication import oauth2

# load business logic
from ..controller.ctr_user import show_all_user, show_user

# build routes
router = APIRouter(prefix="/user", tags=["Users"])


@router.get("s/", response_model=list[schemas.ShowUser])
def get_all_user(
    id: int = 5,
    db: Session = Depends(get_db),
    current_user: schemas.ShowUser = Depends(oauth2.get_current_user),
):
    return show_all_user(db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.ShowUser = Depends(oauth2.get_current_user),
):
    return show_user(id, db)


# @router.post("/", response_model=schemas.ShowUser)
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     return create(request, db)
