Input (REAL public dataset): Project Gutenberg catalog CSV, https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv , downloaded 2026-10-21 (21,263,721 bytes; 79,634 rows; columns: Text#, Type, Issued, Title, Language, Authors, Subjects, LoCC, Bookshelves). Counts measured on the box with Python csv.
PROJECT_BRIEF: A small local web tool for readers and teachers. It loads the public Project Gutenberg catalog CSV (columns Text#, Type, Issued, Title, Language, Authors, Subjects, LoCC, Bookshelves; about 79,600 rows). The user searches by title, author or subject, filters by language and Type, and gets a list with a link to each book's page on gutenberg.org. The user can save a short reading list and export it as Markdown. Nothing is uploaded anywhere; the catalog is refreshed by hand.
STACK: Python 3.12, FastAPI, SQLite
AGENTS: Claude Code, Cursor
STORAGE: SQLite
UI_TYPE: web
SOURCES: docs/brief.md (the brief above) and the pg_catalog.csv header
RULES_MAX_LINES: 150
COVERAGE: 80
