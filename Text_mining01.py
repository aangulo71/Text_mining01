#Text mining
#Go to a lyrics web page and copy the text of a specific song from a list, in a .txt file

################################################################################
#Este es un ejemplo simple para extraer el texto de canciones de varias páginas
#de un sitio de Internet (https://www.lyrics.com/)
################################################################################
#!pip install beautifulsoup4

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


lista_sitios_web = ['https://www.lyrics.com/lyric/35459784/Madonna/Papa+Don%27t+Preach',
                    'https://www.lyrics.com/lyric/36341851/Madonna/Like+a+Prayer',
                    'https://www.lyrics.com/lyric/36290739/Madonna/Medell%C3%ADn',
                    'https://www.lyrics.com/lyric/36050507/Madonna/Live+to+Tell',
                    'https://www.lyrics.com/lyric/36111222/Madonna/Holiday',
                    'https://www.lyrics.com/lyric/35087044/Madonna/Open+Your+Heart',
                    'https://www.lyrics.com/lyric/35737015/Madonna/True+Blue',
                    'https://www.lyrics.com/lyric/35737007/Madonna/Where%27s+the+Party%3F',
                    'https://www.lyrics.com/lyric/35736991/Madonna/Take+a+Bow',
                    'https://www.lyrics.com/lyric/35736983/Madonna/Lucky+Star',
                    'https://www.lyrics.com/lyric/35736998/Madonna/Express+Yourself',
                    'https://www.lyrics.com/lyric/35459778/Madonna/Like+a+Virgin',
                    'https://www.lyrics.com/lyric/35459779/Madonna/Material+Girl',
                    'https://www.lyrics.com/lyric/35459774/Madonna/La+Isla+Bonita']

lista_sitios_web

f= open("lyrics.txt","w+") #Inicializa el archivo
for sitio in lista_sitios_web:
  sitio_web = requests.get(sitio)
  soup = BeautifulSoup(sitio_web.content, 'html.parser')
  titulo = limpiarhtml(str(soup.title))
  print(titulo)  
  write_file(soup, titulo)
  time.sleep(1) #evitar bloqueo de IP address
f.close()
