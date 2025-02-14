import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from utils.charts import (
    format_number,
    plot_histograma,
)

# Carga dos datasets
df_2020 = pd.read_csv("output/data_2020_new.csv", sep=";", encoding="latin-1", engine="python", decimal=".")
df_2021 = pd.read_csv("output/data_2021_new.csv", sep=";", encoding="latin-1", engine="python", decimal=".")
df_2022 = pd.read_csv("output/data_2022_new.csv", sep=";", encoding="latin-1", engine="python", decimal=".")
df_2023 = pd.read_csv("output/data_2023_new.csv", sep=";", encoding="latin-1",engine="python", decimal=".")
df_2024 = pd.read_csv("output/data_2024_new.csv", sep=";", encoding="latin-1",engine="python", decimal=".")

# Ajuste da base 2020
df_2020 = df_2020.drop(columns=["Instituição de Ensino","CONSULTA","ANOS_PM","DESTAQUE_IEG","DESTAQUE_IDA","DESTAQUE_IPV"]).rename(columns={"Nome Anonimizado":"Nome","INDE 22":"INDE 2022"})

# Ajuste da base 2021
df_2021 = df_2021.drop(columns=["Instituição de Ensino","CONSULTA","SINALIZADOR_INGRESSANTE","REC_EQUIPE_1","REC_EQUIPE_2","REC_EQUIPE_3","REC_EQUIPE_4","NIVEL_IDEAL","DEFASAGEM"]).rename(columns={"Nome Anonimizado":"Nome","INDE 22":"INDE 2022"})

# Ajuste da base 2022
df_2022 = df_2022.drop(columns=["RA","Instituição de Ensino","CONSULTA","Ano nasc","Ano ingresso","Pedra 20","Pedra 21","STATUS_PEDRA","TESTE","Cg","Cf","Ct","Nº Av","Avaliador1","Rec Av1","Avaliador2","Rec Av2","Avaliador3","Rec Av3","Avaliador4","Rec Av4","Rec Psicologia","Matem","Portug","Inglês","Indicado","Atingiu PV","FASE IDEAL","DEFASAGEM","Destaque IEG","Destaque IDA","Destaque IPV"]).rename(columns={"Nome Anonimizado":"Nome","INDE 22":"INDE 2022"})

df_2022["INDE"] = df_2022["INDE"].str.replace(',','.')
df_2022["INDE"] = pd.to_numeric(df_2022["INDE"], errors='coerce').apply(lambda x: round(x,2))
df_2022["IAA"] = df_2022["IAA"].str.replace(',','.')
df_2022["IAA"] = pd.to_numeric(df_2022["IAA"], errors='coerce').apply(lambda x: round(x,1))
df_2022["IEG"] = df_2022["IEG"].str.replace(',','.')
df_2022["IEG"] = pd.to_numeric(df_2022["IEG"], errors='coerce').apply(lambda x: round(x,1))
df_2022["IPS"] = df_2022["IPS"].str.replace(',','.')
df_2022["IPS"] = pd.to_numeric(df_2022["IPS"], errors='coerce').apply(lambda x: round(x,1))
df_2022["IDA"] = df_2022["IDA"].str.replace(',','.')
df_2022["IDA"] = pd.to_numeric(df_2022["IDA"], errors='coerce').apply(lambda x: round(x,1))
df_2022["IPP"] = df_2022["IPP"].str.replace(',','.')
df_2022["IPP"] = pd.to_numeric(df_2022["IPP"], errors='coerce').apply(lambda x: round(x,2))
df_2022["IPV"] = df_2022["IPV"].str.replace(',','.')
df_2022["IPV"] = pd.to_numeric(df_2022["IPV"], errors='coerce').apply(lambda x: round(x,2))
df_2022["IAN"] = df_2022["IAN"].str.replace(',','.')
df_2022["IAN"] = pd.to_numeric(df_2022["IAN"], errors='coerce').apply(lambda x: round(x,1))

# Ajuste da base 2023
df_2023 = df_2023.drop(columns=["RA","Instituição de Ensino","CONSULTA","Data de Nasc","Ano ingresso","Pedra 20","Pedra 21","Pedra 22","Pedra 23","INDE 22","INDE 23","STATUS_PEDRA","TESTE","Cg","Cf","Ct","Nº Av","Avaliador1","Rec Av1","Avaliador2","Rec Av2","Avaliador3","Rec Av3","Avaliador4","Rec Av4","Rec Psicologia","Mat","Por","Ing","Indicado","Atingiu PV","FASE IDEAL","DEFASAGEM","Destaque IEG","Destaque IDA","Destaque IPV","Destaque IPV.1"]).rename(columns={"Nome Anonimizado":"NOME"})
df_2023["FASE"] = df_2023["FASE"].astype("int64")

df_2023["INDE"] = df_2023["INDE"].str.replace(',','.')
df_2023["INDE"] = pd.to_numeric(df_2023["INDE"], errors='coerce').apply(lambda x: round(x,2))
df_2023["IAA"] = df_2023["IAA"].str.replace(',','.')
df_2023["IAA"] = pd.to_numeric(df_2023["IAA"], errors='coerce').apply(lambda x: round(x,1))
df_2023["IEG"] = df_2023["IEG"].str.replace(',','.')
df_2023["IEG"] = pd.to_numeric(df_2023["IEG"], errors='coerce').apply(lambda x: round(x,1))
df_2023["IPS"] = df_2023["IPS"].str.replace(',','.')
df_2023["IPS"] = pd.to_numeric(df_2023["IPS"], errors='coerce').apply(lambda x: round(x,1))
df_2023["IDA"] = df_2023["IDA"].str.replace(',','.')
df_2023["IDA"] = pd.to_numeric(df_2023["IDA"], errors='coerce').apply(lambda x: round(x,1))
df_2023["IPP"] = df_2023["IPP"].str.replace(',','.')
df_2023["IPP"] = pd.to_numeric(df_2023["IPP"], errors='coerce').apply(lambda x: round(x,2))
df_2023["IPV"] = df_2023["IPV"].str.replace(',','.')
df_2023["IPV"] = pd.to_numeric(df_2023["IPV"], errors='coerce').apply(lambda x: round(x,2))
df_2023["IAN"] = df_2023["IAN"].str.replace(',','.')
df_2023["IAN"] = pd.to_numeric(df_2023["IAN"], errors='coerce').apply(lambda x: round(x,1))

# Ajuste da base 2024
df_2024 = df_2024.drop(columns=["RA","Instituição de Ensino","CONSULTA","Data de Nasc","Ano ingresso","Pedra 20","Pedra 21","Pedra 22","Pedra 23","INDE 22","INDE 23","STATUS_PEDRA","TESTE","Cg","Cf","Ct","Nº Av","Avaliador1","Rec Av1","Avaliador2","Rec Av2","Avaliador3","Avaliador4","Avaliador5","Avaliador6","Rec Psicologia","Mat","Por","Ing","Indicado","Atingiu PV","FASE IDEAL","DEFASAGEM","Destaque IEG","Destaque IDA","Destaque IPV","Escola","Ativo/ Inativo","Ativo/ Inativo.1"]).rename(columns={"Nome Anonimizado":"NOME"})

df_2024["INDE"] = df_2024["INDE"].str.replace(',','.')
df_2024["INDE"] = pd.to_numeric(df_2024["INDE"], errors='coerce').apply(lambda x: round(x,2))
df_2024["IAA"] = df_2024["IAA"].str.replace(',','.')
df_2024["IAA"] = pd.to_numeric(df_2024["IAA"], errors='coerce').apply(lambda x: round(x,1))
df_2024["IEG"] = df_2024["IEG"].str.replace(',','.')
df_2024["IEG"] = pd.to_numeric(df_2024["IEG"], errors='coerce').apply(lambda x: round(x,1))
df_2024["IPS"] = df_2024["IPS"].str.replace(',','.')
df_2024["IPS"] = pd.to_numeric(df_2024["IPS"], errors='coerce').apply(lambda x: round(x,1))
df_2024["IDA"] = df_2024["IDA"].str.replace(',','.')
df_2024["IDA"] = pd.to_numeric(df_2024["IDA"], errors='coerce').apply(lambda x: round(x,1))
df_2024["IPP"] = df_2024["IPP"].str.replace(',','.')
df_2024["IPP"] = pd.to_numeric(df_2024["IPP"], errors='coerce').apply(lambda x: round(x,2))
df_2024["IPV"] = df_2024["IPV"].str.replace(',','.')
df_2024["IPV"] = pd.to_numeric(df_2024["IPV"], errors='coerce').apply(lambda x: round(x,2))
df_2024["IAN"] = df_2024["IAN"].str.replace(',','.')
df_2024["IAN"] = pd.to_numeric(df_2024["IAN"], errors='coerce').apply(lambda x: round(x,1))

#df_full = pd.read_csv("output/data_full_old.csv", sep=";", encoding="utf-8",engine="python")
#df_full = pd.read_csv("output/data_full_new.csv", sep=";", encoding="latin-1",engine="python")
df_full = pd.concat([df_2020,df_2021,df_2022,df_2023,df_2024])
#print(df_full)

with st.container():
    st.header(f":orange[Análise de Dados 💡 com base em Dashboards 📊]")

    # Conversão do formato da contagem de número inteiro para string
    total_geral = format_number(len(df_full))
    #total_geral_new = format_number(len(df_full_new))
    total_2022 = format_number(len(df_2022))
    total_2023 = format_number(len(df_2023))
    total_2024 = format_number(len(df_2024))

    # Análise das instituições de ensino em que os alunos estudam
    st.subheader("Onde os alunos da Passoa Mágicos estudam", divider="blue")
    st.markdown("""
    No gráfico abaixo podemos identificar o tipo de instituição de ensino em que os alunos da **Passos Mágicos** estão matriculados.
    """)

    fig = go.Figure()
    value_counts_2020 = df_2020["INSTITUICAO_ENSINO_ALUNO"].value_counts()
    value_counts_2021 = df_2021["INSTITUICAO_ENSINO_ALUNO"].value_counts()
    value_counts_2022 = df_2022["INSTITUICAO_ENSINO_ALUNO"].value_counts()
    value_counts_2023 = df_2023["INSTITUICAO_ENSINO_ALUNO"].value_counts()
    value_counts_2024 = df_2024["INSTITUICAO_ENSINO_ALUNO"].value_counts()
    fig.add_trace(go.Bar(y=value_counts_2020.values,x=value_counts_2020.index, name='2020', text=value_counts_2020,  textposition="inside", marker_color='limegreen' ))
    fig.add_trace(go.Bar(y=value_counts_2021.values,x=value_counts_2021.index, name='2021', text=value_counts_2021,  textposition="inside", marker_color='indianred' ))
    fig.add_trace(go.Bar(y=value_counts_2022.values,x=value_counts_2022.index, name='2022', text=value_counts_2022,  textposition="inside", marker_color='royalblue' ))
    fig.add_trace(go.Bar(y=value_counts_2023.values,x=value_counts_2023.index, name='2023', text=value_counts_2023,  textposition="inside", marker_color='pink' ))
    fig.add_trace(go.Bar(y=value_counts_2024.values,x=value_counts_2024.index, name='2024', text=value_counts_2024,  textposition="inside", marker_color='yellow' ))
    fig.update_layout(
        title=f"Distirbuição do número de Alunos de acordo com o tipo de Escola em que estudam (Pública ou Privada)",
        xaxis_title=f'Escola',
        yaxis_title='Número de Alunos',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
        Como podemos obervar no gráfico acima como um primeiro insigth, é a comprovação do perfil dos alunos atendidos pela ONG ser de baixa renda, haja vista, quase na sua totalidade, serem provenientes de escola pública, comprovando a finalidade da **Passos Mágicos** em contribuir com a melhoria de vida desses alunos, que em sua grande maioria vive em condições precárias de vida. 
        Em relação àqueles em que o gráfico apresenta como provenientes de escola privada, são, na verdade, alunos beneficiados por algum tipo de benefício, tal como bolsa de estudos, parcerias ou apadrinhamento.
        <br>""", unsafe_allow_html=True)


    # Análise das instituições de ensino em que os alunos estudam
    st.subheader("Análise com base na distribuição do nº de Pedras/Alunos por Ano", divider="blue")

    fig = go.Figure()
    value_counts_2020 = df_2020["PEDRA"].value_counts()
    value_counts_2021 = df_2021["PEDRA"].value_counts()
    value_counts_2022 = df_2022["PEDRA"].value_counts()
    value_counts_2023 = df_2023["PEDRA"].value_counts()
    value_counts_2024 = df_2024["PEDRA"].value_counts()
    fig.add_trace(go.Bar(y=value_counts_2020.values,x=value_counts_2020.index, name='2020', text=value_counts_2020,  textposition="inside", marker_color='limegreen' ))
    fig.add_trace(go.Bar(y=value_counts_2021.values,x=value_counts_2021.index, name='2021', text=value_counts_2021,  textposition="inside", marker_color='indianred' ))
    fig.add_trace(go.Bar(y=value_counts_2022.values,x=value_counts_2022.index, name='2022', text=value_counts_2022,  textposition="inside", marker_color='royalblue'))
    fig.add_trace(go.Bar(y=value_counts_2023.values,x=value_counts_2023.index, name='2023', text=value_counts_2023,  textposition="inside", marker_color='pink' ))
    fig.add_trace(go.Bar(y=value_counts_2024.values,x=value_counts_2024.index, name='2024', text=value_counts_2024,  textposition="inside", marker_color='yellow' ))
    fig.update_xaxes(
        categoryorder = 'array',
        categoryarray = ['Quartzo','Ágata','Ametista','Topázio'])
    fig.update_layout(
        title=f"Distribuição do Número de Pedras/Alunos por Ano",
        xaxis_title=f'PEDRAS',
        yaxis_title='Número de Pedras/Alunos',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    st.plotly_chart(fig, use_container_width=True)

    #value_counts_full = df_full['PEDRAS'].value_counts()/5
    fig = go.Figure()
    value_counts_full = df_full
    value_counts_full = value_counts_full.groupby(['PEDRA'])['NOME'].count().reset_index()
    value_counts_full = value_counts_full.rename(columns={'NOME': 'Quantidade'})
    total_por_ano_full = value_counts_full.groupby('PEDRA')['Quantidade'].sum().reset_index()
    total_por_ano_full = total_por_ano_full.rename(columns={'Quantidade': 'Total_Ano'})
    value_counts_full['Percentual'] = value_counts_full['Quantidade'] / df_full['NOME'].count() * 100

    fig = px.bar(value_counts_full,  x='PEDRA', y='Percentual', orientation='v', title='Distribuição percentual do Status das PEDRAS/ALUNOS ao longo dos anos', text='Percentual',  #labels={'ANO': 'ANO', 'ATINGIU_PV': 'STATUS DA PEDRA', 'Percentual': 'Percentual de Status das Pedras/Alunos'},
                    category_orders={"ANO":  ['Quartzo','Ágata','Ametista','Topázio']})
    fig.update_xaxes(
        categoryorder = 'array',
        categoryarray = ['Quartzo','Ágata','Ametista','Topázio'])
    fig.update_layout(
        title=f"Distribuição percentual MÉDIA ANUAL do Número de Pedras/Alunos",
        xaxis_title=f'PEDRAS',
        yaxis_title='Número de Pedras/Alunos',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=15))  # Adjust the fontsize as needed
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='inside')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
        Analisando em conjunto os dois gráfico logo acima podemos identificar outros significativos insights, tais como: <br>
        - Mais de 41% dos alunos são detentores <font color='pink'>da pedra AMETISTA</font>, que é a penultima pedra, o que representa um excelete grau de aproveitamento, performance e desenvolvimento do aluno. 
        - Ao analisarmos no gráfico acima, entitulado <font color='yellow'>"Distribuição do Número de Pedras/Alunos apor Ano"</font>, os valores absolutos do número de Pedras/Alunos dos anos anteriores, podemos interpretar que estaria havendo um avanço na proporção de alunos detentores  <font color='pink'>de preda AMETISTA</font>, porém isso não se confirma ao analisarmos o gráfico logo abaixo, entitulado <font color='yellow'>"Distribuição percentual de Pedras/Alunos ao longo dos anos"</font>, onde podemos constatar que essa proporção, na verdade, reduziu de 41% para 43% de 2021 para 2024.
        - Entretanto, em que pese a proporção <font color='pink'>de pedras AMETISTA</font> tenha sofrido uma pequena redução ao longo dos últimos 4 anos, conforme informado no item anterior, podemos constatar também algo muitíssimo positivo para a <font color='yellow'>Passos Mágicos</font>, que é a evolução, ao longo dos últimos 5 anos, do número de alunos detentotes <font color='lightskyblue'>de pedra TOPÁZIO</font>, conforme podemos extrair do gráfico <font color='yellow'>"Distribuição percentual de PEDRAS/ALUNOS ao longo dos anos"</font>, uma evolução de 18% nos últimos 5 anos , em especial nos últimos 3 anos, cujo avanço foi de 16%. Isso representa um insigth fortíssimo para <font color='yellow'>a Associação</font> comprovar seus resultados e os impactos que tem proporcionado na comunidade onde desenvolve seu trabalho.
        <br>""", unsafe_allow_html=True)

########################################################

    # Distribuição do número de Alunos/Pedras ao longo dos anos
    df_pedra_full = df_full.groupby(['PEDRA', 'ANO'])['NOME'].count().reset_index()
    df_pedra_full = df_pedra_full.rename(columns={'NOME': 'Quantidade'})
    df_pedra_media_por_ano = df_pedra_full
    df_pedra_media_por_ano['Qtde_ANO'] = df_pedra_full['Quantidade']
    fig = px.bar(df_pedra_media_por_ano, x="ANO",y='Qtde_ANO', color='PEDRA', barmode = 'group', orientation='v', text = 'Qtde_ANO',
                    category_orders={"ANO": ['2020','2021','2022','2023','2024'],
                                     "PEDRA": ['Topázio','Ametista','Ágata','Quartzo']})
    fig.update_layout( 
        title=f"Distribuição do número de PEDRAS/ALUNOS ao longo dos anos",
        xaxis_title=f'ANO',
        yaxis_title='Número de Pedras/Alunos',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
        #legendgroup="group",
        #name="Quartzo",
        #mode="bars")

    fig.update_traces(texttemplate='%{text:.0f}', textposition='outside')

    st.plotly_chart(fig, use_container_width=True)

    # Distribuição percentual de Alunos/Pedras ao longo do anos
    df_pedra_ano = df_full.groupby(['PEDRA', 'ANO'])['NOME'].count().reset_index()
    df_pedra_ano = df_pedra_ano.rename(columns={'NOME': 'Quantidade'})
    total_por_ano = df_pedra_ano.groupby('ANO')['Quantidade'].sum().reset_index()
    total_por_ano = total_por_ano.rename(columns={'Quantidade': 'Total_Ano'})
    df_pedra_ano = df_pedra_ano.merge(total_por_ano, on='ANO')
    df_pedra_ano['Percentual'] = df_pedra_ano['Quantidade'] / df_pedra_ano['Total_Ano'] * 100       

    fig = px.bar(df_pedra_ano,  x='ANO', y='Percentual', color='PEDRA', title='Distribuição percentual de PEDRAS/ALUNOS ao longo dos anos', labels={'ANO': 'ANO', 'Percentual': 'Percentual de Pedras/Alunos'}, text='Percentual',
                    category_orders={"ANO": ['2020','2021','2022','2023','2024'],
                                     "PEDRA": ['Topázio','Ametista','Ágata','Quartzo']})
    fig.update_traces(texttemplate='%{text:.0f}%', textposition='inside')
    fig.update_xaxes(
            categoryorder = 'array',
            categoryarray = ['2020','2021','2022','2023','2024'])
    st.plotly_chart(fig, use_container_width=True)


   # Análise das instituições de ensino em que os alunos estudam
    st.subheader("Análise com base na distribuição do Status da Pedra por Ano", divider="blue")

    
    fig = go.Figure()
    #value_counts_2020 = df_2020["ATINGIU_PV"].value_counts()
    value_counts_2021 = df_2021["ATINGIU_PV"].value_counts()
    value_counts_2022 = df_2022["ATINGIU_PV"].value_counts()
    value_counts_2023 = df_2023["ATINGIU_PV"].value_counts()
    value_counts_2024 = df_2024["ATINGIU_PV"].value_counts()
    #fig.add_trace(go.Bar(y=value_counts_2020.values,x=value_counts_2020.index, name='2020', marker_color='limegreen' ))
    fig.add_trace(go.Bar(y=value_counts_2021.values,x=value_counts_2021.index, name='2021', text=value_counts_2021, textposition="inside", legendgrouptitle = dict(text='ANO'), marker_color='indianred' ))
    fig.add_trace(go.Bar(y=value_counts_2022.values,x=value_counts_2022.index, name='2022', text=value_counts_2022, textposition="inside", legendgrouptitle = dict(text='ANO'), marker_color='royalblue'))
    fig.add_trace(go.Bar(y=value_counts_2023.values,x=value_counts_2023.index, name='2023', text=value_counts_2023, textposition="inside", legendgrouptitle = dict(text='ANO'), marker_color='pink' ))
    fig.add_trace(go.Bar(y=value_counts_2024.values,x=value_counts_2024.index, name='2024', text=value_counts_2024, textposition="inside", legendgrouptitle = dict(text='ANO'), marker_color='yellow' ))
    fig.update_layout(       
        title=f"Distribuição do número de Alunos em relação ao Status da Pedra",
        xaxis_title=f'STATUS DA PEDRA',
        yaxis_title='Número de Alunos',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    fig.update_xaxes(
        categoryorder = 'array',
        categoryarray = ['INGRESSANTE','MANTIDO','QUEDA','AVANÇO'])
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""Ao analisar esse gráfico acima e o gráfico logo abaixo, construidos com base em valores absolutos (não percentuais ou proporcionais), podemos suspeitar das seguintes hipóteses:
- a proporção de "alunos INGRESSANTES" tem se mantido constante;
- a proporção da condição de "pedra conquistada como MANTIDA" tem se elevado ao longo dos último 4 anos;
- a proporção de "alunos que sofreram QUEDA" na pedra conquistada tem se elevado ao longo dos últimos 4 anos;
- a proporção de "alunos que perceberam AVANÇO" na pedra conquistada tem se elevado ao longo dos último 4 anos;
                
Porém ao analisarmos a distribuição percentual ou proporcional desse valores, ou seja, o número de cada um deles em relação ao total de alunos naquele ano, vamos perceber que, em especial para o caso da prorpoção de QUEDA ter se eleva, não é bem isso que esta acontecendo. .""")



    # Gráfico representando a evolução aos anos da condição de ATINGIU_PV
    df_atingiu_pv_full = df_full[df_full['ANO'] != 2020]
    #df_full_ANO_string['ANO'] = df_full_ANO_string['ANO'].astype(str)
    #df_full_ANO_string = df_full_ANO_string.assign(ITEM=df_full_ANO_string.index)
    df_atingiu_pv_full = df_atingiu_pv_full.groupby(['ATINGIU_PV', 'ANO'])['NOME'].count().reset_index()
    df_atingiu_pv_full = df_atingiu_pv_full.rename(columns={'NOME': 'Quantidade'})
    df_atingiu_pv_full['Qtde_ANO'] = df_atingiu_pv_full['Quantidade']
    fig = px.bar(df_atingiu_pv_full, x='ANO', y='Qtde_ANO', color='ATINGIU_PV', barmode = 'group', orientation='v', text = 'Qtde_ANO', labels={'ATINGIU_PV': 'STATUS DA PEDRA'},  # labels={'IDADE_ALUNO': 'Idade'}, text='FASE'
                category_orders={"ANO": ['2021','2022','2023','2024'],
                                 "ATINGIU_PV": ['AVANÇO','QUEDA','MANTIDO','INGRESSANTE']})

    fig.update_traces(texttemplate='%{text:.0f}', textposition='outside')

    fig.update_layout(
        title=f"Distribuição em quantidade numérica do status das Pedras/Alunos ao longo dos anos",
        xaxis_title=f'ANO',
        yaxis_title='Número de status das Pedras/Alunos',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    st.plotly_chart(fig, use_container_width=True)

    # Distribuição percentual de Alunos/Pedras ao longo do anos
    df_pedra_ano =  df_full[df_full['ANO'] != 2020]
    df_pedra_ano = df_pedra_ano.groupby(['ATINGIU_PV', 'ANO'])['NOME'].count().reset_index()
    df_pedra_ano = df_pedra_ano.rename(columns={'NOME': 'Quantidade'})
    total_por_ano = df_pedra_ano.groupby('ANO')['Quantidade'].sum().reset_index()
    total_por_ano = total_por_ano.rename(columns={'Quantidade': 'Total_Ano'})
    df_pedra_ano = df_pedra_ano.merge(total_por_ano, on='ANO')
    df_pedra_ano['Percentual'] = df_pedra_ano['Quantidade'] / df_pedra_ano['Total_Ano'] * 100       

    fig = px.bar(df_pedra_ano,  x='ANO', y='Percentual', color='ATINGIU_PV', barmode = 'group', orientation='v', title='Distribuição percentual do Status das PEDRAS/ALUNOS ao longo dos anos', labels={'ANO': 'ANO', 'ATINGIU_PV': 'STATUS DA PEDRA', 'Percentual': 'Percentual de Status das Pedras/Alunos'}, text='Percentual',
                    category_orders={"ANO": ['2021','2022','2023','2024'],
                                     "ATINGIU_PV": ['AVANÇO','QUEDA','MANTIDO','INGRESSANTE']})
    fig.update_traces(texttemplate='%{text:.0f}%', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
        A distribuição acima é uma das mais impactantes do presente trabalho, haja vista ela ser capaz de comprovar, de forma contrária ao que se imaginava  na análise acima feita com valores absolutos, quando se supunha um aumento na proporção do nº 
                 de QUEDA que os alunos estavam sofrendo na Pedra que tinham posse. Ou seja, algo negativo, quando o que desejamos é o contrátio. Assim, com base no grafico logo acima, que apresenta uma distribuição proporcional dos valores, podemos constatar efetivamente, na verdade:
    - que houve uma REDUÇÂO de 5%, nos últimos 4 anos, de 22% para 17%, no número de QUEDA que os alunos estavam sofrendo na Pedra que tinham posse; e além  disso, melhor ainda e tão mais impactante, é: 
    - que houve um AUMENTO de 5%, nos últimos 4 anos, de 11% para 16%, no número de AVANÇO que os alunos perceberam ao conquistarem melhores Pedras, <font color='yellow'>representando mais um excelente insight e uma grande conqusita para a Passos Mágico</font >.
    
    Porém, no que se refere a alunos ingressantes, no âmbito proporcional, houve, na verdade, uma redução na proporção de alunos ingressantes, o que talvez possa sinalizar um alerta para a Associação olhar com bastante cuidado esse fator. 
                         
                """, unsafe_allow_html=True)



    # Análise com base no Ponto de Virada
    st.subheader("Análise com base no Ponto de Virada", divider="blue")

    value_counts_2020 = df_2020["PEDRA"][df_2020["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2021 = df_2021["PEDRA"][df_2021["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2022 = df_2022["PEDRA"][df_2022["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2023 = df_2023["PEDRA"][df_2023["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2024 = df_2024["PEDRA"][df_2024["ATINGIU_PV"] == "AVANÇO"].value_counts()

    fig = go.Figure()
    fig.add_trace(go.Bar(y=value_counts_2020.values,x=value_counts_2020.index, name='2020', text=value_counts_2020,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='limegreen'))
    fig.add_trace(go.Bar(y=value_counts_2021.values,x=value_counts_2021.index, name='2021', text=value_counts_2021,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='limegreen'))
    fig.add_trace(go.Bar(y=value_counts_2022.values,x=value_counts_2022.index, name='2022', text=value_counts_2022,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='royalblue'))
    fig.add_trace(go.Bar(y=value_counts_2023.values,x=value_counts_2023.index, name='2023', text=value_counts_2023,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='pink' ))
    fig.add_trace(go.Bar(y=value_counts_2024.values,x=value_counts_2024.index, name='2024', text=value_counts_2024,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='salmon' ))
    fig.update_layout(       
            title=f"Distribuição de Pontos de Virada que ocorreram o longo de cada Ano de acordo com a PEDRA conquistada",
            xaxis_title=f'Pedra Alcançada',
            yaxis_title='Número de Pontos de Virada',
            bargap=0.15,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=10))  # Adjust the fontsize as needed
    fig.update_xaxes(
            matches=None,
            showticklabels=True, 
            type= 'category',
            ticklabelstep = 1,     
            categoryorder = 'array',
            categoryarray = ['Ágata','Ametista','Topázio'])

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
        No gráfico acima, podemos constatar que houve um elevado avanço na quantidade de pedras topázio que foram alcançadas de 2022 para 2023, na proporção de 260%, e de 2023 para 2024, na proporção de 160%, <font color='yellow'>representando mais um forte insight e uma grande conqusita para a Passos Mágico</font >.""", unsafe_allow_html=True)


    #value_counts_2020 = df_2020["GÊNERO"][df_2020["ATINGIU_PV"] == "AVANÇO"].value_counts()
    #value_counts_2021 = df_2021["GÊNERO"][df_2021["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2022 = df_2022["GÊNERO"][df_2022["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2023 = df_2023["GÊNERO"][df_2023["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2024 = df_2024["GÊNERO"][df_2024["ATINGIU_PV"] == "AVANÇO"].value_counts()

    fig = go.Figure()
    #fig.add_trace(go.Bar(y=value_counts_2020.values,x=value_counts_2020.index, name='2020', text=value_counts_2020,  textposition="outside", marker_color='limegreen'))
    #fig.add_trace(go.Bar(y=value_counts_2021.values,x=value_counts_2021.index, name='2021', text=value_counts_2021,  textposition="outside", marker_color='limegreen'))
    fig.add_trace(go.Bar(y=value_counts_2022.values,x=value_counts_2022.index, name='2022', text=value_counts_2022,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='royalblue'))
    fig.add_trace(go.Bar(y=value_counts_2023.values,x=value_counts_2023.index, name='2023', text=value_counts_2023,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='pink' ))
    fig.add_trace(go.Bar(y=value_counts_2024.values,x=value_counts_2024.index, name='2024', text=value_counts_2024,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='salmon' ))
    fig.update_layout(       
            title=f"Distribuição de Pontos de Virada que ocorreram o longo de cada Ano de acordo com o GÊNERO do aluno ",
            xaxis_title=f'Pedra Conquistada',
            yaxis_title='Número de Pontos de Virada',
            bargap=0.15,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=12))  # Adjust the fontsize as needed
    fig.update_xaxes(
            matches=None,
            showticklabels=True, 
            type= 'category',
            ticklabelstep = 1,     
            categoryorder = 'array',
            categoryarray = ['Feminino','Masculino'])

    st.plotly_chart(fig, use_container_width=True)

    value_counts_2020 = df_2020["FASE"][df_2020["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2021 = df_2021["FASE"][df_2021["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2022 = df_2022["FASE"][df_2022["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2023 = df_2023["FASE"][df_2023["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2024 = df_2024["FASE"][df_2024["ATINGIU_PV"] == "AVANÇO"].value_counts()

    fig = go.Figure()
    fig.add_trace(go.Bar(y=value_counts_2020.values,x=value_counts_2020.index, name='2020', text=value_counts_2020,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='limegreen'))
    fig.add_trace(go.Bar(y=value_counts_2021.values,x=value_counts_2021.index, name='2021', text=value_counts_2021,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='limegreen'))
    fig.add_trace(go.Bar(y=value_counts_2022.values,x=value_counts_2022.index, name='2022', text=value_counts_2022,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='royalblue'))
    fig.add_trace(go.Bar(y=value_counts_2023.values,x=value_counts_2023.index, name='2023', text=value_counts_2023,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='pink' ))
    fig.add_trace(go.Bar(y=value_counts_2024.values,x=value_counts_2024.index, name='2024', text=value_counts_2024,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='salmon' ))
    fig.update_layout(       
            title=f"Distribuição de Pontos de Virada que ocorreram o longo de cada Ano de acordo com a FASE em que o aluno se encontrava",
            xaxis_title=f'Fase em que o Aluno se encontra no momento em que conquistou a pedra e percebeu a virada e avanço de nível',
            yaxis_title='Número de Pontos de Virada',
            bargap=0.15,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=15))  # Adjust the fontsize as needed
    fig.update_xaxes(
            matches=None,
            showticklabels=True, 
            type= 'category',
            ticklabelstep = 1,     
            categoryorder = 'array',
            categoryarray = ['0','1','2','3','4','5','6','7','8'])

    st.plotly_chart(fig, use_container_width=True)


    value_counts_2020 = df_2020["IDADE_ALUNO"][df_2020["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2021 = df_2021["IDADE_ALUNO"][df_2021["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2022 = df_2022["IDADE_ALUNO"][df_2022["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2023 = df_2023["IDADE_ALUNO"][df_2023["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2024 = df_2024["IDADE_ALUNO"][df_2024["ATINGIU_PV"] == "AVANÇO"].value_counts()

    fig = go.Figure()
    fig.add_trace(go.Bar(y=value_counts_2020.values,x=value_counts_2020.index, name='2020', text=value_counts_2020,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='limegreen'))
    fig.add_trace(go.Bar(y=value_counts_2021.values,x=value_counts_2021.index, name='2021', text=value_counts_2021,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='limegreen'))
    fig.add_trace(go.Bar(y=value_counts_2022.values,x=value_counts_2022.index, name='2022', text=value_counts_2022,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='royalblue'))
    fig.add_trace(go.Bar(y=value_counts_2023.values,x=value_counts_2023.index, name='2023', text=value_counts_2023,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='pink' ))
    fig.add_trace(go.Bar(y=value_counts_2024.values,x=value_counts_2024.index, name='2024', text=value_counts_2024,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='salmon' ))
    fig.update_layout(       
            title=f"Distribuição de Pontos de Virada que ocorreram de acordo com a IDADE ao longo de cada Ano",
            xaxis_title=f'Idade',
            yaxis_title='Número de Pontos de Virada',
            bargap=0.15,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=10),  # Adjust the fontsize as needed
            )
    fig.update_xaxes(
            matches=None,
            showticklabels=True, 
            type= 'category',
            ticklabelstep = 1,     
            categoryorder = 'array',
            categoryarray = ['7','8','9','10','11','12','13','14','15','16','17','18','19'])

    st.plotly_chart(fig, use_container_width=True)


    # Análise das instituições de ensino em que os alunos estudam
    st.subheader("Análise com base no nº de alunos por FASE ao longo de cada ANO ", divider="blue")


    fig = go.Figure()
    value_counts_2020 = df_2020["FASE"][df_2020["FASE"] != 8].value_counts()
    value_counts_2021 = df_2021["FASE"].value_counts()
    value_counts_2022 = df_2022["FASE"].value_counts()
    value_counts_2023 = df_2023["FASE"].value_counts()
    value_counts_2024 = df_2024["FASE"].value_counts()
    fig.add_trace(go.Bar(y=value_counts_2020.values,x=value_counts_2020.index, name='2020', text=value_counts_2020,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='limegreen' ))
    fig.add_trace(go.Bar(y=value_counts_2021.values,x=value_counts_2021.index, name='2021', text=value_counts_2021,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='indianred' ))
    fig.add_trace(go.Bar(y=value_counts_2022.values,x=value_counts_2022.index, name='2022', text=value_counts_2022,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='royalblue'))
    fig.add_trace(go.Bar(y=value_counts_2023.values,x=value_counts_2023.index, name='2023', text=value_counts_2023,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='pink' ))
    fig.add_trace(go.Bar(y=value_counts_2024.values,x=value_counts_2024.index, name='2024', text=value_counts_2024,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='yellow' ))
    fig.update_layout(       
        title=f"Distribuição do número de Alunos por Fase ao longo de cada ano",
        xaxis_title=f'FASES',
        yaxis_title='Número de Alunos por Fase',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    
    st.plotly_chart(fig, use_container_width=True)


    st.markdown("""
        Como podemos obervar no gráfico acima,os alunos da Passos Màgico se concentram mais nas fases 0,1,2 e 3, que cobre mais o Ensino Fundamental.
        <br><br>""", unsafe_allow_html=True)


    # Análise das instituições de ensino em que os alunos estudam
    st.subheader("Análise com base na distribuição das Pedras ao longo de cada Fase ", divider="blue")

    st.markdown("""
        Obs.: Nos gráficos abaixo, com exceção de 2020, não foi possível contemplar a fase 8 em razão das informações não estarem diponiveis.""", unsafe_allow_html=True)
    
    st.markdown('''Ao analisarmos separadamento as pedras nos gráficos abaixo primeiramente pela quantidade no primeiro gráfico já podemos observar que as primeiras fases se sobressaem, ao ver o gráfico normatizado com o percentual, podemos ver uma estabilidade grande na distribuição do progresso dos alunos, porém ainda assim conseguimos ver destaques no Topazio nas fases 0, 4 e 8, nas fases intermediárias Ágata e Ametista estão quase todas acima do 50% dos alunos de cada fase com exceção a fase 8, e na Quartzo a fase que sai como destaque com menos alunos no nível mais baixo é a fase 7 seguida pelas duas primeiras fases.''', unsafe_allow_html=True)
    fig = go.Figure()
    value_counts_2020_Quartzo = df_2020['FASE'][df_2020["PEDRA"] == 'Quartzo'].value_counts()
    value_counts_2020_Agata = df_2020['FASE'][df_2020["PEDRA"] == 'Ágata'].value_counts()
    value_counts_2020_Ametista = df_2020['FASE'][df_2020["PEDRA"] == 'Ametista'].value_counts()
    value_counts_2020_Topazio = df_2020['FASE'][df_2020["PEDRA"] == 'Topázio'].value_counts()
    
    fig.add_trace(go.Bar(x=value_counts_2020_Quartzo.index,y=value_counts_2020_Quartzo.values, name='Quartzo', text=value_counts_2020_Quartzo,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='limegreen' ))
    fig.add_trace(go.Bar(x=value_counts_2020_Agata.index,y=value_counts_2020_Agata.values, name='Ágata', text=value_counts_2020_Agata,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='indianred' ))
    fig.add_trace(go.Bar(x=value_counts_2020_Ametista.index,y=value_counts_2020_Ametista.values, name='Ametista', text=value_counts_2020_Ametista,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='royalblue'))
    fig.add_trace(go.Bar(x=value_counts_2020_Topazio.index,y=value_counts_2020_Topazio.values, name='Topázio', text=value_counts_2020_Topazio,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='pink' ))
    fig.update_xaxes(
        categoryorder = 'array',
        categoryarray = ['Quartzo','Ágata','Ametista','Topázio'])
    fig.update_layout(
        title=f"Distribuição do número de Pedras/Alunos  por Fase ao longo do Ano de 2020",
        xaxis_title=f'FASES',
        yaxis_title='Número de Alunos com determinada Pedra',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    st.plotly_chart(fig, use_container_width=True)

    fig = go.Figure()
    value_counts_2021_Quartzo = df_2021['FASE'][df_2021["PEDRA"] == 'Quartzo'].value_counts()
    value_counts_2021_Agata = df_2021['FASE'][df_2021["PEDRA"] == 'Ágata'].value_counts()
    value_counts_2021_Ametista = df_2021['FASE'][df_2021["PEDRA"] == 'Ametista'].value_counts()
    value_counts_2021_Topazio = df_2021['FASE'][df_2021["PEDRA"] == 'Topázio'].value_counts()
    
    fig.add_trace(go.Bar(x=value_counts_2021_Quartzo.index,y=value_counts_2021_Quartzo.values, name='Quartzo', text=value_counts_2021_Quartzo,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='limegreen' ))
    fig.add_trace(go.Bar(x=value_counts_2021_Agata.index,y=value_counts_2021_Agata.values, name='Ágata', text=value_counts_2021_Agata,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='indianred' ))
    fig.add_trace(go.Bar(x=value_counts_2021_Ametista.index,y=value_counts_2021_Ametista.values, name='Ametista', text=value_counts_2021_Ametista,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='royalblue'))
    fig.add_trace(go.Bar(x=value_counts_2021_Topazio.index,y=value_counts_2021_Topazio.values, name='Topázio', text=value_counts_2021_Topazio,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='pink' ))
    fig.update_xaxes(
        categoryorder = 'array',
        categoryarray = ['Quartzo','Ágata','Ametista','Topázio'])
    fig.update_layout(
        title=f"Distribuição do número de Pedras/Alunos  por Fase ao longo do Ano de 2021",
        xaxis_title=f'FASES',
        yaxis_title='Número de Alunos com determinada Pedra',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    st.plotly_chart(fig, use_container_width=True)

    fig = go.Figure()
    value_counts_2022_Quartzo = df_2022['FASE'][df_2022["PEDRA"] == 'Quartzo'].value_counts()
    value_counts_2022_Agata = df_2022['FASE'][df_2022["PEDRA"] == 'Ágata'].value_counts()
    value_counts_2022_Ametista = df_2022['FASE'][df_2022["PEDRA"] == 'Ametista'].value_counts()
    value_counts_2022_Topazio = df_2022['FASE'][df_2022["PEDRA"] == 'Topázio'].value_counts()
    
    fig.add_trace(go.Bar(x=value_counts_2022_Quartzo.index,y=value_counts_2022_Quartzo.values, name='Quartzo', text=value_counts_2022_Quartzo,  textposition="outside", legendgrouptitle = dict(text='PDRA'), marker_color='limegreen' ))
    fig.add_trace(go.Bar(x=value_counts_2022_Agata.index,y=value_counts_2022_Agata.values, name='Ágata', text=value_counts_2022_Agata,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='indianred' ))
    fig.add_trace(go.Bar(x=value_counts_2022_Ametista.index,y=value_counts_2022_Ametista.values, name='Ametista', text=value_counts_2022_Ametista,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='royalblue'))
    fig.add_trace(go.Bar(x=value_counts_2022_Topazio.index,y=value_counts_2022_Topazio.values, name='Topázio', text=value_counts_2022_Topazio,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='pink' ))
    fig.update_xaxes(
        categoryorder = 'array',
        categoryarray = ['Quartzo','Ágata','Ametista','Topázio'])
    fig.update_layout(
        title=f"Distribuição do número de Pedras/Alunos  por Fase ao longo do Ano de 2022",
        xaxis_title=f'FASES',
        yaxis_title='Número de Alunos com determinada Pedra',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    st.plotly_chart(fig, use_container_width=True)

    fig = go.Figure()
    value_counts_2023_Quartzo = df_2023['FASE'][df_2023["PEDRA"] == 'Quartzo'].value_counts()
    value_counts_2023_Agata = df_2023['FASE'][df_2023["PEDRA"] == 'Ágata'].value_counts()
    value_counts_2023_Ametista = df_2023['FASE'][df_2023["PEDRA"] == 'Ametista'].value_counts()
    value_counts_2023_Topazio = df_2023['FASE'][df_2023["PEDRA"] == 'Topázio'].value_counts()
    
    fig.add_trace(go.Bar(x=value_counts_2023_Quartzo.index,y=value_counts_2023_Quartzo.values, name='Quartzo', text=value_counts_2023_Quartzo,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='limegreen' ))
    fig.add_trace(go.Bar(x=value_counts_2023_Agata.index,y=value_counts_2023_Agata.values, name='Ágata', text=value_counts_2023_Agata,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='indianred' ))
    fig.add_trace(go.Bar(x=value_counts_2023_Ametista.index,y=value_counts_2023_Ametista.values, name='Ametista', text=value_counts_2023_Ametista,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='royalblue'))
    fig.add_trace(go.Bar(x=value_counts_2023_Topazio.index,y=value_counts_2023_Topazio.values, name='Topázio', text=value_counts_2023_Topazio,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='pink' ))
    fig.update_xaxes(
        categoryorder = 'array',
        categoryarray = ['Quartzo','Ágata','Ametista','Topázio'])
    fig.update_layout(
        title=f"Distribuição do número de Pedras/Alunos  por Fase ao longo do Ano de 2023",
        xaxis_title=f'FASES',
        yaxis_title='Número de Alunos/Pedras por Fase',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    st.plotly_chart(fig, use_container_width=True)

    fig = go.Figure()
    value_counts_2024_Quartzo = df_2024['FASE'][df_2024["PEDRA"] == 'Quartzo'].value_counts()
    value_counts_2024_Agata = df_2024['FASE'][df_2024["PEDRA"] == 'Ágata'].value_counts()
    value_counts_2024_Ametista = df_2024['FASE'][df_2024["PEDRA"] == 'Ametista'].value_counts()
    value_counts_2024_Topazio = df_2024['FASE'][df_2024["PEDRA"] == 'Topázio'].value_counts()
    
    fig.add_trace(go.Bar(x=value_counts_2024_Quartzo.index,y=value_counts_2024_Quartzo.values, name='Quartzo', text=value_counts_2024_Quartzo,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='limegreen' ))
    fig.add_trace(go.Bar(x=value_counts_2024_Agata.index,y=value_counts_2024_Agata.values, name='Ágata', text=value_counts_2024_Agata,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='indianred' ))
    fig.add_trace(go.Bar(x=value_counts_2024_Ametista.index,y=value_counts_2024_Ametista.values, name='Ametista', text=value_counts_2024_Ametista,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='royalblue'))
    fig.add_trace(go.Bar(x=value_counts_2024_Topazio.index,y=value_counts_2024_Topazio.values, name='Topázio', text=value_counts_2024_Topazio,  textposition="outside", legendgrouptitle = dict(text='PEDRA'), marker_color='pink' ))
    fig.update_xaxes(
        categoryorder = 'array',
        categoryarray = ['Quartzo','Ágata','Ametista','Topázio'])
    fig.update_layout(
        title=f"Distribuição do número de Pedras/Alunos  por Fase ao longo do Ano de 2024",
        xaxis_title=f'FASES',
        yaxis_title='Número de Alunos/Pedrads por Fase',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    st.plotly_chart(fig, use_container_width=True)

    
# Distribuição de números e distribuição percentual de ALUNOS/PEDRAS em cada FASE'

   # Análise das instituições de ensino em que os alunos estudam
    st.subheader("Distribuição média ANUAL do nº de Pedras/Alunos por Fase", divider="blue")

    # Distribuição de números e distribuição percentual de ALUNOS/PEDRAS em cada FASE'
    df_pedra_aluno2 = df_full.groupby(['PEDRA', 'FASE'])['NOME'].count().reset_index()
    df_pedra_aluno2 = df_pedra_aluno2.rename(columns={'NOME': 'Quantidade'})
    total_por_fase = df_pedra_aluno2.groupby('FASE')['Quantidade'].sum().reset_index()
    total_por_fase = total_por_fase.rename(columns={'Quantidade': 'Total_Fase'})
    df_pedra_aluno2 = df_pedra_aluno2.merge(total_por_fase, on='FASE')
    df_pedra_aluno_media_por_ano = df_pedra_aluno2
    df_pedra_aluno_media_por_ano['Qtde_ANO'] = df_pedra_aluno2['Quantidade'] / 5
    df_pedra_aluno2['Percentual'] = df_pedra_aluno2['Quantidade'] / df_pedra_aluno2['Total_Fase'] * 100       
    fig = px.bar(df_pedra_aluno2,x='FASE', y='Qtde_ANO', color='PEDRA', title='Distribuição de MÉDIA ANUAL de PEDRAS/ALUNOS em cada FASE', labels={'FASE': 'FASE', 'Qtde_ANO': 'Número de Pedras/Alunos', 'Contagem': 'Contagem de Nomes'}, text='Qtde_ANO',
                    category_orders={"ANO": ['2020','2021','2022','2023','2024'],
                                     "PEDRA": ['Topázio','Ametista','Ágata','Quartzo']})
    fig.update_traces(texttemplate='%{text:.0f}', textposition='inside')
    st.plotly_chart(fig, use_container_width=True)
       
    fig = px.bar(df_pedra_aluno2,  x='FASE', y='Percentual', color='PEDRA', title='Distribuição percentual de MÉDIA ANUAL de PEDRAS/ALUNOS em cada FASE', labels={'FASE': 'FASE', 'Percentual': 'Percentual de Pedras/Alunos'}, text='Percentual',
                    category_orders={"ANO": ['2020','2021','2022','2023','2024'],
                                     "PEDRA": ['Topázio','Ametista','Ágata','Quartzo']})
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='inside')
    st.plotly_chart(fig, use_container_width=True)



   # Análise da distribuição etária
    st.subheader("Análise com base na Distribuição pela Faixa Etária dos Alunos", divider="blue")
    st.markdown("Conforme a distribuição etária presente nos gráficos abaixo, podemos perceber que a maioria total dos alunos são crianças e jovens adolescentes.")

    # Recuperando valores prejudicados de idade
    df_2020["IDADE_ALUNO"] = pd.to_numeric(df_2020["IDADE_ALUNO"], errors="coerce")
    df_2021["IDADE_ALUNO"] = pd.to_numeric(df_2021["IDADE_ALUNO"], errors="coerce")
    df_2022["IDADE_ALUNO"] = pd.to_numeric(df_2022["IDADE_ALUNO"], errors="coerce")
    df_2023["IDADE_ALUNO"] = pd.to_numeric(df_2023["IDADE_ALUNO"], errors="coerce")
    df_2024["IDADE_ALUNO"] = pd.to_numeric(df_2024["IDADE_ALUNO"], errors="coerce")

    fig = go.Figure()
    value_counts_2020 = df_2020["IDADE_ALUNO"][df_2020["IDADE_ALUNO"] < 20].value_counts()
    value_counts_2021 = df_2021["IDADE_ALUNO"][df_2021["IDADE_ALUNO"] < 20].value_counts()
    value_counts_2022 = df_2022["IDADE_ALUNO"][df_2022["IDADE_ALUNO"] < 20].value_counts()
    value_counts_2023 = df_2023["IDADE_ALUNO"][df_2023["IDADE_ALUNO"] < 20].value_counts()
    value_counts_2024 = df_2024["IDADE_ALUNO"][df_2024["IDADE_ALUNO"] < 20].value_counts()
    fig.add_trace(go.Bar(y=value_counts_2020.values,x=value_counts_2020.index, name='2020', text=value_counts_2020,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='limegreen'))
    fig.add_trace(go.Bar(y=value_counts_2021.values,x=value_counts_2021.index, name='2021', text=value_counts_2021,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='indianred'))
    fig.add_trace(go.Bar(y=value_counts_2022.values,x=value_counts_2022.index, name='2022', text=value_counts_2022,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='royalblue'))
    fig.add_trace(go.Bar(y=value_counts_2023.values,x=value_counts_2023.index, name='2023', text=value_counts_2023,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='pink' ))
    fig.add_trace(go.Bar(y=value_counts_2024.values,x=value_counts_2024.index, name='2024', text=value_counts_2024,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='yellow' ))
    fig.update_layout(       
        title=f"Distribuição do número de Alunos por Idade ao longo de cada Ano",
        xaxis_title=f'Idade',
        yaxis_title='Número de Alunos por Idade',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    fig.update_xaxes(
        matches=None,
        showticklabels=True, 
        type= 'category',
        ticklabelstep = 1,     
        categoryorder = 'array',
        categoryarray = ['7','8','9','10','11','12','13','14','15','16','17','18','19'])

    st.plotly_chart(fig, use_container_width=True)

    # Recuperando valores prejudicados de idade
    #df_2024["IDADE_ALUNO"] = pd.to_numeric(df_2024["IDADE_ALUNO"], errors="coerce")

    fig = go.Figure()
    value_counts_2024_fase_0 = df_2024["IDADE_ALUNO"][df_2024["FASE"] == 0].value_counts()
    value_counts_2024_fase_1 = df_2024["IDADE_ALUNO"][df_2024["FASE"] == 1].value_counts()
    value_counts_2024_fase_2 = df_2024["IDADE_ALUNO"][df_2024["FASE"] == 2].value_counts()
    value_counts_2024_fase_3 = df_2024["IDADE_ALUNO"][df_2024["FASE"] == 3].value_counts()
    value_counts_2024_fase_4 = df_2024["IDADE_ALUNO"][df_2024["FASE"] == 4].value_counts()
    value_counts_2024_fase_5 = df_2024["IDADE_ALUNO"][df_2024["FASE"] == 5].value_counts()
    value_counts_2024_fase_6 = df_2024["IDADE_ALUNO"][df_2024["FASE"] == 6].value_counts()
    value_counts_2024_fase_7 = df_2024["IDADE_ALUNO"][df_2024["FASE"] == 7].value_counts()
    value_counts_2024_fase_8 = df_2024["IDADE_ALUNO"][df_2024["FASE"] == 8].value_counts()

    fig.add_trace(go.Bar(y=value_counts_2024_fase_0.values,x=value_counts_2024_fase_0.index, name='FASE 0', text=value_counts_2024_fase_0,  textposition="outside", legendgrouptitle = dict(text='FASE'), marker_color='limegreen'))
    fig.add_trace(go.Bar(y=value_counts_2024_fase_1.values,x=value_counts_2024_fase_1.index, name='FASE 1', text=value_counts_2024_fase_1,  textposition="outside", legendgrouptitle = dict(text='FASE'), marker_color='indianred'))
    fig.add_trace(go.Bar(y=value_counts_2024_fase_2.values,x=value_counts_2024_fase_2.index, name='FASE 2', text=value_counts_2024_fase_2,  textposition="outside", legendgrouptitle = dict(text='FASE'), marker_color='royalblue'))
    fig.add_trace(go.Bar(y=value_counts_2024_fase_3.values,x=value_counts_2024_fase_3.index, name='FASE 3', text=value_counts_2024_fase_3,  textposition="outside", legendgrouptitle = dict(text='FASE'), marker_color='pink' ))
    fig.add_trace(go.Bar(y=value_counts_2024_fase_4.values,x=value_counts_2024_fase_4.index, name='FASE 4', text=value_counts_2024_fase_4,  textposition="outside", legendgrouptitle = dict(text='FASE'), marker_color='yellow' ))
    fig.add_trace(go.Bar(y=value_counts_2024_fase_5.values,x=value_counts_2024_fase_5.index, name='FASE 5', text=value_counts_2024_fase_5,  textposition="outside", legendgrouptitle = dict(text='FASE'), marker_color='salmon' ))
    fig.add_trace(go.Bar(y=value_counts_2024_fase_6.values,x=value_counts_2024_fase_6.index, name='FASE 6', text=value_counts_2024_fase_6,  textposition="outside", legendgrouptitle = dict(text='FASE'), marker_color='orange' ))
    fig.add_trace(go.Bar(y=value_counts_2024_fase_7.values,x=value_counts_2024_fase_7.index, name='FASE 7', text=value_counts_2024_fase_7,  textposition="outside", legendgrouptitle = dict(text='FASE'), marker_color='yellowgreen' ))
    #fig.add_trace(go.Bar(y=value_counts_2024_fase_8.values,x=value_counts_2024_fase_8.index, name='FASE 8', text=value_counts_2024_fase_8,  textposition="outside", legendgrouptitle = dict(text='FASE'), marker_color='green' ))

    fig.update_layout(       
        title=f"Distribuição do número de Alunos por Idade ao longo de cada FASE no contexto do ano 2024",
        xaxis_title=f'Idade',
        yaxis_title='Número de Alunos por Idade',
        bargap=0.001,  # Set the gap between bars
        bargroupgap=0.01,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    fig.update_xaxes(
        matches=None,
        showticklabels=True, 
        type= 'category',
        ticklabelstep = 1,     
        categoryorder = 'array',
        categoryarray = ['7','8','9','10','11','12','13','14','15','16','17','18','19'])


    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    NO gráfico acima podemos perceber a distribuição dos alunos, pela idade, no âmbito de cada FASE, ficando evidente que:
    -  na fase 0 temos alunos de "7" a "11" anos, 
    -  na fase 1 temos alunos de "8" a "13" anos, 
    -  na fase 2 temos alunos de "9" a "15" anos, 
    -  na fase 3 temos alunos de "11" a "16" anos, 
    -  na fase 4 temos alunos de "12" a "17" anos, 
    -  na fase 5 temos alunos de "13" a "18" anos, 
    -  na fase 6 temos alunos de "16" a "18" anos, 
    -  na fase 7 temos alunos de "15" a "19" anos, 
                
    """, unsafe_allow_html=True)


    # Calculo proporcional para grupos etários
    total_alunos = len(df_2022)+len(df_2023)+len(df_2024)
    alunos_8_17 = len(df_2022.query("IDADE_ALUNO >= 8 & IDADE_ALUNO <= 17")) + len(df_2023.query("IDADE_ALUNO >= 8 & IDADE_ALUNO <= 17")) + len(df_2024.query("IDADE_ALUNO >= 8 & IDADE_ALUNO <= 17"))
    proporcao_8_17 = format_number(alunos_8_17 / total_alunos * 100, "%0.2f") + "%"
    
    # Histograma da distribuição etária
    fig = plot_histograma(df_2023, "IDADE_ALUNO", "Distribuição percentual dos Alunos pela Faixa Etária (%) - Ano 2023", rug=False)
    st.plotly_chart(fig, use_container_width=True)

  # Histograma da distribuição etária
    fig = plot_histograma(df_2024, "IDADE_ALUNO", "Distribuição percentual dos Alunos pela Faixa Etária (%) - Ano 2024", rug=False)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    O histograma acima proporciona uma visão bem clara da distribuição etária dos alunos.
    Conforme podemos observar, por meio de uma distribuição proporcional, uma significante parcela de alunos atendidos pela **Passos Mágicos** tem idade entre **7** and **18** anos, 
    representando <font color='yellow'>**{proporcao_8_17}**</font> do total.
    """, unsafe_allow_html=True)

    # Recuperando valores prejudicados de idade
    df_2020["IDADE_ALUNO"] = pd.to_numeric(df_2020["IDADE_ALUNO"], errors="coerce")
    df_2021["IDADE_ALUNO"] = pd.to_numeric(df_2021["IDADE_ALUNO"], errors="coerce")
    df_2022["IDADE_ALUNO"] = pd.to_numeric(df_2022["IDADE_ALUNO"], errors="coerce")
    df_2023["IDADE_ALUNO"] = pd.to_numeric(df_2023["IDADE_ALUNO"], errors="coerce")
    df_2024["IDADE_ALUNO"] = pd.to_numeric(df_2024["IDADE_ALUNO"], errors="coerce")

    fig = go.Figure()
    value_counts_2020 = df_2020["IDADE_ALUNO"][df_2020["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2021 = df_2021["IDADE_ALUNO"][df_2021["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2022 = df_2022["IDADE_ALUNO"][df_2022["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2023 = df_2023["IDADE_ALUNO"][df_2023["ATINGIU_PV"] == "AVANÇO"].value_counts()
    value_counts_2024 = df_2024["IDADE_ALUNO"][df_2024["ATINGIU_PV"] == "AVANÇO"].value_counts()
    fig.add_trace(go.Bar(y=value_counts_2020.values,x=value_counts_2020.index, name='2020', text=value_counts_2020,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='limegreen'))
    fig.add_trace(go.Bar(y=value_counts_2021.values,x=value_counts_2021.index, name='2021', text=value_counts_2021,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='indianred'))
    fig.add_trace(go.Bar(y=value_counts_2022.values,x=value_counts_2022.index, name='2022', text=value_counts_2022,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='royalblue'))
    fig.add_trace(go.Bar(y=value_counts_2023.values,x=value_counts_2023.index, name='2023', text=value_counts_2023,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='pink' ))
    fig.add_trace(go.Bar(y=value_counts_2024.values,x=value_counts_2024.index, name='2024', text=value_counts_2024,  textposition="outside", legendgrouptitle = dict(text='ANO'), marker_color='yellow' ))
    fig.update_layout(       
        title=f"Quantidade de Alunos, por Idade, que conquistaram um avanço (PEDRA) ao longo dos anos",
        xaxis_title=f'Idade',
        yaxis_title='Número de Alunos por Idade',
        bargap=0.15,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10))  # Adjust the fontsize as needed
    fig.update_xaxes(
        matches=None,
        showticklabels=True, 
        type= 'category',
        ticklabelstep = 1,     
        categoryorder = 'array',
        categoryarray = ['7','8','9','10','11','12','13','14','15','16','17','18','19'])


    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    Podemos identificar, no gráfico acima, um significativo aumento no número de alunos que conquistaram um avanço (PEDRAS), de 2023 para 2024, ao longo de quase todas as idades, em especial nas idades iguais ou maiores que 14 anos""", unsafe_allow_html=True)


st.subheader("Histogramas associados ao comportamento dos Indicadores", divider="blue")
tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(tabs=["INDE", "IAN","IDA", "IEG", "IAA", "IPS", "IPP", "IPV"])

with tab0:
    st.markdown('''<b><font color='yellow'>INDE</b></font>''', unsafe_allow_html=True)    

    _, col0, _ = st.columns([1, 3, 1])    

    with col0:
        st.markdown(
            """<b><font color='yellow'>INDE (Índice de Desenvolvimento Educacional)</b></font>""",unsafe_allow_html=True,)

        fig = go.Figure()
        #fig.add_trace(go.Histogram(x=df_2022['GÊNERO'][df_2020["INDE"] > 3.5], name = "Feminino", legendgrouptitle = dict(text='GÊNERO'), marker_color='pink', nbinsx=10))
        #fig.add_trace(go.Histogram(x=df_2022['GÊNERO'][df_2021["INDE"] > 3.5], name = "Masculino", legendgrouptitle = dict(text='GÊNERO'), marker_color='royalblue', nbinsx=10))
        #fig.add_trace(go.Histogram(x=df_2022['INDE'][df_2022["INDE"] > 3.5], name = "2022", legendgrouptitle = dict(text='ANO'), marker_color='orange', nbinsx=10))
        #fig.add_trace(go.Histogram(x=df_2023['INDE'][df_2023["INDE"] > 3.5], name = "2023", legendgrouptitle = dict(text='ANO'), marker_color='limegreen', nbinsx=10))
        #fig.add_trace(go.Histogram(x=df_2024['INDE'][df_2024["INDE"] > 3.5], name = "2024", legendgrouptitle = dict(text='ANO'), marker_color='indianred', nbinsx=10))

        fig.update_layout(      
            title=f"Histograma do INDE ao longo dos anos de 2020, 2021 e 2022",
            xaxis_title=f'INDE',
            yaxis_title='Frequência',
            bargap=0.1,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=10),  # Adjust the fontsize as needed
            barmode='group')

        fig.update_xaxes(
            categoryorder = 'array',
            categoryarray = ['4','5','6','7','8','9'])

    #st.plotly_chart(fig, use_container_width=True)

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_2020['INDE'][df_2020["INDE"] > 3.5], name = "2020", legendgrouptitle = dict(text='ANO'), marker_color='pink', nbinsx=10))
    fig.add_trace(go.Histogram(x=df_2021['INDE'][df_2021["INDE"] > 3.5], name = "2021", legendgrouptitle = dict(text='ANO'), marker_color='royalblue', nbinsx=10))
    fig.add_trace(go.Histogram(x=df_2022['INDE'][df_2022["INDE"] > 3.5], name = "2022", legendgrouptitle = dict(text='ANO'), marker_color='orange', nbinsx=10))
    fig.add_trace(go.Histogram(x=df_2023['INDE'][df_2023["INDE"] > 3.5], name = "2023", legendgrouptitle = dict(text='ANO'), marker_color='limegreen', nbinsx=10))
    fig.add_trace(go.Histogram(x=df_2024['INDE'][df_2024["INDE"] > 3.5], name = "2024", legendgrouptitle = dict(text='ANO'), marker_color='indianred', nbinsx=10))

    fig.update_layout(      
        title=f"Histograma do INDE ao longo dos anos",
        xaxis_title=f'INDE',
        yaxis_title='Frequência',
        bargap=0.1,  # Set the gap between bars
        bargroupgap=0.1,  # Set the gap between groups of bars
        font=dict(size=10),  # Adjust the fontsize as needed
        barmode='group')

    fig.update_xaxes(
        categoryorder = 'array',
        categoryarray = ['4','5','6','7','8','9'])

    st.plotly_chart(fig, use_container_width=True)

    _, col2, _ = st.columns([1, 10, 1])
    with col2:
        st.image("images/projecao_normal.png", width=1000)  

with tab1:

    st.markdown(
            """<b><font color='yellow'>IAN - Indicador de Adequação de Nível</b></font>""",unsafe_allow_html=True,)
    
    _, col1, _ = st.columns([1, 5, 1])
    with col1:
        value_counts_2020 = df_2020["IAN"].value_counts()
        value_counts_2021 = df_2021["IAN"].value_counts()
        value_counts_2022 = df_2022["IAN"].value_counts()
        value_counts_2023 = df_2023["IAN"].value_counts()
        value_counts_2024 = df_2024["IAN"].value_counts()

        fig = go.Figure()
        fig.add_trace(go.Bar(y=value_counts_2020.values, x=value_counts_2020.index, name = "2020", legendgrouptitle = dict(text='ANO'), marker_color='pink'))
        fig.add_trace(go.Bar(y=value_counts_2021.values, x=value_counts_2021.index, name = "2021", legendgrouptitle = dict(text='ANO'), marker_color='royalblue'))
        fig.add_trace(go.Bar(y=value_counts_2022.values, x=value_counts_2022.index, name = "2022", legendgrouptitle = dict(text='ANO'), marker_color='orange'))
        fig.add_trace(go.Bar(y=value_counts_2023.values, x=value_counts_2023.index, name = "2023", legendgrouptitle = dict(text='ANO'), marker_color='limegreen'))
        fig.add_trace(go.Bar(y=value_counts_2024.values, x=value_counts_2024.index, name = "2024", legendgrouptitle = dict(text='ANO'), marker_color='indianred'))


        fig.update_layout(      
            title=f"Histograma IAN - Indicador de Adequação de Nível ao longo dos anos",
            xaxis_title=f'IAN',
            yaxis_title='Frequência',
            bargap=0.1,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=10),  # Adjust the fontsize as needed
            barmode='group')

        fig.update_xaxes(
            categoryorder = 'array',
            categoryarray = ['2.5','5','10'])

        st.plotly_chart(fig, use_container_width=True)
    
 
        fig = go.Figure()
            #fig.add_trace(go.Histogram(x=df_full['IAN'][df_2020["IAN"] > 3.5], name = "Feminino", legendgrouptitle = dict(text='GÊNERO'), marker_color='pink', nbinsx=8))
            #fig.add_trace(go.Histogram(x=df_full['IAN'][df_2021["IAN"] > 3.5], name = "Masculino", legendgrouptitle = dict(text='GÊNERO'), marker_color='royalblue', nbinsx=8))
            #fig.add_trace(go.Histogram(x=df_2022['IAN'][df_2022["IAN"] > 3.5], name = "2022", legendgrouptitle = dict(text='GÊNERO'), marker_color='orange', nbinsx=8))
            #fig.add_trace(go.Histogram(x=df_2023['IAN'][df_2023["IAN"] > 3.5], name = "2023", legendgrouptitle = dict(text='GÊNERO'), marker_color='limegreen', nbinsx=8))
            #fig.add_trace(go.Histogram(x=df_2024['IAN'][df_2024["IAN"] > 3.5], name = "2024", legendgrouptitle = dict(text='GÊNERO'), marker_color='indianred', nbinsx=8))

        fig.update_layout(      
            title=f"Histograma IAN - Indicador de Adequação de Nível ao longo dos anos",
            xaxis_title=f'IAN',
            yaxis_title='Frequência',
            bargap=0.1,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=10),  # Adjust the fontsize as needed
            barmode='group')

        fig.update_xaxes(
            categoryorder = 'array',
            categoryarray = ['2.5','5','10'])

        #st.plotly_chart(fig, use_container_width=True)

with tab2:
    #_, col0, _ = st.columns([1, 3, 1])
    st.markdown(
            """<b><font color='yellow'>IDA - Indicador de Desempenho Acadêmuico</b></font>""",unsafe_allow_html=True,)
    _, col1, _ = st.columns([1, 5, 1])
    with col1:   
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=df_2020['IDA'][df_2020["IDA"] > 1], name = "2020", legendgrouptitle = dict(text='ANO'), marker_color='pink', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2021['IDA'][df_2021["IDA"] > 1], name = "2021", legendgrouptitle = dict(text='ANO'), marker_color='royalblue', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2022['IDA'][df_2022["IDA"] > 1], name = "2022", legendgrouptitle = dict(text='ANO'), marker_color='orange', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2023['IDA'][df_2023["IDA"] > 1], name = "2023", legendgrouptitle = dict(text='ANO'), marker_color='limegreen', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2024['IDA'][df_2024["IDA"] > 1], name = "2024", legendgrouptitle = dict(text='ANO'), marker_color='indianred', nbinsx=8))

        fig.update_layout(      
            title=f"Histograma IDA - Indicador de Desempenho Acadêmuico ao longo dos anos",
            xaxis_title=f'IDA',
            yaxis_title='Frequência',
            bargap=0.1,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=10),  # Adjust the fontsize as needed
            barmode='group')

        fig.update_xaxes(
            categoryorder = 'array',
            categoryarray = ['4','5','6','7','8','9'])

        st.plotly_chart(fig, use_container_width=True)


with tab3:
    _, col0, _ = st.columns([1, 3, 1])
    st.markdown(
            """<b><font color='yellow'>IEG - Indicador de Engajamento </b></font>""",unsafe_allow_html=True,)
    _, col1, _ = st.columns([0.2, 3, 0.8])
    with col1:   
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=df_2020['IEG'][df_2020["IEG"] > 1], name = "2020", legendgrouptitle = dict(text='ANO'), marker_color='pink', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2021['IEG'][df_2021["IEG"] > 1], name = "2021", legendgrouptitle = dict(text='ANO'), marker_color='royalblue', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2022['IEG'][df_2022["IEG"] > 1], name = "2022", legendgrouptitle = dict(text='ANO'), marker_color='orange', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2023['IEG'][df_2023["IEG"] > 1], name = "2023", legendgrouptitle = dict(text='ANO'), marker_color='limegreen', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2024['IEG'][df_2024["IEG"] > 1], name = "2024", legendgrouptitle = dict(text='ANO'), marker_color='indianred', nbinsx=8))

        fig.update_layout(      
            title=f"Histograma do IEG - Indicador de Engajamento ao longo dos anos",
            xaxis_title=f'IEG',
            yaxis_title='Frequência',
            bargap=0.1,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=10),  # Adjust the fontsize as needed
            barmode='group')

        fig.update_xaxes(
            categoryorder = 'array',
            categoryarray = ['4','5','6','7','8','9'])

        st.plotly_chart(fig, use_container_width=True)


with tab4:
    _, col0, _ = st.columns([1, 3, 1])
    st.markdown(
            """<b><font color='yellow'>IAA - Indicador de Autoavaliação  </b></font>""",unsafe_allow_html=True,)
    _, col1, _ = st.columns([1, 3, 1])
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=df_2020['IAA'][df_2020["IAA"] > 1], name = "2020", legendgrouptitle = dict(text='ANO'), marker_color='pink', nbinsx=10))
        fig.add_trace(go.Histogram(x=df_2021['IAA'][df_2021["IAA"] > 1], name = "2021", legendgrouptitle = dict(text='ANO'), marker_color='royalblue', nbinsx=10))
        fig.add_trace(go.Histogram(x=df_2022['IAA'][df_2022["IAA"] > 1], name = "2022", legendgrouptitle = dict(text='ANO'), marker_color='orange', nbinsx=10))
        fig.add_trace(go.Histogram(x=df_2023['IAA'][df_2023["IAA"] > 1], name = "2023", legendgrouptitle = dict(text='ANO'), marker_color='limegreen', nbinsx=10))
        fig.add_trace(go.Histogram(x=df_2024['IAA'][df_2024["IAA"] > 1], name = "2024", legendgrouptitle = dict(text='ANO'), marker_color='indianred', nbinsx=10))

        fig.update_layout(      
            title=f"Histograma do IAA - Indicador de Autoavaliação ao longo dos anos",
            xaxis_title=f'IAA',
            yaxis_title='Frequência',
            bargap=0.1,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=10),  # Adjust the fontsize as needed
            barmode='group')

        fig.update_xaxes(
            categoryorder = 'array',
            categoryarray = ['4','5','6','7','8','9'])

    st.plotly_chart(fig, use_container_width=True)


with tab5:
    _, col0, _ = st.columns([1, 3, 1])
    st.markdown(
            """<b><font color='yellow'>IPS - Indicador Psicososcial</b></font>""",unsafe_allow_html=True,)
    _, col1, _ = st.columns([0.2, 3, 0.2])
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=df_2020['IPS'][df_2020["IPS"] > 1], name = "2020", legendgrouptitle = dict(text='ANO'), marker_color='pink', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2021['IPS'][df_2021["IPS"] > 1], name = "2021", legendgrouptitle = dict(text='ANO'), marker_color='royalblue', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2022['IPS'][df_2022["IPS"] > 1], name = "2022", legendgrouptitle = dict(text='ANO'), marker_color='orange', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2023['IPS'][df_2023["IPS"] > 1], name = "2023", legendgrouptitle = dict(text='ANO'), marker_color='limegreen', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2024['IPS'][df_2024["IPS"] > 1], name = "2024", legendgrouptitle = dict(text='ANO'), marker_color='indianred', nbinsx=8))

        fig.update_layout(      
            title=f"Histograma do IPS - Indicador Psicososcial ao longo dos anos",
            xaxis_title=f'IPS',
            yaxis_title='Frequência',
            bargap=0.3,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=10),  # Adjust the fontsize as needed
            barmode='group')

        fig.update_xaxes(
            categoryorder = 'array',
            categoryarray = ['4','5','6','7','8','9'])

        st.plotly_chart(fig, use_container_width=True)


with tab6:
    _, col0, _ = st.columns([1, 3, 1])
    st.markdown(
            """<b><font color='yellow'>IPP - Indicador Psicopedagógico</b></font>""",unsafe_allow_html=True,)
    _, col1, _ = st.columns([0.2, 3, 0.2])
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=df_2020['IPP'][df_2020["IPP"] > 1], name = "2020", legendgrouptitle = dict(text='ANO'), marker_color='pink', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2021['IPP'][df_2021["IPP"] > 1], name = "2021", legendgrouptitle = dict(text='ANO'), marker_color='royalblue', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2022['IPP'][df_2022["IPP"] > 1], name = "2022", legendgrouptitle = dict(text='ANO'), marker_color='orange', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2023['IPP'][df_2023["IPP"] > 1], name = "2023", legendgrouptitle = dict(text='ANO'), marker_color='limegreen', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2024['IPP'][df_2024["IPP"] > 1], name = "2024", legendgrouptitle = dict(text='ANO'), marker_color='indianred', nbinsx=8))

        fig.update_layout(      
            title=f"Histograma do IPP - Indicador Psicopedagógico ao longo dos anos",
            xaxis_title=f'IPP',
            yaxis_title='Frequência',
            bargap=0.3,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=10),  # Adjust the fontsize as needed
            barmode='group')

        fig.update_xaxes(
            categoryorder = 'array',
            categoryarray = ['4','5','6','7','8','9'])

        st.plotly_chart(fig, use_container_width=True)



with tab7:
    _, col0, _ = st.columns([1, 3, 1])
    st.markdown(
            """<b><font color='yellow'>IPV - Indicador de Ponto de Virada</b></font>""",unsafe_allow_html=True,)
    _, col1, _ = st.columns([0.2, 3, 0.2])
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=df_2020['IPV'][df_2020["IPV"] > 3.5], name = "2020", legendgrouptitle = dict(text='ANO'), marker_color='pink', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2021['IPV'][df_2021["IPV"] > 3.5], name = "2021", legendgrouptitle = dict(text='ANO'), marker_color='royalblue', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2022['IPV'][df_2022["IPV"] > 3.5], name = "2022", legendgrouptitle = dict(text='ANO'), marker_color='orange', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2023['IPV'][df_2023["IPV"] > 3.5], name = "2023", legendgrouptitle = dict(text='ANO'), marker_color='limegreen', nbinsx=8))
        fig.add_trace(go.Histogram(x=df_2024['IPV'][df_2024["IPV"] > 3.5], name = "2024", legendgrouptitle = dict(text='ANO'), marker_color='indianred', nbinsx=8))

        fig.update_layout(      
            title=f"Histograma do IPV - Indicador de Ponto de Virada ao longo dos anos",
            xaxis_title=f'IPV',
            yaxis_title='Frequência',
            bargap=0.3,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=10),  # Adjust the fontsize as needed
            barmode='group')

        fig.update_xaxes(
            categoryorder = 'array',
            categoryarray = ['4','5','6','7','8','9'])

        st.plotly_chart(fig, use_container_width=True)


        df_2020_ipv = df_2020['IPV'][df_2020["IPV"] > 3.5][df_2020["FASE"] == 2]
        df_2020_fase = df_2020['FASE'][df_2020["IPV"] > 3.5][df_2020["FASE"] == 2]
        df_2020_ipv_fase = pd.concat([df_2020_ipv,df_2020_fase], axis = 1)

        df_2021_ipv = df_2021['IPV'][df_2021["IPV"] > 3.5][df_2021["FASE"] == 2]
        df_2021_fase = df_2021['FASE'][df_2021["IPV"] > 3.5][df_2021["FASE"] == 2]
        df_2021_ipv_fase = pd.concat([df_2021_ipv,df_2021_fase], axis = 1)

        df_2022_ipv = df_2022['IPV'][df_2022["IPV"] > 3.5][df_2022["FASE"] == 2]
        df_2022_fase = df_2022['FASE'][df_2022["IPV"] > 3.5][df_2022["FASE"] == 2]
        df_2022_ipv_fase = pd.concat([df_2022_ipv,df_2022_fase], axis = 1)
        
        df_2023_ipv = df_2023['IPV'][df_2023["IPV"] > 3.5][df_2023["FASE"] == 2]
        df_2023_fase = df_2023['FASE'][df_2023["IPV"] > 3.5][df_2023["FASE"] == 2]
        df_2023_ipv_fase = pd.concat([df_2023_ipv,df_2023_fase], axis = 1)

        df_2024_ipv = df_2024['IPV'][df_2024["IPV"] > 3.5][df_2024["FASE"] == 2]
        df_2024_fase = df_2024['FASE'][df_2024["IPV"] > 3.5][df_2024["FASE"] == 2]
        #df_2024_ipv
        #df_2024_fase
        #x = df_2024_ipv.count()
        #y = df_2024_fase.count()
        #x
        #y
        df_2024_ipv_fase = pd.concat([df_2024_ipv,df_2024_fase], axis = 1)
        #z = df_2024_ipv_fase.count()
        #z
        #df_2024_ipv_fase

        #fig = go.Figure()
        #fig.add_trace(go.Histogram(x=df_2020_ipv_fase['IPV'], name = "2020", legendgrouptitle = dict(text='ANO'), marker_color='pink', nbinsx=9))
        #fig.add_trace(go.Histogram(x=df_2021_ipv_fase['IPV'], name = "2021", legendgrouptitle = dict(text='ANO'), marker_color='royalblue', nbinsx=9))
        #fig.add_trace(go.Histogram(x=df_2022_ipv_fase['IPV'], name = "2022", legendgrouptitle = dict(text='ANO'), marker_color='orange', nbinsx=9))
        #fig.add_trace(go.Histogram(x=df_2023_ipv_fase['IPV'], name = "2023", legendgrouptitle = dict(text='ANO'), marker_color='limegreen', nbinsx=9))
        #fig.add_trace(go.Histogram(x=df_2024_ipv_fase['IPV'], name = "2024", legendgrouptitle = dict(text='ANO'), marker_color='indianred', nbinsx=9))

        fig.update_layout(      
            title=f"Histograma do IPV na Fase 2 - Indicador de Ponto de Virada na FASE 2 ao longo dos anos",
            xaxis_title=f'IPV',
            yaxis_title='Frequência',
            bargap=0.3,  # Set the gap between bars
            bargroupgap=0.1,  # Set the gap between groups of bars
            font=dict(size=10),  # Adjust the fontsize as needed
            barmode='group')

        fig.update_xaxes(
            categoryorder = 'array',
            categoryarray = ['4','5','6','7','8','9'])

        #st.plotly_chart(fig, use_container_width=True)