# Scrub report

Checked before the first commit on 2026-10-21.

Removed or replaced:
- Local machine paths replaced with `<book-workspace>/` or `<workspace>/` (paths in runner scripts and attachment fields).
- The sender line used in PT-13 (a street address, town and phone) replaced with `[POSTAL ADDRESS REMOVED]`, `[TOWN REMOVED]` and `[PHONE REMOVED]`.
- The school name in the PT-12 author profile removed.
- A sample email on a `.com` domain in the prompt tests changed to the reserved `.example` domain.
- Large public data files removed (see REMOVED_LARGE_FILES.md).
- Zip archives of the logs removed (the same files are here unzipped).

Kept on purpose:
- Email addresses on reserved `.example` domains. They are fictional test data and cannot belong to anyone.

Scan: regex patterns for xAI, Anthropic and OpenAI style keys, AWS access keys, GitHub tokens, Bearer tokens, private key headers and inline api_key values, plus an exact match against the API key values used for the runs. Result: 0 matches.
