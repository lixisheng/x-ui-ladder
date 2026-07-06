# Change Log

## 2026-07-06 Initial x-ui ladder project

- Created Docker Compose based x-ui deployment project.
- Configured x-ui Web panel host port `25143` mapped to container port `54321`.
- Added `.env.example`, start/stop/healthcheck scripts, and v2rayNG usage notes.
- Kept runtime database, certificates, and local `.env` out of Git.

## 2026-07-06 Switch to classic x-ui

- Replaced 3x-ui image with classic `enwaiax/x-ui:latest` because the requested panel is old x-ui.
- Updated Web panel mapping to `25143:54321`.
- Backed up 3x-ui runtime DB files into ignored `db-3xui-backup/` before starting old x-ui.
- Verification: old x-ui `0.3.2` started and `http://127.0.0.1:25143/` returned `HTTP 200`.
