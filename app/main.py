
from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routes import router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SWYNEX Task Management API",
    description="A task management backend with SQLite and SQLAlchemy CRUD operations.",
    version="1.0.0"
)

app.include_router(router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
