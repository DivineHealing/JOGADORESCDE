@echo off
setlocal
title Ficha - Crônicas de Errat

echo ========================================
echo Ficha desenvolvida por Ariel Silva e Andrey Jhonnes
echo Iniciando o sistema...
echo ========================================

:: Caminho base
set BASE_DIR=%~dp0
cd /d "%BASE_DIR%"

:: Verifica se o Python está instalado
where python >nul 2>&1
if errorlevel 1 (
    echo ⚠ Python não encontrado. Tentando instalar...

    :: Baixar o instalador silenciosamente
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe -OutFile python_installer.exe"

    :: Instalar Python silenciosamente com add ao PATH
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    if errorlevel 1 (
        echo ❌ Falha ao instalar o Python.
        pause
        exit /b
    )

    del python_installer.exe
)

:: Recarrega o ambiente para reconhecer python no PATH
echo 🐍 Python instalado. Atualizando PATH...
setx PATH "%PATH%;C:\Python311\Scripts\;C:\Python311\"

:: Verifica novamente
where python >nul 2>&1
if errorlevel 1 (
    echo ❌ Python ainda não foi reconhecido. Reinicie o sistema ou instale manualmente.
    pause
    exit /b
)

:: Cria ambiente virtual se não existir
if not exist .venv (
    echo 🔧 Criando ambiente virtual...
    python -m venv .venv
)

:: Ativar ambiente virtual
call ".venv\Scripts\activate.bat"
if errorlevel 1 (
    echo ❌ ERRO: Nao foi possivel ativar o ambiente virtual.
    pause
    exit /b
)

:: Instala dependências
if exist requirements.txt (
    echo 📦 Instalando dependências...
    pip install --upgrade pip
    pip install -r requirements.txt
) else (
    echo ⚠ Nenhum requirements.txt encontrado!
)

:: Acessa o diretório do projeto Django
cd personagem

:: Abre o navegador
start http://127.0.0.1:8000/

:: Inicia o servidor Django
python manage.py runserver

:: Fim
echo.
echo Pressione qualquer tecla para sair...
pause >nul
