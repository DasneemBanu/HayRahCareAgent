

import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def summarize_research(question, context):
    # truncate context just in case
    context = context[:4000]
    prompt = f"""
You are HayRahCare, a mental health research assistant.

Use the research papers below to answer the question.

{context}

Question:
{question}

Provide a clear evidence-based summary.
"""
    response = model.generate_content(prompt)
    return response.text
