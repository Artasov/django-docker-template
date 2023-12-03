@echo off
SETLOCAL EnableDelayedExpansion

:: Получаем текущую дату в формате ГГГГ-ММ-ДД
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do (
    set datetime=%%a
)
set current_date=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2%

:: Указываем путь к директории логов
set log_directory=.\logs

:: Создаем директорию, если она не существует
if not exist "%log_directory%" mkdir "%log_directory%"

:: Формируем имя файла лога
set log_file=%log_directory%\project_container_%current_date%.log

:: Запускаем docker-compose с перенаправлением вывода в файл и консоль
PowerShell -Command "docker-compose --env-file .env.prod -f docker-compose.prod.yml up --build | Tee-Object -FilePath '%log_file%'"
