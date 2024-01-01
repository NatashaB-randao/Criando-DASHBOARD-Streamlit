import streamlit as st

# Textos


# Centralizar o título
st.markdown(
    f"<h1 style='text-align: center;'>Meu Dashboard</h1>",
    unsafe_allow_html=True
)
# Adicionar um divisor embaixo do título
st.markdown("<hr style='border: 2px solid #e6e6e6;'>", unsafe_allow_html=True)

st.sidebar.header("Escolha o que deseja filtrar")

#st.markdown("~~Riscado~~")
#.caption("Minha legenda")

#pessoas = [{'Nome': 'Caio', 'Idade': 22}, 
#            {'Nome': 'Marcos', 'Idade': 33}]

#st.write("# Pessoa", pessoas)

# Exibição de Dados
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.rand(10, 4),
    columns=['Preço', 'Taxa de Ocupação', 'Taxa de Inadimplência', 'Pessoas por Casa']
)

st.dataframe(df)
st.markdown("<hr style='border: 2px solid #e6e6e6;'>", unsafe_allow_html=True)
st.line_chart(df)
st.markdown("<hr style='border: 2px solid #e6e6e6;'>", unsafe_allow_html=True)
st.bar_chart(df)
st.markdown("<hr style='border: 2px solid #e6e6e6;'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-size: 18px;'>Variação do Preço ao Longo do Tempo</h2>", unsafe_allow_html=True)
st.line_chart(df['Preço'])
