import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from utils.sidebar import show_sidebar

show_sidebar()

# Logo da Fiap e da Paassos Mágicos
#st.divider()
_, col0, _ = st.columns([2, 3, 1])

with col0:
    st.image("images/logo-fiap.png", width=150)

with col0:
    st.image("images/Passos-magicos.png", width=150)

_, col0, _ = st.columns([1, 5, 1])
# Adding a header in the first column
with col0:
    st.header(f":blue[Datathon - ONG Passos Mágicos]")

# Container to manage the layout of the page
with st.container():
    # Creating two columns, with a 7:3 ratio
    col0, col1 = st.columns([10, 3])



    st.subheader(f":orange[Apresentação da Passos Mágicos] 📢")

    # Adding a detailed markdown description about the Passos Mágicos Association
    st.markdown(
        """
A ONG Passos Mágicos é uma organização sem fins lucrativos que desenvolve um trabalho fundamental na comunidade em que atua, transformando a vida de crianças, jovens e também adultos de baixa renda que por ela são atendidos.

A finalidade da Associação é contribuir para com a mudança, melhorias e o desenvolvimento das condições de vida dos seus alunos que se encontram em condições de vulnerabilidade social, utilizando-se da educação como a ferramenta para tanto.

Através de programas inovadores e uma equipe comprometida a Passos Mágicos tem transformado vidas, capacitando jovens a se tornarem cidadãos engajados e prontos para enfrentar os desafios da vida.

        """,
        unsafe_allow_html=True,
    )

    st.subheader(":orange[Objetivo 🎯 geral do presente trabalho] ")

    # Explanation of the main objectives of the Datathon
    st.markdown(
        """
        O objetivo do presente trabalho é transparecer os impactos que ONG Passos Mágicos vem causando na comunidade em que atua, além de viabilizar um melhor suporte na tomada de decisões pela gestão estratégica da Associação e proporcionar melhorias nos processos internos utilizados, como aquele destinado a concessão de bolsas de estudos. Dessa forma, estaremos contribuindo para com o aperfeiçoamento e crescimento da organização e, consequentemente, para com o desenvolvimento dessas crianças e jovens que estão buscando um melhor encaminhamento sócio profissional em suas vidas.

        Com base em informações educacionais, psicossociais e psicopedagogicas dos estudantes da Passos Mágicos, bem como nas demais infomrações a respeito das atividades da Associação disponíveis na base de dados fornecida, o presente trabalho aplicará metodologias e ferramentas de análise de dados até aqui absorvidas no Curso, como limpeza e tratamento dos dados, elaboração de dashboards (painéis gráficos) e modelos preditivos de redes neurais, conhecidos como Machine Learning, Deep Learning e Natural Language Processing (NLP). Assim, com base em toda essa tecnologia, a finalidade do trabalho será coletar insigths dessas informações, elaborar um storytelling e construir modelos preditivos para identificar se o perfil do aluno se enquadra como passível de alcançar o ponto de virada e avançar na sua performance e crescimento ou se o mesmo se enquadra para a obtenção de uma bolsa de estudos. 
        """,
        unsafe_allow_html=True,
    )

st.subheader(':orange[Indicadores 📌 utilizados para mensurar a perfomance e o desenvovimento dos alunos] ', divider="blue")

st.markdown('''A análise dos dados foi realizada com a base em dados oriundos da <b><font color='yellow'>PEDE (Pesquisa Extensiva do Desenvolvimento Educacional)</b></font> da Passos Mágicos.
            <br> <br> A informação mais representativa que a Associação utiliza na avaliação dos alunos é chamada <b><font color='yellow'>INDE (Índice Nacional de Desenvolvimento Educacional)</b></font>. Esse índice é composto pelos indicadores de Avaliaçõa e de Coselho, separados em 3 dimensões: acadêmica, psicosocial e psicopedagógica, onde são avaliados vários critérios como adequação de nível, desempenho acadêmico, engajamento, autoavaliação, aspectos psicossociais e psicopedagógicos.
            <br> <br> Com base nos valor do <b><font color='yellow'>INDE</b></font> é definida a <b><font color='yellow'>PEDRA</b></font> pela qual a performamce e desenvolvimento do aluno passa a ser melhor representada, até mesmo entre seus colegas, no sentido de estimular o avanço dos demais.
            ''', unsafe_allow_html=True)

st.markdown(
        """<b><font color='yellow'>Projeção Normal e limites da nota padronizada INDE Escolar</b></font>


        """,unsafe_allow_html=True,)
    
_, col4, _ = st.columns([1, 3, 1])
with col4:
        st.image("images/projecao_normal.png", width=1000)    


st.markdown(
        """<b><font color='yellow'>Faixas de Desempenho PEDRA-Conceito INDE Escolar</b></font>


        """,unsafe_allow_html=True,)
    
_, col4, _ = st.columns([1, 3, 1])
with col4:
        st.image("images/faixa_desempenho.png", width=1000)    

st.markdown('''<br> <br> A Associação também criou um indicador chamado <b><font color='yellow'>"Ponto de Virada"</b></font>, que representa um momento de significativa evolução nas condições de performance e desenvolvimento do aluno, concedendo-lhe o direito de ter a posse de uma Pedra de nível mais elevado, funcionando como uma medalha de honra ao mérito e estimulando os demais a também alcancçarem essa honraria.
            
            ''', unsafe_allow_html=True)

st.subheader(f":orange[Índices utilizados pela Passos Mágicos] 🗂️")

st.markdown(
        """ Os índices utilizados pela Passos Mágicos para mensurar a performance dos alunos estão classificados conforme abaixo:

        """,
        unsafe_allow_html=True,
    )
#with st.container():
tab0, tab1, tab2, tab3, tab4 = st.tabs(tabs=["INDE", "Pedras","Ponto de Virada", "Indicadores de Avaliação", "Indicadores do Conselho"])

with tab0:
    st.markdown('''O <b><font color='yellow'>Índice de Desenvolvimento Educacional (INDE)</b></font> da Associação Passos Mágicos é um indicador utilizada para avaliar o progresso educacional dos alunos atendidos pela instituição, sendo uma ferramenta fundamental para a Associação, pois permite monitorar e aprimorar suas estratégias educacionais, garantindo que cada aluno receba um suporte de excelência para alcançar seu pleno potencial. Esse índice é calculado de acordo com a fórmula apresentada logo abaixo:''', unsafe_allow_html=True)    

    _, col0, _ = st.columns([1, 3, 1])    

    with col0:
        st.image("images/indicators.png", width=1000)

    st.markdown(
        """<b><font color='yellow'>Composição do INDE (Índice de Desenvolvimento Educacional)</b></font>""",unsafe_allow_html=True,)

    _, col3, _ = st.columns([1, 3, 1])
    with col3:
        st.image("images/INDE.png", width=1000)    
    st.markdown(
        """<br>""", unsafe_allow_html=True) 
    st.markdown(
        """<b><font color='yellow'>Projeção Normal e limites da nota padronizada INDE Escolar</b></font>""",unsafe_allow_html=True,)
    
    _, col4, _ = st.columns([1, 3, 1])
    with col4:
        st.image("images/projecao_normal.png", width=1000)    


with tab1:
    st.markdown('''O esquema de classificação das pedras nos mostra os grupos de maios volumes de alunos, podendo ser vistos como níveis baixo, semi-intermediário, intermediário e avançado, abaixo deixo um gráfico pra demonstrar como ranking, a classificação das pedras, sendo Quartzo o nível mais baixo e Topázio que é o maior nível esses dois carregar as menores quantidades de alunos, e na sequência temos os níveis Ágata e Ametista como níveis intermediários que contém as maiores quantidades de alunos conforme visto no gráfico abaixo.''')
   
    st.markdown('''As <b><font color='yellow'>Pedras</b></font> podem ser definidas como o quanto os alunos estão pontuando, então ele entra num esquema de classificação, o que traz mais clareza na análise e atenção para o desenvolvimento de cada aluno e também dá uma visão mais competitiva aos alunos, porém eles irão almejar as melhores classificações. Até o último relatório PEDE tinhamos 4 pedras que são:''',unsafe_allow_html=True)
    st.markdown('''- <b><font color='yellow'>Quartzo:</b></font> Alunos com INDE entre <b><font color='yellow'>3,0 a 6,1</b></font>.''',unsafe_allow_html=True)
    st.markdown('''- <b><font color='yellow'>Ágata:</b></font> Alunos com INDE entre <b><font color='yellow'>6,1 a 7,2</b></font>.''',unsafe_allow_html=True)
    st.markdown('''- <b><font color='yellow'>Ametista:</b></font> Alunos com INDE entre <b><font color='yellow'>7,2 a 8,2</b></font>.''',unsafe_allow_html=True)
    st.markdown('''- <b><font color='yellow'>Topázio:</b></font> Alunos com INDE entre <b><font color='yellow'>8,2 a 9,4</b></font>.''',unsafe_allow_html=True)

    st.markdown(
        """<b><font color='yellow'>Faixas de Desempenho PEDRA-Conceito INDE Escolar</b></font>""",unsafe_allow_html=True,)
    
    _, col4, _ = st.columns([1, 3, 1])
    with col4:

        st.image("images/faixa_desempenho.png", width=1000)    

with tab2:
    st.markdown(''' O Ponto de virada indica que o aluno atingiu um passo mágico, é a conquista de uma habilidade fundamental, é medido através das notas, avaliações e outros dados, e demonstra que o aluno teve um grande progresso, essa evolução o ajudará a enfrentar vários desafios que encontrará pela frente, assim como:''' )
    st.markdown('''
    - Os alunos poderão superar dificuldades em matérias específicas e melhorar seu desempenho acadêmico,
    - Isso pode incluir avanços em leitura, matemática, ciências e outras áreas,
    - O ponto de virada traz consigo uma sensação de realização e confiança,
    - Os alunos se sentirão mais capazes e confiantes em suas habilidades,
    - Eles desenvolverão habilidades de comunicação, resolução de conflitos, empatia e trabalho em equipe,
    - Isso os ajudará a lidar com situações sociais e emocionais,
    - O ponto de virada também envolve uma ampliação da visão de mundo,
    - Os alunos estarão mais abertos a diferentes culturas, perspectivas e oportunidades,
    - Os alunos serão incentivados a assumir o protagonismo em suas vidas,
    - Eles tomarão decisões mais conscientes e terão maior autonomia,
    - O ponto de virada ensina a importância da persistência e da resiliência,
    - Os alunos saberão que podem superar obstáculos com esforço contínuo.
    ''')

  
with tab3:

    _, col0, _ = st.columns([1, 3, 1])

    with col0:
        st.image("images/evaluating_indicators.png", width=1000)

    st.markdown(
        """###### <br><font color='yellow'>IAN (Indicador de Adequação de Nível)</font>.
  Calculado com base na fase efetiva em que o aluno se encontra e na fase ideal em ele deveria estar.""", unsafe_allow_html=True)
    st.markdown("""
Fórmula: D = Fase Efetiva - Fase Ideal

Dados necessários:
-	Fase atual do estudante na Associação. Ex.: Fase efetiva: 5 ano
-	Fase ideal conforme a idade. Ex.: Fase ideal: 7 ano

Cálculo: D = 5 - 7 = -2  >>>  Assim, conforme tabela abaixo o resultado é: ....... Moderada = 5 pontos

        """,unsafe_allow_html=True,)

    _, col1, _ = st.columns([1, 3, 1])
    with col1:
        st.image("images/ian_calculating.png", width=1000)

    
    st.markdown(
        """###### <br><font color='yellow'>IDA (Indicador de Desempenho Acadêmico)</font>
Calculado com base nas notas das provas aplicadas pela Passos Mágicos e pela média geral das universitárias.""", unsafe_allow_html=True)
    
    st.markdown(
        """

Fórmula: IDA = (Nota Matemática + Nota Português + Nota Inglês) / 3

Dados necessários: Notas das provas aplicadas pela Passos Mágicos e pela média geral das universitárias.
        """,unsafe_allow_html=True,)

    st.markdown(
        """###### <br><font color='yellow'>IEG (Indicador de Engajamento)</font>
Calculado com base nos registros de entrega de lição de casa e de atividades de voluntariado.
        """, unsafe_allow_html=True)

    st.markdown(
        """    
Fórmula: IEG = Soma das pontuações das tarefas realizadas e registradas / Número de tarefas

Exemplos: Participação em tarefas de casa; Atividades acadêmicas; Voluntariado; etc.

        """,unsafe_allow_html=True,)

    st.markdown(
        """###### <br><font color='yellow'>IIAA (Indicador de Autoavaliação)</font>
Calculado com base em questionário de autoavaliação individual.""", unsafe_allow_html=True)
    
    st.markdown(
        """
Fórmula: IAA = Soma das pontuações das respostas do estudante / Número total de perguntas

PS: Perguntas avaliadas de 0 a 10

        """,unsafe_allow_html=True,)

    _, col2, _ = st.columns([1, 3, 1])
    with col2:
        st.image("images/questões _autoavaliação_e_seus_valores.png", width=1000)   

with tab4:

    _, col0, _ = st.columns([1, 3, 1])

    with col0:
        st.image("images/council_indicators.png", width=1000)

    st.markdown('''######  <br><font color='yellow'>IPS (Indicador Psicossocial)</font>
Calculado com base em questionário individual de avaliação elaborado pelas psicólogas.''',unsafe_allow_html=True)
    
    st.markdown(
        """
Fórmula: IPS = Soma das pontuações dos avaliadores / Número de avaliadores

PS: Avaliações feitas por psicólogos (comportamental, emocional, social)

        """,unsafe_allow_html=True,)
    
    st.markdown('''###### <br><font color='yellow'>IPP (Indicador Psicopedagógico)</font>
Calculado com base em questionário individual de avaliação elaborado pelas pedagogos e professores.''',unsafe_allow_html=True)
    st.markdown(
        """
Fórmula: IPP = Soma das avaliações sobre aspectos pedagógicos / Número de avaliações


        """,unsafe_allow_html=True,)
    
    st.markdown('''###### <br><font color='yellow'>IPV (Indicador do Ponto de Virada)</font>
Calculado com base em questionário individual de avaliação elaborado pelas pedagogos e professores.''',unsafe_allow_html=True)

    st.markdown(
        """

Fórmula: IPV = Análises longitudinais de progresso acadêmico, engajamento e desenvolvimento emocional


        """,unsafe_allow_html=True,)


st.markdown("""<br>""",unsafe_allow_html=True,)
st.subheader(':orange[Base de Dados 🗄️ e Dicionário 📙]', divider='blue')


tab9, tab10 = st.tabs(tabs=['Base de Dados', 'Dicionário'])
with tab9:

    
    # Carregando os dados
    url0 = "https://github.com/ponsoni74/app_datathon_passos_magicos/raw/refs/heads/main/data_2020_new.csv"
    url1 = "https://github.com/ponsoni74/app_datathon_passos_magicos/raw/refs/heads/main/data_2021_new.csv"
    url2 = "https://github.com/ponsoni74/app_datathon_passos_magicos/raw/refs/heads/main/data_2022_new.csv"
    url3 = "https://github.com/ponsoni74/app_datathon_passos_magicos/raw/refs/heads/main/data_2023_new.csv"
    url4 = "https://github.com/ponsoni74/app_datathon_passos_magicos/raw/refs/heads/main/data_2024_new.csv"

    response = requests.get(url0)
    csv_data_2020 = response.content
    response = requests.get(url1)
    csv_data_2021 = response.content
    response = requests.get(url2)
    csv_data_2022 = response.content
    response = requests.get(url3)
    csv_data_2023 = response.content
    response = requests.get(url4)
    csv_data_2024 = response.content

    st.markdown('''As bases de dados <b><font color='yellow'>(Datasets PEDE)</font></b> disponibilizadas pela Passos Mágicos foram reunidas, cuidadosamente limpas, tratadas e separadas por ano, e podem ser baixadas conforme abaixo.''', unsafe_allow_html=True)
    st.download_button(label="Baixar Base de Dados PEDE 2020 (csv)",data=csv_data_2020,file_name="DATASET_PEDE_2020.csv",mime="excel/csv")
    st.download_button(label="Baixar Base de Dados PEDE 2021 (csv)",data=csv_data_2021,file_name="DATASET_PEDE_2021.csv",mime="excel/csv")
    st.download_button(label="Baixar Base de Dados PEDE 2022 (csv)",data=csv_data_2022,file_name="DATASET_PEDE_2022.csv",mime="excel/csv")
    st.download_button(label="Baixar Base de Dados PEDE 2023 (csv)",data=csv_data_2023,file_name="DATASET_PEDE_2023.csv",mime="excel/csv")
    st.download_button(label="Baixar Base de Dados PEDE 2024 (csv)",data=csv_data_2024,file_name="DATASET_PEDE_2024.csv",mime="excel/csv")

with tab10:

    # Heading for the Data Dictionary section
    st.subheader(f":orange[Dicionário de Dados utilizados no presente trabalho]")

    data_dict = {

    "NOME": "Nome do Aluno (dados estão anonimizados)",
    "IDADE_ALUNO_2020": "Idade do Aluno em 2020",
    "ANO": "Ano de origem dos dados",
    "INSTITUICAO_ENSINO_ALUNO": "Informa o tipo de instituição de Ensino em que o aluno esta matriculado, se Pública ou Privada",
    "FASE": "Fase que o aluno se encontra enquadrado na Associação",
    "TURMA": "Tuma da fase em que o aluno se encontra enquadrado na Associação",
    "PEDRA_2020": "Classificação do Aluno baseado no número do INDE (2020), o conceito de classificação é dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294",
    "PONTO DE VIRADA": "Informa se o aluno atingiu o Ponto de Virada, que será representado quanto o campo ATINGIU_PV estiver preenchido com a opção AVANÇO",
    "ATINGIU_PV": "Campo criado pelo desenvolvedor para indicar a condição da PEDRA do aluno, se INGRESSANTE, MANTIDO, QUEDA ou AVANÇO",
    "INDE": "Índice do Desenvolvimento Educacional – Métrica de Processo Avaliativo Geral do Aluno, dado pela ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV em cada ano",
    "IAA": "Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em cada ano",
    "IEG": "Indicador de Engajamento – Média das Notas de Engajamento do Aluno em cada  ano",
    "IPS": "Indicador Psicossocial – Média das Notas Psicossociais do Aluno em cada ano",
    "IDA": "Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem em cada ano",
    "IPP": "Indicador Psicopedagógico – Média das Notas Psicopedagógicas do Aluno em cada ano",
    "IPV": "Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno cada ano",
    "IAN": "Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em cada"
    }
    df = pd.DataFrame(list(data_dict.items()), columns=["Nome da Coluna", "Detalhamento dos dados"])

    st.table(df)

