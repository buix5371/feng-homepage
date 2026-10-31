---
title: Research
permalink: /research/
description: Representations, knowledge, and reliability — three connected directions in text generation.
---
<section markdown="1" class="topic" id="representation"><p class="label">Research direction 01</p><h2>Representation Learning for Text Generation</h2>

Text generation begins with understanding the information a model receives. My research explores how to represent inputs that differ in language, structure, and length, including multilingual text, tables, and long documents. A central question is how to align these inputs with the representations used by generative models while preserving the information needed for faithful output. This line of work aligns cross-lingual lexical representations, structured triples, and long-document discourse. It includes table-to-text generation, structure-aware modeling, and learning from limited examples. TableGPT studies how table structure reconstruction and content matching can support few-shot generation, connecting structured records with natural language descriptions.

<h3>Related publications</h3>
<p class="related"><a href="{{ '/publications/' | relative_url }}#gong-etal-2020-tablegpt">TableGPT: Few-shot Table-to-Text Generation with Table Structure Reconstruction and Content Matching →</a></p>
<p class="related"><a href="{{ '/publications/' | relative_url }}#feng-etal-2020-codebert">CodeBERT: A Pre-Trained Model for Programming and Natural Languages →</a></p>
</section>
<section markdown="1" class="topic" id="knowledge"><p class="label">Research direction 02</p><h2>Knowledge-Enhanced Language Models</h2>

Language models must connect their learned representations with knowledge expressed in different forms. My work investigates how knowledge and complementary data sources can be incorporated during training and inference to support language understanding and generation. CodeBERT learns shared representations of programming and natural languages, with applications in code search and documentation generation. D-HGN incorporates commonsense knowledge and speaker information into dialogue summarization through heterogeneous graph networks. Related work also examines how retrieved information can be filtered before it reaches a generator. Across these settings, the goal is to make relevant information available in a form that supports the task, while limiting interference from irrelevant or noisy evidence.


{% include research_figure.liquid file="/assets/img/research/rag-noise-filtering.png" width="1522" height="438" alt="Information bottleneck-based noise filtering for retrieval-augmented generation" title="Filtering retrieved evidence" caption="An information bottleneck perspective on retaining task-relevant evidence before generation." %}
<h3>Related publications</h3>
<p class="related"><a href="{{ '/publications/' | relative_url }}#feng-etal-2020-codebert">CodeBERT: A Pre-Trained Model for Programming and Natural Languages →</a></p>
<p class="related"><a href="{{ '/publications/' | relative_url }}#feng-etal-2021-commonsense">Incorporating Commonsense Knowledge into Abstractive Dialogue Summarization via Heterogeneous Graph Networks →</a></p>
<p class="related"><a href="{{ '/publications/' | relative_url }}#zhu-etal-2024-information">An Information Bottleneck Perspective for Effective Noise Filtering on Retrieval-Augmented Generation →</a></p>
</section>
<section markdown="1" class="topic" id="trustworthy"><p class="label">Research direction 03</p><h2>Trustworthy Text Generation</h2>

Fluent text is not necessarily reliable text. My research examines why language models hallucinate and how generated responses can remain faithful to evidence and consistent with context. This includes a survey of hallucination in large language models, retrieval-augmented generation, and memory mechanisms for sustained interaction. DeePEn fuses token-level distributions from heterogeneous models, complementing research on retrieval noise filtering and iterative evidence use. Recent work studies retrieval heads as a means of improving contextual faithfulness and develops benchmarks for implicit memory, extending evaluation beyond explicit recall. The broader aim is to understand the limits of current models and develop methods and evaluations that support reliable information use across generation and interaction.

{% include research_figure.liquid file="/assets/img/research/fine-mem.png" width="1568" height="594" alt="Fine-Mem training with chunk-level rewards and evidence-anchored feedback" title="Fine-Mem" caption="Fine-grained rewards connect local memory operations with long-horizon task outcomes." %}

{% include research_figure.liquid file="/assets/img/research/implicit-memory.png" width="1498" height="664" alt="ImplicitMemBench dataset creation and evaluation of implicit memory" title="ImplicitMemBench" caption="Dataset generation and evaluation across procedural memory, priming, and classical conditioning." %}
<h3>Related publications</h3>
<p class="related"><a href="{{ '/publications/' | relative_url }}#huang-etal-2024-deepen">Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration →</a></p>
<p class="related"><a href="{{ '/publications/' | relative_url }}#ma-etal-2026-fine">Fine-Mem: Fine-Grained Feedback Alignment for Long-Horizon Memory Management →</a></p>
<p class="related"><a href="{{ '/publications/' | relative_url }}#huang2023hallucination">A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions →</a></p>
<p class="related"><a href="{{ '/publications/' | relative_url }}#huang-etal-2025-improving">Improving Contextual Faithfulness of Large Language Models via Retrieval Heads-Induced Optimization →</a></p>
<p class="related"><a href="{{ '/publications/' | relative_url }}#qin-etal-2026-implicitmembench">ImplicitMemBench: Measuring Unconscious Behavioral Adaptation in Large Language Models →</a></p>
</section>
