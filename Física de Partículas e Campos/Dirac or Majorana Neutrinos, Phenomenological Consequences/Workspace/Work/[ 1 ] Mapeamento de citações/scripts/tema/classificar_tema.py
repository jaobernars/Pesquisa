# -*- coding: utf-8 -*-
"""Classifica cada referencia por aderencia ao projeto de IC do Joao
(natureza Dirac vs Majorana, 0nubb, PMNS estendida com fases de CP, massa efetiva de Majorana).

Entrada: dados/citacoes/dados_citacoes.csv   Saida: dados/citacoes/dados_citacoes_tema.csv + shortlist
Uso: python3 scripts/consolidacao_tema/classificar_tema.py [--top 40]
"""
import csv,re,argparse,collections
# peso 3 = nucleo teorico do projeto | 2 = adjacente direto | 1 = contexto
EIXOS={
 'majorana_natureza':(3,['majorana fermion','majorana nature','majorana mass','dirac or majorana','dirac vs majorana',
     'dirac-majorana','majorana neutrino','majorana phase','nature of neutrino','majorana condition','self-conjugate']),
 '0nubb':(3,['neutrinoless double beta','neutrinoless double-beta','0nubb',r'0\\nu\\beta\\beta','double beta decay',
     'double-beta decay','half-life limit','effective majorana mass','mass mechanism','light neutrino exchange']),
 'violacao_numero_leptonico':(3,['lepton number violation','lepton number viola','delta l = 2','black box theorem',
     'schechter','leptogenesis','baryon asymmetry','matter-antimatter','matter antimatter']),
 'pmns_cp':(3,['pmns','mixing matrix','cp violation','cp phase','dirac phase','leptonic cp','unitarity of the lepton',
     'mixing angle','delta_cp']),
 'seesaw_massa':(3,['seesaw','see-saw','right-handed neutrino','sterile neutrino','neutrino mass generation',
     'weinberg operator','type-i','type ii seesaw','absolute mass scale','mass ordering','mass hierarchy']),
 'nme_nuclear':(2,['nuclear matrix element','matrix elements','shell model','qrpa','ibm-2','edf','gamow-teller',
     'quenching','g_a','phase space factor']),
 'oscilacao':(2,['oscillation','neutrino oscillation','msw','matter effect','solar neutrino','atmospheric neutrino',
     'reactor','global fit','theta13','theta23','delta m']),
 'experimento':(1,['gerda','legend','kamland-zen','exo','nexo','cuore','cupid','majorana demonstrator','sno',
     'super-kamiokande','t2k','nova','dune','juno','borexino','xenon','amore','nemo','cdex','detector','background']),
 'cosmologia':(1,['cosmolog','planck','sum of neutrino masses','big bang nucleosynthesis','dark matter','cmb']),
}
ap=argparse.ArgumentParser(); ap.add_argument('--top',type=int,default=40)
ap.add_argument('--csv',default='dados/citacoes/dados_citacoes.csv'); a=ap.parse_args()
rows=list(csv.DictReader(open(a.csv,encoding='utf-8')))
for r in rows:
    txt=((r['titulo'] or '')+' '+(r['raw'] or '')).lower()
    eixos=[];score=0
    for nome,(peso,kws) in EIXOS.items():
        if any(k in txt for k in kws): eixos.append(nome); score+=peso
    r['eixos']=';'.join(eixos); r['score_tema']=score
    r['nucleo']='SIM' if any(e in eixos for e in ('majorana_natureza','0nubb','violacao_numero_leptonico','pmns_cp','seesaw_massa')) else 'NAO'
cols=list(rows[0].keys())
with open('dados/citacoes/dados_citacoes_tema.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=cols);w.writeheader();[w.writerow(r) for r in rows]
# exclui duplicatas por inspire_id: senao a shortlist lista o mesmo artigo duas vezes
nuc=[r for r in rows if r['nucleo']=='SIM' and str(r['citacoes']).isdigit()
     and not (r.get('duplicata_de') or '').strip()]
nuc.sort(key=lambda r:(-int(r['citacoes'])))
with open('dados/shortlist/shortlist_leitura.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=cols);w.writeheader();[w.writerow(r) for r in nuc[:a.top]]
c=collections.Counter(e for r in rows for e in r['eixos'].split(';') if e)
print('classificadas:',len(rows),'| no nucleo tematico:',len(nuc))
print('por eixo:',dict(c.most_common()))
print(f'\nTOP {min(a.top,len(nuc))} para leitura (dados/shortlist/shortlist_leitura.csv):')
for r in nuc[:a.top]:
    print(f"  {r['citacoes']:>6}  {r['ano_inspire'] or r['ano_ref']}  {(r['titulo'] or '')[:70]}  [{r['eixos']}]")
