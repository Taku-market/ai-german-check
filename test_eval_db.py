import sqlite3
from eval_db import create_table, add_job

def test_add_job():
    db = sqlite3.connect(":memory:")
    create_table(db)
    add_job(db, 1, "QA Engineer", "We're hiring.", 0)
    rows = db.execute("SELECT * FROM jobs").fetchall()
    assert rows == [(1, "QA Engineer", "We're hiring.", 0)]