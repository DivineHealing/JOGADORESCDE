@echo off
setlocal
title Ficha - Crônicas de Errat

echo ========================================
echo Ficha desenvolvida por Ariel Silva e Andrey Jhonnes
echo Iniciando o sistema...
echo ========================================

:: Caminho base do projeto
set BASE_DIR=%~dp0

:: Ativar o ambiente virtual
call "%BASE_DIR%.venv\Scripts\activate.bat"
if errorlevel 1 (
    echo ❌ ERRO: Nao foi possivel ativar o ambiente virtual.
    pause
    exit /b
)

:: Entrar na pasta do projeto Django
cd "%BASE_DIR%personagem"

:: Abre o navegador na URL padrão do Django
start http://127.0.0.1:8000/

:: Executar o servidor Django
python manage.py runserver

:: Fim
echo.
echo Pressione qualquer tecla para sair...
pause >nul
