import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

#st.set_page_config(page_title="Datathon Dashboard",  page_icon="💎",layout = "wide")

st.subheader(f":orange[Proposta analítica  >>>   Storytelling e Dashboards]")

# Adding a detailed markdown description about the Passos Mágicos Association
st.markdown("""Analisar os indicadores para, com base neles, capturar insigths capazes de demonstrar os impactos que a ONG “Passos Mágicos” esta causando no desempenho, evolução e no desenvolvimento dos alunos, como por exemplo o avanço no alcance do Ponto de Virada e na consequente conquista de melhires Pedras, bem como a viabilidade para a obtenção de bolsa de estudos.
            
Dessa forma, será necessário que sejam elaborados <font color='yellowgreen'>**Dashboards**</font>, representando e clarificando o comportamento dos índices de desempenho dos alunos, e um <font color='pink'>**Storytelling**</font> identificando os insigths para auxiliar a Passos Mágicos a tomar as melhores decisões na gestão e, consequentemente, no perfil dos estudantes.""", unsafe_allow_html=True)


st.subheader(f":orange[Proposta preditiva > > > Modelos de Redes Neurais]")

st.markdown(
        """
Aqui será necessário criar um modelo preditivo para prever o comportamento do estudante com base em algumas variáveis que possam ser cruciais e capazes de serem usadas na identificação e fundamentação de seu avanço e desenvolvimento, tais como:<b><font color='yellow'> 
##### - Se o perfil do aluno se enquadra para o alcance do ponto de virada</font></b>, ou
##### <b><font color='pink'> - Se o perfil do aluno se enquadra para a obtenção de uma bolsa de estudos</font></b>. 

Na proposta preditiva, você pode utilizar a criatividade para propor uma solução de algoritmo supervisionado ou não supervisionado. A ideia é utilizar um dos conhecimentos aprendidos no curso como solução (machine learning, deep learning ou processamento de linguagem natural).
        """,
        unsafe_allow_html=True,
    )

st.subheader(f":orange[Desafios específicos a serem alcançados]")

st.markdown('''
- Interpretar os principais indicadores,
- Analisar e demonstrar o comportamento de cada indicador,
- Realizar comparação da evolução dos alunos por ano,
- Realizar comparação da evolução dos alunos por fase,
- Analisar o perfil individual de cada aluno,
- Analisar como se comportam as Pedras,
- Analisar e explicar a evolução do ponto de virada,
- Demonstrar graficamente em quais condições o ponto de virada é mais facilmente alcançado,
- Analisar como o INDE se comporta. 
''',
            unsafe_allow_html=True,)
