from fastapi import FastAPI

# import Database setup
from api.database.setup import engine
from api.database import models

# import routers
from api.routers import auth, user, sock

# build FastAPI app / Hide schemas from docs
app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": -1})

# setup SQLAlchemy database engine
# models.Base.metadata.create_all(engine)

# include API routs
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(sock.router)
