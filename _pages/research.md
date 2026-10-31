---
title: Research
permalink: /research/
description: Representations, knowledge, and reliability — three connected directions in text generation.
---
<section markdown="1" class="topic" id="representation"><p class="label">Research direction 01</p><h2>Representation Learning for Text Generation</h2>

Text generation begins with understanding the information a model receives. My research explores how to represent inputs that differ in language, structure, and length, including multilingual text, tables, and long documents. A central question is how to align these inputs with the representations used by generative models while preserving the information needed for faithful output. This line of work includes table-to-text generation, structure-aware modeling, and learning from limited examples. TableGPT studies how table structure reconstruction and content matching can support few-shot generation, connecting structured records with natural language descriptions.

<img src="{{ '/assets/img/representation.svg' | relative_url }}" alt="Representation Learning for Text Generation research workflow" width="900" height="190" loading="lazy">
<h3>Related publications</h3>
<p class="related"><a href="{{ '/publications/' | relative_url }}#gong-etal-2020-tablegpt">TableGPT: Few-shot Table-to-Text Generation with Table Structure Reconstruction and Content Matching →</a></p>
<p class="related"><a href="{{ '/publications/' | relative_url }}#feng-etal-2020-codebert">CodeBERT: A Pre-Trained Model for Programming and Natural Languages →</a></p>
</section>
<section markdown="1" class="topic" id="knowledge"><p class="label">Research direction 02</p><h2>Knowledge-Enhanced Language Models</h2>

Language models must connect their learned representations with knowledge expressed in different forms. My work investigates how knowledge and complementary data sources can be incorporated during training and inference to support language understanding and generation. CodeBERT learns shared representations of programming and natural languages, with applications in code search and documentation generation. Related work examines how retrieved information can be filtered and used effectively rather than passed to a model indiscriminately. Across these settings, the goal is to make relevant information available in a form that supports the task, while limiting interference from irrelevant or noisy evidence.

<img src="{{ '/assets/img/knowledge.svg' | relative_url }}" alt="Knowledge-Enhanced Language Models research workflow" width="900" height="190" loading="lazy">
<h3>Related publications</h3>
<p class="related"><a href="{{ '/publications/' | relative_url }}#feng-etal-2020-codebert">CodeBERT: A Pre-Trained Model for Programming and Natural Languages →</a></p>
<p class="related"><a href="{{ '/publications/' | relative_url }}#zhu-etal-2024-information">An Information Bottleneck Perspective for Effective Noise Filtering on Retrieval-Augmented Generation →</a></p>
</section>
<section markdown="1" class="topic" id="trustworthy"><p class="label">Research direction 03</p><h2>Trustworthy Text Generation</h2>

Fluent text is not necessarily reliable text. My research examines why language models hallucinate and how generated responses can remain faithful to evidence and consistent with context. This includes a survey of hallucination in large language models, retrieval-augmented generation, and memory mechanisms for sustained interaction. Recent work studies retrieval heads as a means of improving contextual faithfulness and develops benchmarks for implicit memory, extending evaluation beyond explicit recall. The broader aim is to understand the limits of current models and develop methods and evaluations that support reliable information use across generation and interaction.

<img src="{{ '/assets/img/trustworthy.svg' | relative_url }}" alt="Trustworthy Text Generation research workflow" width="900" height="190" loading="lazy">
<h3>Related publications</h3>
<p class="related"><a href="{{ '/publications/' | relative_url }}#huang2023hallucination">A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions →</a></p>
<p class="related"><a href="{{ '/publications/' | relative_url }}#huang-etal-2025-improving">Improving Contextual Faithfulness of Large Language Models via Retrieval Heads-Induced Optimization →</a></p>
<p class="related"><a href="{{ '/publications/' | relative_url }}#qin-etal-2026-implicitmembench">ImplicitMemBench: Measuring Unconscious Behavioral Adaptation in Large Language Models →</a></p>
</section>
