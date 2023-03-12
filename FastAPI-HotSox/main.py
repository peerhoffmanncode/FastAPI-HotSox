from fastapi import FastAPI

# import Database setup
from api.database.setup import engine
from api.database import models

# import routers
from api.routers import user, auth  # authentication

# build FastAPI app
app = FastAPI()

# setup SQLAlchemy database engine
# models.Base.metadata.create_all(engine)

# include API routs
app.include_router(auth.router)
app.include_router(user.router)
