import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryScaffoldTests(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            "README.md",
            "docs/ARCHITECTURE.md",
            "docs/FINAL_ARCHITECTURE.fa.md",
            "docs/CHAT_BOOTSTRAP.md",
            "docs/WORKFLOW.md",
            "agents/alpha/PROFILE.md",
            "agents/manager/PROFILE.md",
            "agents/technical/PROFILE.md",
            "contracts/task.yaml",
            "contracts/execution-report.yaml",
            "contracts/handoff.yaml",
            "contracts/schemas/task.schema.json",
            "contracts/schemas/execution-report.schema.json",
            "project_state/project-status.yaml",
            "project_state/project-graph.yaml",
            "project_state/information-index.yaml",
        ]
        for relative in required:
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_json_schemas_are_valid_json(self):
        schemas = list((ROOT / "contracts/schemas").glob("*.schema.json"))
        self.assertGreater(len(schemas), 0)
        for path in schemas:
            with self.subTest(path=path.name):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(
                    data.get("$schema"),
                    "https://json-schema.org/draft/2020-12/schema",
                )

    def test_profiles_have_mission_and_startup_protocol(self):
        for role in ("alpha", "manager", "technical"):
            path = ROOT / "agents" / role / "PROFILE.md"
            content = path.read_text(encoding="utf-8")
            with self.subTest(role=role):
                self.assertIn("Mission", content)
                self.assertIn("Startup protocol", content)

    def test_manager_has_no_human_management_channel(self):
        content = (ROOT / "agents/manager/PROFILE.md").read_text(encoding="utf-8")
        self.assertIn("Does not communicate directly with the human user", content)
        self.assertIn("DECISION_REQUEST", content)
        self.assertIn("Alpha", content)

    def test_technical_terminal_rules_are_present(self):
        content = (ROOT / "agents/technical/PROFILE.md").read_text(encoding="utf-8")
        for marker in ("clear", "sed -i", "cat > /path/to/file", "web/app.py", "grep", "sed -n", "AUDIT", "APPLY", "VERIFY"):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_manager_authority_and_alpha_ownership_are_explicit(self):
        manager = (ROOT / "agents/manager/PROFILE.md").read_text(encoding="utf-8")
        alpha = (ROOT / "agents/alpha/PROFILE.md").read_text(encoding="utf-8")
        self.assertIn("without per-task reapproval", manager)
        self.assertIn("Unit Agent definitions", alpha)
        self.assertIn("cannot create, delete, or redefine Unit Agent ownership", manager)

    def test_bootstrap_states_message_relay_and_role_boundaries(self):
        content = (ROOT / "docs/CHAT_BOOTSTRAP.md").read_text(encoding="utf-8")
        self.assertIn("human user relays messages", content)
        self.assertIn("must not ask the human user", content)
        self.assertIn("limited operational way", content)

    def test_published_status_is_not_stale(self):
        content = (ROOT / "project_state/project-status.yaml").read_text(encoding="utf-8")
        self.assertIn("status: published_scaffold_under_review", content)
        self.assertNotIn("scaffold_generated_not_yet_published", content)


if __name__ == "__main__":
    unittest.main()
