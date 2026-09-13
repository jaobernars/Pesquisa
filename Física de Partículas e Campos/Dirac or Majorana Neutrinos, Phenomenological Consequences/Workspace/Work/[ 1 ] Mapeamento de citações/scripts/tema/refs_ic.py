# -*- coding: utf-8 -*-
"""Seleção manual das referências ligadas ao objetivo da IC (natureza Dirac vs Majorana,
matriz PMNS com fases de CP, massa efetiva m_bb, leptogênese e limites sobre m_bb).

Critério: título lido um a um contra os 5 objetivos específicos do README do projeto.
Ficam de fora instrumentação, background, 2vbb, cálculos individuais de elemento de matriz
nuclear, mecanismos alternativos de 0vbb (SUSY, left-right, operadores de EFT), oscilação
em matéria, anomalias estéreis e resultados de 0vbb superados pelo resultado final do mesmo
experimento.

Entrada: dados/citacoes/dados_citacoes.csv   Saída: dados/ic/referencias_ic.csv
Uso: python3 scripts/tema/refs_ic.py
"""
import csv, os, re

EIXOS = {
    1: ('Natureza do neutrino: Dirac, Majorana e quiralidade', 'Formalismo'),
    2: ('Mistura leptônica, matriz PMNS e fases de CP', 'Formalismo'),
    3: ('Geração de massa (seesaw) e violação do número leptônico', 'Formalismo'),
    4: ('Leptogênese e assimetria bariônica', 'Formalismo'),
    5: ('0νββ: formalismo da taxa e da massa efetiva', 'Formalismo'),
    6: ('Fenomenologia da massa efetiva m_ββ', 'Direta'),
    7: ('Revisões sobre 0νββ', 'Direta'),
    8: ('Limites experimentais sobre m_ββ e escala absoluta de massa', 'Direta'),
    9: ('Evidência de massa e parâmetros de oscilação', 'Direta'),
}

SELECAO = {
    1: ['U0465', 'U0482', 'U0483', 'U0485', 'U0514', 'U0520', 'U0521', 'U0524', 'U0519',
        'U0525', 'U0527', 'U0528', 'U0529', 'U0587', 'U0628', 'U0643', 'U0667', 'U0699',
        'U0173', 'U0206', 'U0956'],
    2: ['U0522', 'U0523', 'U0534', 'U0535', 'U0538', 'U0544', 'U0553', 'U0560', 'U0571',
        'U0578', 'U0577', 'U0585', 'U0599', 'U0053', 'U0059', 'U0085', 'U0099', 'U0107',
        'U0191'],
    3: ['U0511', 'U0645', 'U0567', 'U0001', 'U0573', 'U0574', 'U0580', 'U0579', 'U0586',
        'U0003', 'U0031', 'U0069', 'U0932', 'U0102', 'U0166', 'U0944', 'U0204'],
    4: ['U0548', 'U0970', 'U0603', 'U0608', 'U0636', 'U0010', 'U0711', 'U0205', 'U0222',
        'U0948', 'U0249', 'U0827', 'U0423', 'U0424'],
    5: ['U0478', 'U0480', 'U0487', 'U0494', 'U0531', 'U0549', 'U0554', 'U0593', 'U0600',
        'U0668', 'U0121', 'U0147', 'U0152', 'U0252', 'U0822', 'U0821', 'U0422'],
    6: ['U0023', 'U0032', 'U0048', 'U0063', 'U0686', 'U0071', 'U0111', 'U0715', 'U0149',
        'U0941', 'U0748', 'U0200', 'U0203', 'U0215', 'U0237', 'U0244', 'U0276', 'U0826',
        'U0348', 'U0376', 'U0377', 'U0406', 'U0426', 'U0431'],
    7: ['U0062', 'U0091', 'U0114', 'U0127', 'U0138', 'U0139', 'U0145', 'U0151', 'U0729',
        'U0174', 'U0181', 'U0201', 'U0947', 'U0221', 'U0312', 'U0315'],
    8: ['U0033', 'U0044', 'U0064', 'U0168', 'U0159', 'U0197', 'U0228', 'U0267', 'U0300',
        'U0335', 'U0965', 'U0412', 'U0411', 'U0416', 'U0418', 'U0434', 'U0449', 'U0451',
        'U0455'],
    9: ['U0017', 'U0030', 'U0051', 'U0140', 'U0188', 'U0353', 'U0401', 'U0389', 'U0447',
        'U0452'],
}

# o INSPIRE devolveu esses registros sem título, ou a bibliografia inverteu a ordem dos autores
TITULO = {'U0191': 'Non-unitarity of the leptonic mixing matrix: present bounds and future sensitivities'}
AUTOR = {'U0525': 'Radicati'}

def titulo_do_raw(raw):
    m = re.search(r'[“"]([^”"]+)[”"]', raw)
    return m.group(1).strip().rstrip(',') if m else raw[:120]

def sobrenome(nome):
    return re.sub(r'^(?:[A-Z]\.\s*-?)+\s*', '', nome.split(',')[0].strip())

base = {r['uid']: r for r in csv.DictReader(open('dados/citacoes/dados_citacoes.csv', encoding='utf-8'))}
vistos = set()
linhas = []
for n, uids in SELECAO.items():
    eixo, tipo = EIXOS[n]
    for u in uids:
        if u in vistos: raise SystemExit(f'{u} aparece em mais de um eixo')
        if u not in base: raise SystemExit(f'{u} não existe em dados_citacoes.csv')
        r = base[u]
        if (r['duplicata_de'] or '').strip(): raise SystemExit(f'{u} é duplicata de {r["duplicata_de"]}')
        vistos.add(u)
        linhas.append(dict(uid=u, eixo_num=n, eixo=eixo, tipo=tipo, fontes=r['fontes'],
                           ano=(r['ano_inspire'] or r['ano_ref']).strip(), citacoes=r['citacoes'],
                           primeiro_autor=AUTOR.get(u) or sobrenome(r['primeiro_autor'] or r['autor_ref']),
                           n_autores=r['n_autores'], journal=r['journal'],
                           titulo=TITULO.get(u) or r['titulo'] or titulo_do_raw(r['raw'])))

os.makedirs('dados/ic', exist_ok=True)
with open('dados/ic/referencias_ic.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(linhas[0].keys()))
    w.writeheader(); w.writerows(linhas)

sem = sum(1 for l in linhas if not l['citacoes'].isdigit())
print(f'{len(linhas)} referências selecionadas ({sem} sem registro no INSPIRE) -> dados/ic/referencias_ic.csv')
for n, (eixo, tipo) in EIXOS.items():
    print(f'  {n}. [{tipo}] {eixo}: {len(SELECAO[n])}')
