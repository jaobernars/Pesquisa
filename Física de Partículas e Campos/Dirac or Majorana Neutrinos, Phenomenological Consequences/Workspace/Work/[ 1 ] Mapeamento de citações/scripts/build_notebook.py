# -*- coding: utf-8 -*-
"""Monta o notebook Mapeamento_Citacoes.ipynb (analise final do mapeamento)."""
import nbformat as nbf

nb = nbf.v4.new_notebook()
C = []
def md(t): C.append(nbf.v4.new_markdown_cell(t.strip('\n')))
def code(t): C.append(nbf.v4.new_code_cell(t.strip('\n')))

# ----------------------------------------------------------------- capa
md(r"""
# Mapeamento de citações das referências de duas reviews de física de neutrinos

**Iniciação científica:** *Dirac or Majorana Neutrinos — Phenomenological Consequences*
**Autor:** João · Bacharelado em Física, Universidade Estadual de Londrina (UEL)
**Base de citações:** [INSPIRE-HEP](https://inspirehep.net) · coleta entre 6 e 12 de setembro de 2026

---

## O que este documento é

Este notebook fecha a tarefa proposta pelo orientador: pegar **todas** as referências de duas
reviews de referência da área, levantar a contagem de citações de cada uma num banco de citações
e mapear a relação entre idade e impacto dos trabalhos, para então selecionar os mais citados que
dialogam com o projeto de IC.

As duas reviews são:

1. **AGOSTINI, M.; BENATO, G.; DETWILER, J. A.; MENÉNDEZ, J.; VISSANI, F.** Toward the discovery of
   matter creation with neutrinoless ββ decay. **Reviews of Modern Physics**, v. 95, n. 2, p. 025002, 2023.
2. **GONZALEZ-GARCIA, M. C.; YOKOYAMA, M.** *et al.* 14. Neutrino Masses, Mixing, and Oscillations.
   In: **Review of Particle Physics** (Particle Data Group), 2025.

## Como os números foram obtidos

| Etapa | O que foi feito |
|---|---|
| Extração | Parsing do texto das duas bibliografias em PDF, com reconstrução das entradas quebradas por coluna e página |
| Deduplicação | Chave por arXiv ID → DOI → título; depois, deduplicação definitiva pelo `inspire_id` devolvido pela API |
| Identificação | Cadeia `arxiv:` → `doi:` → `j+<revista>,<vol>,<pág>` → `t+<título>` → `a+<autor>+and+date+<ano>` |
| Validação | Cada registro exigiu **duas âncoras independentes**: ano compatível **e** título ou coordenada de journal batendo com o texto da bibliografia |
| Auditoria | Uma linha por bloco reconferida manualmente, fora do processo automático — 47 conferências, todas exatas |

O trabalho foi dividido em 51 blocos de 20 buscas. Uma referência = uma consulta à API: consultas
em lote foram testadas e **reprovadas**, porque a partir de cinco identificadores o INSPIRE passa a
devolver registros sem relação com a query.

### Cobertura

| | |
|---|---|
| Referências brutas extraídas | 996 |
| **Referências únicas** | **970** |
| Com citação recuperada | **888** (91,5%) |
| Sem registro no INSPIRE | 62 (6,4%) |
| Duplicatas entre as duas reviews | 20 |

As 62 ausências não são falhas de busca: são teses de doutorado, atas de workshop, apresentações
em conferência, bancos de dados nucleares (ENSDF, XUNDL) e artigos em revistas de química e
engenharia — categorias que o INSPIRE-HEP não indexa. Onze casos foram reconferidos à mão, um
deles duas vezes: o artigo de Walz *et al.* na **Nature** 526, 406 (2015), sobre decaimento duplo
gama, realmente não tem registro na base.

### Uma advertência sobre o eixo do tempo

O INSPIRE devolve `earliest_date`, que é a data do **preprint**, não a da publicação. Para um
trabalho dos anos 2010 a diferença é de meses; para alguns é de dois anos. **Os gráficos usam
`earliest_date`** (é a data que mede há quanto tempo o trabalho está disponível para ser citado);
**as tabelas de referência usam o ano de publicação no periódico**, como manda a ABNT. Quando os
dois divergem, a tabela registra os dois.
""")

code(r"""
import csv, collections, statistics, textwrap
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, MultipleLocator
from IPython.display import Markdown, display

# Paleta Okabe-Ito: segura para deuteranopia e protanopia. A identidade tambem e
# redundante no marcador, nunca so na cor.
AZUL, LARANJA, VERDE, CINZA = '#0072B2', '#D55E00', '#009E73', '#6B6B6B'
TINTA, TINTA2 = '#1A1A1A', '#5A5A5A'
ESTILO = {
    'AGOSTINI':                 dict(cor=AZUL,    marcador='o', rotulo='Agostini et al. (RMP, 0νββ)'),
    'GONZALEZ-GARCIA':          dict(cor=LARANJA, marcador='^', rotulo='Gonzalez-Garcia et al. (PDG, oscilações)'),
    'AGOSTINI;GONZALEZ-GARCIA': dict(cor=VERDE,   marcador='s', rotulo='Citado pelas duas reviews'),
}
plt.rcParams.update({
    'figure.dpi': 110, 'font.size': 10, 'axes.titlesize': 12, 'axes.labelsize': 10,
    'axes.edgecolor': '#BFBFBF', 'axes.linewidth': .8, 'axes.labelcolor': TINTA,
    'axes.spines.top': False, 'axes.spines.right': False,
    'xtick.color': TINTA2, 'ytick.color': TINTA2,
    'grid.color': '#E2E2E2', 'grid.linewidth': .7, 'legend.frameon': False,
    'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
ANO_REF = 2026   # ano de referencia para calcular idade e taxa de citacao

def carregar(caminho='dados/dados_citacoes.csv', campo='citacoes'):
    '''Le a tabela consolidada, descarta duplicatas por inspire_id e o que nao tem citacao.'''
    fora = []
    for r in csv.DictReader(open(caminho, encoding='utf-8')):
        ano, cit = (r['ano_inspire'] or r['ano_ref']).strip(), (r[campo] or '').strip()
        if not ano.isdigit() or not cit.isdigit():   continue
        if (r.get('duplicata_de') or '').strip():    continue   # ja contabilizado em outro uid
        r['ano'], r['cit'] = int(ano), int(cit)
        r['idade'] = max(ANO_REF - r['ano'], 1)
        r['taxa']  = r['cit'] / r['idade']
        fora.append(r)
    return fora

D = carregar()
print(f'{len(D)} referências na análise')
print(f"mediana {statistics.median(c['cit'] for c in D):.0f} · "
      f"média {statistics.mean(c['cit'] for c in D):.0f} · "
      f"máximo {max(c['cit'] for c in D)}")
print('por fonte:', dict(collections.Counter(r['fontes'] for r in D)))
""")

md(r"""
A mediana de 124 citações contra uma média de 457 já diz a coisa mais importante sobre este corpus:
a distribuição é fortemente assimétrica. Meia dúzia de trabalhos concentra uma fração enorme das
citações, e a maior parte das referências vive na casa das dezenas. Qualquer leitura por média
engana aqui; todos os gráficos que seguem usam escala logarítmica no eixo das citações por causa
disso.
""")

# ----------------------------------------------------------------- fig 1
md(r"""
---
## Figura 1 — Idade × impacto de citação

A pergunta do orientador — *quais são os artigos mais novos e suas citações, e os mais velhos e
suas citações* — é literalmente este gráfico. Cada ponto é uma referência: a posição horizontal é
quando o trabalho apareceu, a vertical é quantas vezes foi citado desde então.
""")

code(r"""
def rotular(ax, pontos, chave, n=6):
    '''Rotula apenas os n extremos, com linha de chamada e deslocamento alternado.'''
    top = sorted(pontos, key=lambda r: -chave(r))[:n]
    xs = [r['ano'] for r in top]; xmin, xmax = min(xs), max(xs)
    for i, r in enumerate(top):
        nome = (r['primeiro_autor'] or r['autor_ref']).split(',')[0][:16]
        borda = (xmax - r['ano']) < .12 * max(xmax - xmin, 1)
        dx, ha = (-7, 'right') if borda else (7, 'left')
        ax.annotate(f"{nome} {r['ano']}", (r['ano'], chave(r)), textcoords='offset points',
                    xytext=(dx, (14, -14, 26, -26, 38, -38)[i % 6]), ha=ha, fontsize=7.5,
                    color=TINTA2, zorder=5,
                    arrowprops=dict(arrowstyle='-', lw=.6, color='#B8B8B8', shrinkA=0, shrinkB=3))

fig, ax = plt.subplots(figsize=(11, 6.4))
ax.set_axisbelow(True); ax.grid(True, alpha=.9)
for chave, e in ESTILO.items():
    g = [r for r in D if r['fontes'] == chave]
    ax.scatter([r['ano'] for r in g], [r['cit'] for r in g], s=26, c=e['cor'],
               marker=e['marcador'], alpha=.62, linewidths=.6, edgecolors='white',
               label=f"{e['rotulo']} (n={len(g)})", zorder=3)
ax.set_yscale('log')
ax.set_xlabel('Ano do trabalho (earliest_date, INSPIRE-HEP)')
ax.set_ylabel('Citações (escala log)')
ax.set_title('Referências das duas reviews: idade × impacto de citação', loc='left', color=TINTA)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_major_formatter(ScalarFormatter())
rotular(ax, D, lambda r: r['cit'])
ax.legend(loc='lower left', fontsize=8.5)
plt.show()
""")

md(r"""
**O que este gráfico mostra.**

Não existe correlação simples entre idade e citação. Se houvesse, os pontos formariam uma faixa
descendente da esquerda para a direita — trabalhos velhos com muitas citações, novos com poucas. O
que se vê é uma nuvem espalhada em três ordens de magnitude em qualquer fatia de tempo depois de
1960: em 1980 há trabalhos com 4.000 citações e trabalhos com 20.

A leitura correta é outra: o eixo vertical separa **o que virou infraestrutura conceitual da área**
do resto. Os pontos no alto, entre 4.000 e 13.000 citações, são quase todos anteriores a 1990 e são
os artigos que fundaram os formalismos — Kobayashi–Maskawa, Cabibbo, Mohapatra–Senjanović,
Wolfenstein, Minkowski, Maki–Nakagawa–Sakata. Nenhum deles é sobre decaimento duplo beta; são sobre
mistura de sabores, massa e violação de simetrias, ou seja, exatamente a camada teórica de que o
0νββ depende.

O ponto isolado no topo à direita é o **Planck 2018**, com 23.108 citações — 2,5 vezes o segundo
colocado. Não é física de neutrinos: é o vínculo cosmológico sobre Σmν que as duas reviews usam
como entrada externa. Vale decidir com o orientador se ele entra na análise final ou é tratado à
parte, porque sozinho ele comprime visualmente todo o resto.

A densidade da nuvem cresce muito depois de 2005, e isso é uma propriedade da **bibliografia**, não
da física: reviews citam preferencialmente literatura recente. A Figura 2 mostra isso de frente.
""")

# ----------------------------------------------------------------- fig 2
md(r"""
---
## Figura 2 — Perfil temporal do corpus

Quantas referências cada ano fornece às duas reviews. É o gráfico que descreve o *viés de recência*
da bibliografia.
""")

code(r"""
c = collections.Counter(r['ano'] for r in D)
anos = sorted(c)
fig, ax = plt.subplots(figsize=(11, 4.2))
ax.set_axisbelow(True); ax.grid(True, axis='y', alpha=.9)
ax.bar(anos, [c[a] for a in anos], color=AZUL, width=.85, linewidth=0)
ax.set_xlabel('Ano'); ax.set_ylabel('Nº de referências citadas')
ax.set_title('Perfil temporal do corpus: quantas referências cada ano fornece', loc='left', color=TINTA)
ax.xaxis.set_major_locator(MultipleLocator(10))
plt.show()

dec = collections.Counter(r['ano'] // 10 * 10 for r in D)
display(Markdown('| Década | Referências | % do corpus |\n|---|---|---|\n' + '\n'.join(
    f'| {d}s | {dec[d]} | {100*dec[d]/len(D):.1f}% |' for d in sorted(dec))))
""")

md(r"""
**O que este gráfico mostra.**

Quase metade do corpus é dos anos 2010 em diante. As décadas de 1930 a 1960 — que contêm Majorana,
Fermi, Racah, Furry, Pauli, Pontecorvo, Lee e Yang — somam pouco mais de 6% das referências.

Isso tem uma consequência prática para a sua IC. As duas reviews são mapas do **estado atual** do
campo, e por isso citam sobretudo resultados experimentais recentes e cálculos de estrutura
nuclear. A camada de formalismo — férmions de Majorana, matriz PMNS estendida com fases de CP,
massa efetiva de Majorana — aparece nelas por referência a meia dúzia de artigos fundadores, não
por uma literatura extensa. Se a sua bibliografia teórica se limitar ao que estas duas reviews
citam, ela vai herdar esse desequilíbrio.
""")

# ----------------------------------------------------------------- fig 3
md(r"""
---
## Figura 3 — Distribuição de citações por década

O gráfico anterior conta quantos trabalhos cada década fornece. Este mostra **como as citações se
distribuem dentro** de cada década: a caixa vai do primeiro ao terceiro quartil, a linha laranja é
a mediana, os bigodes alcançam 1,5 vez a amplitude interquartil.
""")

code(r"""
por_dec = collections.defaultdict(list)
for r in D: por_dec[r['ano'] // 10 * 10].append(r['cit'])
ks = sorted(por_dec)
fig, ax = plt.subplots(figsize=(11, 4.8))
ax.set_axisbelow(True); ax.grid(True, axis='y', alpha=.9)
ax.boxplot([por_dec[k] for k in ks], positions=range(len(ks)), widths=.6, showfliers=False,
           patch_artist=True, medianprops=dict(color=LARANJA, linewidth=1.8),
           boxprops=dict(facecolor='#DCE9F5', edgecolor=CINZA, linewidth=.8),
           whiskerprops=dict(color=CINZA, linewidth=.8), capprops=dict(color=CINZA, linewidth=.8))
ax.set_yscale('log')
ax.set_xticks(range(len(ks))); ax.set_xticklabels([f'{k}s' for k in ks])
for i, k in enumerate(ks):   # em coordenadas de eixo, para nao cair fora da area visivel
    ax.annotate(f'n={len(por_dec[k])}', (i, .015), xycoords=('data', 'axes fraction'),
                ha='center', fontsize=7.5, color=TINTA2)
ax.set_xlabel('Década'); ax.set_ylabel('Citações (escala log)')
ax.set_title('Distribuição de citações por década (caixa: quartis · linha: mediana)',
             loc='left', color=TINTA)
ax.yaxis.set_major_formatter(ScalarFormatter())
plt.show()

display(Markdown('| Década | n | Mediana | 3º quartil | Máximo |\n|---|---|---|---|---|\n' + '\n'.join(
    f'| {k}s | {len(por_dec[k])} | {statistics.median(por_dec[k]):.0f} | '
    f'{sorted(por_dec[k])[int(.75*(len(por_dec[k])-1))]} | {max(por_dec[k])} |' for k in ks)))
""")

md(r"""
**O que este gráfico mostra.**

As medianas desenham uma curva com pico nos anos 1970 — 1.690 citações — e caem monotonicamente
depois: 342 nos anos 1980, 151 nos 1990, 98 nos 2010, 53 nos 2020. Parte dessa queda é trivial: um
artigo de 2020 teve cinco anos para acumular citações, um de 1970 teve cinquenta e cinco. É por
isso que a Figura 4 existe.

O que **não** é trivial é a altura das caixas, que mede a dispersão interna de cada década. A razão
entre terceiro e primeiro quartil vai de **1,6×** nos anos 1930 a **20,6×** nos anos 1960 e **13,2×**
nos 1970, e depois se estabiliza em torno de **5×** de 1980 em diante.

A caixa curta dos anos 1930 com *n* = 12 diz que uma review só volta tão atrás para buscar o que
virou fundamento: tudo que ela cita daquela década é canônico, então a dispersão é pequena. As
caixas altíssimas dos anos 1960 e 1970 são o oposto — ali convivem, na mesma bibliografia, o
Kobayashi–Maskawa com 12.896 citações e trabalhos de instrumentação da época com poucas dezenas. É
a década em que o campo estava se formando e a review precisa citar as duas coisas.

De 1980 em diante a dispersão se estabiliza e o *n* explode: 409 referências só dos anos 2010. A
partir daí a bibliografia deixa de ser seletiva e passa a ser um retrato da literatura corrente.
""")

# ----------------------------------------------------------------- fig 4
md(r"""
---
## Figura 4 — Taxa de citação: citações por ano desde a publicação

Este é o gráfico que corrige o efeito de idade. Dividir as citações pelos anos desde a publicação
põe no mesmo plano um clássico que acumulou devagar por cinco décadas e um trabalho recente de
altíssimo impacto.
""")

code(r"""
fig, ax = plt.subplots(figsize=(11, 5.6))
ax.set_axisbelow(True); ax.grid(True, alpha=.9)
for chave, e in ESTILO.items():
    g = [r for r in D if r['fontes'] == chave]
    ax.scatter([r['ano'] for r in g], [r['taxa'] for r in g], s=24, c=e['cor'],
               marker=e['marcador'], alpha=.6, linewidths=.6, edgecolors='white',
               label=e['rotulo'], zorder=3)
ax.set_yscale('log')
ax.set_xlabel('Ano'); ax.set_ylabel(f'Citações por ano desde a publicação (ref. {ANO_REF})')
ax.set_title('Taxa de citação: separa clássicos antigos de recentes de alto impacto',
             loc='left', color=TINTA)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_major_formatter(ScalarFormatter())
rotular(ax, D, lambda r: r['taxa'])
ax.legend(loc='lower left', fontsize=8.5)
plt.show()

print('Maiores taxas de citação (citações/ano):')
for r in sorted(D, key=lambda z: -z['taxa'])[:10]:
    print(f"  {r['taxa']:7.1f}/ano · {r['cit']:>6} cit. em {r['idade']:>2} anos · "
          f"{r['ano']} · {(r['titulo'] or '')[:58]}")
""")

md(r"""
**O que este gráfico mostra.**

Compare dois casos concretos do corpus. O Super-Kamiokande de 1998 tem 9.245 citações acumuladas em
28 anos, cerca de 330 por ano. O Planck 2018 tem 23.108 em 8 anos, cerca de 2.900 por ano. Em
citações absolutas o Planck lidera por um fator 2,5; em taxa, por um fator 9. São dois regimes
diferentes de influência, e o gráfico de citações absolutas esconde a diferença.

O padrão geral é uma nuvem aproximadamente horizontal, com a borda superior subindo devagar em
direção ao presente. Isso reflete o crescimento do volume de publicação em física de partículas:
um artigo de hoje é citado por uma comunidade maior do que a de 1970, então taxas altas são mais
fáceis de alcançar agora. Para comparar trabalhos de épocas distintas, **nenhuma das duas métricas
basta sozinha** — as duas juntas é que dizem algo.
""")

# ----------------------------------------------------------------- fig 5
md(r"""
---
## Figura 5 — As 30 referências mais citadas

A mesma informação da tabela ABNT que vem a seguir, em forma visual, com a cor indicando qual
review citou o trabalho.
""")

code(r"""
from matplotlib.lines import Line2D
top30 = sorted(D, key=lambda r: -r['cit'])[:30][::-1]
fig, ax = plt.subplots(figsize=(11, 10.4))
ax.set_axisbelow(True); ax.grid(True, axis='x', alpha=.9)
ax.barh(range(len(top30)), [r['cit'] for r in top30],
        color=[ESTILO.get(r['fontes'], {}).get('cor', CINZA) for r in top30], height=.68, linewidth=0)
ax.set_yticks(range(len(top30)))
ax.set_yticklabels([f"{(r['primeiro_autor'] or r['autor_ref']).split(',')[0][:20]} {r['ano']} — "
                    f"{textwrap.shorten(r['titulo'] or '(sem título)', 52, placeholder='…')}"
                    for r in top30], fontsize=7.5)
for i, r in enumerate(top30):
    ax.annotate(f"{r['cit']:,}".replace(',', '.'), (r['cit'], i), xytext=(4, 0),
                textcoords='offset points', va='center', fontsize=7.5, color=TINTA2)
ax.set_xlabel('Citações'); ax.margins(x=.12)
ax.set_title('As 30 referências mais citadas do corpus', loc='left', color=TINTA)
presentes = [k for k in ESTILO if any(r['fontes'] == k for r in top30)]
ax.legend(handles=[Line2D([], [], marker='s', linestyle='none', markersize=7,
                          color=ESTILO[k]['cor'], label=ESTILO[k]['rotulo']) for k in presentes],
          loc='lower right', fontsize=8.5)
plt.show()
""")

md(r"""
**O que este gráfico mostra.**

Contando por review: das 30 mais citadas, a maioria vem da bibliografia do Agostini (0νββ), mas os
trabalhos de **oscilação** dominam o topo. Só três das trinta tratam diretamente de decaimento
duplo beta sem neutrinos. As outras vinte e sete são sobre mistura de sabores, mecanismos de massa,
violação de CP, anomalias e assimetria bariônica.

Isso não diminui o 0νββ — mostra que ele é um campo **jovem e experimental**, cujas bases
conceituais foram estabelecidas por uma literatura mais antiga e mais citada. Os artigos verdes,
citados pelas duas reviews, são precisamente a ponte entre os dois mundos.
""")
nb['cells'] = C
nbf.write(nb, '/tmp/nb_parte1.ipynb')
print('parte 1:', len(C), 'celulas')
