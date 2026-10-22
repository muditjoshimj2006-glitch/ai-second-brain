from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGO = os.getenv("ALGO")
ACCESS_TOKEN_EXPIRE_MINUTES = 30