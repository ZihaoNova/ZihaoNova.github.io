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
    assert 'employer: "Zhejiang A&F University"' in config


def test_homepage_uses_wd7ang_style_contract() -> None:
    homepage = read_text("_pages/about.md")

    required_sections = [
        "layout: default",
        "id='about-me'",
        "id='-news'",
        "# 🔥 News",
        "id='-publications'",
        "# 📝 Publications",
        "# 🚀 Selected Projects",
        "# 💬 Services",
        "id='-invited-talks'",
        "# 🎙 Invited Talks",
        "id='-internships'",
        "# 🏢 Internships",
        "id='-honors-and-awards'",
        "# 🎖 Honors and Awards",
        "id='-educations'",
        "# 📖 Educations",
    ]

    for section in required_sections:
        assert section in homepage


def test_project_cards_cover_geospatial_portfolio() -> None:
    homepage = read_text("_pages/about.md")

    required_projects = [
        "Land-cover simulation workflows",
        "Raster validation and AOI smoke checks",
        "Windowed CA and Dask pipelines",
    ]

    for project in required_projects:
        assert project in homepage

    assert homepage.count("class='paper-box'") == 3


def test_navigation_matches_template_shape() -> None:
    navigation = read_text("_data/navigation.yml")

    required_links = [
        'title: "About Me"',
        'url: "/#about-me"',
        'title: "News"',
        'url: "/#-news"',
        'title: "Publications"',
        'url: "/#-publications"',
        'title: "Honors and Awards"',
        'title: "Educations"',
        'title: "Invited Talks"',
        'title: "Internships"',
    ]

    for link in required_links:
        assert link in navigation


def test_layout_keeps_wd7ang_class_names() -> None:
    default_layout = read_text("_layouts/default.html")
    masthead = read_text("_includes/masthead.html")
    sidebar_include = read_text("_includes/sidebar.html")
    sidebar = read_text("_includes/author-profile.html")
    css = read_text("assets/css/main.scss")

    assert "masthead" in default_layout
    assert "page__content" in default_layout
    assert "sidebar sticky" in sidebar_include

    for snippet in ["profile_box", "author__avatar", "author__urls"]:
        assert snippet in sidebar

    for snippet in [".paper-box", ".badge", ".masthead", ".page__content"]:
        assert snippet in css


def test_no_noisy_profile_widgets() -> None:
    banned_snippets = [
        "github-readme-stats",
        "github-profile-trophy",
        "komarev.com",
        "readme-typing-svg",
        "mapmyvisitors",
        "google-scholar-stats",
    ]

    checked_suffixes = {".html", ".md", ".scss", ".yml", ".yaml", ".svg"}
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


def test_template_attribution_notice_present() -> None:
    notice = read_text("NOTICE.md")

    assert "WD7ang/WD7ang-old.github.io" in notice
    assert "MIT License" in notice
    assert "Copyright (c) 2022 Yi Ren" in notice
