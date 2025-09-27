import pandas as pd  

df = pd.read_csv('spotify-2023.csv', encoding='latin1')  
print(df.head())  
categorical_vars = df.select_dtypes(include='object').columns
numerical_vars = df.select_dtypes(include='number').columns

cat_vars = df.select_dtypes(include='object')
num_vars = df.select_dtypes(include='number')

##Punto A, identificar cuantas variables categóricas (tipo object) y cuantas variables numéricas tiene
print("Variables categóricas:", len(cat_vars.columns))
print("Variables numéricas:", len(num_vars.columns))

## Punto B, hacer un algoritmo que nos diga cuantas canciones de Coldplay hay en la base de datos.
coldplay_songs = df[df['artist(s)_name'] == 'Coldplay']
print("Número de canciones de Coldplay:", len(coldplay_songs))


##Punto C, Encuentre el máximo y el mínimo de cada columna numérica en la base de datos
max_values = num_vars.max()
min_values = num_vars.min()
print("Los máximos de cada columna numérica:\n", max_values)
print("Los mínimos de cada columna numérica:\n", min_values) ##Aquí imprimo los máximos y minimos de cada una de las columnas de la base de datos


##Punto D, desarrolle una función que reciba como parámetro su base de datos y un artista y le devuelva todas las canciones de ese artista en base de datos
def canciones_por_artista(data, artista):
    return data[data['artist(s)_name'] == artista]

print(canciones_por_artista(df, 'Bad Bunny'))


##punto E, cree una tabla con una función de agregación, que muestre la sumatoria de cuantas canciones Taylor Swift y Coldplay aparecen en playlist.

filtro = df[df['artist(s)_name'].isin(['Taylor Swift', 'Coldplay'])]

tabla = filtro['artist(s)_name'].value_counts().reset_index()
tabla.columns = ['Artista', 'Cantidad de canciones']

print(tabla)

##punto F, Desarrolle un subplot con dos gráficos, el primero es un boxplot relacione artist_count(eje x) con streams, y el segundo un histograma de los años de lanzamiento
import matplotlib.pyplot as plt
import pandas as pd

df['artist_count'] = pd.to_numeric(df['artist_count'], errors='coerce')


df_clean = df[['streams', 'artist_count', 'released_year']].dropna()
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
df_clean.boxplot(column='streams', by='artist_count')
plt.title('Streams vs Artist Count')
plt.xlabel('Artist Count')
plt.ylabel('Streams')
plt.suptitle('')  # Elimina el título automático

plt.subplot(1, 2, 2)
df_clean['released_year'] = df_clean['released_year'].astype(int)
df_clean['released_year'].hist(bins=20)
plt.title('Histograma de años de lanzamiento')
plt.xlabel('Año')
plt.ylabel('Cantidad')

plt.tight_layout()
plt.show()

##Aquí hago el subplot con los dos gráficos pedidos, el primero es un boxplot que relaciona artist_count con streams y el segundo es un histograma de los años de lanzamiento.