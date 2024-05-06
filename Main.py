from Ruta import Ruta
from GrafoRutas import GrafoRutas 
from InterfazUser import InterfazUser

class Main:
    def __init__(self):
        self.ejecutar_programa()

    def ejecutar_programa(self):
        grafo_rutas = self.crear_grafo_desde_archivo("rutas.txt")
        interfaz = InterfazUser(grafo_rutas)
        try:
            estacion_salida = input("Ingrese la estación de salida: ")
            interfaz.ver_mapa_destinos(estacion_salida)
            interfaz.encontrar_mejores_rutas(estacion_salida)
            grafo_rutas.dibujar_grafo()
        except:
            print("La estación ingresada no existe en el grafo")

        

    def crear_grafo_desde_archivo(self, nombre_archivo):
        grafo_rutas = GrafoRutas()
        with open(nombre_archivo) as archivo:
            for linea in archivo:
                origen, destino, costo = linea.strip().split(',')
                ruta = Ruta(origen.strip(''), destino.strip(''), int(costo))
                grafo_rutas.agregar_ruta(ruta)
        return grafo_rutas

if __name__ == "__main__":
    Main = Main()
