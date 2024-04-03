import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# getting from .env file
TOKEN = os.getenv('TOKEN')
DB_LITE = os.getenv('DB_LITE')
BOT_LINK = os.getenv('BOT_LINK')

# not used
SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')
