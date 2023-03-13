from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..database.setup import get_db
from ..database import models, schemas

from ..authentication import oauth2

# load business logic
from ..controller import ctr_sock

# build routes
router = APIRouter(prefix="/sock", tags=["Socks"])


@router.get("s/", response_model=list[schemas.ShowSock])
async def get_all_user(
    db: Session = Depends(get_db),
    current_user: schemas.ShowUser = Depends(oauth2.get_current_user),
):
    return ctr_sock.show_all(db)


@router.get("/{id}", response_model=schemas.ShowSock)
async def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.ShowUser = Depends(oauth2.get_current_user),
):
    return ctr_sock.show_specific(id, db)


# @router.post("/", response_model=schemas.ShowUser)
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     return create(request, db)
