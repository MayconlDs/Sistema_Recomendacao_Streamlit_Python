import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Função para carregar e preparar os dados
def load_and_prepare_data():
    dados = pd.read_csv('Dados.csv')
    tags = pd.read_csv('Tags.csv')
    filme = pd.read_csv('Filmes.csv')
    rating = pd.read_csv('Ratings.csv', sep=';')

    # Converter os tipos de colunas para garantir a compatibilidade
    dados['Votes'] = dados['Votes'].str.replace(',', '').astype(float)
    dados['Total'] = dados['Total'].str.replace('$', '').astype(float)
    dados['Tags'] = dados['Tags'].str.replace('\\n', '').str.split().str.join(',')
    dados['Discription'] = dados['Discription'].str.replace('\\n', '')
    filme['movieId'] = filme['movieId'].apply(lambda x: str(x))

    # Mesclar os DataFrames
    df2 = filme.merge(dados, left_on='title', right_on='Name')
    df2 = df2.merge(tags, left_on='movieId', right_on='movieId')
    df2['Infos'] = df2['genres'] + str(df2['Directors_Cast']) + str(df2['Discription']) + df2['tag']

    vetor = TfidfVectorizer()
    tfidf = vetor.fit_transform(df2['Infos'].apply(lambda x: np.str_(x)))

    similar_coss = cosine_similarity(tfidf)

    df_cossi = pd.DataFrame(similar_coss, columns=df2['title'], index=df2['title'])

    return df_cossi, df2

# Função para obter recomendações
def sistema_rec(df_cossi, df2, texto):
    sistema_recomendacao = df_cossi[texto].sort_values(ascending=False)
    sistema_recomendacao = sistema_recomendacao.iloc[1:11].reset_index()
    sistema_recomendacao.columns = ['Titulo', 'Recomendações']
    sistema_recomendacao = sistema_recomendacao.merge(df2[['title', 'genres','year']], left_on='Titulo', right_on='title', how='left')
    sistema_recomendacao = sistema_recomendacao[['Titulo', 'Recomendações', 'genres', 'year']]
    sistema_recomendacao.columns = ['Titulo', 'Recomendações', 'Gêneros', 'Ano de Lançamento']
    sistema_recomendacao.drop_duplicates(subset=['Titulo'], inplace=True)  # Remove duplicatas
    return sistema_recomendacao

    