from concurrent.futures import ThreadPoolExecutor
import requests
import os, sys, time
cls = lambda: os.system('cls')

link = ''
archivo = ''
match = []
directorios = []

def recopilatorio(archivo, link):
	valores = open(archivo, "r")
	if os.path.exists(archivo):
		for word in valores:
			directorios.append(link+word.replace('\n',''))
		valores.close()
		return directorios
	else:
		print('No se ha encontrado el Fichero')
	valores.close()
	
def proceso(urls):
	res = requests.get(urls, timeout=2)
	if res.status_code != 404:
		match.append('👀 -> :' +urls)
	else: 
		print('😕 -> '+urls)
	
def main():
	start = time.perf_counter()
	if len(sys.argv) < 4:
		cls()
		print(f'[*] Uso del programa...! \n\n nombrePrograma.py  url a escanear  "directorio diccionario"  #Threads')
	else:
		url = str(sys.argv[1])
		ruta =os.getcwd()+sys.argv[2]
		threads = int(sys.argv[3]) 	
		cls()
		print(f'[+] Comenzando ... Espere un momento por favor . . .')
		recopilatorio(ruta, url)
		if directorios:
			with ThreadPoolExecutor(max_workers=threads) as executor:
				executor.map(proceso, directorios)
			finish = time.perf_counter()
			print('\nDirectorios encontrados : ', len(match))
			print(f"Terminado en {round(finish-start, 2)} segundos\n")
			for found in match:
				print(found)
		else:
			print('Ha ocurrido un error')

main()