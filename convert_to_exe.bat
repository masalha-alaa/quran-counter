SET PRO=%1
IF %PRO%==pro (
    echo INSTALLING PRO
    SET REQUIREMENTS_FILE=minimal_requirements_pro.txt
) ELSE (
    echo INSTALLING BASIC
    SET REQUIREMENTS_FILE=minimal_requirements.txt
)

python -m venv temp_venv
CALL temp_venv/Scripts/activate
CALL pip install -r %REQUIREMENTS_FILE%

CALL pyinstaller --exclude-module=torch --name=QuranCounter --onedir --windowed --add-data "data;data" --add-data "embeddings/topics_embeddings.pkl;embeddings" --add-data "gui/resources;gui/resources" --add-data "translations;translations" --add-data "fonts;fonts" --add-data "surah_index.yml;." --add-data "python-3.10.11-embed-amd64;python-3.10.11-embed-amd64" main.py

CALL deactivate
RD /s /q "temp_venv"
