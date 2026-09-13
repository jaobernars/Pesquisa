# -*- coding: utf-8 -*-
"""
Graficos tempo x citacoes do mapeamento de referencias das duas reviews
(Agostini et al., RMP "Toward the discovery of matter creation with 0nubb decay"
 e Gonzalez-Garcia et al., PDG "14. Neutrino Masses, Mixing, and Oscillations").

Entrada : dados/citacoes/dados_citacoes.csv   (gerado por scripts/tema/consolidar.py)
Saida   : gráficos/*.png  e  gráficos/*.pdf  (300 dpi, prontos para relatorio)

Uso: python3 scripts/saida/grafico_citacoes.py [--min-cit 0] [--sem-auto]
"""
import csv, argparse, os, statistics, collections
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, MultipleLocator

# --- parametros visuais -------------------------------------------------------
# Paleta Okabe-Ito (segura para daltonismo; separacao verificada para deuteranopia
# e protanopia). Identidade tambem redundante em marcador, nunca so na cor.
AZUL, LARANJA, VERDE, CINZA = '#0072B2', '#D55E00', '#009E73', '#6B6B6B'
TINTA, TINTA2 = '#1A1A1A', '#5A5A5A'
FONTE_ESTILO = {
    'AGOSTINI':                 dict(cor=AZUL,    marcador='o', rotulo='Agostini et al. (RMP, 0νββ)'),
    'GONZALEZ-GARCIA':          dict(cor=LARANJA, marcador='^', rotulo='Gonzalez-Garcia et al. (PDG, oscilações)'),
    'AGOSTINI;GONZALEZ-GARCIA': dict(cor=VERDE,   marcador='s', rotulo='Citado pelas duas reviews'),
}
plt.rcParams.update({
    'figure.dpi': 110, 'savefig.dpi': 300, 'savefig.bbox': 'tight',
    'font.size': 10, 'axes.titlesize': 12, 'axes.labelsize': 10,
    'axes.edgecolor': '#BFBFBF', 'axes.linewidth': 0.8, 'axes.labelcolor': TINTA,
    'axes.spines.top': False, 'axes.spines.right': False,
    'xtick.color': TINTA2, 'ytick.color': TINTA2,
    'grid.color': '#E2E2E2', 'grid.linewidth': 0.7,
    'legend.frameon': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})

COBERTURA = ''   # preenchido em main(): avisa que a amostra e parcial

def subtitulo(ax):
    pass  # a nota de cobertura vai no rodape, montado em salvar()

def salvar(fig, nome, nota=None):
    import textwrap
    if nota is None:
        nota = 'Fonte: INSPIRE-HEP.' + (' ' + COBERTURA if COBERTURA else '')
    fig.text(0.005, -0.02, '\n'.join(textwrap.wrap(nota, 130)),
             fontsize=8, color=TINTA2, va='top')
    os.makedirs('gráficos', exist_ok=True)
    for ext in ('png', 'pdf'):
        fig.savefig(f'gráficos/{nome}.{ext}')
    plt.close(fig)
    print('  ->', f'gráficos/{nome}.png/.pdf')

def carregar(caminho, campo_cit):
    linhas = []
    for r in csv.DictReader(open(caminho, encoding='utf-8')):
        ano = (r['ano_inspire'] or r['ano_ref']).strip()
        cit = (r[campo_cit] or '').strip()
        if not ano.isdigit() or not cit.isdigit():
            continue
        if (r.get('duplicata_de') or '').strip():
            continue   # mesmo inspire_id ja contabilizado em outro uid
        r['_ano'], r['_cit'] = int(ano), int(cit)
        r['_idade'] = max(2026 - r['_ano'], 1)
        r['_taxa'] = r['_cit'] / r['_idade']
        linhas.append(r)
    return linhas


def _rotular_extremos(ax, pontos, chave_y, n=6):
    """Rotula so os n extremos, alternando o deslocamento para reduzir colisao."""
    top = sorted(pontos, key=lambda x: -chave_y(x))[:n]
    xs = [r['_ano'] for r in top]
    xmin, xmax = min(xs), max(xs)
    for i, r in enumerate(top):
        nome = (r['primeiro_autor'] or r['autor_ref']).split(',')[0][:16]
        perto_da_borda = (xmax - r['_ano']) < 0.12 * max(xmax - xmin, 1)
        dx, ha = (-7, 'right') if perto_da_borda else (7, 'left')
        dy = (14, -14, 26, -26, 38, -38)[i % 6]
        ax.annotate(f"{nome} {r['_ano']}", (r['_ano'], chave_y(r)),
                    textcoords='offset points', xytext=(dx, dy), ha=ha,
                    fontsize=7.5, color=TINTA2, zorder=5,
                    arrowprops=dict(arrowstyle='-', lw=0.6, color='#B8B8B8',
                                    shrinkA=0, shrinkB=3))

# --- 1. dispersao ano x citacoes ---------------------------------------------
def fig_dispersao(d, campo_cit):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_axisbelow(True); ax.grid(True, axis='both', alpha=0.9)
    for chave, est in FONTE_ESTILO.items():
        g = [r for r in d if r['fontes'] == chave]
        if not g: continue
        ax.scatter([r['_ano'] for r in g], [max(r['_cit'], 0.5) for r in g],
                   s=26, c=est['cor'], marker=est['marcador'], alpha=0.62,
                   linewidths=0.6, edgecolors='white', label=f"{est['rotulo']} (n={len(g)})", zorder=3)
    ax.set_yscale('symlog', linthresh=1)
    ax.set_xlabel('Ano do trabalho (earliest_date, INSPIRE-HEP)')
    ax.set_ylabel('Citações (escala log)')
    ax.set_title('Referências das duas reviews: idade × impacto de citação', loc='left', color=TINTA)
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_formatter(ScalarFormatter())
    _rotular_extremos(ax, d, lambda r: r['_cit'], n=6)
    ax.legend(loc='upper left', fontsize=8.5)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    salvar(fig, '01_dispersao_ano_citacoes')

# --- 2. volume de referencias por ano ----------------------------------------
def fig_volume(d):
    c = collections.Counter(r['_ano'] for r in d)
    anos = sorted(c)
    fig, ax = plt.subplots(figsize=(10, 4.2))
    ax.set_axisbelow(True); ax.grid(True, axis='y', alpha=0.9)
    ax.bar(anos, [c[a] for a in anos], color=AZUL, width=0.85, linewidth=0)
    ax.set_xlabel('Ano'); ax.set_ylabel('Nº de referências citadas')
    ax.set_title('Perfil temporal do corpus: quantas referências cada ano fornece', loc='left', color=TINTA)
    ax.xaxis.set_major_locator(MultipleLocator(10))
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    salvar(fig, '02_referencias_por_ano')

# --- 3. mediana de citacoes por decada ---------------------------------------
def fig_decadas(d):
    dec = collections.defaultdict(list)
    for r in d: dec[r['_ano'] // 10 * 10].append(r['_cit'])
    ks = sorted(dec)
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.set_axisbelow(True); ax.grid(True, axis='y', alpha=0.9)
    bp = ax.boxplot([dec[k] for k in ks], positions=range(len(ks)), widths=0.6,
                    showfliers=False, patch_artist=True,
                    medianprops=dict(color=LARANJA, linewidth=1.8),
                    boxprops=dict(facecolor='#DCE9F5', edgecolor=CINZA, linewidth=0.8),
                    whiskerprops=dict(color=CINZA, linewidth=0.8),
                    capprops=dict(color=CINZA, linewidth=0.8))
    ax.set_yscale('symlog', linthresh=1)
    ax.set_xticks(range(len(ks))); ax.set_xticklabels([f"{k}s" for k in ks])
    for i, k in enumerate(ks):   # coordenadas de eixo: nao cai fora da area visivel no log
        ax.annotate(f"n={len(dec[k])}", (i, 0.015), xycoords=('data', 'axes fraction'),
                    ha='center', fontsize=7.5, color=TINTA2)
    ax.set_xlabel('Década'); ax.set_ylabel('Citações (escala log)')
    ax.set_title('Distribuição de citações por década (caixa: quartis; linha: mediana)', loc='left', color=TINTA)
    ax.yaxis.set_major_formatter(ScalarFormatter())
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    salvar(fig, '03_citacoes_por_decada')

# --- 4. taxa de citacao (citacoes/ano) x ano ---------------------------------
def fig_taxa(d):
    fig, ax = plt.subplots(figsize=(10, 5.4))
    ax.set_axisbelow(True); ax.grid(True, alpha=0.9)
    for chave, est in FONTE_ESTILO.items():
        g = [r for r in d if r['fontes'] == chave]
        if not g: continue
        ax.scatter([r['_ano'] for r in g], [r['_taxa'] for r in g], s=24, c=est['cor'],
                   marker=est['marcador'], alpha=0.6, linewidths=0.6, edgecolors='white',
                   label=est['rotulo'], zorder=3)
    ax.set_yscale('symlog', linthresh=1)
    ax.set_xlabel('Ano'); ax.set_ylabel('Citações por ano desde a publicação')
    ax.set_title('Taxa de citação: separa clássicos antigos de trabalhos recentes de alto impacto',
                 loc='left', color=TINTA)
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_formatter(ScalarFormatter())
    _rotular_extremos(ax, d, lambda r: r['_taxa'], n=6)
    ax.legend(loc='upper left', fontsize=8.5)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    salvar(fig, '04_taxa_citacao_por_ano')

# --- 5. top 30 mais citados ---------------------------------------------------
def fig_top(d, n=30):
    top = sorted(d, key=lambda r: -r['_cit'])[:n][::-1]
    fig, ax = plt.subplots(figsize=(10, 0.32 * n + 1.6))
    ax.set_axisbelow(True); ax.grid(True, axis='x', alpha=0.9)
    cores = [FONTE_ESTILO.get(r['fontes'], {}).get('cor', CINZA) for r in top]
    y = range(len(top))
    ax.barh(y, [r['_cit'] for r in top], color=cores, height=0.68, linewidth=0)
    ax.set_yticks(y)
    import textwrap as _tw
    ax.set_yticklabels([f"{(r['primeiro_autor'] or r['autor_ref']).split(',')[0][:20]} {r['_ano']} — "
                        f"{_tw.shorten(r['titulo'] or '(sem título)', width=52, placeholder='…')}"
                        for r in top], fontsize=7.5)
    from matplotlib.lines import Line2D
    presentes = [k for k in FONTE_ESTILO if any(r['fontes'] == k for r in top)]
    ax.legend(handles=[Line2D([], [], marker='s', linestyle='none', markersize=7,
                              color=FONTE_ESTILO[k]['cor'], label=FONTE_ESTILO[k]['rotulo'])
                       for k in presentes], loc='lower right', fontsize=8.5)
    for i, r in enumerate(top):
        ax.annotate(f"{r['_cit']:,}".replace(',', '.'), (r['_cit'], i), xytext=(4, 0),
                    textcoords='offset points', va='center', fontsize=7.5, color=TINTA2)
    ax.set_xlabel('Citações'); ax.margins(x=0.12)
    ax.set_title(f'As {n} referências mais citadas do corpus', loc='left', color=TINTA)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    subtitulo(ax)
    salvar(fig, '05_top30_mais_citados')

# --- 6. referencias ligadas ao objetivo da IC ---------------------------------
def fig_ic(caminho='dados/ic/referencias_ic.csv'):
    if not os.path.exists(caminho):
        print('  (sem', caminho, '- rode scripts/tema/refs_ic.py para gerar a Figura 6)')
        return
    d = [dict(r, _ano=int(r['ano']), _cit=int(r['citacoes']))
         for r in csv.DictReader(open(caminho, encoding='utf-8')) if r['citacoes'].isdigit()]
    estilo = {'Formalismo': dict(cor=AZUL, marcador='o', rotulo='Formalismo'),
              'Direta': dict(cor=LARANJA, marcador='^', rotulo='Diretamente correlacionada')}
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_axisbelow(True); ax.grid(True, axis='both', alpha=0.9)
    for tipo, est in estilo.items():
        g = [r for r in d if r['tipo'] == tipo]
        ax.scatter([r['_ano'] for r in g], [r['_cit'] for r in g], s=30, c=est['cor'], marker=est['marcador'],
                   alpha=0.75, linewidths=0.6, edgecolors='white', label=f"{est['rotulo']} (n={len(g)})", zorder=3)
    ax.set_yscale('log')
    ax.set_xlabel('Ano do trabalho (earliest_date, INSPIRE-HEP)')
    ax.set_ylabel('Citações (escala log)')
    ax.set_title('Referências ligadas ao objetivo da IC: ano × impacto de citação', loc='left', color=TINTA)
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_formatter(ScalarFormatter())
    # posicoes fixas por ordem de citacao: a alternancia automatica faz Mohapatra cruzar Kobayashi
    posicoes = [(-10, 0, 'right'), (-8, 10, 'right'), (-8, 12, 'right'), (-8, 4, 'right'), (10, 12, 'left'), (-6, 16, 'right')]
    for r, (dx, dy, ha) in zip(sorted(d, key=lambda r: -r['_cit']), posicoes):
        ax.annotate(f"{r['primeiro_autor']} {r['_ano']}", (r['_ano'], r['_cit']), textcoords='offset points',
                    xytext=(dx, dy), ha=ha, va='center', fontsize=7.5, color=TINTA2, zorder=5,
                    arrowprops=dict(arrowstyle='-', lw=0.6, color='#B8B8B8', shrinkA=0, shrinkB=3))
    ax.legend(loc='upper left', fontsize=8.5)
    salvar(fig, '06_refs_ic', nota=f'Fonte: INSPIRE-HEP. {len(d)} referências das duas reviews selecionadas por '
                                   f'relação com o objetivo da IC (dados/ic/referencias_ic.csv); as sem registro no '
                                   f'INSPIRE ficam de fora.')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--csv', default='dados/citacoes/dados_citacoes.csv')
    ap.add_argument('--sem-auto', action='store_true', help='usar citações sem autocitação')
    ap.add_argument('--min-cit', type=int, default=0)
    a = ap.parse_args()
    campo = 'citacoes_sem_auto' if a.sem_auto else 'citacoes'
    d = [r for r in carregar(a.csv, campo) if r['_cit'] >= a.min_cit]
    if not d:
        raise SystemExit('Sem dados: rode scripts/tema/consolidar.py depois de concluir os blocos.')
    global COBERTURA
    todas = list(csv.DictReader(open(a.csv, encoding='utf-8')))
    total = len(todas)
    pend = sum(1 for r in todas if r['status'] == 'PENDENTE')
    naoenc = sum(1 for r in todas if r['status'] == 'NAO_ENCONTRADO')
    dup = sum(1 for r in todas if (r.get('duplicata_de') or '').strip())
    if pend:
        COBERTURA = (f'AMOSTRA PARCIAL: {len(d)} de {total} referências com citação recuperada; '
                     f'{pend} ainda não foram coletadas. A coleta prioriza as referências com arXiv, '
                     f'então os trabalhos anteriores a ~1991 estão sub-representados neste gráfico.')
    else:
        COBERTURA = (f'Coleta completa: {total} referências únicas extraídas das duas reviews, '
                     f'{len(d)} com citação recuperada no INSPIRE-HEP. Ficam de fora {naoenc} sem '
                     f'registro na base (teses, atas, talks, bancos de dados e revistas de química '
                     f'e engenharia) e {dup} duplicatas — o mesmo trabalho citado pelas duas reviews, '
                     f'contado uma única vez.')
    cits = [r['_cit'] for r in d]
    print(f'{len(d)} referências | mediana {statistics.median(cits):.0f} | '
          f'média {statistics.mean(cits):.0f} | máx {max(cits)}')
    fig_dispersao(d, campo); fig_volume(d); fig_decadas(d); fig_taxa(d); fig_top(d); fig_ic()

if __name__ == '__main__':
    main()
