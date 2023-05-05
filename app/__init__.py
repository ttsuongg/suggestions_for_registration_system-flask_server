from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = f"postgresql://{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_HOST']}:{os.environ['DATABASE_PORT']}/{os.environ['DATABASE']}"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

from app.routes import routes
