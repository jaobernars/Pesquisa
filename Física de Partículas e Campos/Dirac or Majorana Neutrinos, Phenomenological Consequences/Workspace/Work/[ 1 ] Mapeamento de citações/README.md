# Mapeamento de Citações: Referências de Física de Neutrinos


## Objetivo
O objetivo deste levantamento é realizar o **mapeamento completo das citações (por ano)** de cada uma das referências bibliográficas presentes em duas revisões (reviews) selecionadas da área.

As duas referências analisadas são:

[ 1 ] AGOSTINI, M.; BENATO, G.; DETWILER, J. A.; MENÉNDEZ, J.; VISSANI, F. Toward the discovery of matter creation with neutrinoless ββ decay. Reviews of Modern Physics, [S. l.], v. 95, n. 2, p. 025002, 2023.

[ 2 ] GONZALEZ-GARCIA, M. C.; WENDELL, R. Neutrino Masses, Mixing, and Oscillations. In: PARTICLE DATA GROUP. Review of Particle Physics. [S. l.]: Particle Data Group, 2026. cap. 14. Revisado em março de 2026.

O banco de dados utilizado como base para puxar as métricas e histórico de citações é o **INSPIRE-HEP** através de sua API (`https://inspirehep.net/api/literature`). A coleta foi feita entre 6 e 12 de setembro de 2026.

---


## Resumo dos Dados

| Item | Valor |
|---|---|
| Referências extraídas do Agostini et al. (RMP, 0νββ) | **744** |
| Referências extraídas do Gonzalez-Garcia et al. (PDG §14) | **252** (252/252, numeração completa) |
| Total bruto | 996 |
| **Únicas após deduplicação** | **970** (16 citadas pelas duas reviews) |
| Com arXiv ID (busca exata) | 468 |
| Sem arXiv (busca por título, journal ou DOI) | 502 (449 por título, 49 por journal, 4 por DOI) |
| Blocos de coleta de 20 buscas | **51** (B01–B51) |
| Registros encontrados no INSPIRE | 908 (905 confirmados e 3 duvidosos) |
| Duplicatas pelo `inspire_id` | 20 (mesma obra em duas entradas; contada uma vez) |
| **Com citação recuperada** | **888** (91,5%) |
| Sem registro no INSPIRE | 62 (6,4%): teses, atas, apresentações, bancos de dados nucleares e revistas de química e engenharia |

## Resultados

| Item | Valor |
|---|---|
| Mediana de citações | 124 |
| Média de citações | 457 |
| Mais citado | 23.108 (Planck 2018, parâmetros cosmológicos) |
| Período coberto | 1913 a 2025 |
| **Referências ligadas ao objetivo da IC** | **157** (88 de formalismo, 69 diretamente correlacionadas, em 9 eixos) |
| Lista de leitura do núcleo temático | 20 referências |

A análise completa está em [`Mapeamento_Citacoes.ipynb`](Mapeamento_Citacoes.ipynb), com 6 figuras e 5 tabelas:

| Figura | Conteúdo |
|---|---|
| 1 | Ano × impacto de citação |
| 2 | Perfil temporal dos dados (referências por ano) |
| 3 | Distribuição de citações por década |
| 4 | Taxa de citação (citações por ano desde a publicação) |
| 5 | As 30 referências mais citadas |
| 6 | Ano × impacto de citação das referências ligadas à IC |

| Tabela | Conteúdo |
|---|---|
| 1 | Referências ligadas ao objetivo da IC, por eixo |
| 2 | As 30 referências mais citadas (formato ABNT) |
| 3 | O trabalho mais citado de cada ano |
| 4 | Mapeamento dos artigos históricos |
| 5 | Mapeamento dos prêmios Nobel |

As figuras estão em PNG e PDF, 300 dpi, na pasta [`gráficos/`](gráficos/).

## Fases da Pesquisa e Tarefas

Todas as fases foram concluídas.

| Fase | Tarefas | Entrega |
|---|---|---|
| **0. Preparação** | ✅ Concluída | Extração das 996 referências dos dois PDFs, deduplicação em 970 únicas, formação dos blocos de 20 buscas, protocolo de busca ([`PROTOCOLO_BUSCA.md`](PROTOCOLO_BUSCA.md)) e scripts de filtragem |
| **1. Coleta arXiv** | ✅ Concluída (`B01`–`B23`) | Busca exata por **arXiv ID** no INSPIRE |
| **2. Coleta Difícil** | ✅ Concluída (`B24`–`B47`) | Busca por **título, journal ou DOI** para capturar clássicos pré-arXiv e publicações não indexadas por ID |
| **2b. Reconciliação** | ✅ Concluída (`B48`–`B51`) | 48 referências recuperadas pela re-extração corrigida do PDF do Agostini, coletadas em blocos novos sem renumerar os já coletados |
| **3. Tratamento** | ✅ Concluída | Compilação em `dados/citacoes/dados_citacoes.csv`, deduplicação definitiva pelo `inspire_id` e reconferência manual dos não encontrados |
| **4. Gráficos** | ✅ Concluída | 6 figuras em PNG/PDF de tempo (ano) $\times$ citações, geradas por `scripts/saida/grafico_citacoes.py` |
| **5. Seleção da IC** | ✅ Concluída | 157 referências ligadas ao objetivo da IC, lidas título a título, em `dados/ic/referencias_ic.csv` |
| **6. Relatório** | ✅ Concluída | Notebook `Mapeamento_Citacoes.ipynb` com a visão panorâmica, as tendências, as dificuldades e os achados da coleta |
