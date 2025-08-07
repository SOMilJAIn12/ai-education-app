import streamlit as st
import google.generativeai as genai

# --- API Key Setup ---
genai.configure(api_key="YOUR_API_KEY_HERE")

# --- Gemini Model Setup ---
model = genai.GenerativeModel("gemini-pro")

# --- App UI ---
st.set_page_config(page_title="EduContent AI", page_icon="📚")
st.title("📚 AI-Powered Educational Content Generator")

with st.form("content_form"):
    topic = st.text_input("🔍 Topic", placeholder="e.g. Photosynthesis")
    age = st.selectbox("🎂 Age Group", ["5-7", "8-10", "11-13", "14-16"])
    subject = st.selectbox("📘 Subject", ["Science", "Maths", "History", "Geography"])
    content_type = st.selectbox("📦 Content Type", ["Activity", "Learning Plan", "Educational Game", "Study Tip", "Career Guidance", "Concept Explanation"])
    level = st.selectbox("🎯 Difficulty Level", ["Easy", "Medium", "Hard"])

    submit = st.form_submit_button("Generate Content")

if submit and topic:
    with st.spinner("Generating content..."):
        prompt = (
            f"Generate an {content_type} for the topic '{topic}' for students aged {age}. "
            f"The subject is {subject} and difficulty level is {level}. "
            f"Make it fun, age-appropriate, and engaging."
        )
        try:
            response = model.generate_content(prompt)
            st.success("🎉 Here's your AI-generated content:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")

elif submit:
    st.warning("⚠️ Please enter a topic before generating.")
