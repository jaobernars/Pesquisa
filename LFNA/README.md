# LFNA — Rastreabilidade de Amostras de Solo via Física Nuclear Aplicada

**Inovação no combate a fraudes no Crédito Rural e no Seguro Agrícola**

> Laboratório de Física Nuclear Aplicada (LFNA) — pesquisa em desenvolvimento sobre técnicas nucleares e geoquímicas para autenticação forense de amostras de solo.

---

## Sumário

- [Introdução](#introdução)
- [Motivação](#motivação)
- [Objetivos](#objetivos)
- [Metodologia Científica](#metodologia-científica)
  - [Fluorescência de Raios-X (FRX)](#1-fluorescência-de-raios-x-frx)
  - [Espectrometria de Raios Gama](#2-espectrometria-de-raios-gama)
  - [Análise Temporal e Correlação Estatística](#3-análise-temporal-e-correlação-estatística)
- [Contexto Regulatório e Governança](#contexto-regulatório-e-governança)
- [Fundamentação na Literatura](#fundamentação-na-literatura)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Status e Próximas Etapas](#status-e-próximas-etapas)

---

## Introdução

O acesso a linhas de financiamento de custeio e investimento agrícola, bem como a apólices de seguro rural voltadas à recuperação e correção de solos (calagem, gessagem e demais práticas de manejo de fertilidade), exige a apresentação de laudos técnicos baseados em amostras físicas de solo. Esse fluxo — amostragem em campo, análise laboratorial e emissão de laudo — é hoje o elo mais frágil da cadeia de comprovação técnica que sustenta a liberação de crédito rural e o pagamento de sinistros de seguro agrícola no Brasil.

Este projeto propõe um método científico, estatístico e reprodutível para determinar a **procedência geográfica e temporal** de uma amostra de solo, permitindo distinguir com rigor analítico se ela é autêntica (coletada na gleba financiada, na época declarada) ou fraudulenta (adulterada ou trazida de outra área/propriedade). A proposta parte da Física Nuclear Aplicada — fluorescência de raios-X e espectrometria de raios gama — como ferramentas forenses complementares aos laudos químicos tradicionais.

## Motivação

Auditorias conduzidas por um grupo interministerial envolvendo o **Ministério da Agricultura e Pecuária (MAPA)**, o **Banco Central do Brasil (BCB)** e a **Embrapa** identificaram vulnerabilidades recorrentes no processo de comprovação técnica de solo usado para liberar recursos financeiros. Entre as práticas identificadas:

- **Adulteração de amostras físicas** enviadas para laboratório, com o objetivo de simular uma condição de fertilidade que justifique a liberação de crédito para calagem/gessagem que não será de fato aplicado, ou aplicado em volume menor do que o financiado.
- **Substituição da terra amostrada**, isto é, coleta de solo em glebas de maior fertilidade — muitas vezes de outra propriedade — para representar falsamente a área financiada, seja para liberar crédito indevido, seja para simular quebra de safra e acionar indenizações de seguro agrícola.

Laudos químicos convencionais (pH, macro e micronutrientes disponíveis, matéria orgânica) são **suscetíveis a manipulação direta**: podem ser alterados pela simples adição de insumos à amostra antes do envio, ou mascarados pela troca de origem do material coletado. Esse tipo de fraude compromete a integridade dos bilhões de reais movimentados anualmente pelo crédito e pelo seguro rural brasileiros, e hoje carece de um mecanismo técnico de verificação independente da própria amostra declarada.

A motivação central deste projeto é, portanto, fechar essa lacuna: desenvolver uma metodologia que extraia da própria amostra uma **assinatura física intrínseca**, praticamente impossível de forjar sem replicar a geologia e a mineralogia local, criando um mecanismo de auditoria complementar aos laudos de fertilidade já exigidos.

## Objetivos

**Objetivo geral:** desenvolver e validar um método científico-estatístico de rastreabilidade geográfica e temporal de amostras de solo, aplicável como ferramenta de auditoria em processos de concessão de crédito rural e sinistro de seguro agrícola.

**Objetivos específicos:**

1. Caracterizar a impressão digital geoquímica (FRX) e a assinatura radioisotópica (espectrometria gama) de solos de referência em glebas financiadas.
2. Estabelecer, para cada propriedade/gleba, uma linha de base de variação elementar e isotópica aceitável, compatível com práticas legítimas de manejo agrícola (ex.: calagem, gessagem, adubação).
3. Construir modelos estatísticos de correlação entre amostras coletadas em diferentes épocas, capazes de diferenciar variação natural/manejo de ruptura da assinatura mineralógica (indicativa de fraude por substituição).
4. Avaliar a viabilidade de integração da metodologia aos fluxos de auditoria já operados por MAPA, BCB e Embrapa.

## Metodologia Científica

A metodologia combina duas técnicas analíticas não destrutivas da Física Nuclear Aplicada, usadas como ferramentas forenses de rastreabilidade — em vez de depender apenas de laudos químicos tradicionais, o projeto foca na **assinatura elementar e isotópica intrínseca** de cada solo, decorrente da rocha matriz e dos processos pedogenéticos locais.

### 1. Fluorescência de Raios-X (FRX)

Mapeia, de forma não destrutiva, os teores totais de macro e micronutrientes, além de elementos-traço e metais — como **Si, Al, Fe, Ti, Mn e Sr** — presentes na matriz mineralógica da amostra. O conjunto desses teores compõe uma **impressão digital geoquímica**, característica da composição mineral do solo e, portanto, da origem geológica do material.

### 2. Espectrometria de Raios Gama

Avalia a assinatura de radioisótopos naturais (geogênicos) presentes no solo — **Potássio-40 (⁴⁰K), Urânio-238 (²³⁸U) e Tório-232 (²³²Th)**. A distribuição desses radionuclídeos depende diretamente da rocha matriz que originou o solo e dos processos de intemperismo locais, funcionando como um **código geográfico natural** de alta complexidade, difícil de replicar ou falsificar artificialmente. Essa relação entre radioisótopos, mineralogia e textura já é documentada na literatura internacional de espectrometria gama proximal aplicada a solos agrícolas (ver [Fundamentação na Literatura](#fundamentação-na-literatura)).

### 3. Análise Temporal e Correlação Estatística

O núcleo científico do projeto está na capacidade de rastrear a proveniência do solo ao longo do tempo, cruzando as variáveis obtidas por FRX e espectrometria gama:

- **Linha de base geográfica:** amostras históricas ou mapeamentos prévios da propriedade estabelecem os limites aceitáveis de variação elementar e isotópica para aquela coordenada.
- **Modelagem e correlação:** modelos estatísticos (correlação, regressão, classificação) analisam se as flutuações observadas em uma nova amostra — apresentada ao banco ou à seguradora — são compatíveis com manejo agrícola legítimo (ex.: aumento de Ca/Mg por calagem) ou indicam ruptura da assinatura mineralógica de base, evidenciando que a terra foi trazida de outra região (fraude por substituição).

Um ponto crítico, também identificado na literatura de referência, é que essa relação entre sinal físico e propriedade do solo é **fortemente dependente do local** (site-specific): a mesma variável gama pode se correlacionar positiva ou negativamente com a textura/mineralogia dependendo da composição da fração argila de cada região. Isso reforça a necessidade de calibração local por gleba/propriedade, e não de um modelo genérico único — um requisito metodológico central para este projeto.

## Contexto Regulatório e Governança

O monitoramento e a regulamentação das exigências de manejo e conformidade de solo para fins de crédito e seguro agrícola envolvem uma cadeia integrada de governança pública:

| Órgão | Papel no ecossistema |
|---|---|
| **Ministério da Agricultura e Pecuária (MAPA)** | Autoridade responsável pelas normas de defesa agropecuária, fiscalização de insumos e manejo sustentável das safras. Gerencia o Zoneamento Agrícola de Risco Climático (**ZARC**), que vincula o tipo de solo à liberação de recursos de crédito e seguro. |
| **Banco Central do Brasil (BCB)** | Regula o sistema bancário e define, no **Manual de Crédito Rural (MCR)**, os critérios de comprovação técnica exigidos das instituições financeiras para a liberação de recursos de custeio e investimento agrícola. |
| **Embrapa** | Braço tecnológico e científico do ecossistema: valida as ferramentas analíticas propostas e centraliza bancos de dados de solo (como o *Saúde dos Solos BR*), utilizados para cruzar informações e auditar laudos técnicos. |

O sucesso desta pesquisa representa uma transição relevante para o agronegócio: de amostras físicas vulneráveis a manipulação para **laudos periciais lastreados em assinaturas físicas nucleares**, reforçando a integridade dos recursos investidos anualmente no crédito e no seguro rural brasileiro.

## Fundamentação na Literatura

A revisão de literatura do projeto está documentada em [`Referências/Artigos/Revisões de Artigos`](Referências/Artigos/Revisões%20de%20Artigos/) e inclui, até o momento:

1. **Taylor et al. (2023)** — *Portable gamma spectrometry for rapid assessment of soil texture, organic carbon and total nitrogen in agricultural soils.* Journal of Soils and Sediments. Demonstra o uso de espectrômetro gama portátil para prever textura, carbono e nitrogênio do solo a partir da assinatura de ⁴⁰K, ²³⁸U e ²³²Th, com boa correlação estatística (R² ≈ 0,75–0,79). [Revisão completa](Referências/Artigos/Revisões%20de%20Artigos/%5B1%5D%20Taylor%20et%20al.%202023%20-%20Portable%20gamma%20spectrometry%20%28soil%20texture%2C%20SOC%2C%20TN%29.md).
2. **Pätzold, Leenen & Heggemann (2020)** — *Proximal Mobile Gamma Spectrometry as Tool for Precision Farming and Field Experimentation.* Soil Systems. Testa a transferibilidade de modelos de predição de textura entre diferentes campos e conclui que a calibração **local** (site-specific) supera consistentemente modelos genéricos — evidência direta de que a assinatura gama de um solo é ligada às condições geopedológicas específicas do local, sustentando seu uso como identificador de origem. [Revisão completa](Referências/Artigos/Revisões%20de%20Artigos/%5B2%5D%20P%C3%A4tzold%2C%20Leenen%20%26%20Heggemann%202020%20-%20Proximal%20Mobile%20Gamma%20Spectrometry%20%28precision%20farming%29.md).

Esses trabalhos fundamentam tecnicamente duas premissas centrais do projeto: (i) a assinatura de radioisótopos naturais se correlaciona de forma robusta com propriedades físico-químicas do solo; e (ii) essa assinatura é específica de cada local, o que a torna adequada como "código geográfico" para fins de autenticação forense.

## Estrutura do Repositório

```
LFNA/
├── README.md                                  # Este documento
└── Referências/
    └── Artigos/
        ├── [1] Portable gamma spectrometry...pdf
        ├── [2] Proximal Mobile Gamma Spectrometry...pdf
        └── Revisões de Artigos/
            ├── [1] Taylor et al. 2023 - ...md
            └── [2] Pätzold, Leenen & Heggemann 2020 - ...md
```

## Status e Próximas Etapas

Projeto em fase de **revisão de literatura e desenho metodológico**. Próximos passos previstos:

- [ ] Ampliar a revisão bibliográfica sobre FRX aplicada à autenticação forense de solos (proveniência geoquímica).
- [ ] Definir protocolo de amostragem e linha de base para propriedades-piloto.
- [ ] Especificar os modelos estatísticos de correlação temporal (regressão, classificação, detecção de anomalias).
- [ ] Avaliar formatos de integração com bancos de dados existentes (ex.: Saúde dos Solos BR, ZARC).
