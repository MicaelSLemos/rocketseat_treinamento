import pandas as pd
import matplotlib.pyplot as plt

# Dicionário de faturamento
dict_faturamento_desafio = {
    'data_ref': [
        '2023-01-01', 
        '2020-02-01', 
        '2021-03-01', 
        '2022-04-01', 
        '2023-05-01',
        '2023-06-01', 
        '2020-07-01', 
        '2021-08-01', 
        '2022-09-01', 
        '2023-10-01',
        '2022-11-01', 
        '2023-12-01',
        ],
    'valor': [
        400000, 
        890000, 
        760000, 
        430000, 
        920000,
        340000, 
        800000, 
        500000, 
        200000, 
        900000,
        570000, 
        995000,
        ]
}



df_desafio = pd.DataFrame.from_dict(dict_faturamento_desafio)
df_desafio.data_ref = pd.to_datetime(df_desafio.data_ref)
#incluir coluna de mes
df_desafio['mes'] = df_desafio['data_ref'].dt.strftime('%b')


#Média de vendas
media = df_desafio.valor.mean()

#Grafico de barras vertical
df_desafio.plot.bar(x='mes', y='valor')


#Gráfico de linhas
df_desafio.plot.line(x='mes', y='valor')