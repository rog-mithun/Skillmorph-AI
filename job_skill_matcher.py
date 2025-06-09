import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro")

def analyze_skill_gap(user_skills, target_role):
    prompt = f"""
    A user has the following skills: {', '.join(user_skills)}.
    Compare this to the typical skills required for the role of "{target_role}".

    Provide:
    1. Matched skills ✅
    2. Missing important skills ❌
    3. Optional but helpful skills
    4. Recommendations to close the skill gap
    """
    response = model.generate_content(prompt)
    return response.text
