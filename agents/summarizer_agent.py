import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")  #GEMINI_API_KEY IS REMOVED!

model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_research(question, context):

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
