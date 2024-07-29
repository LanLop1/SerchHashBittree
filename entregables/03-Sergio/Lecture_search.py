#%%
import pandas as pd
import tkinter as tk
from tkinter import ttk
import time


# Importo las librerias necesarias, pandas para manejar los datos y ykinter para hacer la interfaz básica que funciona
data = pd.read_csv('data.csv')


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    def __init__(self, capacity):  # cramos la hash table y definimos parámetros para poder definir su tamaño más tarde
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity  # Al hacer la moda de la clave hash nos da el número de casilla donde se guardará la información, este puede repetirse, pero eso no es un problema, dado que se guardará varios elementos en la misma casilla, si esto pasara mucho relentizaría el algoritmo de búsqueda, por ello me aseguro de hacer una tabla significativamente mas grande que el numero de datos, para evitar este problema, aunque eso augmenta la cantidad de memoria que requiere la tabla.

    def insert(self, key, value):
        index = self._hash(key)  # Esta funcion mete los datos, y si la tabla es muy pequeña añade espacios.

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        Pelis=[]
        index = self._hash(key)

        current = self.table[index]  # Esta funcion busca en la hash tabla el elemento que coincide con el id que le hemos proporcionado
        while current:
            if current.key == key:
                Pelis= Pelis.append(current.value)
                print(Pelis)
                print(f"current: {current.value}")
                current = current.next

            return Pelis
            

        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)  # Borra elementos de la tabla

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def __len__(self):
        return self.size  # Nos dice el tamaño de la tabla

    def __contains__(self, key):  # Busca si en la tabla existe el elemento, este a diferencia del search no da error si falla
        try:
            self.search(key)
            return True
        except KeyError:
            return False
ht = HashTable(10000000)

df = pd.DataFrame(data)
i = 0
for index, row in df.iterrows():
    ht.insert(row["title"], df.loc[
        i])  # Uso el índice para llevar la cuenta de las filas que se van añadiendo y las voy añadiendo una a una.                 una,                                esto es lo que tarda mas de
    i = i + 1  # Este proceso el lo que tarda más del programa dado que genera la hash table


def search_movie():
    inicio = time.time()
    query = search_var.get().strip()
    result = ht.search(query)  # recibe input y usa la función de búsqueda en la hash table, tmb medimos el tiempo de ejecución de la
    result_var.set(result)  # busqueda
    final = time.time()
    tiempo_busqueda = final - inicio
    print(tiempo_busqueda)


# Crear la ventana principal
root = tk.Tk()
root.title("Buscador de Películas")

# Variable para el texto de búsqueda
search_var = tk.StringVar()

# Crear y ubicar los widgets
search_label = ttk.Label(root, text="Buscar Película:")
search_label.pack(pady=10)

search_entry = ttk.Entry(root, textvariable=search_var, width=50)
search_entry.pack(pady=10)

search_button = ttk.Button(root, text="Buscar", command=search_movie)
search_button.pack(pady=10)

# Variable para el resultado de la búsqueda
result_var = tk.StringVar()

result_label = ttk.Label(root, textvariable=result_var, wraplength=400)
result_label.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()