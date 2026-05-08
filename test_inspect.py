from app import app, db
from sqlalchemy import inspect

with app.app_context():
    try:
        print(f"db.inspect exists: {hasattr(db, 'inspect')}")
        inspector = db.inspect(db.engine)
        print("db.inspect(db.engine) worked")
    except Exception as e:
        print(f"db.inspect(db.engine) failed: {e}")
        
    try:
        inspector = inspect(db.engine)
        print("inspect(db.engine) from sqlalchemy worked")
    except Exception as e:
        print(f"inspect(db.engine) failed: {e}")
