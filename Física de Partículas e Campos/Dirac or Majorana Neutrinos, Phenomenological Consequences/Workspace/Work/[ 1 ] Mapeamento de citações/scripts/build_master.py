# -*- coding: utf-8 -*-
"""Constroi a tabela mestre deduplicada e atribui os blocos de 20 buscas.
Ordem dos blocos: refs COM arXiv primeiro (busca exata), depois as SEM arXiv
(busca por journal/titulo). Dentro de cada grupo, ordem cronologica."""
import csv,re,collections
rows=[]
for p in ('dados/refs_agostini.csv','dados/refs_gonzalez.csv'):
    for r in csv.DictReader(open(p,encoding='utf-8')):
        r.setdefault('journal',''); r.setdefault('titulo',''); rows.append(r)
def key(r):
    if r['arxiv']: return 'arx:'+r['arxiv'].lower()
    if r['doi']:   return 'doi:'+r['doi'].lower()
    t=re.sub(r'[^a-z0-9]','',(r['titulo'] or '').lower())[:40]
    if t: return 'ttl:'+t
    return 'raw:'+re.sub(r'[^a-z0-9]','',r['raw'].lower())[:60]
master={}
for r in rows:
    k=key(r)
    if k in master:
        m=master[k]; m['ref_ids'].append(r['ref_id']); m['fontes'].add(r['fonte'])
        for c in ('titulo','journal','doi'):
            if not m[c] and r[c]: m[c]=r[c]
    else:
        master[k]=dict(ref_ids=[r['ref_id']],fontes={r['fonte']},autor=r['autor'],ano=r['ano'],
                       arxiv=r['arxiv'],doi=r['doi'],journal=r['journal'],titulo=r['titulo'],raw=r['raw'])
vals=list(master.values())
com=[m for m in vals if m['arxiv']]
sem=[m for m in vals if not m['arxiv']]
sk=lambda m:(m['ano'] or '0000', m['autor'])
ordered=sorted(com,key=sk)+sorted(sem,key=sk)
for i,m in enumerate(ordered):
    m['uid']='U%04d'%(i+1); m['bloco']='B%02d'%(i//20+1)
    m['metodo']='arxiv' if m['arxiv'] else ('doi' if m['doi'] else ('journal' if m['journal'] else 'titulo'))
    m['ref_ids']=';'.join(m['ref_ids']); m['fontes']=';'.join(sorted(m['fontes']))
cols=['uid','bloco','metodo','fontes','ref_ids','autor','ano','arxiv','doi','journal','titulo','raw']
with open('dados/master_refs.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
    for m in ordered: w.writerow({c:m[c] for c in cols})
c=collections.Counter(m['bloco'] for m in ordered)
mt=collections.Counter(m['metodo'] for m in ordered)
print('unicos:',len(ordered),'| blocos:',len(c),'| ultimo bloco tem',c[max(c)],'refs')
print('metodo de busca:',dict(mt))
print('ultimo bloco 100% arXiv:',max(m['bloco'] for m in ordered if m['arxiv']))
