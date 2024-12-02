# Tech Challenge 4 - Data Analytics
Renan Shoji Machado

Criação de dashboard interativo e Prevendo o preço do petróleo Brent

Trabalho desenvolvido para o pós Tech Data Analytics - FIAP, Dezembro de 2024

## Problema
Você foi contratado(a) para uma consultoria, e seu trabalho envolve
analisar os dados de preço do petróleo brent, que pode ser encontrado no site
do [ipea](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view). Essa base de dados histórica envolve duas colunas: data e preço (em
dólares). 
Um grande cliente do segmento pediu para que a consultoria desenvolvesse um dashboard interativo para gerar insights relevantes para tomada de decisão. Além disso, solicitaram que fosse desenvolvido um modelo de Machine Learning para fazer o forecasting do preço do petróleo

## Objetivo
• Criar um dashboard interativo com ferramentas à sua escolha.

• Seu dashboard deve fazer parte de um storytelling que traga insights
relevantes sobre a variação do preço do petróleo, como situações
geopolíticas, crises econômicas, demanda global por energia e etc. Isso
pode te ajudar com seu modelo. É obrigatório que você traga pelo menos
4 (quatro) insights neste desafio.

• Criar um modelo de Machine Learning que faça a previsão do preço do
petróleo diariamente (lembre-se de time series). Esse modelo deve estar
contemplado em seu storytelling e deve conter o código que você
trabalhou, analisando as performances do modelo.

• Criar um plano para fazer o deploy em produção do modelo, com as
ferramentas que são necessárias.

• Faça um MVP do seu modelo em produção utilizando o Streamlit.

## Desenvolvimento
Os dados do preço de petróleo Brent foram pegos do site:

http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view

Também foi utilizado dados extor do PIB mundial, população mundial, produção e consumo de petróleo do Banco Mundial (World Bank) e Energy Information Administration (EIA):

https://databank.worldbank.org/source/world-development-indicators

https://www.eia.gov/

Os dados foram tratados no Google Collab, exportados em xlsx para alimentar o Data Viz no Power BI. Para o modelo, foi exportado do collab o modelo Prophet em pkl e utilizado no vs code para subir a aplicação em Streamlit. Após a aplicação pronta, foi feito o deploy no site do Streamlit vinculado ao github.

O dashboard está em pdf e pbix.

Github: https://github.com/reshoji/Tech-Challenge-4/blob/main/App_Streamlit.py

A aplicação do Stremlit está no seguinte link: https://appapppy-nvtwsc6f5qvmtohv9gumbc.streamlit.app/
