
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from agents.research_agent import hayrah_swarm

st.title("HayRahCare 🧠")
st.subheader("Mental Health Research Swarm")

question = st.text_input("Ask a mental health research question")

if st.button("Research"):

    answer, papers = hayrah_swarm(question)

    st.write("### Research Summary")
    st.write(answer)

    st.write("### Sources")

    for p in papers:
        st.write(p["title"])