# Content sources and editorial decisions

Reviewed 2026-10-31. The supplied 23-slide deck is a private source, not included
in the website or publication package. Public content uses professional facts only.

| Material | Content used | Decision |
| --- | --- | --- |
| Supplied youth innovation award PPT, slides 3–7 | Education, appointments, funding, honors, service | Dates and contributor order retained; translated labels are descriptive English |
| PPT, slides 9–17 | Three research directions | Rewritten as research questions, methods, and representative work; performance claims and endorsements omitted |
| PPT, slides 18–19 | Writing, dialogue, multilingual translation applications | General project summaries; no unreleased data or partner logos |
| PPT, slides 21–22 | Society roles, events, talks | English descriptions; no invented talk titles |
| https://homepage.hit.edu.cn/fengxiaocheng | Professor status and public email | Gmail decoded from reversed display; no personal telephone published |
| https://sai.hit.edu.cn/ldbz/list.htm | Current Vice Dean appointment | Current School of Artificial Intelligence supersedes older PPT organizational wording; start date omitted for current role |
| https://rsc.hit.edu.cn/2025/0422/c10875a367129/page.htm | School appointment | Corroborates School of Artificial Intelligence |
| https://ir.hit.edu.cn/19606/list.htm | Text Generation group leadership and collaborations | Official group link used; older funding counts not copied |
| https://aclanthology.org/people/xiaocheng-feng/ | Bibliography | Imported all 64 BibTeX records linked on the retrieved author page; the initially timed-out record was successfully retried. This is not a claim to exhaust all publications |
| https://arxiv.org/abs/2311.05232 | Hallucination survey | Now cites the 2025 TOIS journal version verified through Crossref; arXiv PDF retained; no duplicate record |

Portrait: supplied PPT, slide 3, original embedded image (335 × 433). The website banner image was inspected and rejected as a portrait.

No Scholar profile identifier was verified, so no guessed Google Scholar URL is
shown. Paper recognition is now shown where verified by official conference records or inspected certificates; see CONTENT_AUDIT.md. No personal citation counts, CCF rankings, funding totals, or celebrity
endorsements are published. The source PPT's young innovation award cover is not
treated as evidence that the award has already been won.

Publication resource links are official Anthology article/PDF endpoints or arXiv.
No unverified code/demo buttons are displayed. Bibliography imports preserve full
author order; Xiaocheng Feng and Xiachong Feng remain distinct people.

Institutional/photo and third-party paper rights are not covered by the template's
MIT license. Preserve academic attribution when reusing these materials.

## Reused presentation figures

Original embedded PNG files are reused without raster editing. Source mapping:

| Website asset | PPT location | Use |
| --- | --- | --- |
| structured-representations.png (removed) | Slide 13, image32.png | Retired: a small schematic component, unsuitable as a standalone research figure |
| projection-decoder.png (removed) | Slide 13, image37.png | Retired: a small projector/decoder component, unsuitable as a standalone research figure |
| retrieval-generation.png | Slide 16, image51.png | Retrieval / generation overview |
| rag-noise-filtering.png | Slide 16, image52.png | Information bottleneck noise filtering |
| fine-mem.png | Slide 16, image53.png | Fine-Mem framework |
| implicit-memory.png | Slide 16, image54.png | ImplicitMemBench workflow |

Figures retain their original English labels and proportions. Captions are written
for the website; click-through links open full-resolution originals. Chinese
certificates, private application documents, and endorsement portraits are not
used as research illustrations. Fine-Mem and ImplicitMemBench are distinguished.

Research Group destination updated to https://hit-scir-tg.netlify.app/ at the owner's request on 2026-10-31. The older HIT page remains a historical factual source.

Content audit expanded verified bibliography to 68 records, including two NeurIPS papers and the CCL 2021 commonsense paper. Full sources, name corrections, omissions and editorial boundaries are recorded in CONTENT_AUDIT.md.

On owner review, the two slide-13 component illustrations were removed from the website and assets. Exact-byte comparisons confirmed they came from the PPT; provenance alone did not justify enlarging them as standalone results. Four substantive slide-16 figures remain.

## Per-topic paper figures and 2026 updates

Additional figures are rendered directly from official ACL Anthology PDFs at
216 dpi, preserving the entire figure. Only page whitespace and surrounding
paragraphs/captions are excluded; no scientific content or labels are redrawn.

| Asset | Authoritative source | Figure / PDF page | Website topic |
| --- | --- | --- | --- |
| tablegpt-training.png | https://aclanthology.org/2020.coling-main.179.pdf | Figure 1 / page 3 | Representation learning |
| codebert-pretraining.png | https://aclanthology.org/2020.findings-emnlp.139.pdf | Figure 2 / page 4 | Knowledge-enhanced modeling |
| length-controlled-generation.png | https://aclanthology.org/2025.acl-long.825.pdf | Figure 1 / page 3 | Writing and controllable generation |
| culture-aware-translation.png | https://aclanthology.org/2026.acl-long.1367.pdf | Figure 1 / page 3 | Multilingual translation |

Captions link to the original paper. Project figures are explicitly research
methods/benchmarks, not purported screenshots of industry products. English
site copy is preserved; the CanMT figure retains original bilingual research
examples. The four extracted figures were visually inspected for completeness.

About updates now contain only non-publication events from the current year:
EMNLP 2026 reviewing recognition (conference site), the August 2026 CIPS youth
committee appointment (supplied PPT, slide 21), and the July 2026 CAAI election
(https://nmlr.muc.edu.cn/info/1106/3382.htm, election on 27 July). Current-year
filtering uses Jekyll's site.time; the section is omitted if there are no matching
updates. Publication awards remain with the bibliography rather than repeated
as news. An event whose month is unknown keeps a year-only date.

Homepage organization revised following the faculty comparison in HOMEPAGE_REFERENCES.md. Research and Research in focus are consolidated into one illustrated Research Interests section. The News heading is stable, dates belong to entries, and calendar-year filtering has been removed. Current news content remains three 2026 non-publication events.


## Project portfolio revision — 2026-10-31

Projects now lists all eleven funded projects from the supplied PPT, slide 5,
in `_data/projects.yml`: three ongoing public projects, four earlier public /
laboratory projects, and four industry collaborations. Dates determine this
presentation as of October 2026; review the grouping when projects end. Personal
roles retain the distinction between PI, Project Lead, and Subproject Lead.
The application narratives use PPT slides 18–19. They do not imply that every
application belongs to one particular funding award or that the advisor owns the
whole partner platform. Existing Qiyuan/Jiuge and service-platform information
is retained. The three former thematic project sections and their adjacent paper
method figures have been removed from this page; Research still explains methods.

| Asset | Public primary source | Treatment / scope |
| --- | --- | --- |
| assets/img/projects/multilingual-toolchain.webp | https://data-starcloud.pcl.ac.cn/image/data-app/multilingual/04.png | Whole original image, converted to WebP; no cropping, redrawing, or label changes. Partner platform interfaces, not exclusive personal deliverables. |

The contextual platform page is https://data-starcloud.pcl.ac.cn/data-app/multilingual,
accessed 2026-10-31. The visible credit links to that page. Original Chinese UI
text remains in the screenshot; surrounding copy, alt text and controls are English.
The group overview https://hit-scir-tg.netlify.app/ corroborates the essay system
and translation collaboration. Its essay screenshot inside the introduction
poster is only a small thumbnail; inspected and omitted rather than enlarged.
The public CCL 2018 talk https://www.cips-cl.org/static/CCL2018/downloads/ppt/04.pdf
was inspected but contains no suitable application screenshot. Original PPT,
full downloaded pages, and public talk PDF are not included in the repository.
No images from unrelated essay systems, stock imagery, or illustrative paper
methods are used as project product screenshots.


## List-based Projects page — 2026-10-31, owner revision

The owner requested a simple funding list, with illustrations only for the two
slide-18/19 applications. The 11 funding records now render as semantic list
items, with period, title, sponsor/program, and personal role; all funding card
styles have been removed. The lists appear before Selected Applications.

`assets/img/projects/writing-applications.svg` is a newly typeset English overview,
not an extracted original or a software screenshot. Its content comes directly
from PPT slide 18: Gaokao argumentative essay generation; third-party evaluation
in 2022; iFLYTEK meeting summaries/document writing; Huawei length-controlled
summaries/text compression; Tencent table-based sports reporting/fiction
writing. It uses no invented performance figures, inferred causal arrows or
product UI. The private certificate with contact details/signatures is not used.
The public PCL whole-image platform screenshot remains beside the multilingual
application, credited as partner platform interfaces. Two application narratives
retain Qiyuan/Jiuge, language-service platforms and NPC/CPPCC workflows.


## Replace partner-platform imagery with the original demo — 2026-10-31

At the owner's request, the Star Cloud / PCL image and its outbound platform
button are removed from the site and current source assets. Prior image-provenance
notes above are historical; the partner screenshot is no longer published.

The replacement is the actual embedded GIF from PPT slide 19,
`ppt/media/image63.gif` (55,335,317 bytes; 1920 × 1248; 1,426 frames;
23.77 seconds). Exact bytes match the supplied deck; SHA-256:
`4270867764cc350ae3d2d9a33ace0c58bba93a824bdd22c6905b07e40fca6c6e`.
The demo shows the Jiuge multilingual information generation interface and
retrieval results in multiple languages. It is not labeled a Naohai translation
UI. The application heading now includes both translation and information
generation, while the narrative keeps the two laboratory collaborations distinct.

Website media: `assets/img/projects/multilingual-system-demo.mp4`, H.264,
1280 × 696, 20 fps, 23.75 seconds, 4,954,231 bytes. Encoded from the complete
animation; crop `(x=0,y=204,width=1920,height=1044)` removes only the browser/
desktop chrome and bookmarks, followed by proportional downscaling. No system
content is relabeled or reconstructed. The poster is the same crop of original
GIF frame 0. Native playback controls permit pause, seek and fullscreen. No
autoplay; video downloads on demand (`preload="none"`). The original 55 MB GIF
and full PPT remain outside the repository. The low-resolution group poster
remains excluded; the writing figure is still an explicitly authored English
application overview from slide 18, not a claimed system screenshot.


## Gaokao application: concise text pending an original screenshot

The owner chose a short introduction after the additional image search found no
verified high-resolution public system screenshot. The authored English writing
overview SVG is removed from the page and current assets. Gaokao Essay Generation
now uses one paragraph covering the system, national research support, 2022
third-party evaluation, and related writing applications (PPT slide 18). The
single-column text layout leaves no empty image area. Detailed slide-18 industry
application examples are condensed in this public introduction; they are not
presented as a complete application inventory. All 11 funding records and the
original slide-19 multilingual system demo remain. Earlier figure notes above
are historical and do not describe the current page.


## Publication status — 2026-10-31

The owner explicitly approved public repository visibility and GitHub Pages
publication. The live site is https://buix5371.github.io/feng-homepage/.
Source is on `main`; generated public files are on `gh-pages`. Earlier private-only
restrictions recorded above are superseded by this approval. The original PPT
and local source-download/runtime folders remain excluded.


## Organization homepage migration — 2026-10-31

The owner created the `xcfeng-hit` organization and explicitly requested migration.
The existing repository, including its main/source history and gh-pages output
history, was transferred and renamed to `xcfeng-hit/xcfeng-hit.github.io`.
The canonical destination is https://xcfeng-hit.github.io/; `_config.yml` uses
this URL and an empty baseurl. Existing factual content and media are retained.
The old account/repository URLs above are historical. Published files remain on
`gh-pages`, root directory. The original PPT remains outside the repository.


## Advisor-requested removal of multilingual application block

The owner relayed the advisor's request to delete the shown multilingual machine
translation and information generation application block. The entire block,
including its title, collaboration narrative, group link, video and caption,
is removed from Projects. The demo MP4 and poster are removed from current source
and published assets. The 11 funded-project records and the concise Gaokao essay
application remain. Earlier notes about including the multilingual demo describe
historical revisions, not the current website. Git history is not rewritten.
