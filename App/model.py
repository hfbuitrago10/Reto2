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
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos
"""

# Construcción de modelos

def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista para guardar
    los videos. Se crean indices (maps) por los siguientes
    criterios:
    video ids
    category
    category ids
    country
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
    catalog['videos'] = lt.newList('ARRAY_LIST', compareVideosids)

    """
    Se crean indices (maps) por diferentes criterios para llegar
    a la información consultada
    """

    """
    Este indice crea un map cuya llave es el video id del video
    """
    catalog['videoids'] = mp.newMap(200000,
                                     maptype='PROBING',
                                     loadfactor=0.30,
                                     comparefunction=compareMapVideosids)

    """
    Este indice crea un map cuya llave es el category name del video
    """
    catalog['category'] = mp.newMap(35, 
                                     maptype='PROBING', 
                                     loadfactor=0.30,
                                     comparefunction=compareCategory)
    
    """
    Este indice crea un map cuya llave es el category id del video
    """
    catalog['categoryids'] = mp.newMap(20,
                                        maptype='PROBING',
                                        loadfactor=0.30,
                                        comparefunction=compareCategoryids)
    
    """
    Este indice crea un map cuya llave es el país del video
    """
    catalog['country'] = mp.newMap(10,
                                    maptype='PROBING',
                                    loadfactor=0.30,
                                    comparefunction=compareMapCountry)
    
    return catalog

# Funciones para agregar información al catálogo

def addVideo(catalog, video):
    """
    Adiciona un video a la lista de videos, adicionalmente lo guarda
    en un map usando su id como llave
    Adicionalmente, crea una entrada en el map de category ids para indicar
    que el video pertenece a una category id específica
    Finalmente, crea una entrada en el map de países para indicar que el
    video pertenece a un país específico
    """
    lt.addLast(catalog['videos'], video)
    addVideoids(catalog, video)
    addCategoryids(catalog, video)
    addVideoCountry(catalog, video)

def addCategory(catalog, category):
    """
    Adiciona las categorías al map de category, donde la llave es
    el name y el valor es el id de la categoría
    """
    mp.put(catalog['category'], category['name'], category['id'])

def addVideoids(catalog, video):
    """
    Adiciona un video a la lista de videos con un video id específico,
    los video ids se guardan en un map, donde la llave es el id del video
    y el valor es el número de días de trending y la lista de videos con
    ese video id
    """
    try:
        videoids = catalog['videoids']
        videoid = video['video_id']
        existvideoid = mp.contains(videoids, videoid)
        if existvideoid:
            entry = mp.get(videoids, videoid)
            id = me.getValue(entry)
        else:
            id = newVideoid(videoid)
            mp.put(videoids, videoid, id)
        lt.addLast(id['videos'], video)
        id['trendingdays'] = lt.size(id['videos'])
    except Exception:
        return None

def addCategoryids(catalog, video):
    """
    Adiciona un video a la lista de videos de una categoría específica,
    las categorías se guardan en un map, donde la llave es el id de la
    categoría y el valor es la lista de videos de esa categoría
    """
    try:
        categoryids = catalog['categoryids']
        videoCategoryid = video['category_id']
        existcategoryid = mp.contains(categoryids, videoCategoryid)
        if existcategoryid:
            entry = mp.get(categoryids, videoCategoryid)
            categoryid = me.getValue(entry)
        else:
            categoryid = newVideoCategory(videoCategoryid)
            mp.put(categoryids, videoCategoryid, categoryid)
        lt.addLast(categoryid['videos'], video)
        categoryid['total_videos'] = lt.size(categoryid['videos'])
    except Exception:
        return None

def addVideoCountry(catalog, video):
    """
    Adiciona un video a la lista de videos de un país específico, los
    países se guardan en un map, donde la llave es el país y el valor
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

# Funciones para creación de datos

def newVideoid(videoid):
    """
    Esta función crea la estructura de videos asociados a
    una video id específica
    """
    videosid = {'videoid': '',
                'trendingdays': 0,
                'videos': None}
    
    videosid['videoid'] = videoid
    videosid['videos'] = lt.newList('ARRAY_LIST')
    return videosid

def newVideoCategory(id):
    """
    Esta función crea la estructura de videos asociados a
    una categoría específica
    """
    category = {'id': '', 
                'total_videos': 0,
                'videos': None}
    
    category['id'] = id
    category['videos'] = lt.newList('ARRAY_LIST')
    return category

def newVideoCountry(country):
    """
    Esta función crea la estructura de videos asociados a
    un país específico
    """
    countryentry = {'country': '',
                    'videos': None}

    countryentry['country'] = country
    countryentry['videos'] = lt.newList('ARRAY_LIST')
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

def getCategoryid(catalog, name):
    """
    Retorna el id de una categoría
    """
    categoryname = " " + name
    entry = mp.get(catalog['category'], categoryname)
    if entry:
        categoryid = me.getValue(entry)
        return categoryid
    else:
        return None

def getVideosByCountry(catalog, country):
    """
    Retorna los videos de un país específico
    """
    country = mp.get(catalog['country'], country)
    if country:
        return me.getValue(country)['videos']

def getVideosByCategory(catalog, category):
    """
    Retorna los videos de una categoría específica
    """
    category = mp.get(catalog['categoryids'], category)
    if category:
        return me.getValue(category)['videos']

def getVideosByCategoryandCountry(catalog, category, country):
    """
    Retorna los videos de una categoría y país específicos
    """
    category = getVideosByCategory(catalog, category)
    try:
        videos = lt.newList('ARRAY_LIST')
        for video in lt.iterator(category):
            if country == video['country']:
                lt.addLast(videos, video)
        return videos
    except Exception:
        return None 

def getVideosByCountryandTag(catalog, country, tag):
    """
    Retorna los videos de un país específico, con un tag
    específico
    """
    country = getVideosByCountry(catalog, country)
    try:
        videos = lt.newList('ARRAY_LIST')
        for video in lt.iterator(country):
            if tag.lower() in video['tags'].lower():
                lt.addLast(videos, video)
        return videos
    except Exception:
        return None

def getFirstVideoByTrendDays(catalog):
    """
    Retorna el video con mayor número de trending days
    """
    videoidsmap = mp.newMap(200000,
                            maptype='CHAINING',
                            loadfactor=4.0,
                            comparefunction=compareMapVideosids)
    try:
        for video in lt.iterator(catalog):
            videoid = video['video_id']
            existvideoid = mp.contains(videoidsmap, videoid)
            if existvideoid:
                entry = mp.get(videoidsmap, videoid)
                id = me.getValue(entry)
            else:
                id = newVideoid(videoid)
                mp.put(videoidsmap, videoid, id)
            lt.addLast(id['videos'], video)
            id['trendingdays'] = lt.size(id['videos'])
    except Exception:
        return None
    
    mp.remove(videoidsmap, '#NAME?')
    videoids = mp.keySet(videoidsmap)

    try:
        maxTrendDays = 0
        firstVideo = None
        for videoid in lt.iterator(videoids):
            entry = mp.get(videoidsmap, videoid)
            trendDays = me.getValue(entry)['trendingdays']
            if trendDays > maxTrendDays:
                maxTrendDays = trendDays
                firstVideo = entry
        return firstVideo
    except Exception:
        return None

# Funciones utilizadas para comparar elementos

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

def compareVideosByViews(video1, video2):
    """
    Compara dos videos por su número de views
    """
    return (float(video1['views']) > float(video2['views']))

def compareVideosByLikes(video1, video2):
    """
    Compara dos videos por su número de likes
    """
    return (float(video1['likes']) > float(video2['likes']))

# Funciones de ordenamiento

def sortVideosByViews(catalog):
    """
    Ordena el catálogo de videos por su número de views
    """
    sortVideosByViews = ms.sort(catalog, compareVideosByViews)
    return sortVideosByViews

def sortVideosByLikes(catalog):
    """
    Ordena el catálogo de videos por su número de likes
    """
    sortVideosByLikes = ms.sort(catalog, compareVideosByLikes)
    return sortVideosByLikes