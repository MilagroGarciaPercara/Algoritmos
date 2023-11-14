from grafo import Graph
"""Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;
d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv."""
grafo = Graph(False)
#a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
habitaciones = ['cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2', 'habitación 1', 'habitación 2', 'sala de estar', 'terraza', 'patio']

class Habitacion():
    def __init__(self, nombre):
        self.nombre = nombre
    
for habitacion in habitaciones:
    grafo.insert_vertice(habitacion)

grafo.insert_arist('cocina', 'comedor', 20)
grafo.insert_arist('comedor', 'cochera', 14)
grafo.insert_arist('cochera', 'quincho', 30)
grafo.insert_arist('quincho', 'baño 1', 3)
grafo.insert_arist('baño 1', 'baño 2', 50)
grafo.insert_arist('baño 2', 'habitacion 1', 10)
grafo.insert_arist('habitacion 1', 'habitacion 2', 17)
grafo.insert_arist('habitacion 2', 'sala de estar', 24)
grafo.insert_arist('sala de estar', 'terraza', 14)
grafo.insert_arist('terraza', 'patio', 32)
grafo.insert_arist('cocina', 'patio', 15)
grafo.insert_arist('comedor', 'terraza', 29)
grafo.insert_arist('cochera', 'sala de estar', 4)
grafo.insert_arist('quincho', 'habitacion 2', 40)
grafo.insert_arist('baño 1', 'habitacion 1', 7)
grafo.insert_arist('patio', 'comedor', 26)
grafo.insert_arist('patio', 'sala de estar', 22)
grafo.insert_arist('patio', 'baño 1', 14)
grafo.insert_arist('cocina', 'baño 2', 9)
grafo.insert_arist('comedor', 'sala de estar', 5)

