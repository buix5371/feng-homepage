"""Make an offline preview of the actual Jekyll output. Run after jekyll build."""
from pathlib import Path
import re,os,shutil
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'_site'
OUT=ROOT/'preview'
if not (SOURCE/'index.html').exists():raise SystemExit('Run the Jekyll production build first.')
shutil.copytree(SOURCE,OUT,dirs_exist_ok=True)
home=(SOURCE/'index.html').read_text(encoding='utf8')
canonical=re.search(r'<link rel="canonical" href="([^"]+)"',home)
base=urlsplit(canonical[1]).path.rstrip('/') if canonical else ''
for p in SOURCE.rglob('*.html'):
    dest=OUT/p.relative_to(SOURCE)
    def replace(m):
        attr,path=m[1],m[2]
        if base and path.startswith(base+'/'):path=path[len(base):]
        clean,sep,fragment=path.partition('#')
        target=OUT/clean.lstrip('/')
        if clean.endswith('/'):target=target/'index.html'
        relative=os.path.relpath(target,dest.parent).replace('\\','/')
        return attr+'="'+relative+(sep+fragment if sep else '')+'"'
    text=re.sub(r'(href|src)="(/[^\"]*)"',replace,p.read_text(encoding='utf8'))
    dest.write_text(text,encoding='utf8')
print('Offline preview created from real Jekyll output:',OUT)
