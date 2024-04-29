from Dijkstra import Dijkstra


class InterfazUser:
    def __init__(self, grafo):
        self.grafo = grafo

    def ver_mapa_destinos(self, estacion_salida):
        print("Posibles destinos desde", estacion_salida, ":")
        destinos = self.grafo.obtener_rutas_posibles(estacion_salida)
        for destino in destinos:
            print(destino)

    def encontrar_mejores_rutas(self, estacion_salida):
        dijkstra = Dijkstra(self.grafo)
        rutas_mas_baratas = dijkstra.calcular_rutas_mas_baratas(estacion_salida)
        print("Mejores rutas desde", estacion_salida, ":")
        for destino, costo in rutas_mas_baratas.items():
            print("Destino:", destino, "- Costo:", costo)
