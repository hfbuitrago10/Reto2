"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf

sys.setrecursionlimit(1000*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada selección
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información de videos en el catálogo")
    print("2- Consultar videos tendencia con más views por categoría y país")
    print("3- Consultar video tendencia por país")
    print("4- Consultar video tendencia por categoría")
    print("5- Consultar videos con más likes por país y tag")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catálogo de videos
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga la información de los videos al catálogo
    """
    return controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print("El total de videos cargados es: " + str(controller.videosSize(catalog)))
        print("El total de categorías cargadas es: " + str(controller.categorySize(catalog)) + "\n")

    elif int(inputs[0]) == 2:
        name = str(input("Ingrese el nombre de la categoría\n"))
        categoryid = controller.getCategoryid(catalog, name)
        country = str(input("Ingrese el país\n"))
        size = int(input("Ingrese el número de videos a listar\n"))

    elif int(inputs[0]) == 3:
        country = str(input("Ingrese el país\n"))
        videos = controller.getVideosByCountry(catalog, country)
        firstVideo = controller.getFirstVideoByTrendDays(videos)
        print(firstVideo)

    elif int(inputs[0]) == 4:
        name = str(input("Ingrese el nombre de la categoría\n"))
        categoryid = controller.getCategoryid(catalog, name)
        videos = controller.getVideosByCategory(catalog, categoryid)
        firstVideo = controller.getFirstVideoByTrendDays(videos)
        print(firstVideo)

    elif int(inputs[0]) == 5:
        pass

    else:
        sys.exit(0)
sys.exit(0)
