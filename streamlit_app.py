import streamlit as st

st.set_page_config(page_title="Portfólio - Rafael Viegas", layout = "wide")
st.title("Rafael Viegas de Carvalho")
st.subheader("Senior Technical Specialist | Telecom, Software Engineering & Data Science")
#valor = st.slider("Escolha um valor", 0, 100)
#st.write("Voce escolheu", valor)


col1, col2 = st.columns(2)

with col1:
    st.markdown('''
                Location: Belo Horizonte / MG
                
                E-mail: [rafavcc@gmail.com](mailto:rafavcc@gmail.com)
                
                [LinkedIn](https://www.linkedin.com/in/rafael-viegas)
                
                [GitHub](https://github.com/rafavcc)
                ''')
with col2:
    st.image("image.jpeg", width=200)
    
st.header("Sobre mim")
st.markdown("""
            Sou engenheiro com mais de 14 anos de experiência em Telecom, Software e Dados. 
Atualmente trabalho no desenvolvimento e liderança técnica de soluções para 5G e IMS, 
com forte atuação em automação, Python, troubleshooting e arquitetura de rede.
            """)


st.header("💼 Projetos")
st.markdown("""
### 📊 Analisador de Logs 5G
Ferramenta feita em Python para analisar logs de rede usando Wireshark, ELT e QXDM.  
[🔗 Código no GitHub](https://github.com/rafavcc/projeto-exemplo)

# 📈 Dashboard de Indicadores
ETL + visualização de KPIs para redes móveis com Streamlit e Plotly.  
[🔗 Código no GitHub](https://github.com/rafavcc/dashboard-kpi)
""")


st.header("Certificações")
st.markdown("""
- AWS Cloud Practitioner  
- Cisco CCNA  
- Huawei HCIA 5G / RNP&RNO / Datacom / Routing & Switching
- LPI Linux Essentials  
- MBA em Data Science (USP)  
""")

st.header("📬 Contato")
st.markdown("""
Quer conversar ou colaborar em um projeto?  
👉 [Me mande um email!](mailto:rafavcc@gmail.com)
""")