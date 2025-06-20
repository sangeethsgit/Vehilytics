import streamlit as st

pages =  [st.Page("home.py", title="EDA"),
          st.Page("dashboard.py",title="Dashboard")]


pg = st.navigation(pages,position="sidebar",expanded=False)
pg.run()