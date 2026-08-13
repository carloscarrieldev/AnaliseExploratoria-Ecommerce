import pandas as pd
from dash import Dash, Input, Output, dcc, html
import plotly.express as px

df = pd.read_csv('ecommerce_estatistica.csv')

def criando_graficos(df):
    df_filtro = df

    fig1 = px.bar(df_filtro,x='Gênero',y='Preço',color='Temporada',barmode='group', color_discrete_sequence=px.colors.qualitative.Set2,opacity=0.8)
    fig1.update_layout(
        title='Gênero + Preço por Temporada',
        xaxis_title='Gênero',
        yaxis_title='Preço',
        legend_title='Temporada',
        plot_bgcolor='white',
        paper_bgcolor='black'
    )
    fig2 = px.scatter_3d(df_filtro,x='Nota',y='N_Avaliações',z='Desconto', color='Gênero')
    fig2.update_layout(
        title='Analise de Clientes + Desconto',
        scene=dict(
        xaxis_title='Nota',
        yaxis_title='Avaliações',
        zaxis_title='Descontos'
    ))
    return fig1, fig2

fig1, fig2 = criando_graficos(df)

app = Dash(__name__)

def criar_app():
    app.layout = html.Div([
        html.H1('Estatistica para E-commerce'),
        html.Div('Dados do E-Commerce'),
        html.Br(),
        dcc.Graph(id='grafico_barra', figure=fig1),
        dcc.Graph(id='grafico_3d', figure=fig2),
    ])
    return app

if __name__ == '__main__':
    app = criar_app()
    app.run(debug=True,
            port=8050)