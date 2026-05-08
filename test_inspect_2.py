from app import app, db
from sqlalchemy import inspect

with app.app_context():
    inspector = inspect(db.engine)
    print(f"Tables: {inspector.get_table_names()}")
    for table in inspector.get_table_names():
        print(f"Columns in {table}: {[c['name'] for c in inspector.get_columns(table)]}")
