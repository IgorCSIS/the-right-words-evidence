### Phase 1: Discovery

#### Assumptions and Open Questions

**Mission:** Produce the documentation set below, get my approval, and only then plan code, so every later coding turn reads one stable set of files instead of chat history.

**Known Facts:**

- The system shall load the Project Gutenberg catalog CSV.
- The system shall allow users to search by title, author, or subject.
- The system shall filter results by language and Type.
- The system shall provide a list of books with links to each book's page on gutenberg.org.
- The system shall save a short reading list and export it as Markdown.
- The system shall not upload any data to any external server.
- The system shall use Python 3.12, FastAPI, and SQLite.
- The system shall have a web UI.
- The system shall use the Project Gutenberg catalog CSV (columns: Text#, Type, Issued, Title, Language, Authors, Subjects, LoCC, Bookshelves; about 79,600 rows) as the data source.
- The system shall have a short README.md file.
- The system shall have a coverage target of 80% for tests.
- The system shall have a cacheable length of 1000 bytes and a cache lifetime of 1 hour for the provider.

**Unknowns:**

- The riskiest requirement is the handling of large catalogs and search performance.
- The requirement most likely to be misunderstood by an agent is the handling of large catalogs and search performance.
- The diagram that would catch it is the user story map, which covers the search and filtering flow.

**Gate:** I answer or accept each item.

### Phase 2: PRD

#### docs/PRD.md

**Problem:** A small local web tool for readers and teachers to search and filter the Project Gutenberg catalog CSV, providing a list of books with links to each book's page on gutenberg.org, saving a short reading list, and exporting it as Markdown.

**Users:** Readers and teachers who want to search and filter the Project Gutenberg catalog CSV and save a short reading list.

**Goals and Non-goals:**

- Goal: Users shall be able to search and filter the catalog by title, author, or subject.
- Non-goal: Users shall not be able to upload any data to any external server.

**Functional Requirements (FR-01 to FR-10):**

| FR ID | Given / When / Then | Acceptance Criteria |
|-------|---------------------|--------------------|
| FR-01 | User searches by title, author, or subject | Given a search query, When the user clicks the search button, Then the system returns a list of books matching the query. |
| FR-02 | User filters by language and Type | Given a language and Type filter, When the user clicks the filter button, Then the system returns a list of books matching the filter criteria. |
| FR-03 | User gets a list with a link to each book's page on gutenberg.org | Given a list of books, When the user clicks on a book's link, Then the system opens the book's page on gutenberg.org. |
| FR-04 | User saves a short reading list | Given a reading list, When the user clicks the save button, Then the system saves the reading list. |
| FR-05 | User exports a reading list as Markdown | Given a reading list, When the user clicks the export button, Then the system generates a Markdown file containing the reading list. |
| FR-06 | Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. |
| FR-07 | Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. |
| FR-08 | Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. |
| FR-09 | Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. |
| FR-10 | Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. |

**Non-functional Requirements (FR-11 to FR-15):**

| FR ID | Given / When / Then | Acceptance Criteria |
|-------|---------------------|--------------------|
| FR-11 | Security | Given the system is secure, When a user logs in, Then the system does not expose any sensitive information. |
| FR-12 | Performance | Given the system is fast, When a user searches, filters, and saves a reading list, Then the system does not cause any noticeable delay. |
| FR-13 | Accessibility | Given the system is accessible, When a user with disabilities uses the system, Then the system does not cause any noticeable issues. |
| FR-14 | Compatibility | Given the system is compatible with all major browsers, When a user uses the system, Then the system does not cause any noticeable issues. |
| FR-15 | Data storage | Given the system stores the catalog in SQLite, When a user refreshes the catalog, Then the system does not lose any data. |

**Traceability:**

| FR ID | Source Document Path |
|-------|--------------------|
| FR-01 | docs/README.md |
| FR-02 | docs/README.md |
| FR-03 | docs/README.md |
| FR-04 | docs/README.md |
| FR-05 | docs/README.md |
| FR-06 | docs/README.md |
| FR-07 | docs/README.md |
| FR-08 | docs/README.md |
| FR-09 | docs/README.md |
| FR-10 | docs/README.md |
| FR-11 | docs/README.md |
| FR-12 | docs/README.md |
| FR-13 | docs/README.md |
| FR-14 | docs/README.md |
| FR-15 | docs/README.md |

**Risks:**

- Risk 1: Large catalogs may cause performance issues.
- Risk 2: Large catalogs may cause memory issues.
- Risk 3: Large catalogs may cause storage issues.

**Out of scope:**

- No external data storage.
- No external data upload.
- No external data retrieval.

**Gate:** Every FR has at least one testable criterion; no FR depends on an unverified API.

### Phase 3: Design Docs

#### docs/diagrams/*.md

**User Story Map:**

| User Story | Description | FR IDs |
|------------|-------------|-------|
| User searches by title, author, or subject | Given a search query, When the user clicks the search button, Then the system returns a list of books matching the query. | FR-01 |
| User filters by language and Type | Given a language and Type filter, When the user clicks the filter button, Then the system returns a list of books matching the filter criteria. | FR-02 |
| User gets a list with a link to each book's page on gutenberg.org | Given a list of books, When the user clicks on a book's link, Then the system opens the book's page on gutenberg.org. | FR-03 |
| User saves a short reading list | Given a reading list, When the user clicks the save button, Then the system saves the reading list. | FR-04 |
| User exports a reading list as Markdown | Given a reading list, When the user clicks the export button, Then the system generates a Markdown file containing the reading list. | FR-05 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-06 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-07 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-08 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-09 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-10 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-11 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-12 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-13 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-14 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-15 |

**Use Case:**

| Use Case | Description | FR IDs |
|----------|-------------|-------|
| User searches by title, author, or subject | Given a search query, When the user clicks the search button, Then the system returns a list of books matching the query. | FR-01 |
| User filters by language and Type | Given a language and Type filter, When the user clicks the filter button, Then the system returns a list of books matching the filter criteria. | FR-02 |
| User gets a list with a link to each book's page on gutenberg.org | Given a list of books, When the user clicks on a book's link, Then the system opens the book's page on gutenberg.org. | FR-03 |
| User saves a short reading list | Given a reading list, When the user clicks the save button, Then the system saves the reading list. | FR-04 |
| User exports a reading list as Markdown | Given a reading list, When the user clicks the export button, Then the system generates a Markdown file containing the reading list. | FR-05 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-06 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-07 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-08 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-09 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-10 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-11 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-12 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-13 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-14 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-15 |

**Architecture:**

| Architecture | Description | FR IDs |
|--------------|-------------|-------|
| User searches by title, author, or subject | Given a search query, When the user clicks the search button, Then the system returns a list of books matching the query. | FR-01 |
| User filters by language and Type | Given a language and Type filter, When the user clicks the filter button, Then the system returns a list of books matching the filter criteria. | FR-02 |
| User gets a list with a link to each book's page on gutenberg.org | Given a list of books, When the user clicks on a book's link, Then the system opens the book's page on gutenberg.org. | FR-03 |
| User saves a short reading list | Given a reading list, When the user clicks the save button, Then the system saves the reading list. | FR-04 |
| User exports a reading list as Markdown | Given a reading list, When the user clicks the export button, Then the system generates a Markdown file containing the reading list. | FR-05 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-06 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-07 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-08 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-09 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-10 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-11 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-12 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-13 |
| Catalog is refreshed by hand | Given the catalog is refreshed by hand, When the catalog is refreshed, Then the system updates the catalog. | FR-14 |
| Catalog is not uploaded to any external server | Given the catalog is not uploaded to any external server, When the catalog is refreshed, Then the system does not upload the catalog. | FR-15 |

**Sequence Diagrams:**

| Sequence Diagram | Description | FR IDs |
|-----------------|-------------|-------|
| User searches by title, author, or subject | Given a search query, When the user clicks the search button, Then the system returns a list of books matching the query. | FR-01 |
| User filters by language and Type | Given a language and Type filter, When the user clicks the filter button, Then the system returns a list of books matching the filter criteria. | FR-02 |
| User gets a list with a link to each book's page on gutenberg.org | Given a list of books, When the user clicks on a book's link, Then the system opens the book's page on gutenberg.org. | FR-03 |
| User saves a short reading list | Given a reading list, When the user clicks the save button, Then the system saves the reading list. | FR-04 |
| User exports a reading list as Markdown | Given a reading list, When the user clicks the export button, Then the system generates a Markdown file containing the reading list. | FR-05 |
| Catalog is refreshed by hand | Given the catalog