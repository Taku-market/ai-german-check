def create_table(db):
    db.execute("CREATE TABLE jobs (id INTEGER, title TEXT, description TEXT, label INTEGER)")

def add_job(db, id, title, description, label):
    db.execute("INSERT INTO jobs VALUES (?, ?, ?, ?)",(id, title, description, label))
    