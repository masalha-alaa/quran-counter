python -m venv temp_venv
CALL temp_venv/Scripts/activate
CALL pip install -r minimal_requirements.txt

CALL pyinstaller --name=QuranCounter --onedir --windowed --add-data "data;data" --add-data "embedding_models/topic_sim_model__2024_01_23__16_57_30.zip;embedding_models" --add-data "embeddings/topics_embeddings.pkl;embeddings/topics_embeddings.pkl" --add-data "gui/resources;gui/resources" --add-data "translations;translations" --add-data "fonts;fonts" --add-data "surah_index.yml;." main.py

CALL deactivate
RD /s /q "temp_venv"
