# Sistema de Agendamiento de Viajes

Este es un programa en Python que permite agendar viajes utilizando el algoritmo de Dijkstra para encontrar las rutas más económicas entre estaciones de salida y destinos posibles.



## Autores
  Diego José López Campos
  Mario Fernando Rocha López


## Requisitos

Antes de ejecutar el programa, asegúrate de tener instalado Python 3 y el módulo networkx. Puedes instalar networkx ejecutando el siguiente comando:

```
pip install networkx
```

## Uso

1. Descarga o clona este repositorio en tu máquina local.
2. Asegúrate de tener un archivo de texto llamado `rutas.txt` en el mismo directorio que contenga las rutas en el siguiente formato:

```
"Pueblo Paleta", "Aldea Azalea", 100
"Aldea Azalea", "Ciudad Safiro", 150
"Pueblo Paleta", "Ciudad Safiro", 800
"Ciudad Lavanda", "Aldea Fuego", 300
```

3. Ejecuta el programa ejecutando el archivo `Main.py`.

El programa te pedirá ingresar el nombre de la estación de salida. Luego, te mostrará los posibles destinos desde esa estación y las mejores rutas para llegar a cada uno de ellos.

## Estructura del Programa

El programa está dividido en varias clases:

- `Ruta`: Representa una ruta entre dos estaciones, con origen, destino y costo.
- `GrafoRutas`: Maneja la estructura del grafo y las operaciones relacionadas con él.
- `Dijkstra`: Implementa el algoritmo de Dijkstra para encontrar las mejores rutas.
- `InterfazUsuario`: Proporciona la interfaz para interactuar con el programa.

## Contribuir

Si deseas contribuir a este proyecto, ¡siéntete libre de hacer un fork y enviar tus pull requests!

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).
