# Xiaocheng Feng — academic homepage

Six-page English Jekyll site, adapted from al-folio v0.14.6. See
`docs/TEMPLATE.md` for provenance and `docs/SOURCES.md` for content sources.

## GitHub Pages hosting

- Public website: https://buix5371.github.io/feng-homepage/
- Source repository: https://github.com/buix5371/feng-homepage (`main`).
- Published files: `gh-pages`, root directory, with `.nojekyll`.
- The owner authorized public visibility and publication on 2026-10-31.
  The original PPT and local source-download/runtime folders are not uploaded.

In **Settings → Pages → Build and deployment**, the source is **Deploy from a
branch**, branch **gh-pages**, folder **/(root)**. GitHub automatically republishes
when the published branch changes. No domain purchase is needed.

To update the current deployment, edit the source on `main`, build and check it,
then synchronize the generated `_site/` files to `gh-pages` (preserving `.git`
and `.nojekyll`) and push that branch. Source edits on `main` alone do not yet
update the website. `docs/deployment/pages.yml` is an optional inactive workflow
for a future GitHub Actions build; activating it needs workflow write permission
and a corresponding switch of the Pages publishing source to GitHub Actions.

If the repository is renamed, update `url`/`baseurl` in `_config.yml`, rebuild,
and republish. The current configuration targets `/feng-homepage/`.

## Local production build

Use Ruby 3.3.6 and Bundler. Run `bundle install`, then
`bundle exec jekyll serve --baseurl ''`. Open http://127.0.0.1:4000.
Gemfile.lock is included for Windows and Linux. Direct and transitive dependencies are locked.
For a production check: `bundle exec jekyll build`, then
`python scripts/check_site.py _site`.

## Offline preview

The included preview is generated from the real Jekyll production output.
Run `python scripts/portable_preview.py` after a successful build to refresh it.
Open `preview/index.html` directly; navigation and assets use relative paths.

## 日常维护

- 简介：修改 `index.md` 的正文；身份栏在 `_layouts/about.liquid`。
- 论文：在 `_bibliography/papers.bib` 追加正式 BibTeX。作者使用
  `姓, 名 and 姓, 名`，保留完整顺序。`url` 为正式文章页，`pdf` 可选。
  添加 `selected = {true}` 会出现在首页；首页保持约 5 篇。
- 动态：修改 `_data/news.yml`，包含字符串格式的 `year`、`date`、`text`、`url`，最新放最前；
  首页 News 最多显示 5 条近期任职、活动等动态，按时间新到旧维护，不按年份清空；论文介绍与奖项留在论文区，避免重复。文字与日期使用英文。
- 研究：正文在 `_pages/research.md`，首页摘要在 `_data/research.yml`。
- 项目、服务和履历：修改 `_pages/` 对应文件。
- 项目清单：在 `_data/projects.yml` 维护标题、资助方、起止时间与本人角色；`group` 为 ongoing、earlier 或 industry。页面先罗列全部项目，再介绍作文生成与多语言翻译应用；作文暂用简短文字，多语言保留原 PPT 系统演示。应用介绍在 `_pages/projects.md`，新图须记录来源。
- 系统演示：多语言应用使用原 PPT 第 19 页 GIF 转成的视频 `assets/img/projects/multilingual-system-demo.mp4`，封面为同目录 `multilingual-system-poster.jpg`。替换演示时同步修改尺寸、封面、英文说明和来源记录；不将其他平台的界面当作本组成果。
- 照片：替换 `assets/img/portrait.jpg`；保持原文件名与人物比例。
- PPT 原图：位于 `assets/img/research/`；图片来源见 `docs/SOURCES.md`，首页方向图位于 `_includes/research_cards.liquid`，由 `_data/research.yml` 配置。
- 当前发布方式：修改 `main` 的源码后，构建检查，再将生成网页同步到 `gh-pages` 并推送；GitHub 会自动发布该分支。只更新 `main` 暂不会自动更新网站。

## Delivery status

The Ruby 3.3.6 / Jekyll 4.3.4 production build passed locally, including six
pages, full author rendering, five selected publications, and internal links.
68 publication records are included. 133 article, institution, and PDF links returned HTTP 200.
Browser-based visual/interaction checks were unavailable because browser control
was stopped by its URL safety check. The owner authorized public repository visibility and GitHub Pages deployment on
2026-10-31. Generated files are published from the `gh-pages` branch.
Automated rebuilding of source changes on `main` is not yet enabled.
The deployment workflow is supplied as an inactive template because the current
Git credential cannot write active workflow files.

On Windows, if a workspace path containing spaces causes `bundle exec` to fail
with a RUBYOPT error, use the same native Jekyll build API:
`ruby scripts/build.rb`.


## 内容完整性检查

`docs/CONTENT_AUDIT.md` 对照 PPT 全部 23 页记录覆盖情况、补充内容和保留边界；论文目录为核实记录，不能当作全部职业生涯论文总数。

首页栏目组织的参考与取舍见 `docs/HOMEPAGE_REFERENCES.md`。
