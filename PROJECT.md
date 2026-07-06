# PROJECT

Project: x-ui-ladder
Source workspace: github
Root path: `/usr/local/mine/workspace/github/repos/x-ui-ladder`
Project type: Docker Compose deployment wrapper for `enwaiax/x-ui:latest`
Web panel port: `25143` -> container `54321`
Active node ports: `46274/tcp+udp` for 电脑端, `25776/tcp+udp` for 移动端
Preset node ports: `10086/tcp+udp`, `9443/tcp+udp`
Client software: v2rayNG on desktop/mobile
Runtime data: `db/`, `cert/`, `.env` are local-only and ignored
Start command: `./scripts/start.sh`
Stop command: `./scripts/stop.sh`
Health check: `./scripts/healthcheck.sh`
Latest verified status: classic x-ui `0.3.2` running healthy; Web `25143` returns `HTTP 200`; mobile v2rayNG scan/import connectivity confirmed.
