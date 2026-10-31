---
title: Projects
permalink: /projects/
description: Funded research and collaborations that connect text generation with writing tools and multilingual communication.
---
<div class="project-portfolio" markdown="0">
  <section class="application-showcase" aria-labelledby="applications-heading">
    <div class="portfolio-heading"><h2 id="applications-heading">Research in Practice</h2><span>Systems &amp; collaboration</span></div>
    <article class="platform-feature">
      <div class="platform-visual">
        <a href="{{ '/assets/img/projects/multilingual-toolchain.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="View full-size multilingual platform interfaces">
          <img src="{{ '/assets/img/projects/multilingual-toolchain.webp' | relative_url }}" width="1327" height="753" alt="Four interfaces from Peng Cheng Laboratory's multilingual toolchain, including translation editing, video translation, and digital presenters" loading="lazy">
        </a>
        <p class="image-credit">Platform interfaces · Peng Cheng Laboratory <a href="https://data-starcloud.pcl.ac.cn/data-app/multilingual">Source ↗</a></p>
      </div>
      <div class="platform-copy">
        <p class="label">Multilingual communication</p>
        <h3>From Translation Models to Multilingual Platforms</h3>
        <p>In collaboration with Peng Cheng Laboratory, our work contributes to multilingual modeling and translation platforms, including the multilingual Naohai model. The laboratory's public platform brings translation and other language tools into practical workflows.</p>
        <dl class="project-facts"><div><dt>Project</dt><dd>Multilingual Communication Platform</dd></div><div><dt>Period / role</dt><dd>2022–2025 · Project Lead</dd></div></dl>
        <a class="project-action" href="https://data-starcloud.pcl.ac.cn/data-app/multilingual">Explore the collaborative platform ↗</a>
      </div>
    </article>
    <article class="writing-case">
      <div><p class="label">Writing systems</p><h3>Gaokao Essay Generation</h3></div>
      <div><p>Our group developed an end-to-end system for generating argumentative essays for China's national college entrance examination. Supported across successive national research programs, the system underwent third-party evaluation in 2022.</p><p class="application-detail">Writing collaborations include iFLYTEK's meeting summaries and document drafting, Huawei's length-controlled summaries and text compression, and Tencent's sports reporting and fiction descriptions. Related drafting and proofreading technologies have been applied in workflows for the National People's Congress and the Chinese People's Political Consultative Conference.</p><a class="project-action" href="https://hit-scir-tg.netlify.app/#research-projects">Research group overview ↗</a></div>
    </article>
    <p class="collaboration-note">Further multilingual collaborations include the Jiuge model and multilingual information generation with Qiyuan Laboratory. Translation models have also been deployed on platforms associated with China International Communications Group and the Ministry of Education's national language-resource services.</p>
  </section>

  {% assign ongoing = site.data.projects | where: 'group', 'ongoing' %}
  {% assign earlier = site.data.projects | where: 'group', 'earlier' %}
  {% assign industry = site.data.projects | where: 'group', 'industry' %}
  <section class="funding-section" aria-labelledby="ongoing-heading">
    <div class="portfolio-heading"><h2 id="ongoing-heading">Ongoing Research Projects</h2><span>National &amp; regional funding</span></div>
    <div class="funding-grid ongoing-grid">
      {% for project in ongoing %}{% include funded_project.liquid project=project %}{% endfor %}
    </div>
  </section>
  <section class="funding-section" aria-labelledby="earlier-heading">
    <div class="portfolio-heading"><h2 id="earlier-heading">Earlier Research Projects</h2><span>Public &amp; laboratory funding</span></div>
    <div class="funding-grid">
      {% for project in earlier %}{% include funded_project.liquid project=project %}{% endfor %}
    </div>
  </section>
  <section class="funding-section" aria-labelledby="industry-heading">
    <div class="portfolio-heading"><h2 id="industry-heading">Industry Collaborations</h2><span>Collaborative research projects</span></div>
    <div class="funding-grid industry-grid">
      {% for project in industry %}{% include funded_project.liquid project=project %}{% endfor %}
    </div>
  </section>
</div>
