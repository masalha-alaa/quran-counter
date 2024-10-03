CALL .venv/Scripts/activate
pyside6-uic .\gui\main_screen.ui -o .\gui\main_screen.py
pyside6-lupdate gui/main_screen.ui -ts gui/translations/ar.ts
pyside6-lrelease gui/translations/ar.ts
pyside6-lrelease gui/translations/en.ts
pyside6-rcc gui\resources\resources.qrc -o resources_rc.py
deactivate