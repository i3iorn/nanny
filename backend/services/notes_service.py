# TODO: Implement encryption using the configured password and key
# For now, store content as plain text or mock encryption.

def create_note(conn, title, content):
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    note_id = cur.lastrowid
    cur.execute("INSERT INTO note_versions (note_id, title, content) VALUES (?, ?, ?)",
                (note_id, title, content))
    conn.commit()
    return note_id

def update_note(conn, note_id, title=None, content=None):
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    note = cur.fetchone()
    if not note:
        return False

    new_title = title if title is not None else note["title"]
    new_content = content if content is not None else note["content"]

    cur.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?",
                (new_title, new_content, note_id))
    cur.execute("INSERT INTO note_versions (note_id, title, content) VALUES (?, ?, ?)",
                (note_id, new_title, new_content))
    conn.commit()
    return True

def get_note(conn, note_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    row = cur.fetchone()
    return dict(row) if row else None
