# -*- coding: utf-8 -*-
import re,csv,json,unicodedata
ARCH=['astro-ph','hep-ph','hep-ex','hep-th','nucl-ex','nucl-th','physics','math-ph','quant-ph','cond-mat','gr-qc','hep-lat','stat','cs','math','eess','q-bio']
SRC='/home/claude/proj/dados/agostini_cols.txt'
raw=open(SRC,encoding='utf-8').read().split('\n')
i=[n for n,l in enumerate(raw) if l.strip()=='REFERENCES'][0]
body=raw[i+1:]
blocks=[];cur=[]
for l in body:
    if not l.strip(): continue
    if re.fullmatch(r'\s*\d{1,3}\s*',l): continue
    if l.startswith(' '):
        if cur: cur.append(l.strip())
    else:
        if cur: blocks.append(cur)
        cur=[l.strip()]
if cur: blocks.append(cur)
NOME=r"[’'ʼ]?[A-ZÀ-Ýa-zà-ÿĀ-ɏ][A-Za-zÀ-ÿĀ-ɏ'’̀-ͯ\-\.]*(?:[ ][A-Za-zÀ-ÿĀ-ɏ'’̀-ͯ\-\.]+){0,2}"
START=re.compile(rf"^({NOME}),\s+[A-ZÀ-ÝĀ-ɏ]|^({NOME})\s+\((?:1[6-9]|20)\d\d")
YEAR=re.compile(r'\((?:1[6-9]|20)\d\d[a-z]?\)')
m1=[]
for b in blocks:
    if m1 and not START.match(b[0]): m1[-1].extend(b)
    else: m1.append(list(b))
ents=[];k=0
while k<len(m1):
    e=list(m1[k]);k+=1
    while not YEAR.search(' '.join(e)) and k<len(m1): e.extend(m1[k]);k+=1
    ents.append(e)

def join(lines):
    t=''
    for j,l in enumerate(lines):
        if j==0: t=l; continue
        if t.endswith('-') and re.search(r'[a-zà-ÿ]-$',t) and re.match(r'[a-zà-ÿ]',l): t=t[:-1]+l
        else: t=t+' '+l
    t=t.replace('–','-').replace('—','-')
    t=re.sub(r'\s{2,}',' ',t)
    for a in ARCH:
        t=t.replace('arXiv:'+a.replace('-','')+'/','arXiv:'+a+'/').replace('['+a.replace('-','')+']','['+a+']').replace('['+a.replace('-','')+'.','['+a+'.')
    return t.strip()
def arx(t):
    m=re.search(r'arXiv:\s*(\d{4}\.\d{4,5})',t) or re.search(r'arXiv:\s*((?:'+'|'.join(ARCH)+r')/\d{7})',t) or re.search(r'\b((?:'+'|'.join(ARCH)+r')/\d{7})\b',t)
    return m.group(1) if m else ''
def doi(t):
    m=re.search(r'(10\.\d{4,9}/[^\s,;\]]+)',t); return m.group(1).rstrip('.') if m else ''
def yr(t):
    m=YEAR.search(t); return m.group(0)[1:5] if m else ''
def ttl(t):
    m=re.search(r'[“"]([^”"]+)[”"]',t); return re.sub(r'\s+',' ',m.group(1)).strip().rstrip(',') if m else ''
def au(t):
    m=re.match(r'^([^,(]+)',t); return m.group(1).strip() if m else ''
rows=[]
for n,e in enumerate(ents,1):
    t=join(e)
    rows.append(dict(ref_id='A%03d'%n,fonte='AGOSTINI',autor=au(t),ano=yr(t),arxiv=arx(t),doi=doi(t),titulo=ttl(t),raw=t))
with open('/home/claude/proj/dados/refs_agostini.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['ref_id','fonte','autor','ano','arxiv','doi','titulo','raw']);w.writeheader()
    for r in rows: w.writerow(r)
def norm(s): return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
viol=sum(1 for a,b in zip(rows,rows[1:]) if norm(a['autor'])>norm(b['autor']))
print('AGOSTINI entradas:',len(rows))
print('com arXiv:',sum(1 for r in rows if r['arxiv']),'| com DOI:',sum(1 for r in rows if r['doi']),'| sem ambos:',sum(1 for r in rows if not r['arxiv'] and not r['doi']))
print('sem titulo:',sum(1 for r in rows if not r['titulo']),'| quebras de ordem alfabetica:',viol)
