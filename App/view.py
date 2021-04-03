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

# Funciones para la impresión de resultados

def printSortedVideosByViews(sortedVideos, sample):
    """
    Imprime la información de los videos con mayor número
    de views
    """
    size = int(lt.size(sortedVideos))
    if size > sample:
        index = 1
        while index <= sample:
            video = lt.getElement(sortedVideos, index)
            print("Fecha de tendencia: " + video['trending_date'] + "  Título: " + video['title'] + "  Canal: " + 
            video['channel_title'] + "  Fecha de publicación: " + video['publish_time'] + "  Views: " + 
            video['views'] + "  Likes: " + video['likes'] + "  Dislikes: " + video['dislikes'])
            index += 1
        print()

def printSortedVideosByLikes(sortedVideos, sample):
    """
    Imprime la información de los videos con mayor número
    de likes
    """
    size = int(lt.size(sortedVideos))
    if size > sample:
        index = 1
        while index <= sample:
            video = lt.getElement(sortedVideos, index)
            print("Título: " + video['title'] + "  Canal: " + video['channel_title'] + "  Fecha de publicación: " +
            video['publish_time'] + "  Views: " + video['views'] + "  Likes: " + video['likes'] + "  Dislikes: " +
            video['dislikes'] + "  Tags: " + video['tags'])
            index += 1
        print()

def printFirstVideoByTrendDays(firstVideo, option):
    """
    Imprime la información del video con mayor número de
    días de tendencia
    """
    video = lt.firstElement(me.getValue(firstVideo)['videos'])
    trenddays = me.getValue(firstVideo)['trendingdays']
    if int(option) == 1:
        print("Título: " + video['title'] + "  Canal: " + video['channel_title'] + "  País: " +
        video['country'] + "  Días tendencia: " + str(trenddays) + "\n")
    elif int(option) == 2:
        print("Título: " + video['title'] + "  Canal: " + video['channel_title'] + "  Categoría: " +
        video['category_id'] + "  Días tendencia: " + str(trenddays) + "\n")

# Menu de opciones

def printMenu():
    print("Bienvenido")
    print("1- Cargar información de videos en el catálogo")
    print("2- Consultar videos tendencia con más views por categoría y país")
    print("3- Consultar video tendencia por país")
    print("4- Consultar video tendencia por categoría")
    print("5- Consultar videos con más likes por país y tag")
    print("0- Salir")

# Funciones de inicialización

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
        sample = int(input("Ingrese el número de videos a listar\n"))
        videos = controller.getVideosByCategoryandCountry(catalog, categoryid, country)
        sortedVideos = controller.sortVideosByViews(videos)
        if sample > int(lt.size(videos)):
            print("El número de videos a listar excede el tamaño del catálogo\n")
        else:
            print("Los " + str(sample) + " videos con más views de la categoría " + name + " de " + 
            country + " son: ")
            printSortedVideosByViews(sortedVideos, sample)

    elif int(inputs[0]) == 3:
        country = str(input("Ingrese el país\n"))
        videos = controller.getVideosByCountry(catalog, country)
        firstVideo = controller.getFirstVideoByTrendDays(videos)
        print("El video con más días tendencia del país " + country + " es: ")
        printFirstVideoByTrendDays(firstVideo, 1)

    elif int(inputs[0]) == 4:
        name = str(input("Ingrese el nombre de la categoría\n"))
        categoryid = controller.getCategoryid(catalog, name)
        videos = controller.getVideosByCategory(catalog, categoryid)
        firstVideo = controller.getFirstVideoByTrendDays(videos)
        print("El video con más días tendencia de la categoría " + name + " es: ")
        printFirstVideoByTrendDays(firstVideo, 2)

    elif int(inputs[0]) == 5:
        country = str(input("Ingrese el país\n"))
        tag = str(input("Ingrese el tag\n"))
        sample = int(input("Ingrese el número de videos a listar\n"))
        videos = controller.getVideosByCountryandTag(catalog, country, tag)
        sortedVideos = controller.sortVideosByLikes(videos)
        if sample > int(lt.size(videos)):
            print("El número de videos a listar excede el tamaño del catálogo\n")
        else:
            print("Los " + str(sample) + " videos con más likes de " + country + " con el tag " + 
            tag + " son: ")
            printSortedVideosByLikes(sortedVideos, sample)

    else:
        sys.exit(0)
sys.exit(0)
