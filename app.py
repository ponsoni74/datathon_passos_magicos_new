import streamlit as st
import warnings
from utils.sidebar import show_sidebar

home_page = st.Page("pages/presentation.py", title="Apresentação, Objetivo e Indicadores", icon="🎯")
datathon_specs_page = st.Page("pages/datathon_specs.py", title="Orientações para elaboração dos trabalhos", icon="📋")
data_analytics_page = st.Page("pages/data_analytics.py", title="Storytelling dos impactos alcançados", icon="🔭")
#bolsa_estudos_model_page = st.Page("pages/bolsa_estudos_model.py", title="Modelo Preditivo - Obtenção Bolsa de Estudos", icon="💡")
ponto_virada_model_page = st.Page("pages/ponto_virada_model.py", title="Modelo Preditivo - Alcance Ponto de Virada", icon="💡")

pg = st.navigation([home_page, datathon_specs_page, data_analytics_page, ponto_virada_model_page])  # bolsa_estudos_model_page,
st.set_page_config(layout="wide", page_title="Tech Challenge 5 | FIAP", page_icon=":material/edit:")
pg.run()


warnings.filterwarnings("ignore")

show_sidebar()