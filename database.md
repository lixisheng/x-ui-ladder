# Database

x-ui stores its runtime SQLite/configuration files inside `db/`, mounted to `/etc/x-ui` in the container.

The `db/` directory is intentionally ignored except for `.gitkeep` because it may contain generated credentials, node configuration, and runtime state.
