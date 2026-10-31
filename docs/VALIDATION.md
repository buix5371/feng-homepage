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
