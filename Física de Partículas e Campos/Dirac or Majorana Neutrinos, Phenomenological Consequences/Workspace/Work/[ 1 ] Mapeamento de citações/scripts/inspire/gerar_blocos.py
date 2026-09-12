# -*- coding: utf-8 -*-
import csv,os,collections,json
os.makedirs('tarefas/blocos',exist_ok=True)
rows=list(csv.DictReader(open('dados/master ref/master_refs.csv',encoding='utf-8')))
by=collections.OrderedDict()
for r in rows: by.setdefault(r['bloco'],[]).append(r)
idx=[]
for b,rs in by.items():
    metodos=collections.Counter(r['metodo'] for r in rs)
    anos=[r['ano'] for r in rs if r['ano']]
    linhas=[f"# TAREFA {b} — {len(rs)} referencias",
            f"", f"Metodos: {dict(metodos)} | Faixa de anos: {min(anos) if anos else '?'}–{max(anos) if anos else '?'}",
            f"Saida obrigatoria: `resultados/{b}.csv` (mesmo cabecalho de `resultados/_schema.csv`)","",
            "| uid | metodo | ano | arxiv | doi | journal (rev|vol|pag) | autor | titulo/raw |",
            "|---|---|---|---|---|---|---|---|"]
    for r in rs:
        ident = r['arxiv'] or r['doi'] or r['journal'] or ''
        titulo = (r['titulo'] or r['raw'])[:150].replace('|','/')
        linhas.append(f"| {r['uid']} | {r['metodo']} | {r['ano']} | {r['arxiv']} | {r['doi']} | {r['journal']} | {r['autor'][:35].replace('|','/')} | {titulo} |")
    linhas.append("")
    linhas.append("## Referencias brutas (use quando a busca por identificador falhar)")
    for r in rs:
        linhas.append(f"- **{r['uid']}**: {r['raw'][:400]}")
    open(f'tarefas/blocos/{b}.md','w',encoding='utf-8').write('\n'.join(linhas)+'\n')
    idx.append(dict(bloco=b,n=len(rs),metodos=dict(metodos),ano_min=min(anos) if anos else None,ano_max=max(anos) if anos else None,status='pendente'))
json.dump(idx,open('tarefas/indice_blocos.json','w'),ensure_ascii=False,indent=1)
os.makedirs('resultados',exist_ok=True)
SCHEMA=['uid','status','inspire_id','titulo_inspire','primeiro_autor','n_autores','ano_inspire','data_inspire','arxiv','doi','journal','citacoes','citacoes_sem_auto','tipo_doc','query_usada','obs']
open('resultados/_schema.csv','w',encoding='utf-8').write(','.join(SCHEMA)+'\n')
print('blocos gerados:',len(idx))
print(open('tarefas/blocos/B01.md',encoding='utf-8').read()[:1200])
