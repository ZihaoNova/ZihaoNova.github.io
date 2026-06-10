from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_site_identity_config() -> None:
    config = read_text("_config.yml")

    assert 'title: "Zihao Huang"' in config
    assert 'repository: "ZihaoNova/ZihaoNova.github.io"' in config
    assert 'url: "https://zihaonova.github.io"' in config
    assert 'name: "Zihao Huang"' in config
    assert 'affiliation: "Zhejiang A&F University"' in config


def test_homepage_has_required_sections() -> None:
    homepage = read_text("index.md")

    required_sections = [
        "## About Me",
        "## News",
        "## Publications",
        "## Selected Projects",
        "## Research Interests",
        "## Education",
        "## Awards & Honors",
        "## Contact",
    ]

    for section in required_sections:
        assert section in homepage


def test_project_data_covers_geospatial_portfolio() -> None:
    projects = read_text("_data/projects.yml")

    required_projects = [
        "Land-cover Simulation Workflows",
        "Raster Validation and AOI Smoke Checks",
        "Windowed CA and Dask Pipelines",
    ]

    for project in required_projects:
        assert project in projects


def test_no_noisy_profile_widgets() -> None:
    banned_snippets = [
        "github-readme-stats",
        "github-profile-trophy",
        "komarev.com",
        "readme-typing-svg",
        "mapmyvisitors",
    ]

    checked_suffixes = {".html", ".md", ".scss", ".yml", ".yaml"}
    checked_files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and "tests" not in path.parts
        and path.suffix.lower() in checked_suffixes
    ]

    assert checked_files

    for path in checked_files:
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for snippet in banned_snippets:
            assert snippet not in text, f"{snippet} found in {path.relative_to(ROOT)}"
