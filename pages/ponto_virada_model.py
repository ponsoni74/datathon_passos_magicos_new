import joblib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go


# Setting the title of the Streamlit app
st.title('**:green[Modelo Preditivo - Ponto de Virada]**')

# Providing a brief description of the app and the model it uses
st.markdown(
        """
        O modelo preditivo desenvolvido para a **:orange[ONG Passos Mágicos]** para prever a probabilidade que um aluno terá de avançar
        para a próxima fase com base nos indicadores de desempenho por ele alcançados até então,  foi elaborado com base em um algoritmo
        de Random Forest, conhecido por sua robustez em tarefas de classificação.

        """, unsafe_allow_html=True)

# Loading the pre-trained model and scaler from disk using joblib
with st.container():
    model_path = "model/random_forest_ponto_virada_model.pkl"
    scaler_path = "model/random_forest_ponto_virada_scaler.pkl"
    feature_importance_df = pd.read_csv(
        "output/ponto_virada_feature_importance.csv", sep=","
    )

    # Load the model and scaler using joblib
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)


    st.success("Modelo preditivo carregado com sucesso!")

    st.markdown(
        """
        <br>Razões pelas quais foi escolhido o modelo Random Forest:
        - **Interpretabilidade**: os modelos Random Forest são fáceis de interpretar e entender.
        - **Importância do recurso**: os modelos Random Forest fornecem importância dos atributos ou indicadores, o que ajuda a compreender o impacto de cada indicador na previsão.
        - **Robustez**: os modelos Random Forest são robustos ao overfitting e ao ruído nos dados.
        - **Relacionamentos não lineares**: os modelos Random Forest podem capturar relacionamentos não lineares entre recursos e a variável de destino.
        - **Lida com dados ausentes e conjuntos de dados desequilibrados**: os modelos Random Forest podem lidar com dados ausentes e conjuntos de dados desequilibrados de maneira eficaz. Pode ser ajustado com pesos de classe ou combinado com técnicas como SMOTE para lidar com classes desequilibradas
        
        """, unsafe_allow_html=True)

    st.markdown(
        """
        <br>Os indicadores de desempenho utilizados no modelo são os seguintes:

    ###### <font color='lightblue'>IPV - Indicador do Ponto de Virada</font>, calculado com base em questionário individual de avaliação elaborado pelas pedagogos e professores.
    ###### <font color='lightblue'>IPP - Indicador Psicopedagógico</font>, calculado com base em questionário individual de avaliação elaborado pelas pedagogos e professores.
    ###### <font color='lightblue'>IAA - Indicador de Autoavaliação</font>, calculado com base em questionário de autoavaliação individual.
    ###### <font color='lightblue'>IPS - Indicador Psicossocial</font>, calculado com base em questionário individual de avaliação elaborado pelas psicólogas.
    ###### <font color='lightblue'>IAN - Indicador de Adequação de Nível</font>, calculado com base na fase efetiva em que o aluno se encontra e na fase ideal em ele deveria estar.

        """, unsafe_allow_html=True)
    
    st.markdown(
        """
        O gráfico de importância de cada indicador abaixo mostra a importância, peso ou influência de cada um deles no modelo. Quanto maior o valor, mais importante é o indicador na previsão da probabilidade de avanço de fase do aluno.

        """, unsafe_allow_html=True)

    with st.container():

        # Plot using Plotly
        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=feature_importance_df['Importance'],
                y=feature_importance_df['Feature'],
                orientation='h',
                marker=dict(color='lightskyblue'),  # Set the color to light green
                name="Feature Importance",
            )
        )

        fig.update_layout(
            title="Importância dos Indicadores no modelo Random Forest",
            xaxis_title="Importância",
            yaxis_title="Indicador",
            yaxis=dict(
                autorange="reversed"  # To invert y-axis like plt.gca().invert_yaxis()
            ),
            height=600,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
            ),
        )

        # Display the plot in Streamlit
        st.plotly_chart(fig)

        # Explanation of how to use the controls and what the model predicts
    st.markdown(
        """    
Para fazer uso do modelo, é necessário informar nos campos abaixo os indicadores de desempenho alcançados pelo aluno. A seguir, para executar o modelo e descobrir se o aluno passará para a próxima fase com base em seu desempenho, é necessário clicar no botão **:orange[🎯Modelo, qual é a sua previsão?]**

**:red[ATENÇÂO]**: Os campos precisam ser preenchidos lentamente, caso contrário o modelo não reconhecerá a matriz de entrada no formato requerido.""", unsafe_allow_html=True)

    # Collecting input values for various student performance indicators from the user
    with st.container():
        col0, col1, col2, col3, col4 = st.columns(5)

        # Collecting input for IPV indicator
        with col0:
            indicator_ipv = st.number_input(
                label="**:blue[IPV]**",
                key="ipv",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )


        # Collecting input for IPP indicator
        with col1:
            indicator_ipp = st.number_input(
                label="**:blue[IPP]**",
                key="ipp",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )


        # Collecting input for IAA indicator
        with col2:
            indicator_iaa = st.number_input(
                label="**:blue[IAA]**",
                key="iaa",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )


        # Collecting input for IPS indicator
        with col3:
            indicator_ips = st.number_input(
                label="**:blue[IPS]**",
                key="ips",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )


        # Collecting input for IAN indicator
        with col4:
            indicator_ian = st.number_input(
                label="**:blue[IAN]**",
                key="ian",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )



    # Creating a DataFrame from the input values to feed into the model
    student_data = pd.DataFrame(
        {
            'IAA': indicator_iaa,
            'IPS': indicator_ips,
            'IPP': indicator_ipp,
            'IPV': indicator_ipv,
            'IAN': indicator_ian,
        },
        index=[0],
    )

    student_data_ordered = student_data.reindex(["IPV","IPP", "IAA","IPS","IAN"], axis=1)

    # Adding a button to trigger the model prediction
    if st.button("**:orange[🎯Modelo, qual é a sua previsão?]**", key="btn_predict_mlp"):
        with st.spinner("Processing..."):
            st.subheader(":blue[Dados de Entrada do Modelo]", divider="blue")
            st.dataframe(student_data_ordered, hide_index=True)

            st.subheader(":blue[Resposta do Modelo]", divider="blue")

            # Scaling the input data using the loaded scaler
            student_data_scaled = scaler.transform(student_data)

            # Predicting whether the student will pass to the next grade using the pre-trained model
            prediction = model.predict(student_data_scaled)

            # Displaying the result of the prediction
            if prediction.round()[0] > 0:
                st.success(
                    ":white_check_mark: **Previsão:** O aluno apresenta alta probabilidade de passar para uma fase mais elevada. 🏆"
                )
            else:
                st.error(
                    ":x: **Previsão:** O aluno apresenta baixa probabilidade de passar para uma fase mais elevada. 😞"
                )
