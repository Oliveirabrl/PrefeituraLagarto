import streamlit as st
import pandas as pd

# Carregar e tratar os dados
dados = pd.read_excel("2025.xlsx", sheet_name="aaa")
dados = dados.rename(columns={"Empenhado": "Projetado"})
dados = dados.rename(columns={"Credor": "Quem Recebeu"})

# Configurações do dashboard
st.set_page_config(layout="wide")
st.title("Gastos da Prefeitura")
st.text("Painel de gastos da Prefeitura de Lagarto/Sergipe")
st.divider()

# Injetar CSS personalizado para mudar a cor do texto dentro do campo de entrada
st.markdown(
    """
    <style>
    /* Estiliza o texto digitado no campo de entrada */
    input[type="text"] {
        color: #FF0000 !important; /* Cor vermelha, pode mudar para outra */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Rótulo e campo de entrada para o filtro
st.markdown("<p style='font-size: 16px; margin-bottom: -10px;'>QUEM RECEBEU ?? ----- Digite o nome para filtrar: ---------- DICAS; pode ser; Nome, Sobrenome ou CNPJ</p>", unsafe_allow_html=True)
nome_filtro = st.text_input("", placeholder="Digite aqui...")

# Filtrar os dados
if nome_filtro:
    dados_filtrados = dados[dados['Quem Recebeu'].str.contains(nome_filtro, case=False, na=False)]
else:
    dados_filtrados = dados

# Exibir os dados filtrados
st.subheader("Lista")
st.dataframe(dados_filtrados)
