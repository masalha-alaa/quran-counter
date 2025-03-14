CALL .venv/Scripts/activate

REM main_screen
pyside6-uic .\gui\main_window\main_screen.ui -o .\gui\main_window\main_screen.py
pyside6-lupdate gui/main_window/main_screen.ui -ts translations/main_screen_ar.ts
pyside6-lrelease translations/main_screen_ar.ts
pyside6-lrelease translations/main_screen_en.ts

REM disambiguation_dialog
pyside6-uic .\gui\disambiguation_dialog\disambiguation_dialog.ui -o .\gui\disambiguation_dialog\disambiguation_dialog.py
pyside6-lupdate gui/disambiguation_dialog/disambiguation_dialog.ui -ts translations/disambiguation_dialog_ar.ts
pyside6-lrelease translations/disambiguation_dialog_ar.ts
pyside6-lrelease translations/disambiguation_dialog_en.ts

REM waiting_dialog
pyside6-uic .\gui\waiting_dialog\waiting_dialog.ui -o .\gui\waiting_dialog\waiting_dialog.py
pyside6-lupdate gui/waiting_dialog/waiting_dialog.ui -ts translations/waiting_dialog_ar.ts
pyside6-lrelease translations/waiting_dialog_ar.ts
pyside6-lrelease translations/waiting_dialog_en.ts

REM word_detailed_display dialog
pyside6-uic .\gui\detailed_display_dialog\word_detailed_display_dialog.ui -o .\gui\detailed_display_dialog\word_detailed_display_dialog.py
pyside6-lupdate gui/detailed_display_dialog/word_detailed_display_dialog.ui -ts translations/word_detailed_display_dialog_ar.ts
pyside6-lrelease translations/word_detailed_display_dialog_ar.ts
pyside6-lrelease translations/word_detailed_display_dialog_en.ts

REM openai_key_setup dialog
pyside6-uic .\gui\openai_key_setup_dialog\openai_key_setup_dialog.ui -o .\gui\openai_key_setup_dialog\openai_key_setup_dialog.py
pyside6-lupdate gui/openai_key_setup_dialog/openai_key_setup_dialog.ui -ts translations/openai_key_setup_dialog_ar.ts
pyside6-lrelease translations/openai_key_setup_dialog_ar.ts
pyside6-lrelease translations/openai_key_setup_dialog_en.ts

REM mushaf_view dialog
pyside6-uic .\gui\mushaf_view_dialog\mushaf_view.ui -o .\gui\mushaf_view_dialog\mushaf_view.py
pyside6-lupdate gui/mushaf_view_dialog/mushaf_view.ui -ts translations/mushaf_view_ar.ts
pyside6-lrelease translations/mushaf_view_ar.ts
pyside6-lrelease translations/mushaf_view_en.ts

REM download_dialog dialog
pyside6-uic .\gui\download_dialog\download_dialog.ui -o .\gui\download_dialog\download_dialog.py
pyside6-lupdate gui/download_dialog/download_dialog.ui -ts translations/download_dialog_ar.ts
pyside6-lrelease translations/download_dialog_ar.ts
pyside6-lrelease translations/download_dialog_en.ts

REM version_update_dialog dialog
pyside6-uic .\gui\version_update_dialog\version_update_dialog.ui -o .\gui\version_update_dialog\version_update_dialog.py
pyside6-lupdate gui/version_update_dialog/version_update_dialog.ui -ts translations/version_update_dialog_ar.ts
pyside6-lrelease translations/version_update_dialog_ar.ts
pyside6-lrelease translations/version_update_dialog_en.ts

REM relations_graph dialog
pyside6-uic .\gui\relations_graph\relations_graph.ui -o .\gui\relations_graph\relations_graph.py
pyside6-lupdate gui/relations_graph/relations_graph.ui -ts translations/relations_graph_ar.ts
pyside6-lrelease translations/relations_graph_ar.ts
pyside6-lrelease translations/relations_graph_en.ts

REM dynamic_translations
pyside6-lrelease translations/dynamic_translations_ar_src_ar.ts
pyside6-lrelease translations/dynamic_translations_ar_src_en.ts
pyside6-lrelease translations/dynamic_translations_en_src_ar.ts
pyside6-lrelease translations/dynamic_translations_en_src_en.ts

pyside6-rcc gui\resources\resources.qrc -o resources_rc.py
deactivate