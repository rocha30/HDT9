import heapq

class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo

    def calcular_rutas_mas_baratas(self, estacion_salida):
        rutas_mas_baratas = {}
        for nodo in self.grafo.grafo.nodes():
            if nodo != estacion_salida:
                costo = self.grafo.obtener_costo_ruta(estacion_salida, nodo)
                rutas_mas_baratas[nodo] = costo
        return rutas_mas_baratas
