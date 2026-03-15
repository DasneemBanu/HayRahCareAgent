# HayRahCareAgent

# HayRahCare: Mental Health Research Swarm Architecture

This repository contains the infographic and architectural documentation for **HayRahCare**, a multi-agent system designed to provide evidence-based insights for mental health queries.

## 📊 Infographic Overview

The infographic illustrates the **logical communication** flow within the HayRahCare ecosystem, demonstrating how independent AI agents collaborate to fulfill a user request.

### System Components

1.  **User Interface (Streamlit Web App):** 
    *   The network edge where the user initiates a request. 
    *   Following **User Interface (UI) design** principles , this serves as the entry point for mental health inquiries.
2.  **Coordinator Agent:**
    *   Acts as the central management layer, similar to the **management issues** covered in software engineering .
    *   Directs the workflow and handles task delegation between sub-agents.
3.  **Research Agent (arXiv API):**
    *   Utilizes an **Application Programming Interface (API)** to communicate with external academic databases .
    *   Retrieves relevant academic papers from the arXiv repository.
4.  **Summarizer Agent (Powered by Gemini):**
    *   Performs complex data analysis and synthesis.
    *   Uses advanced AI to transform raw research into evidence-based insights.
  
    ![Infographic Illustration:](notebooklm-agent.png)
    

## 🔄 Workflow Logic

The infographic uses a sequential flow to represent the system's **process** :

1.  **User Input:** Mental health question submitted via Streamlit.
2.  **Coordination:** Coordinator Agent analyzes the intent and activates the Research Agent.
3.  **Retrieval:** Research Agent fetches academic summaries via the arXiv API.
4.  **Synthesis:** Summarizer Agent (Gemini) analyzes the evidence.
5.  **Delivery:** The final synthesized response is returned to the user.



---
*Note: This architecture is a conceptual model for the HayRahCare Research Swarm.*
