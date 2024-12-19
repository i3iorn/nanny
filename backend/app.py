from fastapi import FastAPI
from backend.routes import tasks, notes
from backend.config.loader import Config
from backend.db.database import initialize_db

app = FastAPI()

# Include routers
app.include_router(tasks.router)
app.include_router(notes.router)

# TODO: Add authentication endpoints if needed
# TODO: Add middleware for logging, security headers, etc.
