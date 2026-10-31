# Verification — 2026-10-31

Passed locally using official RubyInstaller 3.3.6 and Jekyll 4.3.4:

- Real production build with Jekyll Scholar and Sitemap.
- All six required routes, local assets, and internal anchor targets.
- English HTML language; no unrendered Liquid or template placeholders.
- 65 publication records; five selected homepage papers; full author rendering.
- CodeBERT author sequence inspected in generated HTML.
- Research/project Markdown rendered as HTML, not raw Markdown links.
- JavaScript syntax check.
- 133 external article/institution/PDF endpoints returned HTTP 200.
- Offline preview generated from real Jekyll output; relative navigation checked.
- Portrait visually inspected against the supplied PPT embedded image.

Not verified: desktop/tablet/mobile browser rendering and menu interaction;
browser control was stopped because it could not reliably determine the current
browser URL. Responsive CSS, viewport metadata, menu semantics and Escape-key
handling are implemented, but are not a substitute for browser verification.

Source uploaded to buix5371/feng-homepage on 2026-10-31. GitHub API confirmed
45 files on main and private=true. No active workflow is installed; the deployment
template is stored at docs/deployment/pages.yml. Pages configuration, Actions
execution, and public deployment are deferred at the owner's request.

## Presentation figure update

Six original embedded PNGs reused from slides 13 and 16. The rebuilt homepage
contains three original research figures, Research contains five, and Projects
contains one (some figures appear on more than one page). All image files decode
correctly; figure captions, alt text, dimensions, and full-size links are present.
The real Jekyll build and internal-link checks pass after this change. Browser
layout inspection was attempted but localhost access timed out; no desktop or
mobile visual pass is claimed.

## PPT content audit update

Re-read all 23 slide text layers and inspected the MUG, CCL and ACL award
certificates plus the ACL SAC Highlight screenshot. All 11 projects from slide 5
are now represented; expanded bibliography contains 68 records and three paper
recognition labels. The CCL author sequence and TOIS publication year were checked
in generated HTML. See CONTENT_AUDIT.md for scope and remaining bibliography limits.
Nine newly added resource URLs returned 200; publisher automated access returned
403, so the survey retains an accessible arXiv landing page and PDF.

## Figure selection correction

Removed the two slide-13 schematic components after owner feedback. Four
substantive slide-16 figures remain. The removed PNGs are no longer present in
the website source or offline preview. Earlier figure counts describe the
previous revision, not the current selection.

## Topic illustrations and About updates revision

All three Research topics and all three Projects topics now contain at least
one corresponding figure. TableGPT, CodeBERT, length-controlled generation and
culture-aware translation images were rendered from complete original paper
figures and visually inspected; captions link to the original articles. Existing
PPT method figures remain where relevant.

Fixed Markdown parsing of figure captions and section closing tags. Generated
HTML now has three sibling research sections (figure counts 1/2/2) and three
sibling project sections (1/1/1), with no escaped structural tags. The standard
site checker now guards these conditions. The About section contains exactly
three 2026 non-publication updates and five selected papers. It no longer repeats
paper summaries or publication awards as news. Jekyll build and both production
and offline-preview link checks pass. No new browser layout verification is claimed.

## Faculty-reference homepage simplification

Compared Wei Xu, Graham Neubig and Antonis Anastasopoulos personal homepages.
Consolidated research overview and visual highlights into a single illustrated
Research Interests section; removed the redundant include. News has a stable
heading with dates on rows and no calendar-year clearing. Current three entries
are all 2026 non-publication events. Generated homepage headings were checked
exactly: Research Interests, Selected Publications, News, Contact. Three overview
images, five selected papers, and three news entries are present. Detail-page
figures remain in place. Production build and local link checks pass.


## Real-project portfolio and public platform image — 2026-10-31

Native Jekyll production build and both production / offline-preview checks pass.
The rendered Projects page contains all 11 slide-5 funding records: titles,
sponsors, dates and personal roles match `_data/projects.yml`. Groups contain
3 ongoing, 4 earlier public/laboratory and 4 industry projects. There are four
sibling page sections and no nested topic/escaped-tag errors. Projects contains
an official PCL whole-image platform screenshot (1327 × 753, WebP 88,686 bytes)
with source credit, two application narratives, and no paper-method figures or
paper-link substitutes. The text-only grant cards are intentionally allowed by
the owner's latest preference; Research topics retain the figure requirement.
Both external destinations were fetched successfully; the group link uses the
verified `research-projects` anchor. No browser responsive-layout verification
is claimed; previous local browser preview remained unavailable.


## List layout with two application figures — owner revision

Production build and both production/offline internal-link checks pass. All 11
records render as `ul.funding-list > li.funded-project`, retaining source titles,
sponsors, periods and roles. Exactly two application entries each have one image,
after the funding lists. No former grid-card or platform-feature containers
remain. The new English writing overview SVG was rendered with CairoSVG and
visually inspected: text and rows fit, with no clipping. Its source is PPT slide
18; it is a summary graphic rather than an original system screenshot. The PCL
image and source link remain. Browser responsive-layout verification remains
unavailable; no new browser QA is claimed.


## Use original PPT demo; remove partner-platform screenshot

Production build and six-page checks pass for both production and portable
preview, now checking video sources and poster paths as well as ordinary assets.
There are 11 funding list entries, two applications, one original-source system
video and one English writing overview. Native video controls and playsinline
are enabled; there is no autoplay and preload is none. Portable source and poster
paths resolve to existing files. The Star Cloud screenshot, link and generated
asset are absent. The slide-19 GIF extraction matches the embedded PPT bytes by
SHA-256. Encoded H.264 is 1280 × 696 at 20 fps / 23.75 seconds / 4,954,231 bytes;
a full FFmpeg decode check passed. The first-frame poster, sampled original GIF
frames and middle video frame were visually inspected. Jiuge multilingual
information generation is distinguished from Naohai translation collaboration.
Browser playback and responsive interaction have not been verified because the
local browser preview remains unavailable.
