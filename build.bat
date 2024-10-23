CALL .venv/Scripts/activate

REM main_screen
pyside6-uic .\gui\main_screen.ui -o .\gui\main_screen.py
pyside6-lupdate gui/main_screen.ui -ts gui/translations/main_screen_ar.ts
pyside6-lrelease gui/translations/main_screen_ar.ts
pyside6-lrelease gui/translations/main_screen_en.ts

REM disambiguation_dialog
pyside6-uic .\gui\disambiguation_dialog.ui -o .\gui\disambiguation_dialog.py
pyside6-lupdate gui/disambiguation_dialog.ui -ts gui/translations/disambig_dlg_ar.ts
pyside6-lrelease gui/translations/disambig_dlg_ar.ts
pyside6-lrelease gui/translations/disambig_dlg_en.ts

REM waiting_dialog
pyside6-uic .\gui\waiting_dialog.ui -o .\gui\waiting_dialog.py
pyside6-lupdate gui/waiting_dialog.ui -ts gui/translations/waiting_dlg_ar.ts
pyside6-lrelease gui/translations/waiting_dlg_ar.ts
pyside6-lrelease gui/translations/waiting_dlg_en.ts

REM word_detailed_display dialog
pyside6-uic .\gui\word_detailed_display.ui -o .\gui\word_detailed_display.py
pyside6-lupdate gui/word_detailed_display.ui -ts gui/translations/word_detailed_display_ar.ts
pyside6-lrelease gui/translations/word_detailed_display_ar.ts
pyside6-lrelease gui/translations/word_detailed_display_en.ts

REM mushaf_view dialog
pyside6-uic .\gui\mushaf_view.ui -o .\gui\mushaf_view.py
pyside6-lupdate gui/mushaf_view.ui -ts gui/translations/mushaf_view_ar.ts
pyside6-lrelease gui/translations/mushaf_view_ar.ts
pyside6-lrelease gui/translations/mushaf_view_en.ts

REM dynamic_translations
pyside6-lrelease gui/translations/dynamic_translations_ar.ts
pyside6-lrelease gui/translations/dynamic_translations_en.ts

pyside6-rcc gui\resources\resources.qrc -o resources_rc.py
deactivate