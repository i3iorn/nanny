from fastapi import APIRouter, HTTPException
from backend.config.loader import Config
from backend.db.database import get_connection
from backend.services.tasks_service import create_task, update_task, get_task

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/")
def create_task_endpoint(title: str, description: str):
    conn = get_connection()
    task_id = create_task(conn, title, description)
    return {"task_id": task_id}

@router.put("/{task_id}")
def update_task_endpoint(task_id: int, title: str = None, description: str = None):
    conn = get_connection()
    updated = update_task(conn, task_id, title, description)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "success"}

@router.get("/{task_id}")
def get_task_endpoint(task_id: int):
    conn = get_connection()
    task = get_task(conn, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
