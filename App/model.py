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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista para guardar
    los videos. Se crean indices (maps) por los siguientes
    criterios:
    Video ids
    Category
    Category ids
    """
    catalog = {'videos': None, 
               'videoids': None,
               'category': None, 
               'categoryids': None,
               'country': None}
    
    """
    Esta lista contiene los videos del archivo. Los videos son
    referenciados por los indices creados a continuación
    """
    catalog['videos'] = lt.newList('SINGLE_LINKED', compareVideosids)

    """
    Se crean indices (maps) por diferentes criterios para llegar
    a la información consultada
    """

    """
    Este indice crea un map cuya llave es el video id del video
    """
    catalog['videoids'] = mp.newMap(1000,
                                    maptype='CHAINING',
                                    loadfactor=4.0,
                                    comparefunction=compareMapVideosids)

    """
    Este indice crea un map cuya llave es el category name del video
    """
    catalog['category'] = mp.newMap(100, 
                                      maptype='CHAINING', 
                                      loadfactor=4.0,
                                      comparefunction=compareCategory)
    
    """
    Este indice crea un map cuya llave es el category id del video
    """
    catalog['categoryids'] = mp.newMap(100,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction=compareCategoryids)
    
    """
    Este indice crea un map cuya llave es el país del video
    """
    catalog['country'] = mp.newMap(100,
                                    maptype='CHAINING',
                                    loadfactor=4.0,
                                    comparefunction=compareMapCountry)
    
    return catalog

# Funciones para agregar informacion al catálogo

def addVideo(catalog, video):
    """
    Adiciona un video a la lista de videos, adicionalmente lo guarda
    en un map usando su id como llave.
    Además, crea una entrada en el map de paises para indicar que ese
    video pertenece a un país específico.
    """
    lt.addLast(catalog['videos'], video)
    mp.put(catalog['videoids'], video['video_id'], video)
    addVideoCountry(catalog, video)

def addCategory(catalog, category):
    """
    """
    newCategory = newVideoCategory(category['name'], category['id'])
    mp.put(catalog['category'], category['name'], newCategory)
    mp.put(catalog['categoryids'], category['id'], newCategory)

def addVideoCountry(catalog, video):
    """
    Adiciona un video a la lista de videos de un país específico, los
    paises se guardan en un map, donde la llave es el país y el valor
    es la lista de videos de ese país
    """
    try:
        countries = catalog['country']
        videoCountry = video['country']
        existcountry = mp.contains(countries, videoCountry)
        if existcountry:
            entry = mp.get(countries, videoCountry)
            country = me.getValue(entry)
        else:
            country = newVideoCountry(videoCountry)
            mp.put(countries, videoCountry, country)
        lt.addLast(country['videos'], video)
    except Exception:
        return None

# Funciones para creacion de datos

def newVideoCategory(name, id):
    """
    Esta función crea la estructura de videps asociados a
    una categoría específica
    """
    category = {'name': '', 
                'id': '', 
                'total_videos': 0,
                'videos': None}
    
    category['name'] = name
    category['id'] = id
    category['videos'] = lt.newList()
    return category

def newVideoCountry(country):
    """
    Esta función crea la estructura de videos asociados a
    un país específico
    """
    countryentry = {'country': '',
                    'videos': None}

    countryentry['country'] = country
    countryentry['videos'] = lt.newList()
    return countryentry

# Funciones de consulta

def videosSize(catalog):
    """
    Número de videos cargados en el catálogo
    """
    return lt.size(catalog['videos'])

def categorySize(catalog):
    """
    Número de categorías cargadas en el catálogo
    """
    return mp.size(catalog['category'])

def getVideosByCountry(catalog, country):
    """
    Retorna los videos de un país específico
    """
    country = mp.get(catalog['country'], country)
    if country:
        return me.getValue(country)['videos']

# Funciones utilizadas para comparar elementos dentro de una lista

def compareVideosids(id1, id2):
    """
    Compara los ids de dos videos
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMapVideosids(id, entry):
    """
    Compara los ids de dos videos, id es un identificador
    del video y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (str(id) == str(identry)):
        return 0
    elif (str(id) > str(identry)):
        return 1
    else:
        return -1

def compareCategory(name, category):
    """
    Compara los category name de dos videos, name es el 
    nombre de la categoría y category una pareja llave-valor
    """
    categoryentry = me.getKey(category)
    if (name == categoryentry):
        return 0
    elif (name > categoryentry):
        return 1
    else:
        return -1

def compareCategoryids(id, category):
    """
    Compara los category ids de dos videos, id es un identificador
    de la categoría y category una pareja llave-valor
    """
    categoryentry = me.getKey(category)
    if (int(id) == int(categoryentry)):
        return 0
    elif (int(id) > int(categoryentry)):
        return 1
    else:
        return -1

def compareMapCountry(country, entry):
    """
    Compara el país de dos videos, country es el país del
    video y entry una pareja llave-valor
    """
    countryentry = me.getKey(entry)
    if (country == countryentry):
        return 0
    elif (country > countryentry):
        return 1
    else:
        return -1

def compareCountry(country1, country2):
    """
    Compara el país de dos videos
    """
    if (country1 == country2):
        return 0
    elif (country1 > country2):
        return 1
    else:
        return -1

# Funciones de ordenamiento

def sortVideosByViews(catalog):
    """
    Ordena el catálogo de videos por sus 'views'
    """
    pass