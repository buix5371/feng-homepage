# Xiaocheng Feng — academic homepage

Six-page English Jekyll site, adapted from al-folio v0.14.6. See
`docs/TEMPLATE.md` for provenance and `docs/SOURCES.md` for content sources.

## Publish to GitHub Pages

1. The source repository is `buix5371/feng-homepage` and remains **private**.
   Publication is deferred at the owner's request.
2. When ready to publish, copy `docs/deployment/pages.yml` to
   `.github/workflows/pages.yml` using GitHub's web editor or a credential with
   workflow permission. Do not upload the source-download folder or original PPT.
3. In repository **Settings → Pages → Build and deployment**, choose
   **GitHub Actions** as the source.
4. Run **Build and deploy homepage** under Actions and check **publish**.
   Normal pushes only build and check the site; publication is manual.
5. Once the deployment succeeds, open `https://buix5371.github.io/feng-homepage/`.

This address is the expected address, not a claim that deployment has occurred.
The workflow detects project vs account repository names automatically. If the
repository is renamed, update `url`/`baseurl` in `_config.yml` for local previews;
CI overrides them with the actual repository owner and name.

## Local production build

Use Ruby 3.3.6 and Bundler. Run `bundle install`, then
`bundle exec jekyll serve --baseurl ''`. Open http://127.0.0.1:4000.
Gemfile.lock is included for Windows and Linux. Direct and transitive dependencies are locked.
For a production check: `bundle exec jekyll build`, then
`python scripts/check_site.py _site`.

## Offline preview
+
+The included preview is generated from the real Jekyll production output.
+Run `python scripts/portable_preview.py` after a successful build to refresh it.
+Open `preview/index.html` directly; navigation and assets use relative paths.
+
+## 日常维护

- 简介：修改 `index.md` 的正文；身份栏在 `_layouts/about.liquid`。
- 论文：在 `_bibliography/papers.bib` 追加正式 BibTeX。作者使用
  `姓, 名 and 姓, 名`，保留完整顺序。`url` 为正式文章页，`pdf` 可选。
  添加 `selected = {true}` 会出现在首页；首页保持约 5 篇。
- 动态：修改 `_data/news.yml`，包含 `date`、`text`、`url`，最新放最前；
  首页最多显示 5 条。文字与日期使用英文。
- 研究：正文在 `_pages/research.md`，首页摘要在 `_data/research.yml`。
- 项目、服务和履历：修改 `_pages/` 对应文件。
- 照片：替换 `assets/img/portrait.jpg`；保持原文件名与人物比例。
- 启用工作流后，提交到 `main` 会自动构建检查；发布需手动运行工作流并勾选
  publish。发布前检查姓名、年份、链接和手机显示。

## Delivery status

The Ruby 3.3.6 / Jekyll 4.3.4 production build passed locally, including six
pages, full author rendering, five selected publications, and internal links.
65 publication records are included. 133 article, institution, and PDF links returned HTTP 200.
Browser-based visual/interaction checks were unavailable because browser control
was stopped by its URL safety check. The source is intended for the owner's private
repository. Automated workflow activation and public deployment are deferred.
The deployment workflow is supplied as an inactive template because the current
Git credential cannot write active workflow files.

On Windows, if a workspace path containing spaces causes `bundle exec` to fail
with a RUBYOPT error, use the same native Jekyll build API:
`ruby scripts/build.rb`.

