import networkx as nx # type: ignore

class GrafoRutas:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_ruta(self, ruta):
        self.grafo.add_edge(ruta.origen, ruta.destino, weight=ruta.costo)
        self.grafo.add_edge(ruta.destino, ruta.origen, weight=ruta.costo)

    def obtener_rutas_posibles(self, estacion_salida):
        return list(self.grafo.neighbors(estacion_salida))

    def obtener_costo_ruta(self, origen, destino):
        return nx.shortest_path_length(self.grafo, origen, destino, weight='weight')

    def dibujar_grafo(self):
        nx.draw(self.grafo, with_labels=True, font_weight='bold')
