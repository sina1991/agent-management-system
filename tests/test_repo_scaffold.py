import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryScaffoldTests(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            "README.md",
            "docs/ARCHITECTURE.md",
            "docs/CHAT_BOOTSTRAP.md",
            "docs/WORKFLOW.md",
            "agents/alpha/PROFILE.md",
            "agents/manager/PROFILE.md",
            "agents/technical/PROFILE.md",
            "contracts/task.yaml",
            "contracts/execution-report.yaml",
            "contracts/handoff.yaml",
            "project_state/project-status.yaml",
            "project_state/project-graph.yaml",
            "project_state/information-index.yaml",
        ]
        for relative in required:
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_json_schemas_are_valid_json(self):
        for path in (ROOT / "contracts/schemas").glob("*.schema.json"):
            with self.subTest(path=path.name):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(
                    data.get("$schema"),
                    "https://json-schema.org/draft/2020-12/schema",
                )

    def test_profiles_have_mission(self):
        for path in (ROOT / "agents").glob("*/PROFILE.md"):
            with self.subTest(path=path.name):
                self.assertIn("Mission", path.read_text(encoding="utf-8"))

    def test_all_core_roles_define_startup_protocol(self):
        for role in ("alpha", "manager", "technical"):
            path = ROOT / "agents" / role / "PROFILE.md"
            with self.subTest(role=role):
                self.assertIn("Startup protocol", path.read_text(encoding="utf-8"))

    def test_bootstrap_requires_explicit_alpha_confirmation(self):
        content = (ROOT / "docs/CHAT_BOOTSTRAP.md").read_text(encoding="utf-8")
        self.assertIn("Do not claim the role is activated until the user confirms.", content)
        self.assertIn("Phase 1 — Project discovery and planning", content)
        self.assertIn("Phase 2 — Execution governance", content)

    def test_published_status_is_not_stale(self):
        content = (ROOT / "project_state/project-status.yaml").read_text(encoding="utf-8")
        self.assertIn("status: published_scaffold_under_review", content)
        self.assertNotIn("scaffold_generated_not_yet_published", content)


if __name__ == "__main__":
    unittest.main()
