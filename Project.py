from threading import Thread
import sys, os, time, requests, colorama
cls = lambda: os.system('cls')
from queue import Queue
from fake_useragent import UserAgent
from colorama import Fore
from colorama import Style
colorama.init()
concurrent = 50
q = Queue(concurrent * 2)

def menu():
    cls()
    print(f"""{Fore.CYAN}
 __                     _                    _             _  _    ___  _  _
/ _\ ___  __ _ _ __ ___| |__   ___ _ __ /\ /(_)_ __   __ _| || |  / _ \| || |
\ \ / _ \/ _` | '__/ __| '_ \ / _ \ '__/ //_/ | '_ \ / _` | || |_| | | | || |_
_\ \  __/ (_| | | | (__| | | |  __/ | / __ \| | | | | (_| |__   _| |_| |__   _|
\__/\___|\__,_|_|  \___|_| |_|\___|_| \/  \/|_|_| |_|\__, |  |_|  \___/   |_|
                                                     |___/
                                                           By: 183381,183423
{Style.RESET_ALL}""")
    print(f'{Fore.LIGHTMAGENTA_EX}[+] Comenzando ... Espere un momento por favor . . .\n{Style.RESET_ALL}')
    global link,ruta
    link = str(sys.argv[1])
    ruta = os.getcwd()+sys.argv[2]

def userAgent():
    ua = UserAgent()
    return ua.random

def proceso():
    global contador
    contador = 0
    while True:
        url = link + q.get()
        status, url = Peticiones(url)
        directoriosEncontrados(status, url)
        contador+=1
        q.task_done()

def Peticiones(ourl):
    try:
        res = requests.get(ourl, timeout=2)
        return res.status_code, ourl
    except:
        return "Ha ocurrido un error, verifique la url.\n", ourl

def directoriosEncontrados(status, url):
    if status != 404:
        if status == 200:
            print(f'{Fore.LIGHTGREEN_EX}status: {status}  |  url: {url} {Style.RESET_ALL}')
        elif status ==403:
            print(f'{Fore.YELLOW}status: {status} Administrador  |  url: {url} {Style.RESET_ALL}')
    
def Fuzzing():
    ua = userAgent()
    for i in range(concurrent):
        t = Thread(target=proceso)
        t.daemon = True
        t.start()
    try:
        valores = open(ruta, 'r')
        for url in valores:
            q.put(url.strip())
        q.join()
    except KeyboardInterrupt:
        sys.exit(1)

def main():
    menu()
    start = time.perf_counter()
    Fuzzing()
    finish = time.perf_counter()
    print(f"\n{Fore.LIGHTCYAN_EX}Fuzzing terminado en {round(finish-start, 2)} segundos\n")
    print(f'{Fore.LIGHTYELLOW_EX}Directorios probados : ', contador)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        cls()
        print(f"""{Fore.LIGHTGREEN_EX}
 __                     _                    _             _  _    ___  _  _
/ _\ ___  __ _ _ __ ___| |__   ___ _ __ /\ /(_)_ __   __ _| || |  / _ \| || |
\ \ / _ \/ _` | '__/ __| '_ \ / _ \ '__/ //_/ | '_ \ / _` | || |_| | | | || |_
_\ \  __/ (_| | | | (__| | | |  __/ | / __ \| | | | | (_| |__   _| |_| |__   _|
\__/\___|\__,_|_|  \___|_| |_|\___|_| \/  \/|_|_| |_|\__, |  |_|  \___/   |_|
                                                     |___/
                                                           By: 183381,183423
{Style.RESET_ALL}""")
        print(f'{Fore.LIGHTYELLOW_EX}[*] Uso del programa...! \n\n nombrePrograma.py  <url>   <diccionario> {Style.RESET_ALL}')
    else:
        main()