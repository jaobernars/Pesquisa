# Revisão Científica

## Proximal Mobile Gamma Spectrometry as Tool for Precision Farming and Field Experimentation

---

## 1. Referência completa

Pätzold, S., Leenen, M., & Heggemann, T. W. (2020). Proximal Mobile Gamma Spectrometry as Tool for Precision Farming and Field Experimentation. *Soil Systems*, 4(2), 31. https://doi.org/10.3390/soilsystems4020031

- **Tipo:** Article (pesquisa original, open access)
- **Revista:** Soil Systems (MDPI)
- **Recebido:** 29 fev. 2020 · **Aceito:** 9 maio 2020 · **Publicado:** 14 maio 2020
- **Instituição:** Institute of Crop Science and Resource Conservation (INRES) — Soil Science and Soil Ecology, University of Bonn, Alemanha
- **Financiamento:** German Federal Ministry of Education and Research (BMBF), programa BonaRes, projeto I4S (subprojeto F, Grant No. 031B0513F)
- **Licença:** Creative Commons CC BY 4.0 (acesso aberto integral)

---

## 2. Resumo em uma frase

Estudo alemão que testa, em cinco campos agrícolas com condições geopedológicas distintas, a **transferibilidade** de um modelo de predição de textura do solo calibrado por machine learning (SVM, de estudo anterior do mesmo grupo) versus modelos lineares locais (site-specific), concluindo que a calibração local supera consistentemente o modelo genérico "site-independent", e demonstrando aplicações práticas em calagem de precisão, capacidade de campo e desenho experimental de parcelas.

---

## 3. Objetivo e hipóteses

**Objetivo geral:** avaliar o estado da arte da espectrometria gama móvel proximal (GS) para (i) elucidar limitações e (ii) fornecer exemplos de aplicação em agricultura de precisão e experimentação de campo.

**Duas hipóteses centrais testadas:**
1. **H1:** o modelo de calibração "site-independent" publicado por Heggemann et al. (2017) prediz precisamente a textura do solo em sites desconhecidos (não usados na calibração original).
2. **H2:** a GS fornece dados de textura do solo "on-the-go" e em tempo real (sem pós-processamento geoestatístico) com precisão suficiente para uso em agricultura de precisão e experimentação de campo.

**Resultado antecipado no resumo:** H1 é refutada de forma geral (modelo não é universalmente válido); H2 é parcialmente confirmada (reconhecimento de padrões espaciais funciona mesmo sem processamento, mas predição quantitativa exige calibração local).

---

## 4. Fundamentação teórica (síntese)

- ~90% da radiação gama medida acima do solo origina-se dos **0,3 m superficiais** (zona radicular principal).
- Dois mecanismos ligam textura e radionuclídeos:
  1. Tamanho de partícula ↔ área superficial específica ↔ capacidade de sorção de radionuclídeos;
  2. ⁴⁰K, ²³⁸U e ²³²Th são incorporados na **estrutura cristalina de certos minerais** (não apenas adsorvidos).
- Fração de areia em solos europeus é tipicamente dominada por **quartzo** (baixíssimo teor de radionuclídeos); fração argila é dominada por **minerais de argila e óxidos de Fe** (mais ricos em radionuclídeos) — mecanismo geral, mas **modulado pela mineralogia específica** do material de origem (ponto central do artigo).
- Introduz o conceito-chave de **"condições geopedológicas"** (geopedological conditions): o complexo de fatores geológicos, mineralógicos e pedológicos que determinam a relação local entre sinal gama e textura — termo usado ao longo de todo o artigo para explicar por que modelos não se transferem bem entre sites.
- Cita estudos prévios de sucesso em campo único (Priori et al. 2014), poucos sites (Petersen et al. 2012) ou paisagens geologicamente homogêneas (van der Klooster et al. 2011; van Egmond et al. 2010) — mas reconhece que, para datasets heterogêneos, **machine learning (SVM)** pode superar correlação linear simples (Heggemann et al. 2017).

---

## 5. Materiais e métodos

### 5.1 Sites e amostragem (Tabela 1 do artigo)

7 campos agrícolas na Alemanha, cobrindo diferentes materiais de origem geológica:

| Site | Uso do solo | N amostras | Areia (%) | Silte (%) | Argila (%) |
|---|---|---|---|---|---|
| Münster | Cultivo | 45 (raster) | 57 (21–80) | 15 (9–21) | 26 (9–55) |
| Düren | Cultivo (campo + parcelas) | 11 + 48 | 44 (34–59) | 38 (26–44) | 16 (11–20) |
| Ahrweiler | Cultivo | 71 (raster) | 12 (7–23) | 57 (37–70) | 30 (18–57) |
| Rheinbach-1 | Cultivo | 42 (raster) | 25 (12–37) | 43 (40–65) | 14 (21–28)* |
| Rheinbach-2 | Pastagem permanente | 81 (raster) | 38 (22–51) | 40 (27–49) | 20 (14–28) |
| Uckermark-1 | Cultivo | 81 (estratificada) | 61 (36–81) | 23 (11–40) | 14 (5–21) |
| Uckermark-2 | Cultivo | 39 (estratificada) | 57 (34–78) | 26 (16–37) | 16 (6–27) |

*(\*valor de mínimo/máximo da argila em Rheinbach-1 conforme extraído do PDF original — a ordem "21–28" sugere possível troca com a coluna adjacente na tabela fonte; verificar o PDF original se for citar esse dado especificamente.)*

**Contextos geológicos distintos**, condição central para testar transferibilidade:
- **Münster:** margas cretáceas + areia eólica + sedimentos fluviais saalianos + till glacial
- **Düren:** depósitos periglaciais de encosta pleistocênicos (PPSD) sobre arenito Bunter + loess
- **Ahrweiler / Rheinbach:** PPSD derivados de rochas sedimentares do Devoniano Inferior (Maciço Renano/Eifel) + loess, com graus variáveis de intemperismo
- **Uckermark (1 e 2):** till glacial weichseliano sobre morena de fundo — dois campos vizinhos (8,4 km de distância), mesmas condições geopedológicas

### 5.2 Experimentos de parcela (plot experiments)
- **Düren:** experimento de fertilização já existente, 48 parcelas de 108 m² cada (área total 8613 m²), montado **antes** do levantamento gama (não influenciado por ele) — usado retrospectivamente para avaliar se a GS poderia ter otimizado o desenho.
- **Rheinbach-2:** experimento de calagem estabelecido **após** o levantamento gama preliminar — o mapa legado de solo (1:5000) sugeria homogeneidade, mas a GS revelou heterogeneidade considerável de textura, levando à **modificação do desenho experimental** (faixas de 6 m de largura capturando a heterogeneidade).

### 5.3 Instrumentação
- **RSX-1** (Radiation Solutions Inc., Canadá), dois cristais de iodeto de sódio (NaI) de 4,2 L cada, ativados com tálio, montados em quadro de aço no engate de três pontos do trator.
- Espectro de 1024 canais; GPS interno; taxa de 1 Hz; altura fixa de **0,3 m** acima do solo.
- Dois modos de coleta: **on-the-go** (em movimento, 0,7–1,4 m/s; espaçamento entre faixas de 6–27 m) e **stop-and-go** (60 s parado, para calibração com dados de referência).
- Avaliação via **método de janelas (ROI)**: Total Counts (TC, 0,4–2,81 MeV), K-40 (1,37–1,57 MeV), U-238 (1,66–1,86 MeV), Th-232 (2,41–2,81 MeV) — software RadAssist (Radiation Solutions).
- **Redução de ruído:** média móvel de 5 espectros consecutivos (moving window), preservando a densidade espacial de pontos.

### 5.4 Análises de solo
- Método combinado de peneira + pipeta para granulometria (classes: areia 2000–63 µm; silte 63–2 µm; argila <2 µm — esquema WRB e do levantamento de solos alemão).
- Matéria orgânica e carbonato de cálcio removidos antes da análise textural.
- Classes de textura adaptadas ao esquema alemão (GD-NRW / AG Boden) para permitir comparação com mapas de solo legados.
- Duas aplicações-exemplo derivadas da textura: **necessidade de calagem** (via esquema VDLUFA) e **capacidade de campo (FC)** (via funções de pedotransferência do manual alemão de levantamento de solos).

### 5.5 Calibração dos modelos
- **Modelo site-independent:** SVM (Support Vector Machines) de Heggemann et al. (2017), ampliado com dados de Ahrweiler; treino por validação cruzada 100× 10-fold.
- **Teste de transferibilidade:** exclusão de um site por vez do conjunto de calibração, reaplicação do modelo re-calibrado ao site excluído (test-set validation "leave-one-site-out").
- **Teste de substituição cruzada:** pares de sites (Uckermark-1↔Uckermark-2; Ahrweiler↔Rheinbach-1) testados quanto à capacidade de um substituir o outro na calibração.
- **Modelos site-specific:** correlação linear simples/múltipla por site, treino com 70% dos dados (aleatório), validação com os 30% restantes.
- Métricas: RMSE, MAE, R² (equações 1–3 do artigo); **critério de aceitação: RMSE e MAE < 5%** para frações individuais de textura.

---

## 6. Principais resultados

### 6.1 Falha de generalização do modelo site-independent (Tabela 2 do artigo)
- Excluindo **Münster** da calibração e testando nele: MAE inaceitável (Areia 21%, Silte 15%, Argila 15%) — muito acima do limiar de 5%.
- Excluindo **Rheinbach-1** e testando nele: MAE ainda alto (Areia 5%, Silte 18%, Argila 12%).
- **Uckermark-1 e Uckermark-2 conseguiram se substituir mutuamente** com sucesso (MAE 3–4% em todas as frações) — resultado esperado, dado que os dois campos distam apenas 8,4 km e compartilham as mesmas condições geopedológicas (till glacial weichseliano).
- **Ahrweiler e Rheinbach-1** (7,5 km de distância, mesma unidade geológica regional — Maciço Renano) **falharam** ao se substituir (MAE >5%), apesar da proximidade geográfica e do mesmo mapa geológico regional. Causa apontada: diferenças na composição do PPSD (proporção de loess) e no grau de intemperismo — presença de esmectita em Rheinbach, ausente em Ahrweiler (confirmado por difração de raios-X, 1 amostra por campo).

> **Achado central do artigo:** proximidade geográfica e mesma unidade geológica mapeada **não garantem** transferibilidade do modelo — mineralogia fina (ex.: presença/ausência de esmectita) pode ser mais determinante que distância espacial.

### 6.2 Modelo local supera modelo genérico (Fig. 3)
- Em Ahrweiler: modelo site-independent SVM → R² = 0,09, MAE = 7,1% argila (praticamente sem poder preditivo).
- Modelo linear local (site-specific): R² = 0,73, MAE = 3,5% argila — desempenho muito superior com abordagem estatística muito mais simples.

### 6.3 Reconhecimento de padrões espaciais sem calibração quantitativa
- Em Rheinbach-2 (pastagem), 4666 espectros on-the-go revelaram **distribuição bimodal** de Total Counts, definindo dois "clusters" espaciais nítidos (separados no mínimo local de 825 cps).
- O **mapa de solo legado (1:5000)** não capturou essa heterogeneidade — a GS revelou uma zonação de textura muito mais fina do que a cartografia tradicional, mesmo sem qualquer calibração numérica (apenas classificação relativa de contagens).
- Interpretação geológica: dobramento hercínico de rochas sedimentares do Devoniano Inferior (arenitos e folhelhos/shales alternados), retrabalhados por solifluxão no Pleistoceno — resultando em mosaico de materiais-fonte em escala métrica.

### 6.4 Relações Textura × sinal gama — sinais opostos entre sites (Fig. 5, Tabela 3)
- **Münster:** correlação **positiva** entre TC e argila (TC = 8,50×argila + 543,4; R²=0,85) — mineralogia dominada por montmorillonita/ilita na argila, quartzo dominante na areia.
- **Ahrweiler:** correlação **negativa** entre TC e argila (TC = −6,67×argila + 1477,8; R²=0,81) — argila provavelmente dominada por caulinita (mineral 2:1 pobre em K, baixa capacidade de troca catiônica).
- **Rheinbach-1** (cultivo): correlação TC×argila fraca e não significativa na prática (R²=0,06) — porém, correlação forte entre **K-40 e areia** (R²=0,86 combinando os dois campos de Rheinbach).
- **Conclusão prática:** a variável gama que melhor prediz textura **muda de site para site** dependendo da mineralogia da fração argila — não existe um "melhor ROI" universal.

### 6.5 Aplicações em agricultura de precisão

**a) Calagem de precisão (lime requirement) — Tabela 4**
- Ahrweiler: modelo de argila calibrado em K-40 (48 amostras: Argila = −0,45×K40 + 91; R²=0,82, RMSE=3,3%); validação em 23 amostras (R²=0,88, MAE=2,8% argila).
- Recomendação de calagem variável: **1700–2000 kg CaO/ha/ano** dependendo da zona em Ahrweiler; em Münster, 4 classes distintas, de **600 a 1700 kg CaO/ha/ano** dentro do mesmo campo.
- Achado de relevância econômica direta: a média de argila medida convencionalmente no campo inteiro de Ahrweiler foi 29,5%, mas a média predita on-the-go (N=2494 pontos!) foi 24,1% — a amostragem convencional pontual **teria levado à superdosagem de calcário em grande parte do campo**.

**b) Capacidade de campo (FC) para irrigação — Fig. 8**
- Em Münster, condições geopedológicas mais simples permitiram predizer tanto areia quanto argila a partir de TC, derivando classes de textura e FC via tabelas de pedotransferência (26–44% v/v de FC ao longo do campo), mapeadas em grade de 20×20 m sem interpolação geoestatística.

**c) Otimização de desenho experimental — Düren (Tabela 5) e Rheinbach-2**
- Análise retrospectiva do experimento de fertilização de Düren: a posição real das parcelas teve CV(K-40) = 11,2%, mas posições alternativas testadas via simulação teriam produzido CV tão baixo quanto 9,3–9,9% — ou seja, **a GS poderia ter orientado uma posição de parcelas com menor heterogeneidade de solo não explicada**, aumentando a potência estatística do experimento.
- Modelo de textura calibrado com apenas 12 parcelas (de 48) previu argila e areia nas 36 parcelas restantes com boa precisão (Argila: R²=0,69, MAE=0,96%; Areia: R²=0,81, MAE=2,2%) — demonstra viabilidade de **reduzir custos analíticos** em experimentos de parcela usando poucas amostras de calibração + GS para o restante.
- Em Rheinbach-2, o desenho do experimento de calagem foi **efetivamente modificado** com base no mapa de padrões espaciais da GS (antes mesmo de qualquer calibração quantitativa), maximizando a heterogeneidade capturada para o estudo de longo prazo de mudanças na vegetação de pastagem.

---

## 7. Discussão dos autores (síntese crítica)

- **4.1 (Aplicabilidade universal):** reforça que o modelo site-independent de Heggemann et al. (2017) **não é universalmente válido**; calibração site-specific supera consistentemente. Cita van der Klooster et al. (2011) e Coulouma et al. (2016) sobre transferibilidade condicionada à similaridade geopedológica, não apenas geográfica.
- **4.2 (Reconhecimento de padrões):** para fins de mapeamento exploratório e definição de zonas de manejo, **Total Counts (TC) sozinho já é suficiente e mais robusto** que ROIs individuais (menos sujeito a erro) — não é necessário processamento sofisticado quando o objetivo é apenas identificar padrões, não quantificar.
- **4.3 (Predição quantitativa):** MAE geralmente na mesma faixa da **incerteza laboratorial** de métodos convencionais de textura (citando Vos et al. 2016) — ou seja, a GS não é necessariamente "menos precisa" que a análise tradicional, apenas tem fontes de erro diferentes. Solos de PPSD (material periglacial complexo) e solos estratificados exigem cautela redobrada.
- **4.4 (Aplicações):** discute vantagens da calagem em taxa variável (economicamente comprovada — Mills et al. 2019) e da estimativa de FC para irrigação de precisão; nota que a GS **não mede diretamente pH ou nutrientes disponíveis**, recomendando combinação com sensores de infravermelho médio (MIRS) para dados complementares.
- **4.5 (Complementaridade com EMI):** compara com **indução eletromagnética (EMI)**, outra técnica proximal comum. GS é considerada "método direto" (mede radionuclídeos ligados à mineralogia), enquanto EMI é proxy indireto (integra argila + umidade, difícil de separar). GS é pouco afetada por umidade do solo se medida em solo seco (atenuação ~1%/1% de umidade, corrigível) e não sofre interferência de instalações metálicas — mas atinge profundidade menor (0,3–0,5 m) e fixa, enquanto EMI pode sondar múltiplas profundidades. **Combinação das duas técnicas é apontada como a mais promissora.**

---

## 8. Conclusões dos autores

1. Diferenças de geologia, mineralogia e posição na paisagem, **mesmo dentro de uma mesma unidade geopedológica**, impedem o uso universal de um modelo site-independent.
2. Reconhecimento de padrões espaciais (sem calibração numérica) funciona bem e é útil para mapeamento e amostragem — confirma H2 parcialmente.
3. Calibração local (site-specific) permite predições quantitativas com MAE <5% quando os dados de calibração cobrem variabilidade textural suficiente.
4. Aplicações demonstradas têm valor prático real: calagem de precisão, estimativa de capacidade de campo, otimização de posicionamento de parcelas experimentais.
5. **Principal obstáculo para adoção ampla:** ausência de modelo universal — os autores pedem a criação de uma **biblioteca espectral abrangente** (banco de dados padronizado de instrumentos, protocolos de amostragem, processamento) como próximo passo estratégico para o campo.

---

## 9. Pontos fortes (para uso em revisão de literatura)

- Estudo robusto, com **7 campos** em condições geopedológicas variadas — muito mais abrangente que estudos de site único, permitindo conclusões generalizáveis sobre transferibilidade (que é justamente o ponto fraco do artigo 1 desta revisão).
- Testa explicitamente e refuta (com evidência quantitativa clara) a hipótese de universalidade de modelos de calibração — contribuição metodológica importante para o campo, com implicações diretas de custo/benefício (vale a pena calibrar localmente vs. usar modelo genérico).
- Exemplos de aplicação prática muito concretos e quantificados (kg CaO/ha, % v/v de FC, CV de heterogeneidade em desenho de parcelas) — vai além da correlação estatística pura, mostrando **valor agronômico e econômico direto**.
- Publicado em revista de acesso aberto (MDPI, CC BY), com dados e figuras detalhadas, permitindo replicação/comparação direta.
- A comparação com **EMI** (seção 4.5) oferece contexto valioso sobre onde a GS se encaixa no ecossistema mais amplo de sensoriamento proximal de solo.

## 10. Limitações e pontos de atenção crítica

- O artigo depende fortemente de um estudo anterior do mesmo grupo (Heggemann et al. 2017) para o modelo SVM "site-independent" — os detalhes completos do treinamento original desse modelo não estão neste artigo, exigindo leitura cruzada da referência [8] para reprodução completa.
- Validação cruzada "leave-one-site-out" é rigorosa, mas o número de sites (10 no modelo original, ampliado aqui) ainda é limitado para generalizar sobre "toda a Alemanha" ou regiões geologicamente diferentes fora da Europa Central.
- A determinação de mineralogia da argila (esmectita vs. caulinita) foi feita com **apenas 1 análise de DRX por campo** — amostra única para explicar diferenças sistemáticas de comportamento é uma evidência qualitativa, não estatisticamente robusta (os próprios autores reconhecem isso ao dizer "not shown").
- Alguns modelos de calibração local usam **N pequeno** (ex.: 12 parcelas em Düren para o modelo de textura das 36 parcelas restantes) — R² e MAE reportados podem ser otimistas dado o tamanho amostral reduzido.
- O artigo não aborda explicitamente o **custo comparativo** (tempo, equipamento, mão de obra) entre GS site-specific (que exige campanha de calibração em cada novo campo) versus métodos laboratoriais tradicionais — a viabilidade econômica real da abordagem "recalibrar em cada site" não é quantificada.
- Diferente do artigo 1 (Taylor et al. 2023), este estudo foca **exclusivamente em textura** (areia/silte/argila) e não trata diretamente de carbono orgânico ou nitrogênio do solo — a leitura conjunta dos dois artigos é complementar, mas não deve ser confundida (mesmo fenômeno físico, variáveis-alvo diferentes).

---

## 11. Relevância para a pesquisa (LFNA) — pontos de conexão sugeridos

- Este artigo é **referência metodológica fundamental** para qualquer estudo que pretenda calibrar modelos de espectrometria gama para textura de solo — especialmente por demonstrar, com dados concretos, que **calibração local é preferível** a modelos genéricos importados de outras regiões/países.
- O conceito de **"condições geopedológicas"** como variável de confusão é central e deve ser considerado no desenho experimental de qualquer estudo próprio (ex.: necessidade de caracterizar mineralogia da fração argila, não apenas a granulometria).
- Fornece **exemplos quantitativos de aplicação agronômica** (calagem variável, capacidade de campo) que podem servir de modelo para propor aplicações práticas em um estudo próprio no contexto brasileiro/local.
- A discussão sobre complementaridade **GS + EMI** e **GS + NIRS/MIRS** (também mencionada no artigo 1) sinaliza uma tendência da área para sensoriamento multissensor integrado — relevante se a pesquisa do usuário considerar combinar técnicas.
- Ver também artigo 1 desta revisão (Taylor et al., 2023) para uma aplicação do mesmo tipo de sensor (mas modelo Medusa MS-700, não RSX-1) focada em C/N em vez de textura — leitura conjunta recomendada para visão mais completa do estado da arte em espectrometria gama proximal aplicada a solos agrícolas.

---

## 12. Referências-chave citadas no artigo (para aprofundamento)

- Heggemann, T. et al. (2017). Proximal gamma-ray spectrometry for site-independent in situ prediction of soil texture on ten heterogeneous fields in Germany using support vector machines. *Soil Tillage Res.*, 168, 99–109. *(estudo-base do modelo SVM testado neste artigo)*
- Reinhardt, N. & Herrmann, L. (2019). Gamma-ray spectrometry as versatile tool in soil science: a critical review. *J. Plant Nutr. Soil Sci.*, 182, 9–27.
- van der Klooster, E., van Egmond, F.M., Sonneveld, M.P.W. (2011). Mapping soil clay contents in Dutch marine districts using gamma-ray spectrometry. *Eur. J. Soil Sci.*, 62, 743–753.
- Coulouma, G. et al. (2016). Analysing the proximal gamma radiometry in contrasting Mediterranean landscapes... *Geoderma*, 266, 127–135.
- Priori, S., Bianconi, N., Costantini, E.A.C. (2014). Can γ-radiometrics predict soil textural data and stoniness in different parent materials? *Geoderma*, 226–227, 354–364.
- Vos, C. et al. (2016). Field-based soil-texture estimates could replace laboratory analysis. *Geoderma*, 267, 215–219.
- Dennerley, C. et al. (2018). Identifying soil management zones... using proximal sensed electromagnetic induction and gamma-ray spectrometry data. *Soil Use Manag.*, 34, 219–235.

---

*Revisão elaborada a partir da leitura integral do PDF do artigo. Documento de apoio ao estudo — recomenda-se leitura do artigo original antes de citação formal em trabalho acadêmico.*
