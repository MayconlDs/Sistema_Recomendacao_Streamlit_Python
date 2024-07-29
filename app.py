import streamlit as st
from recomendation import load_and_prepare_data, sistema_rec
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def get_data():
    return load_and_prepare_data()

# Carregar os dados e criar a matriz de similaridade
df_cossi, df2 = get_data()  # Descompactar a tupla

# Adicionar CSS personalizado
st.markdown("""
<style>
    .stButton button {
        background-color: #008000;
        color: white;
        border-radius: 15px;
        border: none;
        padding: 10px 20px;
        font-size: 20px;
    }
    .stButton button:hover {
        background-color: #3a9149;
        cursor: pointer;
        color: white;
    }
    .stSelectbox label {
        font-weight: bold;
        font-size: 20px;
    }
    .recommendation-card {
        background-color: #21C3541A;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
   .stApp {
        background-color: #F8FBF8;
    }
</style>
""", unsafe_allow_html=True)


# Título do aplicativo com estilo personalizado
st.markdown("""
    <div style="background-color:#008000;padding:10px;border-radius:15px;text-align:center;">
        <h1 style="color:white;">Sistema de Recomendação de Filmes</h1>
    </div>
    <br>
    <div style="background-color:#008000;padding:10px;border-radius:15px; display: flex; align-items: center; justify-content: center;">
        <h4 style="color:white;margin-right: 10px;">Selecione um filme para obter Recomendações</h4>
        <img src="https://cdn.freebiesupply.com/images/large/2x/imdb-logo-transparent.png" style="width: 140px; height: auto;">
    </div>
    """, unsafe_allow_html=True)

st.divider()
# Seleção do filme
movie_list = df_cossi.columns.tolist()
movie_list = list(dict.fromkeys(movie_list))
selected_movie = st.selectbox("Selecione um filme:", movie_list)

# Botão para obter recomendações
try:
    if st.button("Obter Recomendações"):
        with st.spinner('Buscando recomendações...'):
            time.sleep(2)  # Simulate a delay for loading recommendations
            st.session_state['recommendations'] = sistema_rec(df_cossi, df2, selected_movie)
        st.success('Recomendações encontradas com sucesso!', icon="✅")
        st.subheader("Filmes recomendados")

        # Apresentar recomendações em forma de cartões
        for i, row in st.session_state['recommendations'].iterrows():
            descricao = row.get('Discription', 'Descrição não disponível')
            generos = row.get('genres', 'Gêneros não disponíveis')
            tags = row.get('Tags', 'Tags não disponíveis')
            
            st.markdown(f"""
            <div class='recommendation-card'>
                <h3>{i+1}º.     {row['Titulo']}</h3>
                <ul>
                    <li style='font-size: 22px'>Genero : {row['Gêneros'].replace('|', ' - ')}</li>
                    <li style='font-size: 22px'>Ano de lançamento : {row['Ano de Lançamento']}</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
      # Preparar os dados para o gráfico de barras
        recommendations_for_plot = st.session_state['recommendations']
        
        # Verificar se a coluna 'Titulo' está presente
        if 'Titulo' in recommendations_for_plot.columns and 'Recomendações' in recommendations_for_plot.columns:
            plt.figure(figsize=(10, 6))
            sns.barplot(x='Recomendações', y='Titulo', data=recommendations_for_plot, palette='viridis', orient='h')

            # Adicionar título e rótulos aos eixos
            plt.title('Top 10 Recomendações de Filmes', fontsize=25)
            plt.xlabel('Similaridade', fontsize=20)
            plt.ylabel('Titulo', fontsize=20)
            
            plt.tick_params(axis='both', which='major', labelsize=16)

            # Exibir o gráfico no Streamlit
            st.pyplot(plt)
            
            # Limpar o gráfico
            plt.clf()
            plt.close()
        else:
            st.warning('Os dados para o gráfico estão incompletos.')
    
except Exception as e:
    st.error(f'Algo deu errado durante a pesquisa: {e}', icon="🚨")
    st.info('Por favor, selecione outro filme..', icon="ℹ️")