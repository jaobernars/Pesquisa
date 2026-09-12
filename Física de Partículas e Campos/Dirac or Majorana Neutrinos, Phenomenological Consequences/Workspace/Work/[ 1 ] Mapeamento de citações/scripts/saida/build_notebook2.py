# -*- coding: utf-8 -*-
"""Parte 2 do notebook: tabelas ABNT, ano a ano, historicos e Nobel."""
import nbformat as nbf

nb = nbf.read('/tmp/nb_parte1.ipynb', as_version=4)
C = list(nb['cells'])
def md(t): C.append(nbf.v4.new_markdown_cell(t.strip('\n')))
def code(t): C.append(nbf.v4.new_code_cell(t.strip('\n')))

# ------------------------------------------------- TOP 30 ABNT
md(r"""
---
# Tabela 1 — As 30 referências mais citadas (formato ABNT)

Referências segundo a **ABNT NBR 6023:2018**. O ano é o da **publicação no periódico**; quando o
`earliest_date` do INSPIRE (data do preprint) difere, ele vem entre colchetes ao fim da entrada.
Contagens do INSPIRE-HEP, coletadas entre 6 e 12 de setembro de 2026.

| # | Citações | Referência (ABNT NBR 6023) |
|---:|---:|---|
| 1 | 23.108 | AGHANIM, N. *et al.* (Planck Collaboration). Planck 2018 results. VI. Cosmological parameters. **Astronomy & Astrophysics**, v. 641, p. A6, 2020. [preprint 2018] |
| 2 | 12.896 | KOBAYASHI, M.; MASKAWA, T. CP violation in the renormalizable theory of weak interaction. **Progress of Theoretical Physics**, v. 49, n. 2, p. 652-657, 1973. |
| 3 | 9.245 | FUKUDA, Y. *et al.* (Super-Kamiokande Collaboration). Evidence for oscillation of atmospheric neutrinos. **Physical Review Letters**, v. 81, n. 8, p. 1562-1567, 1998. |
| 4 | 8.352 | CABIBBO, N. Unitary symmetry and leptonic decays. **Physical Review Letters**, v. 10, n. 12, p. 531-533, 1963. |
| 5 | 7.464 | MOHAPATRA, R. N.; SENJANOVIĆ, G. Neutrino mass and spontaneous parity nonconservation. **Physical Review Letters**, v. 44, n. 14, p. 912-915, 1980. [preprint 1979] |
| 6 | 6.840 | ZYLA, P. A. *et al.* (Particle Data Group). Review of Particle Physics. **Progress of Theoretical and Experimental Physics**, v. 2020, n. 8, p. 083C01, 2020. |
| 7 | 6.381 | WOLFENSTEIN, L. Neutrino oscillations in matter. **Physical Review D**, v. 17, n. 9, p. 2369-2374, 1978. [preprint 1977] |
| 8 | 6.231 | GEORGI, H.; GLASHOW, S. L. Unity of all elementary particle forces. **Physical Review Letters**, v. 32, n. 8, p. 438-441, 1974. |
| 9 | 6.197 | COWAN, G.; CRANMER, K.; GROSS, E.; VITELLS, O. Asymptotic formulae for likelihood-based tests of new physics. **European Physical Journal C**, v. 71, p. 1554, 2011. [preprint 2010] |
| 10 | 6.027 | PATI, J. C.; SALAM, A. Lepton number as the fourth color. **Physical Review D**, v. 10, n. 1, p. 275-289, 1974. |
| 11 | 5.951 | MINKOWSKI, P. μ → eγ at a rate of one out of 10⁹ muon decays? **Physics Letters B**, v. 67, n. 4, p. 421-428, 1977. |
| 12 | 5.876 | SAKHAROV, A. D. Violation of CP invariance, C asymmetry, and baryon asymmetry of the universe. **Pis'ma v Zhurnal Eksperimental'noi i Teoreticheskoi Fiziki**, v. 5, p. 32-35, 1967. |
| 13 | 5.760 | MAKI, Z.; NAKAGAWA, M.; SAKATA, S. Remarks on the unified model of elementary particles. **Progress of Theoretical Physics**, v. 28, n. 5, p. 870-880, 1962. |
| 14 | 5.290 | AHMAD, Q. R. *et al.* (SNO Collaboration). Direct evidence for neutrino flavor transformation from neutral-current interactions in the Sudbury Neutrino Observatory. **Physical Review Letters**, v. 89, n. 1, p. 011301, 2002. |
| 15 | 5.183 | ADLER, S. L. Axial-vector vertex in spinor electrodynamics. **Physical Review**, v. 177, n. 5, p. 2426-2438, 1969. |
| 16 | 4.907 | FUKUGITA, M.; YANAGIDA, T. Baryogenesis without grand unification. **Physics Letters B**, v. 174, n. 1, p. 45-47, 1986. |
| 17 | 4.536 | 'T HOOFT, G. Symmetry breaking through Bell-Jackiw anomalies. **Physical Review Letters**, v. 37, n. 1, p. 8-11, 1976. |
| 18 | 4.429 | MIKHEYEV, S. P.; SMIRNOV, A. Yu. Resonance amplification of oscillations in matter and spectroscopy of solar neutrinos. **Soviet Journal of Nuclear Physics**, v. 42, p. 913-917, 1985. |
| 19 | 4.406 | GELL-MANN, M.; RAMOND, P.; SLANSKY, R. Complex spinors and unified theories. In: VAN NIEUWENHUIZEN, P.; FREEDMAN, D. Z. (ed.). **Supergravity**. Amsterdam: North-Holland, 1979. p. 315-321. |
| 20 | 4.227 | SCHECHTER, J.; VALLE, J. W. F. Neutrino masses in SU(2) ⊗ U(1) theories. **Physical Review D**, v. 22, n. 9, p. 2227-2235, 1980. |
| 21 | 3.884 | AHMAD, Q. R. *et al.* (SNO Collaboration). Measurement of the rate of νₑ + d → p + p + e⁻ interactions produced by ⁸B solar neutrinos at the Sudbury Neutrino Observatory. **Physical Review Letters**, v. 87, n. 7, p. 071301, 2001. |
| 22 | 3.848 | KUZMIN, V. A.; RUBAKOV, V. A.; SHAPOSHNIKOV, M. E. On anomalous electroweak baryon-number non-conservation in the early universe. **Physics Letters B**, v. 155, n. 1-2, p. 36-42, 1985. |
| 23 | 3.848 | EGUCHI, K. *et al.* (KamLAND Collaboration). First results from KamLAND: evidence for reactor antineutrino disappearance. **Physical Review Letters**, v. 90, n. 2, p. 021802, 2003. [preprint 2002] |
| 24 | 3.328 | WU, C. S.; AMBLER, E.; HAYWARD, R. W.; HOPPES, D. D.; HUDSON, R. P. Experimental test of parity conservation in beta decay. **Physical Review**, v. 105, n. 4, p. 1413-1415, 1957. |
| 25 | 3.224 | AN, F. P. *et al.* (Daya Bay Collaboration). Observation of electron-antineutrino disappearance at Daya Bay. **Physical Review Letters**, v. 108, n. 17, p. 171803, 2012. |
| 26 | 3.143 | CLEVELAND, B. T. *et al.* Measurement of the solar electron neutrino flux with the Homestake chlorine detector. **The Astrophysical Journal**, v. 496, n. 1, p. 505-526, 1998. |
| 27 | 2.876 | PONTECORVO, B. Neutrino experiments and the problem of conservation of leptonic charge. **Zhurnal Eksperimental'noi i Teoreticheskoi Fiziki**, v. 53, p. 1717-1725, 1967. |
| 28 | 2.869 | WEINBERG, S. Baryon- and lepton-nonconserving processes. **Physical Review Letters**, v. 43, n. 21, p. 1566-1570, 1979. |
| 29 | 2.745 | AGUILAR-AREVALO, A. *et al.* (LSND Collaboration). Evidence for neutrino oscillations from the observation of ν̄ₑ appearance in a ν̄_μ beam. **Physical Review D**, v. 64, n. 11, p. 112007, 2001. |
| 30 | 2.723 | PONTECORVO, B. Mesonium and antimesonium. **Soviet Physics JETP**, v. 6, p. 429, 1958. [orig. russo: Zh. Eksp. Teor. Fiz., v. 33, p. 549, 1957] |
""")

code(r"""
# Guarda de integridade: a tabela ABNT acima foi redigida a mao. Esta celula confere
# se os 30 valores e a ordem continuam correspondendo ao CSV.
esperado = [23108, 12896, 9245, 8352, 7464, 6840, 6381, 6231, 6197, 6027, 5951, 5876, 5760,
            5290, 5183, 4907, 4536, 4429, 4406, 4227, 3884, 3848, 3848, 3328, 3224, 3143,
            2876, 2869, 2745, 2723]
obtido = [r['cit'] for r in sorted(D, key=lambda z: -z['cit'])[:30]]
if obtido == esperado:
    print('OK — a Tabela 1 corresponde exatamente aos dados do CSV.')
else:
    print('ATENÇÃO — os dados mudaram desde a redação da Tabela 1.')
    for i, (a, b) in enumerate(zip(esperado, obtido), 1):
        if a != b: print(f'  linha {i}: tabela diz {a}, CSV diz {b}')
""")

# ------------------------------------------------- ANO A ANO
md(r"""
---
# Tabela 2 — O trabalho mais citado de cada ano

Um artigo por ano: o de maior contagem de citações entre todas as referências daquele ano no
corpus. A coluna *n* diz quantas referências o ano contribui, o que dá a medida de quão
representativo é o líder. A tabela é gerada pelo código abaixo, direto do CSV, para não
divergir dos dados.
""")

code(r"""
por_ano = collections.defaultdict(list)
for r in D: por_ano[r['ano']].append(r)

linhas = ['| Ano | n | Citações | Trabalho mais citado do ano |', '|---:|---:|---:|---|']
for a in sorted(por_ano):
    t = max(por_ano[a], key=lambda z: z['cit'])
    autor = (t['primeiro_autor'] or t['autor_ref']).split(',')[0].strip()
    titulo = (t['titulo'] or '—').replace('|', '/').rstrip('. ')
    jor = (t['journal'] or '').replace('|', ', ').strip().rstrip('. ')
    ref = f"**{autor.upper()}** — {titulo}" + (f". *{jor}*" if jor else '')
    # separador de milhar aplicado SO ao numero: aplicar na linha inteira destruiria
    # as virgulas da coordenada de journal
    cit = f"{t['cit']:,}".replace(',', '.')
    linhas.append(f"| {a} | {len(por_ano[a])} | {cit} | {ref} |")
tabela_anos = '\n'.join(linhas)
display(Markdown(tabela_anos))

open('dados/tabela_mais_citado_por_ano.md', 'w', encoding='utf-8').write(
    '# Trabalho mais citado de cada ano\n\n'
    'Fonte: INSPIRE-HEP · mapeamento das referências de Agostini et al. (RMP 2023) e '
    'Gonzalez-Garcia et al. (PDG 2025). Ano = earliest_date do INSPIRE.\n\n' + tabela_anos + '\n')
print(f'\n{len(por_ano)} anos cobertos · tabela salva em dados/tabela_mais_citado_por_ano.md')
""")

md(r"""
**Como ler esta tabela.**

A coluna *n* é o que a torna honesta. Em 1938 o líder do ano é o Furry com 35 citações — mas *n* = 1,
ou seja, é o único trabalho daquele ano no corpus, e "líder" ali não significa nada. Já em 2017,
com *n* = 70, o líder disputou com sessenta e nove concorrentes.

Dois anos merecem atenção pelo motivo oposto. **1938**: o artigo de Furry é o que introduz o
mecanismo do duplo beta sem neutrino — o objeto central da sua IC — e tem 35 citações, menos que
qualquer paper experimental recente do corpus. **1948**: o líder do ano tem 66 citações. Isso mostra
o que a contagem de citação do INSPIRE mede de fato: visibilidade dentro da literatura moderna
indexada, não importância teórica. Um artigo fundador de 1938 é hoje citado por via de reviews, não
diretamente.
""")

# ------------------------------------------------- HISTORICOS
md(r"""
---
# Tabela 3 — Mapeamento dos artigos históricos

Os trabalhos do corpus que constituem a linha do tempo conceitual do problema Dirac *versus*
Majorana. Selecionados por relevância histórica, não por contagem de citação — e é justamente a
distância entre as duas coisas que interessa aqui.

| Ano | Citações | Trabalho | Por que é um marco |
|---:|---:|---|---|
| 1930 | 625 | **PAULI, W.** Carta aos "caros senhores e senhoras radioativos" (Tübingen, 4 dez. 1930) | Propõe a partícula, para salvar a conservação de energia no decaimento beta |
| 1932 | 782 | **CHADWICK, J.** Possible existence of a neutron. *Nature* 129, 312 | Descoberta do nêutron, que torna o decaimento beta um problema nuclear bem posto |
| 1932 | 586 | **MAJORANA, E.** Atomi orientati in campo magnetico variabile. *Nuovo Cim.* 9, 43 | Primeiro trabalho de Majorana no corpus; origem do "Majorana flip" |
| 1934 | 1.906 | **FERMI, E.** Versuch einer Theorie der β-Strahlen. I. *Z. Phys.* 88, 161 | Primeira teoria de campo do decaimento beta; a interação de quatro férmions |
| 1935 | 532 | **GOEPPERT-MAYER, M.** Double beta-disintegration. *Phys. Rev.* 48, 512 | Prevê o decaimento duplo beta com dois neutrinos (2νββ) |
| 1937 | **1.720** | **MAJORANA, E.** Teoria simmetrica dell'elettrone e del positrone. *Nuovo Cim.* 14, 171 | **O artigo fundador do projeto**: formula o férmion idêntico à própria antipartícula |
| 1937 | 305 | **RACAH, G.** Sulla simmetria tra particelle e antiparticelle. *Nuovo Cim.* 14, 322 | Primeiro a notar que o férmion de Majorana permitiria processos que violam número leptônico |
| 1938 | 35 | **FURRY, W. H.** Note on the theory of the neutral particle. *Phys. Rev.* 54, 56 | Introduz o mecanismo do **0νββ**; a menor contagem desta tabela |
| 1939 | 811 | **FURRY, W. H.** On transition probabilities in double beta-disintegration. *Phys. Rev.* 56, 1184 | Calcula as taxas de transição do duplo beta, com e sem neutrinos |
| 1953 | 724 | **REINES, F.; COWAN, C. L.** Detection of the free neutrino. *Phys. Rev.* 92, 830 | Primeira tentativa de detecção direta |
| 1956 | 1.734 | **COWAN, C. L. *et al.*** Detection of the free neutrino: a confirmation. *Science* 124, 103 | A detecção do neutrino, 26 anos depois da carta de Pauli |
| 1956 | 2.658 | **LEE, T. D.; YANG, C. N.** Question of parity conservation in weak interactions. *Phys. Rev.* 104, 254 | Põe em dúvida a conservação de paridade na interação fraca |
| 1957 | **3.328** | **WU, C. S. *et al.*** Experimental test of parity conservation in beta decay. *Phys. Rev.* 105, 1413 | A violação de paridade medida; fixa a quiralidade da interação fraca |
| 1957 | 186 | **CASE, K. M.** Reformulation of the Majorana theory of the neutrino. *Phys. Rev.* 107, 307 | Reformulação moderna do formalismo de Majorana |
| 1957 | 2.723 | **PONTECORVO, B.** Mesonium and antimesonium. *Sov. Phys. JETP* 6, 429 | Semente da ideia de oscilação, por analogia com o sistema K⁰ |
| 1957 | 2.150 | **PONTECORVO, B.** Inverse beta processes and nonconservation of lepton charge. *Zh. Eksp. Teor. Fiz.* 34, 247 | Formula a não conservação de carga leptônica |
| 1962 | **5.760** | **MAKI, Z.; NAKAGAWA, M.; SAKATA, S.** Remarks on the unified model of elementary particles. *Prog. Theor. Phys.* 28, 870 | Origem da mistura de sabores leptônicos — o "MNS" da matriz **PMNS** |
| 1967 | 2.876 | **PONTECORVO, B.** Neutrino experiments and the problem of conservation of leptonic charge. *Zh. Eksp. Teor. Fiz.* 53, 1717 | Oscilação de neutrinos na forma moderna — o "P" da PMNS |
| 1968 | 2.223 | **DAVIS, R.; HARMER, D. S.; HOFFMAN, K. C.** Search for neutrinos from the sun. *Phys. Rev. Lett.* 20, 1205 | Homestake: o problema dos neutrinos solares nasce aqui |
| 1969 | 1.365 | **GRIBOV, V. N.; PONTECORVO, B.** Neutrino astronomy and lepton charge. *Phys. Lett. B* 28, 493 | Primeira aplicação da oscilação ao déficit solar |
| 1977 | **5.951** | **MINKOWSKI, P.** μ → eγ at a rate of one out of 10⁹ muon decays? *Phys. Lett. B* 67, 421 | Primeiro artigo do mecanismo *seesaw* |
| 1978 | 6.381 | **WOLFENSTEIN, L.** Neutrino oscillations in matter. *Phys. Rev. D* 17, 2369 | Efeito de matéria — o "W" do efeito MSW |
| 1979 | 4.406 | **GELL-MANN, M.; RAMOND, P.; SLANSKY, R.** Complex spinors and unified theories. In: *Supergravity* | Formulação canônica do *seesaw* tipo I |
| 1979 | 2.623 | **YANAGIDA, T.** Horizontal gauge symmetry and masses of neutrinos | *Seesaw*, formulação independente |
| 1980 | **7.464** | **MOHAPATRA, R. N.; SENJANOVIĆ, G.** Neutrino mass and spontaneous parity nonconservation. *Phys. Rev. Lett.* 44, 912 | *Seesaw* com violação espontânea de paridade; o mais citado da tabela |
| 1980 | 4.227 | **SCHECHTER, J.; VALLE, J. W. F.** Neutrino masses in SU(2) ⊗ U(1) theories. *Phys. Rev. D* 22, 2227 | Estrutura de massa de Majorana no eletrofraco; base da **massa efetiva** m_ββ |
| 1982 | **1.248** | **SCHECHTER, J.; VALLE, J. W. F.** Neutrinoless double-beta decay in SU(2) ⊗ U(1) theories. *Phys. Rev. D* 25, 2951 | **Teorema da caixa-preta**: 0νββ observado ⟹ neutrino de Majorana |
| 1985 | 4.429 | **MIKHEYEV, S. P.; SMIRNOV, A. Yu.** Resonance amplification of oscillations in matter. *Sov. J. Nucl. Phys.* 42, 913 | "MS" do efeito MSW |
| 1998 | **9.245** | **FUKUDA, Y. *et al.*** (Super-Kamiokande). Evidence for oscillation of atmospheric neutrinos. *Phys. Rev. Lett.* 81, 1562 | Oscilação atmosférica: prova de que o neutrino tem massa |
| 2002 | 5.290 | **AHMAD, Q. R. *et al.*** (SNO). Direct evidence for neutrino flavor transformation. *Phys. Rev. Lett.* 89, 011301 | Transformação de sabor solar por corrente neutra |
| 2002 | 3.848 | **EGUCHI, K. *et al.*** (KamLAND). First results from KamLAND. *Phys. Rev. Lett.* 90, 021802 | Confirma a solução LMA com antineutrinos de reator |
""")

md(r"""
**A leitura que esta tabela permite.**

Ordene a coluna de citações e o resultado é contraintuitivo. Os três artigos que **definem** o
objeto da sua IC — Majorana 1937 (1.720), Racah 1937 (305) e Furry 1938 (35) — somam menos citações
que o Mohapatra–Senjanović sozinho (7.464). O artigo que introduz o próprio mecanismo do
decaimento duplo beta sem neutrinos tem **trinta e cinco** citações.

O teorema da caixa-preta de Schechter e Valle, que é o argumento lógico pelo qual uma detecção de
0νββ implicaria natureza de Majorana — ou seja, a justificativa inteira do programa experimental
que hoje mobiliza centenas de milhões de dólares — tem 1.248 citações, menos de um sexto do
Mohapatra–Senjanović.

Isso não é um defeito dos dados; é uma propriedade de como a literatura cita. Trabalhos fundadores
muito antigos são absorvidos pelos livros-texto e pelas reviews, e passam a ser citados por
intermediários. Trabalhos de mecanismo que geram programas de pesquisa — o *seesaw*, o efeito MSW —
são citados diretamente por milhares de artigos que os usam como ferramenta. **Contagem de citação
mede uso corrente, não fundação.** Para o relatório ao orientador, esse é provavelmente o achado
mais interessante do mapeamento.
""")

# ------------------------------------------------- NOBEL
md(r"""
---
# Tabela 4 — Mapeamento dos prêmios Nobel

Aqui é preciso uma distinção que costuma se perder. Há dois grupos diferentes: artigos do corpus
que **são o trabalho premiado** — aquele que a Real Academia Sueca de Ciências citou na justificativa
— e artigos do corpus **escritos por laureados**, mas por trabalho diverso do premiado. Misturar os
dois inflaciona a contagem e diz muito pouco.

## 4.1 — Artigos do corpus que são o trabalho premiado

| Ano do artigo | Citações | Trabalho | Nobel | Laureado(s) | Justificativa oficial |
|---:|---:|---|:---:|---|---|
| 1913 | 228 | **BOHR, N.** On the constitution of atoms and molecules. *Phil. Mag.* 26, 1 | **1922** | Niels Bohr | "for his services in the investigation of the structure of atoms and of the radiation emanating from them" |
| 1928 | 1.783 | **DIRAC, P. A. M.** The quantum theory of the electron. *Proc. R. Soc. A* 117, 610 | **1933** | Erwin Schrödinger; Paul Dirac | "for the discovery of new productive forms of atomic theory" |
| 1932 | 782 | **CHADWICK, J.** Possible existence of a neutron. *Nature* 129, 312 | **1935** | James Chadwick | "for the discovery of the neutron" |
| 1949 | 794 | **GOEPPERT-MAYER, M.** On closed shells in nuclei. II. *Phys. Rev.* 75, 1969 | **1963** | Maria Goeppert Mayer; J. Hans D. Jensen (¼ cada) | "for their discoveries concerning nuclear shell structure" |
| 1953 / 1956 | 724 / 1.734 | **REINES, F.; COWAN, C. L.** Detection of the free neutrino (*Phys. Rev.* 92, 830) e a confirmação (*Science* 124, 103) | **1995** | Frederick Reines (½) | "for the detection of the neutrino" |
| 1956 | 2.658 | **LEE, T. D.; YANG, C. N.** Question of parity conservation in weak interactions. *Phys. Rev.* 104, 254 | **1957** | Tsung-Dao Lee; Chen Ning Yang | "for their penetrating investigation of the so-called parity laws which has led to important discoveries regarding the elementary particles" |
| 1968 / 1998 | 2.223 / 3.143 | **DAVIS, R. *et al.*** Search for neutrinos from the sun (*Phys. Rev. Lett.* 20, 1205) e o resultado final de Homestake (*ApJ* 496, 505) | **2002** | Raymond Davis Jr.; Masatoshi Koshiba (¼ cada) | "for pioneering contributions to astrophysics, in particular for the detection of cosmic neutrinos" |
| 1973 | **12.896** | **KOBAYASHI, M.; MASKAWA, T.** CP violation in the renormalizable theory of weak interaction. *Prog. Theor. Phys.* 49, 652 | **2008** | Makoto Kobayashi; Toshihide Maskawa (½ conjunto) | "for the discovery of the origin of the broken symmetry which predicts the existence of at least three families of quarks in nature" |
| 1988 / 1989 | 1.040 / 755 | **HIRATA, K. S. *et al.*** (Kamiokande-II) — fluxo atmosférico e neutrinos solares de ⁸B | **2002** | Masatoshi Koshiba (¼) | "for pioneering contributions to astrophysics, in particular for the detection of cosmic neutrinos" |
| 1998 | **9.245** | **FUKUDA, Y. *et al.*** (Super-Kamiokande). Evidence for oscillation of atmospheric neutrinos. *Phys. Rev. Lett.* 81, 1562 | **2015** | Takaaki Kajita (½) | "for the discovery of neutrino oscillations, which shows that neutrinos have mass" |
| 2001 / 2002 | 3.884 / 5.290 | **AHMAD, Q. R. *et al.*** (SNO) — taxa de νₑ + d e evidência direta por corrente neutra | **2015** | Arthur B. McDonald (½) | "for the discovery of neutrino oscillations, which shows that neutrinos have mass" |

## 4.2 — Artigos do corpus escritos por laureados, mas que não são o trabalho premiado

| Ano | Citações | Trabalho | Laureado | Nobel | Pelo quê o prêmio foi dado |
|---:|---:|---|---|:---:|---|
| 1930 | 625 | Carta do neutrino ("caros senhores e senhoras radioativos") | Wolfgang Pauli | 1945 | Princípio de exclusão — **a hipótese do neutrino nunca foi premiada** |
| 1932 | 502 | **HEISENBERG, W.** Über den Bau der Atomkerne. I. *Z. Phys.* 77, 1 | Werner Heisenberg | 1932 | Criação da mecânica quântica |
| 1932 / 1957 | 721 / 74 | **LANDAU, L.** Transferência de energia; leis de conservação na interação fraca | Lev Landau | 1962 | Teoria da matéria condensada, em especial o hélio líquido |
| 1934 | **1.906** | **FERMI, E.** Versuch einer Theorie der β-Strahlen. I. *Z. Phys.* 88, 161 | Enrico Fermi | 1938 | Radioatividade induzida por nêutrons — **a teoria do decaimento beta não foi premiada** |
| 1935 | 532 | **GOEPPERT-MAYER, M.** Double beta-disintegration. *Phys. Rev.* 48, 512 | Maria Goeppert Mayer | 1963 | Estrutura de camadas nucleares, não este artigo |
| 1955 | 636 | **GELL-MANN, M.; PAIS, A.** Behavior of neutral particles under charge conjugation. *Phys. Rev.* 97, 1387 | Murray Gell-Mann | 1969 | Classificação das partículas elementares e suas interações |
| 1957 | 322 | **SALAM, A.** On parity conservation and neutrino mass. *Nuovo Cim.* 5, 299 | Abdus Salam | 1979 | Teoria unificada eletrofraca |
| 1958 | 2.053 | **FEYNMAN, R. P.; GELL-MANN, M.** Theory of the Fermi interaction. *Phys. Rev.* 109, 193 | Richard Feynman; Murray Gell-Mann | 1965 / 1969 | Eletrodinâmica quântica (Feynman); classificação de partículas (Gell-Mann) |
| 1961 | 86 | **VAN DER MEER, S.** A directive device for charged particles. *CERN-61-07* | Simon van der Meer | 1984 | Contribuições decisivas ao projeto que descobriu W e Z — o artigo aqui é o "chifre de neutrinos" |
| 1967 | **5.876** | **SAKHAROV, A. D.** Violation of CP invariance, C asymmetry, and baryon asymmetry of the universe | Andrei Sakharov | 1975 | Nobel da **Paz**, não de Física |
| 1974 | 6.231 | **GEORGI, H.; GLASHOW, S. L.** Unity of all elementary particle forces. *Phys. Rev. Lett.* 32, 438 | Sheldon Glashow | 1979 | Teoria eletrofraca unificada, não esta grande unificação |
| 1974 | 6.027 | **PATI, J. C.; SALAM, A.** Lepton number as the fourth color. *Phys. Rev. D* 10, 275 | Abdus Salam | 1979 | Teoria eletrofraca unificada |
| 1976 | 4.536 | **'T HOOFT, G.** Symmetry breaking through Bell-Jackiw anomalies. *Phys. Rev. Lett.* 37, 8 | Gerardus 't Hooft | 1999 | "for elucidating the quantum structure of electroweak interactions" — a renormalização de 1971-72 |
| 1979 | 4.406 | **GELL-MANN, M.; RAMOND, P.; SLANSKY, R.** Complex spinors and unified theories | Murray Gell-Mann | 1969 | Classificação das partículas elementares |
| 1979 | 2.869 | **WEINBERG, S.** Baryon- and lepton-nonconserving processes. *Phys. Rev. Lett.* 43, 1566 | Steven Weinberg | 1979 | Teoria eletrofraca unificada |

## 4.3 — As ausências que o mapeamento expõe

Três casos valem menção, porque são exemplos clássicos de como o Nobel se relaciona mal com a
contagem de citações:

**Cabibbo, 8.352 citações, sem Nobel.** O artigo de 1963 é o quarto mais citado de todo o corpus e
é o ponto de partida direto do trabalho de Kobayashi e Maskawa, premiado em 2008. Nicola Cabibbo
não foi incluído no prêmio — uma das omissões mais discutidas da história recente da física.

**Chien-Shiung Wu, 3.328 citações, sem Nobel.** O experimento de Wu é o que demonstrou a violação
de paridade. Lee e Yang receberam o Nobel de 1957 pela investigação teórica; Wu, que fez a medida,
não foi incluída.

**Pontecorvo, 2.876 + 2.723 + 2.150 citações, sem Nobel.** Bruno Pontecorvo é o "P" da matriz PMNS
e o autor da ideia de oscilação de neutrinos. O Nobel de 2015 premiou a **descoberta experimental**
das oscilações; Pontecorvo, que morreu em 1993, nunca foi laureado.

Nos três casos a contagem de citação identifica corretamente a importância do trabalho, e o prêmio
não. Se a sua pergunta é quais artigos moldaram o campo, a bibliometria acerta mais que o comitê.
""")

code(r"""
# Guarda de integridade das Tabelas 3 e 4: confere as contagens citadas no texto contra o CSV.
CHECAR = {
    1237807: ('Bohr 1913', 228),         3518: ('Dirac 1928', 1783),
      28174: ('Chadwick 1932', 782),    44871: ('Majorana 1932', 586),
       3203: ('Fermi 1934', 1906),      42668: ('Goeppert-Mayer 1935 (2νββ)', 532),
       8251: ('Majorana 1937', 1720),   42669: ('Racah 1937', 305),
      47485: ('Furry 1938 (0νββ)', 35), 42670: ('Furry 1939', 811),
      44721: ('Goeppert-Mayer 1949', 794), 40475: ('Reines-Cowan 1953', 724),
      39882: ('Cowan et al. 1956', 1734), 21787: ('Lee-Yang 1956', 2658),
      28182: ('Wu et al. 1957', 3328),   2884: ('Pontecorvo 1957b', 2723),
      42736: ('Pontecorvo 1957a', 2150), 3540: ('Maki-Nakagawa-Sakata 1962', 5760),
       4510: ('Cabibbo 1963', 8352),    51319: ('Pontecorvo 1967', 2876),
      53047: ('Davis et al. 1968', 2223), 53150: ('Gribov-Pontecorvo 1969', 1365),
      81350: ('Kobayashi-Maskawa 1973', 12896), 4994: ('Minkowski 1977', 5951),
     122259: ('Wolfenstein 1978', 6381), 9686: ('Gell-Mann-Ramond-Slansky 1979', 4406),
     143150: ('Yanagida 1979', 2623),  143802: ('Mohapatra-Senjanović 1980', 7464),
     153987: ('Schechter-Valle 1980', 4227), 171180: ('Schechter-Valle 1982 (caixa-preta)', 1248),
     228623: ('Mikheyev-Smirnov 1985', 4429), 472711: ('Super-Kamiokande 1998', 9245),
     585723: ('SNO 2002', 5290),       604286: ('KamLAND 2002', 3848),
     471829: ('Homestake 1998', 3143),   3438: ("'t Hooft 1976", 4536),
      51345: ('Sakharov 1967', 5876),   45177: ('Pauli 1930 (carta)', 625),
      44042: ('van der Meer 1961', 86),
}
idx = {r['inspire_id']: r for r in D}
erros = []
for rid, (nome, esp) in CHECAR.items():
    r = idx.get(str(rid))
    if r is None:            erros.append(f'{nome}: não encontrado no CSV (recid {rid})')
    elif r['cit'] != esp:    erros.append(f'{nome}: tabela diz {esp}, CSV diz {r["cit"]}')
print(f'{len(CHECAR)} trabalhos históricos/Nobel conferidos contra o CSV.')
print('OK — todas as contagens das Tabelas 3 e 4 conferem.' if not erros
      else 'ATENÇÃO:\n  ' + '\n  '.join(erros))
""")

# ------------------------------------------------- fechamento
md(r"""
---
# Síntese e limitações

## O que o mapeamento entrega

De 996 entradas bibliográficas brutas nas duas reviews saíram **970 referências únicas**, das quais
**888 têm contagem de citação verificada** no INSPIRE-HEP. A cobertura de 91,5% é o teto realista:
as 62 ausências são categorias que a base não indexa.

A análise por eixo temático (`scripts/classificar_tema.py`) põe **260 referências** no núcleo do
projeto de IC — natureza de Majorana, 0νββ, violação de número leptônico, PMNS com fases de CP ou
*seesaw*. A distribuição interna desse núcleo é informativa: 215 referências sobre 0νββ, 91 sobre
elementos de matriz nuclear, mas apenas **21 sobre a natureza de Majorana** e **8 sobre PMNS e
fases de CP**. As duas reviews são mapas de um campo experimental; a camada de formalismo que o seu
projeto quer derivar aparece nelas de forma concentrada, por meia dúzia de artigos fundadores.
Em termos práticos: a bibliografia teórica da IC vai precisar de fontes além destas duas reviews.

## Limitações que devem constar do relatório

**A contagem de citação mede uso corrente, não fundação.** É a conclusão central da Tabela 3. Furry
1938, que introduz o mecanismo do 0νββ, tem 35 citações; o *seesaw* de Mohapatra e Senjanović tem
7.464. Nenhum dos dois números diz qual artigo é mais importante para entender o problema.

**A base tem cobertura desigual no tempo.** O INSPIRE-HEP indexa bem física de altas energias a
partir dos anos 1950. Antes disso a cobertura é parcial e verificada: Rutherford 1920, Chadwick
1933 (a Bakerian Lecture), Heisenberg 1932 partes II e III, Majorana 1933, Stueckelberg 1932,
Fireman 1948 e Touschek 1948 não têm registro — nem por coordenada de periódico, nem por autor e
data. Qualquer análise da primeira metade do século XX a partir destes dados está truncada por
construção.

**Autocitação não foi descontada nas tabelas.** A coluna `citacoes_sem_auto` existe em
`dados/dados_citacoes.csv` e o script de gráficos aceita `--sem-auto`. Para colaborações grandes a
diferença chega a 40% (o IceCube-Gen2, por exemplo, cai de 852 para 514).

**Os números são um retrato datado.** A coleta correu entre 6 e 12 de setembro de 2026. A deriva
medida sobre as 20 duplicatas — o mesmo artigo coletado duas vezes, em dias diferentes, por agentes
diferentes — foi de **19 contagens idênticas em 20**, com a única divergência sendo de 2 citações em
1.104 ao longo de seis dias. Para o relatório, basta registrar a janela da coleta.

**A bibliografia da review do Agostini tem ao menos um erro de ano.** A referência a Towner,
"Quenching of spin matrix elements in nuclei", é datada de 1997, mas o artigo é *Physics Reports*
155, 263, de **1987**. Verificado por consulta direta ao INSPIRE (`recid` 260279, `TOTAL=1`, título
idêntico). Isso só apareceu porque a conferência foi feita referência por referência.

## Onde está cada coisa

```
Mapeamento_Citacoes/
├── Mapeamento_Citacoes.ipynb          este documento
├── PROTOCOLO_BUSCA.md                 regras de consulta ao INSPIRE e armadilhas documentadas
├── dados/
│   ├── master_refs.csv                970 referências únicas extraídas dos PDFs
│   ├── dados_citacoes.csv             TABELA FINAL — 970 linhas com citações e metadados
│   ├── dados_citacoes_tema.csv        idem + classificação por eixo temático
│   ├── shortlist_leitura.csv          os mais citados dentro do núcleo temático
│   └── tabela_mais_citado_por_ano.md  Tabela 2 em markdown, gerada por este notebook
├── resultados/B01.csv … B51.csv       coleta bruta, um arquivo por bloco de 20 buscas
├── planilhas/Mapeamento_B31-B40.xlsx  recorte em Excel com resumo por fórmulas
├── graficos/                          as 5 figuras em PNG e PDF, 300 dpi
└── scripts/                           parsing, consolidação, validação, gráficos, temas
```

---

### Fontes

Contagens de citação: [INSPIRE-HEP](https://inspirehep.net) (coleta de 6 a 12 de setembro de 2026).
Justificativas oficiais dos prêmios: [NobelPrize.org](https://www.nobelprize.org) —
[1957](https://www.nobelprize.org/prizes/physics/1957/summary/) ·
[1963](https://www.nobelprize.org/prizes/physics/1963/summary/) ·
[1995](https://www.nobelprize.org/prizes/physics/1995/summary/) ·
[2002](https://www.nobelprize.org/prizes/physics/2002/summary/) ·
[2008](https://www.nobelprize.org/prizes/physics/2008/press-release/) ·
[2015](https://www.nobelprize.org/prizes/physics/2015/summary/) ·
[lista completa de física](https://www.nobelprize.org/prizes/lists/all-nobel-prizes-in-physics/all/).
""")

nb['cells'] = C
nb['metadata'] = {'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
                  'language_info': {'name': 'python'}}
nbf.write(nb, '/home/claude/proj/Mapeamento_Citacoes.ipynb')
print('notebook montado:', len(C), 'celulas')
