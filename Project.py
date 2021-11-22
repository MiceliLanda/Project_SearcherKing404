from concurrent.futures import ThreadPoolExecutor
import requests
import os

link = 'https://virtual.upchiapas.edu.mx/'
archivo = os.getcwd()+'\diccionario\/rutas.txt'
match = []

def recopilatorio():
	directorios = []
	valores = open(archivo, "r")
	if os.path.exists(archivo):
		for word in valores:
			directorios.append(link+word.replace('\n',''))
		print('Fichero Leído Correctamente')
		return directorios
	else:
		print('No se encuentra el Fichero')
	valores.close()
	
def proceso(urls):
	res = requests.get(urls, timeout=2)
	if res.status_code == 200:
		match.append('👀 -> :' +urls)
	else: 
		print('😕 -> '+urls)
	
def main():
	if recopilatorio():
		with ThreadPoolExecutor(max_workers=800) as executor:
			executor.map(proceso, recopilatorio())
		print('\nDirectorios encontrados : ', len(match))
		for found in match:
			print(found)
	else:
		print('Ha ocurrido un error')

main()
