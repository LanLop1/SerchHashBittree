#%%
import matplotlib.pyplot as plt

data = [7.139869213104248, 10.896265506744385]
buscadores = ['Hash Table', 'Biblioteca Pandas']

# Crear gráfico de barras
plt.bar(buscadores, data, color=['blue', 'green'])

# Añadir título y etiquetas
plt.title("Comparación del tiempo de búsqueda de dos buscadores")
plt.xlabel("Buscadores")
plt.ylabel("Tiempo de búsqueda (segundos)")
