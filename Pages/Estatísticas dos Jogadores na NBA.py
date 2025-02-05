import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def load_data():
    file_path = "NBA_Data.csv"  
    return pd.read_csv(file_path)

df = load_data()
st.set_page_config(layout="wide")



if 'tm' not in df.columns:
    st.error("A coluna 'tm' não foi encontrada no DataFrame.")
else:
    # Título do Dashboard
    st.title("Dashboard de Estatísticas da NBA")

    # Adicionar a coluna com o nome completo do time
    nba_teams = {
        "MIL": "Milwaukee Bucks",
        "TOR": "Toronto Raptors",
        "DEN": "Denver Nuggets",
        "HOU": "Houston Rockets",
        "IND": "Indiana Pacers",
        "OKC": "Oklahoma City Thunder",
        "CHI": "Chicago Bulls",
        "PHI": "Philadelphia 76ers",
        "BOS": "Boston Celtics",
        "MIA": "Miami Heat",
        "SAC": "Sacramento Kings",
        "WAS": "Washington Wizards",
        "DET": "Detroit Pistons",
        "LAC": "Los Angeles Clippers",
        "GSW": "Golden State Warriors",
        "POR": "Portland Trail Blazers",
        "ORL": "Orlando Magic",
        "LAL": "Los Angeles Lakers",
        "MIN": "Minnesota Timberwolves",
        "NOP": "New Orleans Pelicans",
        "NYK": "New York Knicks",
        "BRK": "Brooklyn Nets",
        "SAS": "San Antonio Spurs",
        "ATL": "Atlanta Hawks",
        "PHO": "Phoenix Suns",
        "MEM": "Memphis Grizzlies",
        "CHO": "Charlotte Hornets",
        "DAL": "Dallas Mavericks",
        "UTA": "Utah Jazz",
        "CLE": "Cleveland Cavaliers"
        # Adicione outros times conforme necessário
    }

    df['team_name'] = df['tm'].map(nba_teams)

    # Selectbox para selecionar o time
    option = st.selectbox(
        'Qual jogador você deseja visualizar?',
        df['player'].sort_values().unique()
    )

    # Filtrar os dados pelo time selecionado
    filtered_df = df[df['player'] == option]

    fig1 = go.Figure(data=[go.Scatter(x=filtered_df["season"], y=filtered_df["pts_per_game"], mode='lines+markers', name='Points per game', marker=dict(color='orange') )])
    fig1.update_layout(title=f'Pontos por jogo do {option}', xaxis_title='Temporada', yaxis_title='Pontos por jogo')
    st.plotly_chart(fig1)

    fig2 = go.Figure(data=[go.Scatter(x=filtered_df["season"], y=filtered_df["ast_per_game"], mode='lines+markers', name='Assists per game', marker=dict(color='purple'))])
    fig2.update_layout(title=f'Assistências por jogo do {option}', xaxis_title='Temporada', yaxis_title='Assistências por jogo')
    st.plotly_chart(fig2)

    fig3 = go.Figure(data=[go.Scatter(x=filtered_df["season"], y=filtered_df["trb_per_game"], mode='lines+markers', name='Rebounds per game', marker=dict(color='green'))])
    fig3.update_layout(title=f'Rebotes por jogo do {option}', xaxis_title='Temporada', yaxis_title='Rebotes por jogo')
    st.plotly_chart(fig3)