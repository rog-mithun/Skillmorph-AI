import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-pro")

def generate_skill_report(linkedin_name, linkedin_email, github_data, user_input=None):
    prompt = f"""
    You are an expert career coach. Based on the following profile, give only a clean analysis report.

    LinkedIn Name: {linkedin_name}
    GitHub Repos: {github_data['total_repos']}
    GitHub Languages: {', '.join(github_data['languages'])}

    Optional User Input:
    {user_input}

    🔴 Important: Do NOT include LinkedIn Name, Email, or GitHub info in the report again.
    
    Format:
    1. Strengths
    2. Areas to improve
    3. Weekly learning goals
    4. Career suggestions
    5. Motivational note
    """

    response = model.generate_content(prompt)
    return response.text
