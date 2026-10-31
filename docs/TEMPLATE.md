# Template provenance

This is a deliberately trimmed, vendored adaptation of **al-folio v0.14.6**
(https://github.com/alshedivat/al-folio/tree/v0.14.6), licensed under MIT.
Verified upstream commit: `693c3beacb9c284573145884f8306441f75e30aa`.
The official files inspected through GitHub are retained under `docs/upstream/`.
The profile/content layout and the selected-papers include are adapted from that
release. Publication storage remains `_bibliography/papers.bib`, rendered by
Jekyll Scholar and a local `bib.liquid` layout, as in al-folio.

The default wrapper, navigation, bibliography presentation, and CSS are customized.
Unused upstream plugins, demo assets, blog, analytics, and animation dependencies
are intentionally omitted. This is not an unmodified full upstream checkout.
Jekyll and direct plugin versions are pinned in Gemfile. Gemfile.lock includes
Windows and Linux platforms. A real Ruby 3.3.6 / Jekyll 4.3.4 production build
passed locally. The offline preview is derived from this real output.
