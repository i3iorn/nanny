from fastapi import APIRouter, HTTPException
from backend.db.database import get_connection
from backend.services.notes_service import create_note, get_note, update_note
# TODO: Implement password protection/encryption in notes_service

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("/")
def create_note_endpoint(title: str, content: str):
    conn = get_connection()
    note_id = create_note(conn, title, content)
    return {"note_id": note_id}

@router.put("/{note_id}")
def update_note_endpoint(note_id: int, title: str = None, content: str = None):
    conn = get_connection()
    updated = update_note(conn, note_id, title, content)
    if not updated:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"status": "success"}

@router.get("/{note_id}")
def get_note_endpoint(note_id: int):
    conn = get_connection()
    note = get_note(conn, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
