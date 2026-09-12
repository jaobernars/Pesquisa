# -*- coding: utf-8 -*-
"""Reconcilia a lista mestre CONGELADA (uids ja atribuidos e blocos ja coletados)
com a re-extracao corrigida do PDF do Agostini.

- uids existentes NAO mudam de numero nem de bloco (preserva o trabalho ja feito);
- entradas que estavam fundidas tem raw/arxiv/titulo corrigidos para a 1a referencia;
- referencias que faltavam entram como uids novos, em blocos novos no fim da fila.
"""
import csv,re,collections
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
def key(r):
    if r['arxiv']: return 'arx:'+r['arxiv'].lower()
    if r['doi']:   return 'doi:'+r['doi'].lower()
    t=norm(r.get('titulo') or '')[:40]
    return ('ttl:'+t) if t else ('raw:'+norm(r['raw'])[:60])

novo=[]
for p in ('dados/refs_agostini.csv','dados/refs_gonzalez.csv'):
    for r in csv.DictReader(open(p,encoding='utf-8')):
        r.setdefault('journal',''); r.setdefault('titulo',''); novo.append(r)
uni={}
for r in novo:
    k=key(r)
    if k in uni:
        m=uni[k]; m['ref_ids'].append(r['ref_id']); m['fontes'].add(r['fonte'])
        for c in ('titulo','journal','doi'):
            if not m[c] and r[c]: m[c]=r[c]
    else:
        uni[k]=dict(ref_ids=[r['ref_id']],fontes={r['fonte']},autor=r['autor'],ano=r['ano'],
                    arxiv=r['arxiv'],doi=r['doi'],journal=r['journal'],titulo=r['titulo'],raw=r['raw'])
print('re-extracao:',len(novo),'brutas ->',len(uni),'unicas')

antigo=list(csv.DictReader(open('dados/master_refs.csv',encoding='utf-8')))
por_prefixo={norm(v['raw'])[:70]:k for k,v in uni.items()}
usados=set(); corrigidos=0
for a in antigo:
    pref=norm(a['raw'])[:70]
    k=por_prefixo.get(pref) or (key(a) if key(a) in uni else None)
    if k is None or k in usados:   # ultimo recurso: casar pelo inicio mais longo em comum
        cands=[kk for pp,kk in por_prefixo.items() if kk not in usados and pp[:40]==pref[:40]]
        k=cands[0] if cands else None
    if k:
        usados.add(k); n=uni[k]
        if a['raw']!=n['raw']:
            corrigidos+=1
            a['raw']=n['raw']; a['arxiv']=n['arxiv']; a['doi']=n['doi'] or a['doi']
            a['titulo']=n['titulo'] or a['titulo']; a['journal']=n['journal'] or a['journal']
            a['autor']=n['autor']; a['ano']=n['ano'] or a['ano']
            a['metodo']='arxiv' if n['arxiv'] else ('doi' if n['doi'] else ('journal' if n['journal'] else 'titulo'))
        a['ref_ids']=';'.join(n['ref_ids']); a['fontes']=';'.join(sorted(n['fontes']))
    else:
        a['obs_reconciliacao']='sem correspondencia na re-extracao'
faltando=[uni[k] for k in uni if k not in usados]
faltando.sort(key=lambda m:(m['ano'] or '0000', m['autor']))
uid=max(int(a['uid'][1:]) for a in antigo)
bloco=max(int(a['bloco'][1:]) for a in antigo)
novos=[]
for i,m in enumerate(faltando):
    uid+=1
    novos.append(dict(uid='U%04d'%uid, bloco='B%02d'%(bloco+1+i//20),
        metodo='arxiv' if m['arxiv'] else ('doi' if m['doi'] else ('journal' if m['journal'] else 'titulo')),
        fontes=';'.join(sorted(m['fontes'])), ref_ids=';'.join(m['ref_ids']), autor=m['autor'], ano=m['ano'],
        arxiv=m['arxiv'], doi=m['doi'], journal=m['journal'], titulo=m['titulo'], raw=m['raw']))
cols=['uid','bloco','metodo','fontes','ref_ids','autor','ano','arxiv','doi','journal','titulo','raw']
with open('dados/master_refs.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
    for r in antigo+novos: w.writerow({c:r.get(c,'') for c in cols})
print('uids preservados:',len(antigo),'| linhas corrigidas (entrada fundida):',corrigidos)
print('referencias NOVAS recuperadas:',len(novos),'-> uids',novos[0]['uid'] if novos else '-', 'a', novos[-1]['uid'] if novos else '-')
print('blocos novos:',sorted(set(n['bloco'] for n in novos)))
print('TOTAL agora:',len(antigo)+len(novos))
