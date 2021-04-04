"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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

import time
import tracemalloc
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo
"""

# Inicialización del catálogo de videos

def initCatalog():
    """
    Llama la función de inicialización del catálogo al modelo
    """
    catalog = model.newCatalog()
    return catalog
    
# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y carga los datos en las
    estructuras de datos. Retorna el tiempo de procesamiento
    y la memoria alocada
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    loadVideos(catalog)
    loadCategory(catalog)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return deltatime, deltamemory

def loadVideos(catalog):
    """
    Carga los videos del archivo. Por cada video se indica al
    modelo que debe adicionarlo al catálogo
    """
    videosfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategory(catalog):
    """
    Carga las categorías del archivo. Por cada categoría se indica al
    modelo que debe adicionarla al catálogo
    """
    categoryidfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoryidfile, encoding='utf-8'), delimiter='\t')
    for category in input_file:
        model.addCategory(catalog, category)

# Funciones de ordenamiento

def sortVideosByViews(catalog):
    """
    Ordena el catálogo de videos por su número de views
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    sortedvideos = model.sortVideosByViews(catalog)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return sortedvideos, deltatime, deltamemory


def sortVideosByLikes(catalog):
    """
    Ordena el catálogo de videos por su número de likes
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    sortedvideos = model.sortVideosByLikes(catalog)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return sortedvideos, deltatime, deltamemory

# Funciones de consulta sobre el catálogo

def videosSize(catalog):
    """
    Número de videos cargados en el catálogo
    """
    return model.videosSize(catalog)

def categorySize(catalog):
    """
    Número de categorías cargadas en el catálogo
    """
    return model.categorySize(catalog)

def getCategoryid(catalog, name):
    """
    Retorna el id de una categoría
    """
    return model.getCategoryid(catalog, name)

def getVideosByCountry(catalog, country):
    """
    Retorna los videos de un país específico, el tiempo de
    procesamiento y la memoria alocada
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    videos = model.getVideosByCountry(catalog, country)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return videos, deltatime, deltamemory

def getVideosByCategory(catalog, category):
    """
    Retorna los videos de una categoría específica, el tiempo de
    procesamiento y la memoria alocada
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    videos = model.getVideosByCategory(catalog, category)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return videos, deltatime, deltamemory

def getVideosByCategoryandCountry(catalog, category, country):
    """
    Retorna los videos de una categoría y país específicos, el tiempo
    de procesamiento y la memoria alocada
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    videos = model.getVideosByCategoryandCountry(catalog, category, country)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return videos, deltatime, deltamemory

def getVideosByCountryandTag(catalog, country, tag):
    """
    Retorna los videos de un país específico, con un tag específico,
    el tiempo de procesamiento y la memoria alocada
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    videos = model.getVideosByCountryandTag(catalog, country, tag)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return videos, deltatime, deltamemory

def getFirstVideoByTrendDays(catalog):
    """
    Retorna el video con mayor número de trending days, el tiempo
    de procesamiento y la memoria alocada
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    videos = model.getFirstVideoByTrendDays(catalog)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return videos, deltatime, deltamemory

# Funciones para medir tiempo y memoria

def getTime():
    """
    Retorna el instante de tiempo de procesamiento en
    milisegundos
    """
    return float(time.perf_counter()*1000)

def getMemory():
    """
    Retorna la memoria alocada en un instante de tiempo
    """
    return tracemalloc.take_snapshot()

def deltaMemory(startmemory, stopmemory):
    """
    Retorna la diferencia de memoria alocada entre dos instantes
    de tiempo en bytes
    """
    memorydiff = stopmemory.compare_to(startmemory, 'filename')
    deltamemory = 0.0
    for stat in memorydiff:
        deltamemory = deltamemory + stat.size_diff
    deltamemory = deltamemory/1024.0
    return deltamemory