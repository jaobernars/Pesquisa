# -*- coding: utf-8 -*-
import re,csv
ARCH=['astro-ph','hep-ph','hep-ex','hep-th','nucl-ex','nucl-th','physics','math-ph','quant-ph','cond-mat','gr-qc','hep-lat']
SRC='/tmp/claude-0/-home-claude/9e61252c-ae46-59f8-a689-7a8d08e03155/scratchpad/gonzalez.txt'
raw=open(SRC,encoding='utf-8').read().split('\n')
try: s=[n for n,l in enumerate(raw) if l.strip()=='References'][0]
except IndexError: s=0
body=raw[s+1:]
NUM=re.compile(r'^\s*\[(\d{1,3})\]\s+(.*)$')
ents={};cur=None
for l in body:
    if not l.strip(): continue
    if re.match(r'^\s*\d+\s+14\. Neutrino',l): continue
    if re.match(r'^\s*1st December, 2025\s*$',l): continue
    m=NUM.match(l)
    if m:
        cur=int(m.group(1)); ents[cur]=[m.group(2).strip()]
    elif cur is not None:
        ents[cur].append(l.strip())
def join(lines):
    t=''
    for j,l in enumerate(lines):
        if j==0: t=l;continue
        if re.search(r'[a-zà-ÿ]-$',t) and re.match(r'[a-zà-ÿ]',l): t=t[:-1]+l
        else: t=t+' '+l
    t=re.sub(r'\s{2,}',' ',t).replace('–','-')
    for a in ARCH:
        t=t.replace('arXiv:'+a.replace('-','')+'/','arXiv:'+a+'/').replace('['+a.replace('-','')+'/','['+a+'/')
    return t.strip()
def arx(t):
    m=re.search(r'arXiv:\s*(\d{4}\.\d{4,5})',t) or re.search(r'\b((?:'+'|'.join(ARCH)+r')/\d{7})\b',t) or re.search(r'arXiv:\s*((?:'+'|'.join(ARCH)+r')/\d{7})',t)
    return m.group(1) if m else ''
def doi(t):
    m=re.search(r'(10\.\d{4,9}/[^\s,;\]]+)',t); return m.group(1).rstrip('.') if m else ''
def yr(t):
    ms=re.findall(r'\((\d{4})\)',t); return ms[0] if ms else ''
def jr(t):
    # journal coordinate: "Phys. Rev. D 17, 2369 (1978)" or "Phys. Rev. D21, 309 (1980)"
    m=re.search(r'([A-Z][A-Za-z\.\s]{2,30}?)\s?([A-Z]?\d{1,4}),\s*(\d{1,6})\s*\((\d{4})\)',t)
    return f"{m.group(1).strip()}|{m.group(2)}|{m.group(3)}" if m else ''
rows=[]
for n in sorted(ents):
    t=join(ents[n])
    rows.append(dict(ref_id='G%03d'%n,fonte='GONZALEZ-GARCIA',autor=t.split(',')[0][:60],ano=yr(t),arxiv=arx(t),doi=doi(t),journal=jr(t),titulo='',raw=t))
with open('/home/claude/proj/data/refs_gonzalez.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['ref_id','fonte','autor','ano','arxiv','doi','journal','titulo','raw']);w.writeheader()
    for r in rows: w.writerow(r)
print('GONZALEZ entradas:',len(rows),'(esperado 252) | faltando:',[i for i in range(1,253) if i not in ents])
print('com arXiv:',sum(1 for r in rows if r['arxiv']),'| com journal:',sum(1 for r in rows if r['journal']),
      '| sem arxiv e sem journal:',sum(1 for r in rows if not r['arxiv'] and not r['journal']))
for r in rows[:4]: print(' ',r['ref_id'],'|',r['ano'],'|',r['arxiv'],'|',r['journal'],'|',r['raw'][:80])
for r in [x for x in rows if not x['arxiv'] and not x['journal']][:6]: print('  SEM-ID',r['ref_id'],r['raw'][:110])
