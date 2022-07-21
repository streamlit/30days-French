import streamlit as st
import os
import numpy as np
import pandas as pd
import urllib.request
from PIL import Image
import glob


def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)


md_files = sorted(
    [int(x.strip("Day").strip(".md")) for x in glob.glob1("content", "*.md")]
)

# Logo and Navigation
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("streamlit-logo-secondary-colormark-darktext.png"))
st.markdown("# 30 Days of Streamlit en Français! 🇫🇷")

days_list = [f"Day {x}" for x in md_files]

query_params = st.experimental_get_query_params()

if query_params and query_params["challenge"][0] in days_list:
    st.session_state.day = query_params["challenge"][0]

selected_day = st.selectbox(
    "Choisissez votre défi 👇", days_list, key="day", on_change=update_params
)

with st.expander("À propos du challenge #30DaysOfStreamlit"):
    st.markdown(
        """

    Le **#30DaysOfStreamlit** est un défi conçu pour vous aider à démarrer dans la création d'applications Streamlit.
    
     Vous pourrez notamment :
     - Configurer un environnement pour créer des apps Streamlit
     - Créez votre première app
     - Découvrir l'éventail des widgets à utiliser pour votre application!
    """
    )
    st.write("")

# Sidebar

st.sidebar.header("À propos")
st.sidebar.markdown(
    "[Streamlit](https://streamlit.io) est une bibliothèque open source Python qui permet la création d'applications Web interactives très facilement!"
)

st.sidebar.header("Resources")
st.sidebar.markdown(
    """
- [Documentation de Streamlit](https://docs.streamlit.io/)
- [Cheat sheet](https://docs.streamlit.io/library/cheatsheet)
- [Ouvrage](https://www.amazon.com/dp/180056550X) (Getting Started with Streamlit for Data Science)
- [Blog](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (How to master Streamlit for data science)
"""
)

st.sidebar.header("Déploiement")
st.sidebar.markdown(
    "Déployez vos applications Streamlit à l'aide de [Streamlit Cloud](https://streamlit.io/cloud) en quelques clics!"
)

# Display content
for i in days_list:
    if selected_day == i:
        st.markdown(f"# 🗓️ {i}")
        j = i.replace(" ", "")
        with open(f"content/{j}.md", "r") as f:
            st.markdown(f.read())
        if os.path.isfile(f"content/figures/{j}.csv") == True:
            st.markdown("---")
            st.markdown("### Figures")
            df = pd.read_csv(f"content/figures/{j}.csv", engine="python")
            for i in range(len(df)):
                st.image(f"content/images/{df.img[i]}")
                st.info(f"{df.figure[i]}: {df.caption[i]}")
