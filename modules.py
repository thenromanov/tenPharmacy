import requests


def getAddresses(address):
    geocoderServer = 'http://geocode-maps.yandex.ru/1.x/'
    geocoderParams = {
        'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
        'geocode':  address,
        'format': 'json'}
    return requests.get(geocoderServer, params=geocoderParams).json()


def getAddressCoords(address):
    jsonResponse = getAddresses(address)
    toponym = jsonResponse['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    requestCoords = list(map(float, toponym['Point']['pos'].split()))
    toponymCorners = jsonResponse['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']
    lowerCorner = list(map(float, toponymCorners['lowerCorner'].split()))
    upperCorner = list(map(float, toponymCorners['upperCorner'].split()))
    return [requestCoords, lowerCorner, upperCorner]


def getOrganizations(text, coords):
    searchServer = 'https://search-maps.yandex.ru/v1/'
    searchParams = {
        'apikey': 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3',
        'text': text,
        'lang': 'ru_RU',
        'll': '{},{}'.format(coords[0], coords[1]),
        'type': 'biz'
    }
    return requests.get(searchServer, params=searchParams).json()


def getOrganizationInfo(organization):
    info = {'name': organization['properties']['CompanyMetaData']['name'],
            'address': organization['properties']['CompanyMetaData']['address'],
            'time': None,
            'coords': organization['geometry']['coordinates'],
            'corners': organization['properties']['boundedBy']}
    if 'Hours' in organization['properties']['CompanyMetaData'].keys():
        info['time'] = organization['properties']['CompanyMetaData']['Hours']['text']
    return info
