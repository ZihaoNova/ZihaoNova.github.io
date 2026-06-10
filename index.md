---
layout: home
title: "Zihao Huang"
---

## About Me
{: #about }

I am Zihao Huang, a student at Zhejiang A&F University working on geospatial Python systems for land-cover simulation, raster processing, and scalable spatial modeling.

My current work focuses on turning large spatial simulation workflows into reproducible, inspectable, and testable tools. I care about localized validation before expensive full-raster runs, clear modeling assumptions, and outputs that are easy to compare, debug, and explain.

## News
{: #news }

<ul class="news-list">
{% for item in site.data.news %}
  <li><span class="news-date">{{ item.date }}</span>{{ item.text }}</li>
{% endfor %}
</ul>

## Publications
{: #publications }

Selected publications, manuscripts, and public preprints related to land-cover simulation, raster validation, and scalable geospatial modeling will be listed here as they become available.

## Selected Projects
{: #projects }

<div class="project-grid">
{% for project in site.data.projects %}
  {% include project-card.html project=project %}
{% endfor %}
</div>

## Research Interests
{: #interests }

- Land-cover and land-use change simulation
- Raster processing and GeoTIFF validation
- Cellular automata and scenario modeling
- Scalable spatial computing with Dask/PyTorch
- Reproducible geospatial research software

## Education
{: #education }

**Zhejiang A&F University**  
Hangzhou, Zhejiang, China  
Research direction: geospatial modeling, environmental simulation, and Python geospatial workflows.

## Awards & Honors
{: #awards }

Selected awards and honors will be added when public entries are ready.

## Contact
{: #contact }

For research discussion and project collaboration, GitHub is the preferred contact path.

- GitHub: [@ZihaoNova](https://github.com/ZihaoNova)
- Email: [huangzihao@zafu.edu.cn](mailto:huangzihao@zafu.edu.cn)
