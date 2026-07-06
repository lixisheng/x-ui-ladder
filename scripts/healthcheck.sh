#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
if [[ -f .env ]]; then
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
fi
url="http://127.0.0.1:${XUI_PANEL_PORT:-25143}"
for _ in $(seq 1 30); do
  code="$(curl -s -o /dev/null -w '%{http_code}' "$url" || true)"
  if [[ "$code" =~ ^(200|301|302|303|307|308|404)$ ]]; then
    echo "x-ui web is reachable: $url HTTP $code"
    docker compose ps
    exit 0
  fi
  sleep 2
done
echo "x-ui web is not reachable: $url" >&2
docker compose ps >&2 || true
exit 1
