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

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo
"""

# Inicialización del catálogo de libros

def initCatalog():
    """
    Llama la función de inicialización del catálogo al modelo
    """
    catalog = model.newCatalog()
    return catalog
    
# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y carga los datos
    en las estructuras de datos
    """
    loadVideos(catalog)
    loadCategory(catalog)

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
    return model.sortVideosByViews(catalog)

def sortVideosByLikes(catalog):
    """
    Ordena el catálogo de videos por su número de likes
    """
    return model.sortVideosByLikes(catalog)

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
    Retorna los videos de un país específico
    """
    return model.getVideosByCountry(catalog, country)

def getVideosByCategory(catalog, category):
    """
    Retorna los videos de una categoría específica
    """
    return model.getVideosByCategory(catalog, category)

def getVideosByCategoryandCountry(catalog, category, country):
    """
    Retorna los videos de una categoría y país específicos
    """
    return model.getVideosByCategoryandCountry(catalog, category, country)

def getVideosByCountryandTag(catalog, country, tag):
    """
    Retorna los videos de un país específico, con un tag
    específico
    """
    return model.getVideosByCountryandTag(catalog, country, tag)

def getFirstVideoByTrendDays(catalog):
    """
    Retorna el video con mayor número de trending days
    """
    return model.getFirstVideoByTrendDays(catalog)