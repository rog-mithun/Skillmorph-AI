# 🧠 SkillMorph AI – Personalized Career Simulator with AI Feedback and Talking Avatar

SkillMorph AI is a career development tool that uses Generative AI, resume parsing, and real-time visual feedback to help users identify skill gaps, generate personalized weekly upskilling plans, and receive feedback through a talking avatar.

---

## 📌 Key Features

- 📝 Resume Analysis using Google Gemini API  
- 🧠 Skill Feedback & Gap Detection  
- 📅 Weekly Upskilling Planner  
- 🧑‍💼 GitHub & LinkedIn Profile Matching  
- 🗣️ Voice-Based Feedback Generation  
- 🎥 Talking Avatar using SadTalker  
- 🌐 Interactive UI via Streamlit

---

## 🛠️ Tech Stack

### Languages:
![Python](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Frameworks & Tools:
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Gradio](https://img.shields.io/badge/-Gradio-3C3C3C?style=for-the-badge)

### APIs & Integrations:
![Google Gemini](https://img.shields.io/badge/-Gemini%20API-4285F4?style=for-the-badge&logo=google&logoColor=white)
![GitHub API](https://img.shields.io/badge/-GitHub%20API-181717?style=for-the-badge&logo=github&logoColor=white)
![LinkedIn API](https://img.shields.io/badge/-LinkedIn%20API-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)

### Voice & Audio:
![gTTS](https://img.shields.io/badge/-gTTS-FF9800?style=for-the-badge)
![MP3](https://img.shields.io/badge/-MP3-000000?style=for-the-badge)

### Avatar & Video:
![SadTalker](https://img.shields.io/badge/-SadTalker-8E24AA?style=for-the-badge)

### PDF & Report Generation:
![PDF Generator](https://img.shields.io/badge/-PDF%20Generation-4CAF50?style=for-the-badge)

### Other Tools:
![Dotenv](https://img.shields.io/badge/-Dotenv-1E1E1E?style=for-the-badge)

---

## 📁 Project Structure

| File/Folder             | Description                                  |
|-------------------------|----------------------------------------------|
| `main.py`               | Streamlit app – UI entry point               |
| `resume_reviewer.py`    | Analyzes resume using Gemini API             |
| `job_skill_matcher.py`  | Matches skills with job roles                |
| `weekly_planner.py`     | Generates weekly learning plan               |
| `pdf_generator.py`      | Creates a visual PDF summary                 |
| `feedback_engine.py`    | Compiles AI feedback into structured format  |
| `feedback_voice.py`     | Converts feedback into MP3 audio             |
| `sadtalker_wrapper.py`  | Wraps SadTalker inference pipeline           |
| `github_utils.py`       | Pulls GitHub profile data                    |
| `linkedin_utils.py`     | Pulls LinkedIn profile data                  |
| `requirements.txt`      | Python dependency list                       |
| `SadTalker/`            | Deep learning avatar animation engine        |
| `avatar_input/`         | User-uploaded image for talking avatar       |
| `sadtalker_output.mp4`  | Final avatar video file                      |

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rog-mithun/skillmorph-ai.git
   cd skillmorph-ai

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Create a `.env` File and Add Your API Keys:**
   ```bash
   GEMINI_API_KEY=your_google_gemini_api_key
   GITHUB_TOKEN=your_github_token
   LINKEDIN_TOKEN=your_linkedin_token

4. **Run the Streamlit App:**
   ```bash
   streamlit run main.py

---

## 🎬 Demo & Sample Outputs

- PDF Resume Report with AI Feedback  
- Weekly Upskilling Planner  
- MP3 Voice Feedback  
- Talking Avatar Feedback Video (MP4)

*You can add screenshots or sample output videos here.*

---

## 📖 License
MIT License
© 2025 Mithunsankar S

---


