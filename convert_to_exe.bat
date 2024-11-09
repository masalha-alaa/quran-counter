CALL .venv/Scripts/activate

CALL pyinstaller --name=QuranCounter --onefile --windowed --add-data "data;data" --add-data "gui/resources;gui/resources" --add-data "translations;translations" --add-data "fonts;fonts" --add-data "config.yml;." --add-data "surah_index.yml;." main.py

CALL deactivate