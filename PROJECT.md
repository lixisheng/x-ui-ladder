# PROJECT

Project: x-ui-ladder
Source workspace: github
Root path: `/usr/local/mine/workspace/github/repos/x-ui-ladder`
Project type: Docker Compose deployment wrapper for `ghcr.io/mhsanaei/3x-ui:latest`
Web panel port: `25143` -> container `2053`
Client software: v2rayNG on desktop/mobile
Runtime data: `db/`, `cert/`, `.env` are local-only and ignored
Start command: `./scripts/start.sh`
Stop command: `./scripts/stop.sh`
Health check: `./scripts/healthcheck.sh`
