################################################################################
#Web scraping & Text mining
#Go to a lyrics web page and find all songs from one artist (Madonna in this case)
#and search for the lyrics (creates a list) and add each text in a .txt file
#Sitio de Internet (https://www.lyrics.com/)

!pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests
import re
import time

def limpiarhtml(html_text):
  cadena = re.compile('<.*?>')
  return re.sub(cadena,'',html_text)

def write_file(soup, titulo):
  texto_interes = soup.find_all("pre", {'class': 'lyric-body'})
  f.write('\n' + '#'*50 + '\n'+ str(titulo)+ '\n' + '#'*50 + '\n\n' )
  for texto in texto_interes:
    f.write(limpiarhtml(str(texto)))

raiz_enlace= 'https://www.lyrics.com'
sitio_web = requests.get('https://www.lyrics.com/artist/Madonna/64565')
soup = BeautifulSoup(sitio_web.content, 'html.parser')

elementos = soup.find('body').find_all('a')
print(list(elementos))

lista_revisados = set()
lista_pendientes= set()

for link in soup.findAll('a'):
  linea = link.get('href')
  if len(str(linea)) > 6:
    if (str(linea)[0:7] == '/lyric/') and (raiz_enlace+ link.get('href')) not in lista_revisados:
      #print('-->', linea)
      lista_pendientes.add(raiz_enlace+ linea)

print('No. de canciones por explorar: ',len(lista_pendientes))

i = 1
f= open("lyrics.txt","w+") #Inicializa el archivo
while (len(lista_pendientes) != 0):
  sitio = lista_pendientes.pop()
  sitio_web = requests.get(sitio)
  soup = BeautifulSoup(sitio_web.content, 'html.parser')
  titulo = limpiarhtml(str(soup.title))
  print(i, '. ',titulo)  
  write_file(soup, titulo)
  time.sleep(1) #evitar bloqueo de IP address
  i += 1
f.close()
