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
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

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
    videosfile = cf.data_dir + 'videos/videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategory(catalog):
    """
    Cargar las categorías del archivo. Por cada categoría se indica al
    modelo que debe adicionarla al catálogo
    """
    categoryidfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoryidfile, encoding='utf-8'), delimiter='\t')
    for category in input_file:
        model.addCategory(catalog, category)

# Funciones de ordenamiento

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

def getVideosByCountry(catalog, country):
    """
    Retorna los videos de un país específico
    """
    return model.getVideosByCountry(catalog, country)
