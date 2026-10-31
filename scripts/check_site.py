"""Check the real Jekyll output (also usable with the local content preview)."""
import sys,re
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote

root=Path(sys.argv[1] if len(sys.argv)>1 else '_site').resolve()
class Page(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=[];self.lang=None;self.nav=0;self.sections=[];self.section_errors=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.lang=a.get('lang')
        if tag=='nav':self.nav+=1
        if tag=='section':
            # Research topics require explanatory figures. Funded projects may
            # have no suitable public image; never require filler illustrations.
            topic='topic' in a.get('class','').split()
            if topic and any(s['topic'] for s in self.sections):self.section_errors.append('Nested research topics')
            self.sections.append({'topic':topic,'image':False})
        if tag=='img' and self.sections:self.sections[-1]['image']=True
        if 'id' in a:self.ids.append(a['id'])
        if tag in ('a','img','script','link','video','source'):
            u=a.get('href') or a.get('src')
            if u:self.links.append(u)
            if a.get('poster'):self.links.append(a['poster'])
    def handle_endtag(self,tag):
        if tag=='section' and self.sections:
            section=self.sections.pop()
            if section['topic'] and not section['image']:self.section_errors.append('Research topic without an image')

errors=[];parsed={}
home=(root/'index.html').read_text(encoding='utf8')
canonical=re.search(r'<link rel="canonical" href="([^"]+)"',home)
base=urlsplit(canonical[1]).path.rstrip('/') if canonical else ''
for route in ['','research','publications','projects','service','cv']:
    p=root/route/'index.html'
    if not p.exists():errors.append(f'Missing {p}');continue
    txt=p.read_text(encoding='utf8');parser=Page();parser.feed(txt);parsed[p]=parser
    if parser.lang!='en':errors.append(f'Wrong language: {p}')
    if parser.nav!=1:errors.append(f'Navigation missing: {p}')
    if re.search(r'{[%{]|Your Name|You R\. Name|Write your biography|example\.com',txt):errors.append(f'Unrendered template or placeholder: {p}')
    if len(parser.ids)!=len(set(parser.ids)):errors.append(f'Duplicate anchors: {p}')
    errors.extend(f'{issue}: {p}' for issue in parser.section_errors)
    if re.search(r'&lt;/(section|figure|figcaption)&gt;',txt):errors.append(f'Escaped structural HTML: {p}')
for p,parser in parsed.items():
    for url in parser.links:
        u=urlsplit(url)
        if u.scheme or u.netloc:continue
        path=unquote(u.path)
        if base and path.startswith(base+'/'):path=path[len(base):]
        target=(root/path.lstrip('/')) if path.startswith('/') else p.parent/path
        if target.is_dir():target=target/'index.html'
        if not target.exists():errors.append(f'Broken local link {url} in {p.relative_to(root)}')
        elif u.fragment and target.suffix=='.html':
            q=Page();q.feed(target.read_text(encoding='utf8'))
            if unquote(u.fragment) not in q.ids:errors.append(f'Missing anchor {url}')
pubs=(root/'publications/index.html').read_text(encoding='utf8')
for name in ['Xiaocheng Feng','Zhangyin Feng','Ming Zhou','Lingpeng Kong']:
    if name not in pubs:errors.append(f'Author metadata did not render: {name}')
if len(re.findall(r'class="paper"',pubs))<65:errors.append('Publication list is incomplete')
if len(re.findall(r'class="paper"',home))!=5:errors.append('Homepage must contain five selected papers')
projects=(root/'projects/index.html').read_text(encoding='utf8')
if len(re.findall(r'class="funded-project"',projects))!=11:errors.append('Project portfolio must include all eleven supplied projects')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: six English pages, local assets, links, anchors, and rendered templates ({len(list(root.rglob("*.html")))} HTML files).')
