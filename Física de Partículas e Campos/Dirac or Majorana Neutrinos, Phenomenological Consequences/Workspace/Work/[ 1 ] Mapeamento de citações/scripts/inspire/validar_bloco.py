# -*- coding: utf-8 -*-
"""Valida resultados/<BLOCO>.csv contra a lista mestre. Uso: python3 scripts/inspire/validar_bloco.py B01"""
import csv,sys,os,json,datetime
b=sys.argv[1].upper()
SCHEMA=open('resultados/_schema.csv',encoding='utf-8').read().strip().split(',')
esp=[r['uid'] for r in csv.DictReader(open('dados/master ref/master_refs.csv',encoding='utf-8')) if r['bloco']==b]
p=f'resultados/{b}.csv'
err=[]
if not os.path.exists(p): print(f'FALHA: {p} nao existe'); sys.exit(1)
rows=list(csv.DictReader(open(p,encoding='utf-8')))
if rows and list(rows[0].keys())!=SCHEMA: err.append(f'cabecalho diferente do schema: {list(rows[0].keys())}')
got=[r['uid'] for r in rows]
if len(got)!=len(set(got)): err.append('uids duplicados')
falta=[u for u in esp if u not in got]; sobra=[u for u in got if u not in esp]
if falta: err.append(f'faltam {len(falta)} uids: {falta[:8]}')
if sobra: err.append(f'uids fora do bloco: {sobra[:8]}')
VAL={'OK','DUVIDOSO','AMBIGUO','NAO_ENCONTRADO','ERRO_FETCH'}
for r in rows:
    if r['status'] not in VAL: err.append(f"{r['uid']}: status invalido '{r['status']}'")
    if r['status']=='OK':
        if not r['inspire_id'].strip().isdigit(): err.append(f"{r['uid']}: inspire_id invalido")
        if not r['citacoes'].strip().isdigit(): err.append(f"{r['uid']}: citacoes nao numerico")
        if not r['ano_inspire'].strip().isdigit(): err.append(f"{r['uid']}: ano_inspire invalido")
ids=[r['inspire_id'] for r in rows if r['status']=='OK' and r['inspire_id']]
dup=set(i for i in ids if ids.count(i)>1)
if dup:
    # Duplicata de inspire_id eh esperada quando o mesmo paper classico e citado
    # independentemente pelas duas reviews-fonte (AGOSTINI e GONZALEZ-GARCIA) — a
    # dedup entre reviews so acontece na Fase 3 (CONSOLIDAR), usando a coluna
    # `fontes` de dados/master ref/master_refs.csv.
    # So reportar como erro se as fontes das linhas duplicadas coincidirem, o que
    # indicaria um match de query realmente errado.
    fontes_por_uid={}
    if os.path.exists('dados/master ref/master_refs.csv'):
        for r in csv.DictReader(open('dados/master ref/master_refs.csv',encoding='utf-8')):
            fontes_por_uid[r['uid']]=r.get('fontes','')
    real_dup=set()
    for i in dup:
        uids_i=[r['uid'] for r in rows if r['status']=='OK' and r['inspire_id']==i]
        fontes_i=[fontes_por_uid.get(u,'') for u in uids_i]
        if len(set(fontes_i))<len(fontes_i) or not fontes_por_uid:
            real_dup.add(i)
    if real_dup:
        err.append(f'inspire_id repetido dentro do bloco com a MESMA fonte (possivel match errado): {sorted(real_dup)}')
benignas=sorted(dup-set(real_dup)) if dup else []
if benignas:
    print(f'  AVISO: mesmo inspire_id em uids diferentes deste bloco (mesma obra citada pelas duas reviews): {benignas}')
    print('         nao e erro; a deduplicacao definitiva acontece em scripts/tema/consolidar.py, por inspire_id.')
c=lambda s:sum(1 for r in rows if r['status']==s)
if err:
    print(f'BLOCO {b}: REPROVADO'); [print('  -',e) for e in err]; sys.exit(1)
print(f'BLOCO {b}: APROVADO | {len(rows)} linhas | OK={c("OK")} DUVIDOSO={c("DUVIDOSO")} AMBIGUO={c("AMBIGUO")} NAO_ENCONTRADO={c("NAO_ENCONTRADO")} ERRO_FETCH={c("ERRO_FETCH")}')
top=max((r for r in rows if r['status']=='OK' and r['citacoes'].isdigit()),key=lambda r:int(r['citacoes']),default=None)
if top: print(f'  mais citado: {top["citacoes"]} — {top["titulo_inspire"][:80]}')
idx=json.load(open('tarefas/indice_blocos.json',encoding='utf-8'))
for it in idx:
    if it['bloco']==b:
        it['status']='concluido'; it['data']=datetime.date.today().isoformat()
        it['ok']=c('OK'); it['revisar']=len(rows)-c('OK')
json.dump(idx,open('tarefas/indice_blocos.json','w'),ensure_ascii=False,indent=1)
