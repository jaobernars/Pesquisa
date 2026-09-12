# Mapeamento de Citações: Referências de Física de Neutrinos


## Objetivo
O objetivo deste levantamento, é realizar o **mapeamento completo das citações (por ano)** de cada uma das referências bibliográficas presentes em duas revisões (reviews) selecionadas da área.

As duas referências analisadas são:

[ 1 ] AGOSTINI, M.; BENATO, G.; DETWILER, J. A.; MENÉNDEZ, J.; VISSANI, F. Toward the discovery of matter creation with neutrinoless ββ decay. Reviews of Modern Physics, [S. l.], v. 95, n. 2, p. 025002, 2023.

[ 2 ] GONZALEZ-GARCIA, M. C.; WENDELL, R. Neutrino Masses, Mixing, and Oscillations. In: PARTICLE DATA GROUP. Review of Particle Physics. [S. l.]: Particle Data Group, 2026. cap. 14. Revisado em março de 2026.

O banco de dados utilizado como base para puxar as métricas e histórico de citações é o **INSPIRE-HEP** através de sua API (`https://inspirehep.net/api/literature`).

---


## Resumo dos Dados

Após extração completa, os dados base revelam:

| Item | Valor |
|---|---|
| Referências extraídas do Agostini et al. (RMP, 0νββ) | **742** |
| Referências extraídas do Gonzalez-Garcia et al. (PDG §14) | **252** (252/252, numeração completa) |
| Total bruto | 994 |
| **Únicas após deduplicação** | **968** (16 citadas pelas duas reviews) |
| Com arXiv ID (busca exata) | 468 |
| Sem arXiv (busca por journal/título) | 500 |
| Blocos de coleta de 20 buscas | **50** (B01–B50) |

## Fases da Pesquisa e Tarefas

Os processamentos foram organizados e segregados da seguinte maneira:

| Fase | Tarefas | Entrega |
|---|---|---|
| **0. Preparação** | ✅ Concluída | coleta das 968 refs únicas, formação dos 50 blocos de processamento de 20 ref, definição de protocolo e elaboração dos scripts base de filtragem |
| **1. Coleta arXiv** | `B01` ao processamento arXiv (468 refs) | Extração baseada em buscar exata por **arXiv ID** no INSPIRE (garante alta taxa de acerto). |
| **2. Coleta Difícil** | Blocos finais até `B50` (500 refs) | Busca por nome de **journal/título** para capturar clássicos pré-arXiv e publicações não indexadas por ID. |
| **3. Tramamento** | `Tratamento` | Compilação geral em uma base única `dados_citacoes.csv` e triagem ativa para resolver registros "não-encontrados". |
| **4. Gráficos** | `GRAFICOS` (Análise) | Produção de material gráfico em PNG/PDF evidenciando as métricas de tempo (ano) $\times$ incidência de citações para as referências principais. |
| **5. Relatório** | `RELATORIO` | Documento em resumo contendo a visão panorâmica, mapeamento de tendências, dificuldades e achados da coleta. |

