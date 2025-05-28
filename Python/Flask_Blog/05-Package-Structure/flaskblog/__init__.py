from flask import Flask
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
import os
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)
SB_PASSWORD = os.environ["SUPABASE_PASSWORD"]

app.config["SECRET_KEY"] = "5791628bb0b13ce0c676dfde280ba245"

# site.db inside ./instance/
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

# Supabase stateless ipv4 - preferred
# app.config["SQLALCHEMY_DATABASE_URI"] = (f"postgresql://postgres.ekiwycazuqpglzqcmfly:{SB_PASSWORD}@aws-0-us-west-1.pooler.supabase.com:6543/postgres")
# Supabase stateful ipv4 - fallback?
# app.config["SQLALCHEMY_DATABASE_URI"] = (f"postgresql://postgres.ekiwycazuqpglzqcmfly:{SB_PASSWORD}@aws-0-us-west-1.pooler.supabase.com:5432/postgres")
db = SQLAlchemy(app)
app.app_context().push()

from flaskblog import routes
