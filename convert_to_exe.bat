@echo off
SET PRO=%1
REM NOTE: THERE'S NO DIFFERENCE BETWEEN PRO AND NOT PRO ANYMORE
IF /I "%PRO%"=="pro" (
    echo INSTALLING PRO
    SET REQUIREMENTS_FILE=minimal_requirements.txt
) ELSE (
    echo INSTALLING BASIC
    SET REQUIREMENTS_FILE=minimal_requirements.txt
)

IF EXIST dist (
    RD /s /q "dist"
)

python -m venv temp_venv
CALL temp_venv/Scripts/activate
CALL pip3 install pyinstaller
CALL pip3 install -r %REQUIREMENTS_FILE%

CALL pyinstaller --name=QuranCounter --onedir --window --icon=gui/resources/app-icon.ico --add-data "data;data" --add-data "embeddings/topics_embeddings.pkl;embeddings" --add-data "gui/resources;gui/resources" --add-data "translations;translations" --add-data "fonts;fonts" --add-data "surah_index.yml;." --add-data "app_info.json;." main.py

CALL deactivate
RD /s /q "temp_venv"

COPY "app_info.json" "dist/app_info.json"
COPY "README.md" "dist/README.md"
COPY "changelog.txt" "dist/changelog.txt"
COPY "LICENSE" "dist/LICENSE"
CD dist
"C:\Program Files\7-Zip\7z.exe" a QuranCounter.zip QuranCounter
CD ..
