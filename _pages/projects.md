---
title: Projects
permalink: /projects/
description: Funded research, industry collaborations, and applications in text generation.
---
<div class="project-portfolio" markdown="0">
  {% assign ongoing = site.data.projects | where: 'group', 'ongoing' %}
  {% assign earlier = site.data.projects | where: 'group', 'earlier' %}
  {% assign industry = site.data.projects | where: 'group', 'industry' %}
  <section class="funding-section" aria-labelledby="ongoing-heading">
    <h2 id="ongoing-heading">Ongoing Research Projects</h2>
    <ul class="funding-list">
      {% for project in ongoing %}{% include funded_project.liquid project=project %}{% endfor %}
    </ul>
  </section>
  <section class="funding-section" aria-labelledby="earlier-heading">
    <h2 id="earlier-heading">Earlier Research Projects</h2>
    <ul class="funding-list">
      {% for project in earlier %}{% include funded_project.liquid project=project %}{% endfor %}
    </ul>
  </section>
  <section class="funding-section" aria-labelledby="industry-heading">
    <h2 id="industry-heading">Industry Collaborations</h2>
    <ul class="funding-list">
      {% for project in industry %}{% include funded_project.liquid project=project %}{% endfor %}
    </ul>
  </section>

  <section class="application-showcase" aria-labelledby="applications-heading">
    <h2 id="applications-heading">Selected Application</h2>
    <article class="application-entry application-text-only">
      <div class="application-copy">
        <h3>Gaokao Essay Generation</h3>
        <p>Our group developed an end-to-end system that generates argumentative essays for China's national college entrance examination (Gaokao). The work was supported by successive national research programs and underwent third-party evaluation in 2022. Related technologies support document drafting, proofreading, and meeting summarization.</p>
        <a class="project-action" href="https://hit-scir-tg.netlify.app/#research-projects">Research group overview ↗</a>
      </div>
    </article>
  </section>
</div>
