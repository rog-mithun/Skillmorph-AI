import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro")

def generate_weekly_plan(user_skills, target_role=None):
    role_part = f"for the role of {target_role}" if target_role else ""
    prompt = f"""
    I am a developer with the following skills: {', '.join(user_skills)}.
    Generate a personalized 7-day upskilling plan {role_part}.
    
    Structure:
    - Day 1 to Day 7
    - Each day should have:
        - A focus topic
        - A small hands-on task or project
        - 1–2 free learning resources (preferably YouTube, GitHub, docs)

    Keep it short, actionable, and beginner-friendly.
    """
    response = model.generate_content(prompt)
    return response.text
