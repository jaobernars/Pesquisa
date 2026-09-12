# -*- coding: utf-8 -*-
"""Junta resultados/B*.csv com dados/master_refs.csv -> dados/dados_citacoes.csv (tabela final de analise)."""
import csv,glob,os,collections
master={r['uid']:r for r in csv.DictReader(open('dados/master_refs.csv',encoding='utf-8'))}
res={}
for p in sorted(glob.glob('resultados/B*.csv')):
    for r in csv.DictReader(open(p,encoding='utf-8')): res[r['uid']]=r
COLS=['uid','bloco','fontes','citado_por_ambas','ref_ids','status','duplicata_de','inspire_id','autor_ref','primeiro_autor',
      'n_autores','ano_ref','ano_inspire','data_inspire','arxiv','doi','journal','titulo','citacoes',
      'citacoes_sem_auto','idade_anos','citacoes_por_ano','tipo_doc','raw']
ANO_ATUAL=2026
out=[]
for uid,m in master.items():
    r=res.get(uid,{})
    ano=(r.get('ano_inspire') or m['ano'] or '').strip()
    cit=r.get('citacoes','').strip()
    idade=ANO_ATUAL-int(ano) if ano.isdigit() else ''
    cpa=round(int(cit)/max(idade,1),2) if cit.isdigit() and idade!='' else ''
    out.append(dict(uid=uid,bloco=m['bloco'],fontes=m['fontes'],citado_por_ambas='SIM' if ';' in m['fontes'] else 'NAO',
        ref_ids=m['ref_ids'],status=r.get('status','PENDENTE'),inspire_id=r.get('inspire_id',''),
        autor_ref=m['autor'],primeiro_autor=r.get('primeiro_autor',''),n_autores=r.get('n_autores',''),
        ano_ref=m['ano'],ano_inspire=r.get('ano_inspire',''),data_inspire=r.get('data_inspire',''),
        arxiv=r.get('arxiv') or m['arxiv'],doi=r.get('doi') or m['doi'],journal=r.get('journal') or m['journal'],
        titulo=r.get('titulo_inspire') or m['titulo'],citacoes=cit,citacoes_sem_auto=r.get('citacoes_sem_auto',''),
        idade_anos=idade,citacoes_por_ano=cpa,tipo_doc=r.get('tipo_doc',''),raw=m['raw']))
# dedup definitivo: dois uids com o mesmo inspire_id sao o mesmo trabalho.
# O primeiro uid mantem a linha; os demais sao marcados e excluidos da analise.
visto={}
for r in out: r['duplicata_de']=''
for r in sorted(out,key=lambda r:r['uid']):
    i=(r.get('inspire_id') or '').strip()
    if not i: continue
    if i in visto: r['duplicata_de']=visto[i]
    else: visto[i]=r['uid']
ndup=sum(1 for r in out if r['duplicata_de'])
print('duplicatas por inspire_id marcadas:',ndup)
out.sort(key=lambda r:(r['ano_inspire'] or r['ano_ref'] or '0000', r['uid']))
with open('dados/dados_citacoes.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=COLS);w.writeheader();[w.writerow(r) for r in out]
c=collections.Counter(r['status'] for r in out)
print('linhas:',len(out),'| status:',dict(c))
print('com citacoes:',sum(1 for r in out if str(r['citacoes']).isdigit()))
