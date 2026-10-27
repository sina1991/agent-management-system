import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RepositoryScaffoldTests(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            "README.md",
            "docs/ARCHITECTURE.md",
            "agents/alpha/PROFILE.md",
            "agents/manager/PROFILE.md",
            "agents/technical/PROFILE.md",
            "contracts/task.yaml",
            "contracts/execution-report.yaml",
            "contracts/handoff.yaml",
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
                self.assertEqual(data.get("$schema"), "https://json-schema.org/draft/2020-12/schema")

    def test_profiles_have_mission(self):
        for path in (ROOT / "agents").glob("*/PROFILE.md"):
            with self.subTest(path=path.name):
                self.assertIn("Mission", path.read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
