import streamlit as st

st.set_page_config(page_title="Portfólio - Rafael Viegas",\
                  layout = "wide")

mainPage = st.Page("home.py", title = "Home Page", icon = ":material/house:")
certPage = st.Page("certificacoes.py", title = "Certificações",  icon = ":material/star:")
contactPage = st.Page("contato.py", title = "Contato", icon = ":material/phone:")
projPage = st.Page("projetos.py", title = "Projetos", icon = ":material/folder:")

pg = st.navigation([mainPage, certPage, projPage, contactPage])
pg.run()