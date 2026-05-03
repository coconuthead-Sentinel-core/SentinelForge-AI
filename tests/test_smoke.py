"""
Smoke test suite for canon #9 — SentinelForge AI.

Verifies the repo's structural promise per the README:
  - 01_BACK_END/ FastAPI service
  - 02_MIDDLE_LAYER/ protocol activation
  - 03_FRONT_END/ React component
  - 04_CONTEXT/ Glyphic Codex master + schemas
  - Three-zone (GREEN/YELLOW/RED) cognitive routing model
"""
from pathlib import Path

ROOT = Path(__file__).parent.parent


class TestRepoStructure:
    def test_readme_exists(self):
        assert (ROOT / "README.md").exists()

    def test_readme_has_h1(self):
        c = (ROOT / "README.md").read_text(encoding="utf-8")
        assert c.strip().startswith("#")

    def test_readme_mentions_sentinelforge(self):
        c = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        assert "sentinelforge" in c or "sentinel forge" in c

    def test_license_exists(self):
        assert (ROOT / "LICENSE").exists()

    def test_license_is_mit(self):
        c = (ROOT / "LICENSE").read_text(encoding="utf-8")
        assert "MIT License" in c
        assert "Shannon Brian Kelly" in c


class TestArchitectureFolders:
    """Verify each tier promised in the README actually exists."""

    def test_back_end_folder_exists(self):
        assert (ROOT / "01_BACK_END").exists() and (ROOT / "01_BACK_END").is_dir()

    def test_middle_layer_folder_exists(self):
        assert (ROOT / "02_MIDDLE_LAYER").exists() and (ROOT / "02_MIDDLE_LAYER").is_dir()

    def test_front_end_folder_exists(self):
        assert (ROOT / "03_FRONT_END").exists() and (ROOT / "03_FRONT_END").is_dir()

    def test_context_folder_exists(self):
        assert (ROOT / "04_CONTEXT").exists() and (ROOT / "04_CONTEXT").is_dir()

    def test_each_tier_has_content(self):
        for tier in ("01_BACK_END", "02_MIDDLE_LAYER", "03_FRONT_END", "04_CONTEXT"):
            d = ROOT / tier
            files = list(d.iterdir())
            assert files, f"{tier} is empty"


class TestBackendServer:
    """The README promises FastAPI service in 01_BACK_END/."""

    def test_server_module_present(self):
        assert (ROOT / "01_BACK_END" / "server.py").exists()

    def test_server_module_nonempty(self):
        size = (ROOT / "01_BACK_END" / "server.py").stat().st_size
        assert size > 100, f"server.py too small ({size} bytes) — likely empty"


class TestZoneRoutingDoc:
    """Verify the three-zone GREEN/YELLOW/RED model is documented in README."""

    def test_three_zones_mentioned(self):
        c = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        assert "green" in c
        assert "yellow" in c
        assert "red" in c

    def test_cognitive_load_mentioned(self):
        c = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        assert "cognitive" in c or "load" in c


class TestRepoCleanliness:
    def test_no_pycache_in_root(self):
        assert not (ROOT / "__pycache__").exists()

    def test_no_stray_pyc_files(self):
        pycs = [p for p in ROOT.rglob("*.pyc") if "__pycache__" not in str(p)]
        assert not pycs, f"found stray .pyc files: {pycs}"

    def test_no_env_files_committed(self):
        envs = list(ROOT.rglob(".env"))
        assert not envs, f"committed .env files: {envs}"
