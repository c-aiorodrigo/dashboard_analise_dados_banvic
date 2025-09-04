import pandas as pd
import streamlit as st
import plotly.express as px

#criando pagina com os dados
st.set_page_config(
    page_title= "Analise de Transações",
    layout= "wide"
)

df = pd.read_csv'/workspaces/dashboard_analise_dados_banvic/df_transacoes_merge.csv'