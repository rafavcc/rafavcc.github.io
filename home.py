import streamlit as st


st.title("Rafael Viegas de Carvalho")
st.subheader("Senior Technical Specialist | Telecom, Software Engineering & Data Science")

col1, col2 = st.columns(2)

with col1:
    st.markdown('''
                Localização: Belo Horizonte / MG
                
                E-mail: [rafavcc@gmail.com](mailto:rafavcc@gmail.com)
                
                [LinkedIn](https://www.linkedin.com/in/rafael-viegas)
                
                [GitHub](https://github.com/rafavcc)
                ''')
with col2:
    st.image("image.jpeg", width=200)
    
st.header("Sobre mim")
st.markdown("""
Sou engenheiro eletricista, formado na Universidade Federal de Minas Gerais (UFMG), 
com mais de 14 anos de experiência nas áreas de Telecomunicações, 
Engenharia de Software e Ciência de Dados, com uma carreira marcada pela inovação técnica,
liderança de equipes multidisciplinares e entrega de soluções de alto impacto.

Atuei no desenvolvimento e liderança técnica de funcionalidades avançadas para redes 5G, IMS,
VoLTE/VoNR e demais tecnologias de ponta. Tenho expertise sólida em automação de processos com Python,
análise de logs e KPIs, troubleshooting de redes móveis (GSM/UMTS/LTE/NR), além de domínio das 
especificações 3GPP e protocolos de comunicação como SIP, TCP/IP e RIL.

Sou apaixonado por tecnologia e resolução de problemas complexos — já conduzi projetos com mais de 100
operadoras em 33 países, colaborando com empresas como Samsung, Huawei, Nokia e Ericsson. Além disso,
venho aprofundando minha formação em dados e inteligência artificial, com MBA em Data Science
& Analytics (USP) e diversos projetos envolvendo ETL, visualização de dados e Machine Learning.

Recentemente concluí meu ciclo na última empresa, onde tive a oportunidade de atuar em posições 
de liderança técnica e desenvolvimento em larga escala. No momento, estou aberto a novos desafios
— especialmente nas áreas de Engenharia de Software, Ciência de Dados e Inteligência Artificial,
onde posso unir minha bagagem técnica com projetos orientados a dados e soluções inteligentes.
""")