---
title: Projects
permalink: /projects/
description: Funded research, industry collaborations, and selected applications in writing and multilingual communication.
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
    <h2 id="applications-heading">Selected Applications</h2>
    <article class="application-entry">
      <div class="application-copy">
        <h3>Gaokao Essay Generation and Writing Assistance</h3>
        <p>Our group developed an end-to-end system for generating argumentative essays for China's national college entrance examination, supported across successive national research programs and evaluated by a third party in 2022.</p>
        <p>Related collaborations address meeting summaries, document drafting, length-controlled summaries, text compression, sports reporting, and fiction descriptions. Drafting and proofreading technologies have also been applied in workflows for the National People's Congress and the Chinese People's Political Consultative Conference.</p>
        <a class="project-action" href="https://hit-scir-tg.netlify.app/#research-projects">Research group overview ↗</a>
      </div>
      <figure class="application-figure">
        <a href="{{ '/assets/img/projects/writing-applications.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="View full-size overview of writing applications"><img src="{{ '/assets/img/projects/writing-applications.svg' | relative_url }}" width="1100" height="640" alt="English overview of Gaokao essay generation and related writing applications with iFLYTEK, Huawei, and Tencent" loading="lazy"></a>
        <figcaption>Gaokao essay generation and related writing applications. An English summary of the documented application areas.</figcaption>
      </figure>
    </article>
    <article class="application-entry">
      <div class="application-copy">
        <h3>Multilingual Machine Translation</h3>
        <p>Collaboration with Peng Cheng Laboratory contributes to the multilingual Naohai model and translation platforms. Work with Qiyuan Laboratory supports the Jiuge model and multilingual information generation.</p>
        <p>Translation models have also been deployed on platforms associated with China International Communications Group and the Ministry of Education's national language-resource services.</p>
        <a class="project-action" href="https://data-starcloud.pcl.ac.cn/data-app/multilingual">Collaborative platform ↗</a>
      </div>
      <figure class="application-figure">
        <a href="{{ '/assets/img/projects/multilingual-toolchain.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="View full-size multilingual platform interfaces"><img src="{{ '/assets/img/projects/multilingual-toolchain.webp' | relative_url }}" width="1327" height="753" alt="Four interfaces from Peng Cheng Laboratory's multilingual toolchain, including translation editing, video translation, and digital presenters" loading="lazy"></a>
        <figcaption>Interfaces from the collaborative multilingual platform. Image: Peng Cheng Laboratory. <a href="https://data-starcloud.pcl.ac.cn/data-app/multilingual">Source ↗</a></figcaption>
      </figure>
    </article>
  </section>
</div>
