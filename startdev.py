import webbrowser
import threading
import time
import subprocess
import os

def abrir_navegador():
    time.sleep(1.5)
    webbrowser.open_new("http://127.0.0.1:8000")

def iniciar_django_com_venv():
    venv_python = os.path.abspath(".venv/Scripts/python.exe")
    manage_py = os.path.abspath("personagem/manage.py")
    subprocess.call([venv_python, manage_py, "runserver"])

if __name__ == "__main__":
    threading.Thread(target=abrir_navegador).start()
    iniciar_django_com_venv()
