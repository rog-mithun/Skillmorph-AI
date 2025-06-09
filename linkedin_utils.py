import os
from dotenv import load_dotenv
from jose import jwt  # Library to decode JWT

load_dotenv()

def get_user_profile():
    id_token = os.getenv("LINKEDIN_ID_TOKEN")  # Add this to your .env
    try:
        decoded = jwt.get_unverified_claims(id_token)
        name = decoded.get("name", "Unknown User")
        return name
    except Exception as e:
        print("Error decoding id_token:", e)
        return "Unknown User"

def get_user_email():
    id_token = os.getenv("LINKEDIN_ID_TOKEN")
    try:
        decoded = jwt.get_unverified_claims(id_token)
        email = decoded.get("email", "No Email Found")
        return email
    except Exception as e:
        print("Error decoding id_token:", e)
        return "No Email Found"
