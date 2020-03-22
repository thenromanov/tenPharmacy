import sys
import requests
from io import BytesIO
from PIL import Image
from centerMap import getCenter
from scaleMap import getScale
from modules import getAddressCoords, getOrganizations, getOrganizationInfo


address = ' '.join(sys.argv[1:])
searchCoords, *searchCorners = getAddressCoords(address)

organizations = getOrganizations('аптека', searchCoords)['features']

coords = [searchCoords]
corners = [searchCorners]
points = '{},flag~'.format(','.join(map(str, searchCoords)))
for i in range(min(10, len(organizations))):
    info = getOrganizationInfo(organizations[i])
    coords.append(info['coords'])
    corners.append(info['corners'])
    if not info['time']:
        points += '{},pm2grl{}~'.format(','.join(map(str, info['coords'])), str(i + 1))
    elif 'круглосуточно' in info['time']:
        points += '{},pm2gnl{}~'.format(','.join(map(str, info['coords'])), str(i + 1))
    else:
        points += '{},pm2bll{}~'.format(','.join(map(str, info['coords'])), str(i + 1))


mapParams = {
    'll': ','.join(map(str, getCenter(*coords))),
    'spn': ','.join(map(str, getScale(*corners))),
    'l': 'map',
    'pt': points[:-1]
}

mapServer = 'http://static-maps.yandex.ru/1.x/'
response = requests.get(mapServer, params=mapParams)
Image.open(BytesIO(response.content)).show()
