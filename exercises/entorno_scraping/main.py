# Aplicación para bajar el contenido html de una web

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


def run():
    for i in range(1, 6):
        # Traer los datos de la web
        response = requests.get('https://xkcd.com/{}'.format(i))
        # Parsear la respuesta
        soup = BeautifulSoup(response.content, 'html.parser')
        # Obtener el contenedor (id=comic) o div de la imagen
        image_container = soup.find(id = 'comic')
        # Obtener la imagen del contenedor, primero indica la etiqueda y despues un atributo
        image_url = image_container.find('img')['src']
        # Ontener el nombre original de la imagen
        image_name = image_url.split('/')[-1]

        print('Descargando la imagen {}'.format(image_name))

        # Guardar la imagen descargada
        urlretrieve('https:{}'.format(image_url), image_name)
        

if __name__ == '__main__':
    run()
