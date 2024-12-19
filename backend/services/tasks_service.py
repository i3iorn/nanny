def create_task(conn, title, description):
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
    task_id = cur.lastrowid
    cur.execute("INSERT INTO task_versions (task_id, title, description) VALUES (?, ?, ?)",
                (task_id, title, description))
    conn.commit()
    return task_id

def update_task(conn, task_id, title=None, description=None):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cur.fetchone()
    if not task:
        return False

    new_title = title if title is not None else task["title"]
    new_description = description if description is not None else task["description"]

    cur.execute("UPDATE tasks SET title = ?, description = ? WHERE id = ?",
                (new_title, new_description, task_id))
    cur.execute("INSERT INTO task_versions (task_id, title, description) VALUES (?, ?, ?)",
                (task_id, new_title, new_description))
    conn.commit()
    return True

def get_task(conn, task_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    return dict(cur.fetchone()) if cur.fetchone() else None
