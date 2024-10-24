CALL ./venv Scripts/activate

CALL pyinstaller --name=QuranCounter --onefile --windowed --add-data "data;data" --add-data "gui/resources;g
ui/resources" --add-data "gui/translations;gui/translations" --add-data "config.yml;." --add-data "surah_index.yml;." main.

CALL deactivate