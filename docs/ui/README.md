# Desktop screen gallery

These images capture the actual Qt presentation layers in Arabic and English. The reader text, graph, meanings, and progress are deterministic visual fixtures, not results from a live search or network request. The same detailed-results layout is used for words, surahs, and topics.

| Screen | Arabic | English |
| --- | --- | --- |
| Main search | [Preview](arabic.png) | [Preview](english.png) |
| Quran reader | [Preview](dialogs/mushaf-ar.png) | [Preview](dialogs/mushaf-en.png) |
| Reader selection tools | [Preview](dialogs/mushaf-selection-ar.png) | [Preview](dialogs/mushaf-selection-en.png) |
| Reader statistics | [Preview](dialogs/mushaf-statistics-ar.png) | [Preview](dialogs/mushaf-statistics-en.png) |
| Detailed results | [Preview](dialogs/details-ar.png) | [Preview](dialogs/details-en.png) |
| Relations graph | [Preview](dialogs/relations-ar.png) | [Preview](dialogs/relations-en.png) |
| Assistant key setup | [Preview](dialogs/key-ar.png) | [Preview](dialogs/key-en.png) |
| Meaning selection | [Preview](dialogs/disambiguation-ar.png) | [Preview](dialogs/disambiguation-en.png) |
| Downloads | [Preview](dialogs/download-ar.png) | [Preview](dialogs/download-en.png) |
| Update checking | [Preview](dialogs/update-ar.png) | [Preview](dialogs/update-en.png) |
| Waiting | [Preview](dialogs/waiting-ar.png) | [Preview](dialogs/waiting-en.png) |

Regenerate from the repository root:

```sh
python tools/render_ui_preview.py --language ar --output docs/ui/arabic.png
python tools/render_ui_preview.py --language en --output docs/ui/english.png
python tools/render_dialog_previews.py --output-dir docs/ui/dialogs
```

The full application and Windows EXE still need the separately distributed Quran data and topic embeddings. These screenshots do not verify data-backed searches or Windows packaging.
