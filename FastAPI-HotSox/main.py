import os
from fastapi import FastAPI

# cloudinary
import cloudinary


# import Database setup
from api.database.setup import engine
from api.database import models

# import routers
from api.routers import auth, user, sock

# load envs
if os.path.isfile("env.py"):
    import env

cloudinary.config(
    cloud_name=os.environ.get("cloudinary_cloud_name"),
    api_key=os.environ.get("cloudinary_api_key"),
    api_secret=os.environ.get("cloudinary_api_secret"),
)

# build FastAPI app / Hide schemas from docs
app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": -1})

# setup SQLAlchemy database engine
# models.Base.metadata.create_all(engine)

# include API routs
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(sock.router)
