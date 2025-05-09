import webbrowser
import threading
import time
import os

def abrir_navegador():
    time.sleep(1.5)  # Espera o servidor subir
    webbrowser.open_new("http://127.0.0.1:8000")  # Altere para sua URL, se necessário

def iniciar_django():
    os.system("python manage.py runserver")

if __name__ == "__main__":
    threading.Thread(target=abrir_navegador).start()
    iniciar_django()
