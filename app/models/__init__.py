from app.db.session import engine  # --- IGNORE ---
from app.models import user  # , school


def create_all_tables():  # --- IGNORE ---
    user.Base.metadata.create_all(bind=engine)  # --- IGNORE ---


def drop_all_tables():
    user.Base.metadata.drop_all(bind=engine)


def recreate_all_tables():
    drop_all_tables()
    create_all_tables()
