# Zihao Huang Academic Homepage

This repository hosts [https://zihaonova.github.io](https://zihaonova.github.io).

The site is built from the full WD7ang-old / AcadHomepage-style Jekyll template, then customized for Zihao Huang's geospatial Python, land-cover simulation, raster validation, and scalable spatial modeling profile.

## Editing Content

- Main homepage content: `_pages/about.md`
- Profile metadata: `_config.yml`
- Navigation: `_data/navigation.yml`
- Styling and project-card polish: `assets/css/main.scss`
- Template includes and layouts: `_includes/`, `_layouts/`
- Full theme styling: `_sass/`

## Google Scholar

The `google_scholar_crawler/` folder and workflow are retained from the template for future use. The workflow is set to manual trigger until a personal Google Scholar ID is configured.

## Local Checks

```powershell
D:\anaconda3\envs\torchenv\python.exe -m pytest -v
```

Jekyll preview requires Ruby/Bundler:

```bash
bundle exec jekyll serve
```

## Acknowledgements

This site is adapted from `WD7ang/WD7ang-old.github.io`, which itself is based on AcadHomepage, Minimal Mistakes, and academicpages. Template licensing notices are preserved in `LICENSE`.
