# src/config.py
from dotenv import load_dotenv
import os

def load_env():
    """Load environment variables from .env file"""
    load_dotenv()
    print("Environment variables loaded.")

def get_key(key_name):
    """Retrieve a specific environment variable"""
    value = os.getenv(key_name)
    if value is None:
        raise ValueError(f"{key_name} not found in environment")
    return value


