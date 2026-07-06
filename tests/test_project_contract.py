import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class XuiLadderContractTests(unittest.TestCase):
    def read(self, relative):
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_compose_maps_old_xui_panel_to_host_port_25143(self):
        compose = self.read("docker-compose.yml")
        self.assertIn("enwaiax/x-ui:latest", compose)
        self.assertRegex(compose, r'"25143:54321"')
        self.assertIn("./db:/etc/x-ui", compose)
        self.assertIn("./cert:/root/cert", compose)

    def test_runtime_ports_are_documented_for_v2rayng_clients(self):
        env_example = self.read(".env.example")
        self.assertIn("XUI_PANEL_PORT=25143", env_example)
        self.assertIn("VLESS_TCP_PORT=10086", env_example)
        self.assertIn("REALITY_TLS_PORT=9443", env_example)
        readme = self.read("README.md")
        self.assertIn("v2rayNG", readme)
        self.assertIn("http://127.0.0.1:25143", readme)

    def test_scripts_use_project_compose_and_have_strict_shell(self):
        for name in ["scripts/start.sh", "scripts/stop.sh", "scripts/healthcheck.sh"]:
            content = self.read(name)
            self.assertTrue(content.startswith("#!/usr/bin/env bash\nset -euo pipefail\n"), name)
            self.assertIn("docker compose", content, name)
        health = self.read("scripts/healthcheck.sh")
        self.assertIn("http://127.0.0.1:${XUI_PANEL_PORT:-25143}", health)

    def test_sensitive_runtime_outputs_are_gitignored(self):
        gitignore = self.read(".gitignore")
        for pattern in [".env", "db/*", "cert/*", "*.log"]:
            self.assertIn(pattern, gitignore)
        self.assertIn("!db/.gitkeep", gitignore)
        self.assertIn("!cert/.gitkeep", gitignore)


if __name__ == "__main__":
    unittest.main()
