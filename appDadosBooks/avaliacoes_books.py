import pandas as pd

df_listaComments_B000IEZE3G_20 = pd.read_csv('/home/gilmarsan/listaComments_B000IEZE3G_20.csv')

lista_comentarios_clientes = df_listaComments_B000IEZE3G_20['summary'].tolist()





