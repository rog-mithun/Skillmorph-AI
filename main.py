import streamlit as st
import job_skill_matcher
import weekly_planner
import pyttsx3
from linkedin_utils import get_user_profile, get_user_email
from github_utils import get_github_stats, get_public_github_stats
from feedback_engine import generate_skill_report
from pdf_generator import generate_pdf
from resume_reviewer import extract_resume_text, review_resume
from master_report import generate_master_report
from sadtalker_wrapper import run_sadtalker

st.set_page_config(page_title="SkillMorph AI", layout="centered")
st.title("🧠 SkillMorph AI")
st.subheader("Personalized Skill Growth Coach using LinkedIn + GitHub + Gemini")
st.divider()

st.markdown("## 🔗 Enter Your Profile")

linkedin_url = st.text_input("🔗 LinkedIn Profile URL (e.g., https://www.linkedin.com/in/yourname)")
github_username = st.text_input("🐙 GitHub Username (e.g., johndoe)")

if st.button("📥 Load Profile"):
    if github_username:
        github_info = get_public_github_stats(github_username)
        # Try to extract name from LinkedIn URL
        linkedin_name = linkedin_url.rstrip('/').split('/')[-1].replace('-', ' ').title()
        if linkedin_url:
            # Extract last part and prettify it
            profile_id = linkedin_url.rstrip('/').split('/')[-1]
            parsed_name = profile_id.replace('-', ' ').title()
            st.session_state.linkedin_name = parsed_name
        else:
            st.session_state.linkedin_name = "Manual LinkedIn"

        st.session_state.linkedin_url = linkedin_url
        st.session_state.linkedin_email = get_user_email()
        st.session_state.github_info = github_info
        st.success("✅ Profile Loaded!")
    else:
        st.error("GitHub username is required to proceed.")

# Show data if available
if st.session_state.get("linkedin_name") and st.session_state.get("github_info"):
    github_info = st.session_state.github_info
    st.markdown("### 👤 **Profile Overview**")
    st.markdown("---")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://avatars.githubusercontent.com/" + github_info["username"], width=100)
    with col2:
        st.markdown(f"**🧑‍💼 Name:** {st.session_state.linkedin_name}")
        st.markdown(f"**🔗 LinkedIn:** [{linkedin_url}]({linkedin_url})")
        st.markdown(f"**🐙 GitHub Username:** `{github_info.get('username', 'N/A')}`")
        st.markdown(f"**📁 Repositories:** {github_info.get('total_repos', 0)}")
        st.markdown(f"**💻 Languages:** {', '.join(github_info.get('languages', []))}")

    st.markdown("---")



# Step 2: Generate Skill Report
if st.session_state.get("linkedin_name"):
    with st.expander("📋 Step 2: Generate Your AI Skill Report", expanded=True):
        user_note = st.text_area("✍️ Add anything you'd like Gemini to consider")
        if st.button("🚀 Generate Report"):
            with st.spinner("Gemini analyzing your profile..."):
                st.session_state.report = generate_skill_report(
                    st.session_state.linkedin_name,
                    st.session_state.linkedin_email,
                    st.session_state.github_info,
                    user_note
                )
            st.success("✅ Report Generated")

# Show report if exists
if st.session_state.get("report"):
    st.markdown("### 📄 Your Skill Report")
    st.write(st.session_state.report)

    if st.button("📄 Download Report as PDF"):
        pdf_path = generate_pdf(
            report_text=st.session_state.report,
            name=st.session_state.linkedin_name,
            email=st.session_state.linkedin_email,
            github_info=st.session_state.github_info
        )
        with open(pdf_path, "rb") as f:
            st.download_button("📥 Click to Download", f, file_name="SkillMorphAI_Report.pdf", mime="application/pdf")

# Step 3: Skill Gap Analyzer
if st.session_state.get("report"):
    with st.expander("🧠 Step 3: Skill Gap Analyzer"):
        target_role = st.text_input("🎯 Enter your dream role (e.g., Data Scientist)")
        if st.button("📊 Analyze Skill Fit"):
            with st.spinner("Comparing your skills to industry needs..."):
                result = job_skill_matcher.analyze_skill_gap(
                    st.session_state.github_info["languages"],
                    target_role
                )
                st.session_state.skill_gap_result = result  # 🔐 store safely
            st.success("✅ Here's how you match up:")
            st.write(result)

if st.session_state.get("report"):
    with st.expander("📅 Step 4: Weekly Upskilling Planner"):
        planner_role = st.text_input("💼 (Optional) Job Role for Planning")
        if st.button("🧠 Generate Weekly Plan"):
            with st.spinner("Planning your 7-day growth journey..."):
                plan = weekly_planner.generate_weekly_plan(
                    user_skills=st.session_state.github_info["languages"],
                    target_role=planner_role
                )
                st.session_state.weekly_plan = plan
            st.success("🗓️ Here's Your Plan:")
            st.write(plan)

            if st.button("📥 Download Plan as PDF"):
                from pdf_generator import generate_pdf
                pdf_path = generate_pdf(
                    report_text=plan,
                    name=st.session_state.linkedin_name,
                    email=st.session_state.linkedin_email,
                    github_info=st.session_state.github_info,
                    output_path="weekly_plan.pdf"
                )
                with open(pdf_path, "rb") as f:
                    st.download_button("📄 Download Weekly Plan", f, file_name="Weekly_Upskilling_Plan.pdf", mime="application/pdf")

if st.session_state.get("report"):
    with st.expander("📄 Step 5: Upload Resume for AI Review"):
        uploaded_resume = st.file_uploader("📤 Upload your resume (PDF only)", type=["pdf"])
        
        if uploaded_resume:
            st.success("✅ Resume uploaded. Click below to get review.")
            
            if st.button("🔍 Analyze Resume"):
                with st.spinner("Extracting and reviewing..."):
                    resume_text = extract_resume_text(uploaded_resume)
                    feedback = review_resume(resume_text)
                    st.session_state.resume_feedback = feedback
                st.success("📋 Review Complete")
                st.markdown("### ✨ Resume Feedback")
                st.write(st.session_state.resume_feedback)

if st.session_state.get("resume_feedback"):  # Only shows if resume feedback exists
    with st.expander("📘 Step 6: Generate Master Career Report"):
        if st.button("📘 Download Master Career Report"):
            master_path = generate_master_report(
                name =st.session_state.linkedin_name,
                github_info=st.session_state.github_info,
                resume_feedback=st.session_state.resume_feedback,
                gap_analysis=st.session_state.get("skill_gap_result", "Not yet generated."),
                weekly_plan=st.session_state.get("weekly_plan", "Not yet generated.")
            )
            with open(master_path, "rb") as f:
                st.download_button("📘 Download Complete Career Report", f, file_name="SkillMorphAI_Master_Career_Report.pdf", mime="application/pdf")
            st.success("✅ Master Career Report Generated")

if st.session_state.get("resume_feedback"):
    with st.expander("🎬 AI Talking Avatar (SadTalker v0.0.2)"):
        uploaded_avatar = st.file_uploader("🖼️ Upload Avatar (PNG/JPG)", type=["jpg", "png"])
        if uploaded_avatar:
            with open("avatar_input.png", "wb") as f:
                f.write(uploaded_avatar.read())

            feedback_text = st.session_state.resume_feedback or "You're growing steadily. Keep learning and improving."

            # Generate voice using gTTS
            engine = pyttsx3.init()
            engine.setProperty("rate", 160)
            engine.save_to_file(feedback_text, "feedback_voice.mp3")
            engine.runAndWait()

            if st.button("🎥 Generate Talking Avatar"):
                with st.spinner("Generating high-resolution avatar using SadTalker..."):
                    final_video_path = run_sadtalker("avatar_input.png", "feedback_voice.mp3")
                    st.video(final_video_path)
                    with open(final_video_path, "rb") as f:
                        st.download_button("⬇️ Download Avatar Video", f, file_name="Talking_Avatar.mp4", mime="video/mp4")
