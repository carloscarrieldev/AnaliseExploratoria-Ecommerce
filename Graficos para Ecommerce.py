import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from fontTools.diff import color
from pandas.core.groupby import groupby

df = pd.read_csv('ecommerce_estatistica.csv')

# Gráfico - Histograma
# Objetivo: Visualizar como os valores estão distribuídos é identificar onde há maior concentração de dados.
plt.figure(figsize=(10,6))
plt.hist(df['Preço'], bins=50, color='blue', alpha=1.0)
plt.title('Analisando - Preço')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.show()

# Gráfico - Disperso
# Objetivo: Visualizar a relação entre duas variáveis é identificar possíveis padrões e valores outliers.
plt.figure(figsize=(10,6))
plt.scatter(df['Qtd_Vendidos'],df['Preço'],color='Red')
plt.title('Dispersão - Vendas + Preço')
plt.xlabel('Vendas')
plt.ylabel('Preços')
plt.show()

# Gráfico - Mapa de Calor
# Objetivo: Visualizar relações entre duas variáveis, quanto mais próximo de 1, mais forte é a correlação.
plt.figure(figsize=(10,6))
correl = (df[['N_Avaliações','Desconto','Qtd_Vendidos_Cod','Preço']]).corr()
sns.heatmap(correl, annot=True, fmt='.2f',cmap= 'viridis')
plt.title('Correlações entre Produtos')
plt.show()

# Grafico - Barra
# Objetivo: Comparar mostrando quanto foi vendido de cada variável. Permitindo identificar quais apresentam maior ou menor quantidade
vendas = df.groupby('Marca')['Qtd_Vendidos'].sum()
plt.figure(figsize=(30,20))
plt.bar(vendas.values, vendas.index, color='black')
plt.title('Quantidade de Vendas por Marca')
plt.xlabel('Marca')
plt.ylabel('Vendas')
plt.show()

# Gráfico - Pizza
# Objetivo: Mostrar o total por categoria, distribuindo e deixando mais fácil a visualização.
avalia = df.groupby('Temporada')[ 'N_Avaliações' ].sum()
plt.figure(figsize=(10,6))
plt.pie(avalia.values, labels=avalia.index, autopct='%.1f%%', startangle=90)
plt.title('Temporadas e Avaliações')
plt.show()

# Gráfico - Densidade
# Objetivo: Mostra a distribuição e a concentração dos valores, permitindo identificar onde os dados estão mais concentrados.
plt.figure(figsize=(10,6))
sns.kdeplot(df['Desconto'], fill=True, color='black')
plt.title('Analise - Desconto')
plt.xlabel('Desconto')
plt.show()

# Gráfico - Regressão
# Objetivo: Analisar a relação entre duas variáveis, ajudando a identificar tendências nos dados.
plt.figure(figsize=(10,6))
sns.regplot(x='Qtd_Vendidos_Cod', y='Preço', data=df, color='red',scatter_kws={'alpha':0.5,'color':'black'})
plt.title('Regressão - Vendas + Preço')
plt.xlabel('Vendas')
plt.ylabel('Preços')
plt.show()