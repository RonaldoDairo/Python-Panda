import pandas as pd

df_data_history = pd.read_csv('fifa_worldcup_matches.csv')
df_fixture = pd.read_csv('fifa_worldcup_fixture.csv')
missing_data = pd.read_csv('fifa_worldcup_missing_data.csv')

df_fixture['home'] = df_fixture['home'].str.strip()# limpiando los espacios en blanco
df_fixture['away'] = df_fixture['away'].str.strip()# limpiando los espacios en blanco

missing_data.dropna(inplace=True)#Es utilizado para eliminar filas o columnas que contengan valores faltantes (NaN) en un DataFrame en pandas.
print(missing_data)

df_data_history = pd.concat([df_data_history, missing_data], ignore_index=True)
 # se utiliza para combinar dos DataFrames en pandas en un solo DataFrame utilizando la función concat
df_data_history.drop_duplicates(inplace=True)# se utiliza para eliminar filas duplicadas de un DataFrame en pandas.
df_data_history.sort_values('year', inplace=True)
#se utiliza para ordenar un DataFrame en pandas en base a los valores de una columna específica, en este caso, la columna llamada 'year'

index_eliminar = df_data_history[
    df_data_history['home'].str.contains('Sweden') &
    df_data_history['away'].str.contains('Austria')
].index
df_data_history.drop(index=index_eliminar, inplace=True)# para eliminar

df_data_history['score'] = df_data_history['score'].str.replace('[^\d-]', '', regex=True)
# df_data_history = df_data_history[df_data_history['score'].str.contains('[^\d-]')] #para limpiar algunas inicial que aparecen

df_data_history['home'] = df_data_history['home'].str.strip()  # limpiando los espacios en blanco
df_data_history['away'] = df_data_history['away'].str.strip()  # limpiando los espacios en blanco

df_data_history['score'] = df_data_history['score'].str.split('-', expand=True)

print(df_data_history['score'])
