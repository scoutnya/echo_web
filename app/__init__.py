from flask import Flask
from dotenv import load_dotenv
import secrets
import os
#import sqlite3
'''
def create_db():

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        approved INTEGER
    )
    """)

    conn.commit()
    conn.close()
'''

load_dotenv()

def create_app():
    app = Flask(__name__,
            static_folder="../static",
            template_folder="../templates")
    app.secret_key = os.getenv("SECRET_KEY")

    from .routes import main
    app.register_blueprint(main)

    return app
