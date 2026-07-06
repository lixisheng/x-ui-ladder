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

## 2026-07-06 Publish active node ports

- Published the x-ui-created active node ports through Docker Compose: `46274/tcp+udp` for 电脑端 and `25776/tcp+udp` for 移动端.
- Added `XUI_DESKTOP_NODE_PORT=46274` and `XUI_MOBILE_NODE_PORT=25776` to `.env.example`.
- Verified Docker published `0.0.0.0:25776->25776/tcp+udp` and `0.0.0.0:46274->46274/tcp+udp`.
- Verified x-ui Web remained reachable on `http://127.0.0.1:25143` with `HTTP 200`.
- User confirmed mobile v2rayNG scan/import connectivity after the port mapping fix.
- Pushed the fix to GitHub as commit `02d736f fix: publish configured x-ui node ports`.
