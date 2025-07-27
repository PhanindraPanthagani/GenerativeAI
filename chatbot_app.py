import streamlit as st
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("👵 Elder Fraud Protection Assistant")

questions = [
    ("Have you met this person before?", [
        "A) Yes, within the last month",
        "B) Yes, but not for over a year",
        "C) No, this is the first time",
        "D) Just today"
    ]),
    ("Have they asked for money or personal info?", [
        "A) Yes, bank details",
        "B) Gift card/cash",
        "C) No",
        "D) Not sure"
    ]),
    ("How did they contact you?", [
        "A) Phone call",
        "B) Text message",
        "C) Social media / dating app",
        "D) In person"
    ])
]

responses = []
for i, (question, options) in enumerate(questions):
    responses.append(st.radio(f"{i+1}. {question}", options, key=f"q{i}"))

if st.button("Evaluate Risk"):
    prompt = f"""You are a fraud protection assistant. Based on the answers below, determine if the user is at high, medium, or low risk of being scammed. Provide a short warning if needed.

Answers:
1. {responses[0]}
2. {responses[1]}
3. {responses[2]}

Respond in this format:
Risk Level: [Low/Medium/High]
Message: [brief explanation and what they should do]
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    result = response['choices'][0]['message']['content']
    st.markdown("### 🛡️ Result")
    st.success(result)