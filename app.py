import streamlit as st

# Textos


# Centralizar o título
# st.markdown(
#     f"<h1 style='text-align: center;'>Meu Dashboard</h1>",
#     unsafe_allow_html=True
# )
# # Adicionar um divisor embaixo do título
# st.markdown("<hr style='border: 2px solid #e6e6e6;'>", unsafe_allow_html=True)


#st.markdown("~~Riscado~~")
#.caption("Minha legenda")

#pessoas = [{'Nome': 'Caio', 'Idade': 22}, 
#            {'Nome': 'Marcos', 'Idade': 33}]

#st.write("# Pessoa", pessoas)

# Exibição de Dados
# import pandas as pd
# import numpy as np

# df = pd.DataFrame(
#     np.random.rand(10, 4),
#     columns=['Preço', 'Taxa de Ocupação', 'Taxa de Inadimplência', 'Pessoas por Casa']
# )

# st.dataframe(df)
# st.markdown("<hr style='border: 2px solid #e6e6e6;'>", unsafe_allow_html=True)
# st.line_chart(df)
# st.markdown("<hr style='border: 2px solid #e6e6e6;'>", unsafe_allow_html=True)
# st.bar_chart(df)
# st.markdown("<hr style='border: 2px solid #e6e6e6;'>", unsafe_allow_html=True)
# st.markdown("<h2 style='text-align: center; font-size: 18px;'>Variação do Preço ao Longo do Tempo</h2>", unsafe_allow_html=True)
# st.line_chart(df['Preço'])

# if st.sidebar.button("Exibir Gráfico"):
#     st.header("Meu Gráfico")
#     df = pd.DataFrame(
#         np.random.rand(10, 4),
#         columns=['Preço', 'Taxa de Ocupação', 'Taxa de Inadimplência', 'Pessoas por Casa']

# )
#     st.bar_chart(df)

# check = st.sidebar.checkbox("Aceitos")

# if check:
#     st.write('Marcado')

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Adicionando a seção inicial no sidebar
st.sidebar.header("Escolha o que deseja filtrar")

# Função para exibir a seção inicial
def show_home():
    st.markdown("""
        # Exploração de Indicadores
        
        Bem-vindo à nossa plataforma de exploração de indicadores. Selecione uma opção no menu lateral para visualizar a variação ao longo do tempo.
    """)

# Função para exibir os gráficos com base na opção selecionada
def show_option(opcao):
    if opcao == "Preço":
        st.markdown("<h2 style='text-align: center; font-size: 18px;'>Variação do Preço ao Longo do Tempo</h2>", unsafe_allow_html=True)
            
        # Adicionando sliders para definir preço mínimo e máximo
        preco_minimo, preco_maximo = st.slider("Selecione o intervalo de Preços", 0.0, 100.0, (25.0, 75.0), 0.1)
        
        # Gerando dados aleatórios para o gráfico de linha (substitua isso pelos seus dados reais)
        df_linha = pd.DataFrame(
            np.random.uniform(preco_minimo, preco_maximo, size=(10, 1)),
            columns=['Preço']
        )

        # Gerando dados aleatórios para o gráfico de pizza
        df_pizza = pd.DataFrame(
            {'Tipo de Propriedade': ['Apartamento', 'Casa', 'Escritório'],
            'Percentual': [30, 40, 30]}
        )

        # Gráfico de linha
        st.line_chart(df_linha)
        st.table(df_linha)

        # Gráfico de pizza
        st.markdown("<h2 style='text-align: center; font-size: 18px;'>Distribuição por Tipo de Propriedade</h2>", unsafe_allow_html=True)
        st.plotly_chart(criar_grafico_pizza(df_pizza))

    elif opcao == "Taxa de Ocupação":
        # Gerando dados aleatórios para o gráfico de linha
        df_linha = pd.DataFrame(
            np.random.rand(10, 1),
            columns=['Taxa de Ocupação']
        )

        # Gerando dados aleatórios para o gráfico de pizza
        df_pizza = pd.DataFrame(
            {'Tipo de Propriedade': ['Residencial', 'Comercial', 'Industrial'],
            'Percentual': [25, 35, 40]}
        )

        # Gráfico de linha
        st.markdown("<h2 style='text-align: center; font-size: 18px;'>Variação da Taxa de Ocupação ao aoLongo do Tempo</h2>", unsafe_allow_html=True)
        st.line_chart(df_linha)
        st.table(df_linha)

        # Gráfico de pizza
        st.markdown("<h2 style='text-align: center; font-size: 18px;'>Distribuição por Tipo de Propriedade</h2>", unsafe_allow_html=True)
        st.plotly_chart(criar_grafico_pizza(df_pizza))

    elif opcao == "Taxa de Inadimplência":
        # Gerando dados aleatórios para o gráfico de linha
        df_linha = pd.DataFrame(
            np.random.rand(10, 1),
            columns=['Taxa de Inadimplência']
        )

        # Gerando dados aleatórios para o gráfico de pizza
        df_pizza = pd.DataFrame(
            {'Tipo de Propriedade': ['Residencial', 'Comercial', 'Industrial'],
            'Percentual': [45, 20, 35]}
        )

        # Gráfico de linha
        st.markdown("<h2 style='text-align: center; font-size: 18px;'>Variação da Taxa de Inadimplência ao Longo do Tempo</h2>", unsafe_allow_html=True)
        st.line_chart(df_linha)
        st.table(df_linha)

        # Gráfico de pizza
        st.markdown("<h2 style='text-align: center; font-size: 18px;'>Distribuição por Tipo de Propriedade</h2>", unsafe_allow_html=True)
        st.plotly_chart(criar_grafico_pizza(df_pizza))

# Função para criar gráfico de pizza
def criar_grafico_pizza(df):
    fig = px.pie(df, names='Tipo de Propriedade', values='Percentual', title='Distribuição por Tipo de Propriedade')
    return fig

# Seleção de opção no menu lateral
opcao = st.sidebar.radio(
    "Selecione uma opção",
    ["Página Inicial", "Preço", "Taxa de Ocupação", "Taxa de Inadimplência"],
    index=0  # Definindo o índice inicial para a primeira opção (Página Inicial).
)

# Verificação da opção selecionada
if opcao == "Página Inicial":
    show_home()
else:
    show_option(opcao)


