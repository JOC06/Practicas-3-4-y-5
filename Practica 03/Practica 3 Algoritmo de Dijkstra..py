# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:59:33 2023

@author: Dell
"""

import heapq

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.aristas = {}

    def agregar_vertice(self, valor):
        self.vertices.add(valor)
        self.aristas[valor] = []

    def agregar_arista(self, origen, destino, peso):
        self.aristas[origen].append((destino, peso))
        self.aristas[destino].append((origen, peso))

    def dijkstra(self, inicio):
        distancias = {vertice: float('infinity') for vertice in self.vertices}
        distancias[inicio] = 0
        pendientes = [(0, inicio)]

        while pendientes:
            (distancia_actual, vertice_actual) = heapq.heappop(pendientes)

            if distancia_actual > distancias[vertice_actual]:
                continue

            for (vecino, peso) in self.aristas[vertice_actual]:
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(pendientes, (distancia, vecino))

        return distancias

if __name__ == "__main__":
    grafo = Grafo()

    # Agregamos vértices
    for v in ['A', 'B', 'C', 'D', 'E']:
        grafo.agregar_vertice(v)

    # Agregamos aristas con pesos
    grafo.agregar_arista('A', 'B', 3)
    grafo.agregar_arista('A', 'C', 2)
    grafo.agregar_arista('B', 'C', 1)
    grafo.agregar_arista('B', 'D', 5)
    grafo.agregar_arista('C', 'D', 6)
    grafo.agregar_arista('C', 'E', 4)
    grafo.agregar_arista('D', 'E', 2)

    inicio = 'A'
    distancias = grafo.dijkstra(inicio)

    for vertice, distancia in distancias.items():
        print(f'Distancia desde {inicio} a {vertice}: {distancia}')
