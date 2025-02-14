import joblib
import streamlit as st
#from keras.models import load_model
import plotly.graph_objs as go
import pandas as pd
import numpy as np

st.title('**:blue[Modelo Preditivo - Bolsa de Estudos]**')
st.markdown(
    """
    O modelo preditivo para concessão de bolsa de estudos, desenvolvido para a **:orange[ONG Passos Mágicos]**, foi elaborado com base em um algoritmo de aprendizado de máquina para prever se um aluno é elegível ou não para receber uma bolsa de estudos com base em seus indicadores de desempenho.
    """
)

with st.container():
    model_path = "model/perfil_receber_bolsa_estudos_model.pkl"
    scaler_path = "model/perfil_receber_bolsa_estudos_scaler.pkl"

    # Load the model and scaler using joblib
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    epochs = np.array(range(2000))
    training = pd.read_csv(
        "model/model_training_data_hist.csv", sep=";"
    )

    st.success("Modelo preditivo carregado com sucesso!")

    st.markdown(
        """
        Os indicadores de desempenho utilizados no modelo são os seguintes:

    ###### <font color='lightblue'>INDE - Índice de Desenvolvimento Educacional.</font>
    ###### <font color='lightblue'>IAN - Indicador de Adequação de Nível</font>, calculado com base na fase efetiva em que o aluno se encontra e na fase ideal em ele deveria estar.
    ###### <font color='lightblue'>IDA - Indicador de Desempenho Acadêmico</font>, calculado com base nas notas das provas aplicadas pela Passos Mágicos e pela média geral das universitárias.
    ###### <font color='lightblue'>IEG - Indicador de Engajamento</font>, calculado com base nos registros de entrega de lição de casa e de atividades de voluntariado.
    ###### <font color='lightblue'>IAA - Indicador de Autoavaliação</font>, calculado com base em questionário de autoavaliação individual.
    ###### <font color='lightblue'>IPS - Indicador Psicossocial</font>, calculado com base em questionário individual de avaliação elaborado pelas psicólogas.
    ###### <font color='lightblue'>IPP - Indicador Psicopedagógico</font>, calculado com base em questionário individual de avaliação elaborado pelas pedagogos e professores.
    ###### <font color='lightblue'>IPV - Indicador do Ponto de Virada</font>, calculado com base em questionário individual de avaliação elaborado pelas pedagogos e professores.
        """, unsafe_allow_html=True)

    st.markdown(
        f"""
        Conforme os gráficos abaixo, o modelo foi avaliado com base nos indicadores de performance  **:blue["accuracy"]** e **:orange["loss"]**, que representam **:blue["precisão"]**  e **:orange["erro"]**, respectivamente. Tais indicadores mostram que o modelo está se comportando bem diante de dados novos fornecidos, indicando que ele não sofre de *overfitting*.

        """,
        unsafe_allow_html=True)
    
    with st.container():
        col0, col1 = st.columns(2)

        with col0:
            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=epochs,
                    y=training["accuracy"],
                    mode="lines",
                    name="Traning Accuracy",
                    marker=dict(color='lightskyblue')  # Set the color to light blue
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=epochs,
                    y=training["val_accuracy"],
                    mode="lines",
                    name="Validation Accuracy",
                    line=dict(color="orange"),
                )
            )

            fig.update_layout(
                title="Performance (Accuracy)",
                xaxis_title="Epochs",
                yaxis_title="Value",
                height=600,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                ),
            )

            st.plotly_chart(fig, use_container_width=True)

        with col1:
            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=epochs,
                    y=training["loss"],
                    mode="lines",
                    name="Loss of training",
                    marker=dict(color='#90ee90')  # Set the color to light blue
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=epochs,
                    y=training["val_loss"],
                    mode="lines",
                    name="Loss of Validation",
                    line=dict(color="red"),
                )
            )

            fig.update_layout(
                title="Performance (Loss)",
                xaxis_title="Epochs",
                yaxis_title="Value",
                height=600,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                ),
            )

            st.plotly_chart(fig, use_container_width=True)


    st.markdown(
        """Para fazer uso do modelo, é necessário informar nos campos abaixo os indicadores de desempenho alcançados pelo aluno. A seguir, para executar o modelo e descobrir se será possível conceder uma bolsa de estudos ao aluno, é necessário clicar no botão **:orange[🎯Modelo, qual é a sua recomendação?]**
    
**:red[ATENÇÂO]**: Os valores precisam ser preenchidos lentamente nos campos abaixo, caso contrário o modelo não reconhecerá a matriz de entrada no formato requerido.

        """, unsafe_allow_html=True)
    st.markdown(
        """O modelo fornece dois resultados possíveis:
- recomendar a **:blue[CONCESSÂO]** de bolsa de estudos ao aluno, ou
- recomendar a **:orange[NÃO CONCESSÂO]** de bolsa de estudos ao aluno.""")


    with st.container():
        col0, col1, col2, col3, col4, col5, col6, col7 = st.columns(8)


        with col0:
            indicator_inde = st.number_input(
                label="**:blue[INDE]**",
                key="inde",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col1:
            indicator_ian = st.number_input(
                label="**:blue[IAN]**",
                key="ian",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col2:
            indicator_ida = st.number_input(
                label="**:blue[IDA]**",
                key="ida",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col3:
            indicator_ieg = st.number_input(
                label="**:blue[IEG]**",
                key="ieg",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col4:
            indicator_iaa = st.number_input(
                label="**:blue[IAA]**",
                key="iaa",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col5:
            indicator_ips = st.number_input(
                label="**:blue[IPS]**",
                key="ips",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col6:
            indicator_ipp = st.number_input(
                label="**:blue[IPP]**",
                key="ipp",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col7:
            indicator_ipv = st.number_input(
                label="**:blue[IPV]**",
                key="ipv",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

    student_data = pd.DataFrame(
        {
            "IAA": indicator_iaa,
            "IAN": indicator_ian,
            "IDA": indicator_ida,
            "IEG": indicator_ieg,
            "INDE": indicator_inde,
            "IPP": indicator_ipp,
            "IPS": indicator_ips,
            "IPV": indicator_ipv,
        },
        index=[0],
    )

    student_data_ordered = student_data.reindex(["INDE","IAN","IDA","IEG","IAA","IPS","IPP","IPV"], axis=1)

    if st.button("🎯Modelo, qual é a sua recomendação?", key="btn_predict_mlp"):
        with st.spinner("Processing..."):
            st.subheader(":blue[Dados de Entrada do Modelo]", divider="blue")
            st.dataframe(student_data_ordered, hide_index=True)

            st.subheader(":blue[Resposta do Modelo]", divider="blue")
            student_data_scaled = scaler.transform(student_data)
            prediction = model.predict(student_data_scaled)

            if prediction.round()[0] > 0:
                st.success(
                    ":white_check_mark: O aluno é elegível 🏆, recomendo que seja concedida uma bolsa de estudo ao mesmo."
                )
            else:
                st.error(
                    ":x: O aluno não é elegível 😞, infelizmente não posso recomedar a concessão de uma bolsa de estudo ao mesmo "
                )
