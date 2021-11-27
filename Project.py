from concurrent.futures import ThreadPoolExecutor
import requests
import os, sys, time
cls = lambda: os.system('cls')
directorios = []
contador =0

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
	global contador
	res = requests.get(urls, timeout=2);
	if res.status_code != 404:
		contador+=1
		print(f'   {os.getpid()}  url-> {urls}')

def main():
	if len(sys.argv) < 4:
		cls()
		print(f'[*] Uso del programa...! \n\n nombrePrograma.py  url a escanear  "directorio diccionario"  #Threads')
	else:
		url = str(sys.argv[1])
		ruta =os.getcwd()+sys.argv[2]
		threads = int(sys.argv[3]) 	
		cls()
		print(f'[+] Comenzando ... Espere un momento por favor . . .\n')
		recopilatorio(ruta, url)
		if directorios:
			start = time.perf_counter()
			with ThreadPoolExecutor(max_workers=threads) as p:
				p.map(proceso, directorios)
			finish = time.perf_counter()
			print(f"Fuzzing terminado en {round(finish-start, 2)} segundos\n")
			print('\nDirectorios encontrados : ', contador)
		else:
			print('Ha ocurrido un error')

if __name__ == '__main__':

    main()  