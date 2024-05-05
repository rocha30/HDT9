import networkx as nx # type: ignore
import matplotlib.pyplot as plt

class GrafoRutas:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_ruta(self, ruta):
        self.grafo.add_edge(ruta.origen, ruta.destino, weight=ruta.costo)
        self.grafo.add_edge(ruta.destino, ruta.origen, weight=ruta.costo)

    def obtener_rutas_posibles(self, estacion_salida):
        return list(self.grafo.neighbors(estacion_salida))

    def obtener_costo_ruta(self, origen, destino):
        try:
            return nx.shortest_path_length(self.grafo, origen, destino, weight='weight')
        except nx.NetworkXNoPath:
            return float('inf')
        

    def dibujar_grafo(self):
        options = {
            "font_size": 10,
            "node_size": 2000,
            "node_color": "skyblue",
            "edgecolors": "gray",
            "linewidths": 1,
            "width": 1,
        }
        pos = nx.spring_layout(self.grafo, scale=3, center=(0, 0))
        nx.draw(self.grafo,pos, with_labels=True, font_weight='bold', **options)
        plt.show()
