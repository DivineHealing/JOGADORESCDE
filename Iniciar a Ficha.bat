@echo off
setlocal
title Ficha - Crônicas de Errat

echo ========================================
echo Ficha desenvolvida por Ariel Silva e Andrey J. G. Santos
echo Iniciando o sistema...
echo ========================================

:: Caminho base
set BASE_DIR=%~dp0
cd /d "%BASE_DIR%"

:: Verifica se o Python está instalado
where python >nul 2>&1
if errorlevel 1 (
    echo ⚠ Python não encontrado. Tentando instalar...

    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe -OutFile python_installer.exe"
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    if errorlevel 1 (
        echo ❌ Falha ao instalar o Python.
        pause
        exit /b
    )
    del python_installer.exe
)

:: Garante que o Python esteja acessível
set PATH=%PATH%;%ProgramFiles%\Python311\Scripts;%ProgramFiles%\Python311\

:: Cria ambiente virtual, se não existir
if not exist .venv (
    echo 🔧 Criando ambiente virtual...
    python -m venv .venv
)

:: Ativar ambiente virtual
call ".venv\Scripts\activate.bat"
if errorlevel 1 (
    echo ❌ Erro ao ativar o ambiente virtual.
    pause
    exit /b
)
:: Instala dependências SOMENTE se necessário
if exist requirements.txt (
    echo 📦 Checando dependências...
    >"%TEMP%\req_check.txt" (
        for /f "usebackq delims=" %%d in (`type requirements.txt`) do (
            echo Checking: %%d
            pip show %%d >nul 2>&1
            if errorlevel 1 (
                echo ❗ Dependência faltando: %%d
                echo Faltando: %%d>>"%TEMP%\missing_reqs.txt"
            )
        )
    )

    if exist "%TEMP%\missing_reqs.txt" (
        echo ⚙ Instalando dependências ausentes...
        pip install -r requirements.txt
        del "%TEMP%\missing_reqs.txt"
    ) else (
        echo ✅ Todas as dependências já estão instaladas.
    )
) else (
    echo ⚠ Nenhum arquivo requirements.txt encontrado!
)

:: Acessa o diretório do projeto
cd personagem

:: Abre o navegador
start http://127.0.0.1:8000/

:: Executa o Migrate
python manage.py migrate
if errorlevel 1 (
    echo ❌ Erro ao executar o migrate.
    pause
    exit /b
)

:: Inicia o servidor
python manage.py runserver

echo.
echo Pressione qualquer tecla para sair...
pause >nul
