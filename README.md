# Sistema de Recomendação de Filmes

## Descrição

O Sistema de Recomendação de Filmes é uma aplicação que fornece sugestões de filmes com base na similaridade de conteúdo. Utiliza técnicas de Processamento de Linguagem Natural (PLN) e análise de similaridade para recomendar filmes semelhantes ao escolhido pelo usuário.

## Funcionalidades

- **Recomendação de Filmes:** Sugere filmes similares ao que o usuário selecionou.

- **Análise de Similaridade:** Avalia a similaridade entre filmes com base em características.

- **Visualização:** Exibe as recomendações em um formato de cartão com detalhes sobre cada filme, incluindo gênero e ano de lançamento.

- **Gráfico de Recomendação:** Mostra um gráfico de barras horizontais das principais recomendações.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- **Streamlit:** Framework para criação de interfaces web interativas.
- **Pandas:** Manipulação e análise de dados.
- **Scikit-Learn:** Implementação de modelos de Machine Learning e técnicas de vetorização e similaridade.
- **Seaborn & Matplotlib:** Visualização de dados.

## Estrutura do Projeto

1. **`load_and_prepare_data`**: Função para carregar e preparar os dados necessários para o sistema de recomendação.
2. **`sistema_rec`**: Função para obter recomendações de filmes com base na similaridade de conteúdo.
3. **Interface Streamlit (`app.py`)**: Interface do usuário para interação com o sistema de recomendação e visualização das recomendações.

## Requisitos

Para rodar este projeto, você precisará instalar as seguintes bibliotecas:

```bash
pip install pandas scikit-learn numpy seaborn matplotlib streamlit
