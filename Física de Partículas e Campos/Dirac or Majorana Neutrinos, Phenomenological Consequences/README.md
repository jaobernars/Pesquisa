# Dirac or Majorana Neutrinos — Phenomenological Consequences

**Natureza da massa dos neutrinos e suas consequências fenomenológicas**

> Pesquisa teórica em Física de Partículas e Campos sobre o formalismo dos férmions de Majorana, a matriz de mistura PMNS e a massa efetiva de Majorana no contexto do decaimento duplo beta sem neutrinos ($0\nu\beta\beta$).

---

## Sumário

- [Introdução](#introdução)
- [Motivação](#motivação)
- [Objetivos](#objetivos)
- [Fundamentação Teórica](#fundamentação-teórica)
  - [O Neutrino no Modelo Padrão](#1-o-neutrino-no-modelo-padrão)
  - [Oscilação de Neutrinos e a Matriz PMNS](#2-oscilação-de-neutrinos-e-a-matriz-pmns)
  - [Dirac vs. Majorana: Duas Naturezas Possíveis para a Massa](#3-dirac-vs-majorana-duas-naturezas-possíveis-para-a-massa)
  - [Violação do Número Leptônico e a Assimetria Matéria-Antimatéria](#4-violação-do-número-leptônico-e-a-assimetria-matéria-antimatéria)
  - [Decaimento Duplo Beta sem Neutrinos e a Massa Efetiva de Majorana](#5-decaimento-duplo-beta-sem-neutrinos-e-a-massa-efetiva-de-majorana)

---

## Introdução

Os neutrinos são partículas elementares propostas por Wolfgang Pauli em 1930 como uma "solução desesperada" para o problema do espectro contínuo observado no decaimento beta nuclear. Sem a existência de uma partícula neutra, leve e de interação fraquíssima emitida junto ao elétron, o decaimento beta pareceria violar os princípios de conservação de energia, momento linear e momento angular. A hipótese de Pauli — batizada de "neutrino" por Enrico Fermi, que a incorporou em 1934 em sua teoria quanticamente consistente do decaimento beta — preservou esses princípios fundamentais e inaugurou o estudo de uma das partículas mais abundantes e, ao mesmo tempo, mais elusivas do universo.

No arcabouço do Modelo Padrão da física de partículas, os neutrinos são férmions de spin $1/2$ pertencentes à família dos léptons, desprovidos de carga elétrica e de carga de cor, interagindo exclusivamente via força fraca (e gravitacionalmente). Existem três estados de sabor, associados aos respectivos léptons carregados: o neutrino eletrônico ($\nu_e$), o muônico ($\nu_\mu$) e o tauônico ($\nu_\tau$). Na formulação original do Modelo Padrão, os neutrinos eram tratados como partículas estritamente não massivas — uma simplificação que se mostrou incompatível com a observação experimental.

Este projeto propõe um estudo analítico e teórico da questão hoje mais fundamental em aberto sobre os neutrinos: **qual é a natureza intrínseca de sua massa?** A resposta a essa pergunta — se os neutrinos são férmions de Dirac ou de Majorana — carrega implicações que extrapolam a física de partículas, tocando a cosmologia e a própria razão pela qual existe mais matéria do que antimatéria no universo observável.

## Motivação

Durante décadas, a hipótese de neutrinos com massa nula foi sustentada tanto por conveniência teórica quanto pela ausência de evidência experimental em contrário. Esse cenário mudou de forma definitiva com os resultados dos observatórios **Super-Kamiokande** (1998, neutrinos atmosféricos) e **Sudbury Neutrino Observatory — SNO** (2001–2002, neutrinos solares), agraciados com o Prêmio Nobel de Física de 2015. Ambos os experimentos demonstraram, de forma independente e complementar, o fenômeno da **oscilação de neutrinos**: a probabilidade de um neutrino produzido em um sabor definido ser detectado em outro sabor após propagar-se por uma distância finita.

A oscilação só é possível se os autoestados de sabor ($\nu_e, \nu_\mu, \nu_\tau$) — nos quais os neutrinos são produzidos e detectados via interação fraca — forem combinações lineares de autoestados de massa ($\nu_1, \nu_2, \nu_3$), que evoluem no espaço-tempo com fases distintas por possuírem massas distintas. A observação da oscilação é, portanto, prova inequívoca de que **ao menos dois dos três neutrinos possuem massa não nula**, contrariando a formulação original do Modelo Padrão e abrindo uma das poucas janelas experimentais conhecidas para física além dele.

Entretanto, os experimentos de oscilação — por dependerem de um termo de interferência entre autoestados de massa — são sensíveis apenas às **diferenças dos quadrados das massas** ($\Delta m^2_{21}$ e $\Delta m^2_{31}$), e não à escala absoluta de massa, tampouco à natureza intrínseca dessa massa. Como os neutrinos são os únicos férmions elementares eletricamente neutros do Modelo Padrão, essa lacuna teórica admite duas soluções fisicamente distintas e experimentalmente distinguíveis, cuja elucidação está entre os objetivos mais perseguidos da física de partículas contemporânea. É essa lacuna — e suas profundas consequências fenomenológicas — que motiva o presente projeto.

## Objetivos

**Objetivo geral:** consolidar o arcabouço físico-matemático necessário para compreender como a natureza de Dirac ou de Majorana dos neutrinos determina os observáveis fenomenológicos associados à violação do número leptônico, com ênfase no decaimento duplo beta sem emissão de neutrinos ($0\nu\beta\beta$).

**Objetivos específicos:**

1. Derivar o formalismo de campo dos férmions de Majorana a partir da equação de Dirac, explicitando a condição de auto-conjugação de carga ($\psi = \psi^c$) que torna a partícula indistinguível de sua antipartícula.
2. Construir a estrutura da matriz de mistura leptônica de Pontecorvo-Maki-Nakagawa-Sakata (PMNS), incluindo a fase de violação de CP do tipo Dirac ($\delta$) e as duas fases adicionais de Majorana ($\alpha_1, \alpha_2$), ausentes no setor de quarks.
3. Formular matematicamente a massa efetiva de Majorana ($m_{\beta\beta}$) em função dos parâmetros de mistura, das massas dos autoestados e das fases de CP, relacionando-a à taxa de transição do decaimento $0\nu\beta\beta$.
4. Investigar como a confirmação da hipótese de Majorana e a consequente violação do número leptônico se conectam mecanismos de geração da assimetria bariônica do universo primordial (leptogênese).
5. Revisar criticamente a literatura teórica e experimental sobre o tema, situando o formalismo derivado no contexto dos limites experimentais atuais sobre $m_{\beta\beta}$.

## Fundamentação Teórica

### 1. O Neutrino no Modelo Padrão

No setor eletrofraco do Modelo Padrão, os neutrinos surgem como a componente neutra dos dubletos de isospin fraco left-handed, sem um parceiro right-handed correspondente na formulação mínima da teoria. Essa ausência é, por construção, a razão pela qual o mecanismo usual de Brout-Englert-Higgs — responsável por gerar a massa dos quarks e dos léptons carregados via acoplamento de Yukawa entre as componentes left- e right-handed de cada férmion — não pode gerar massa para os neutrinos sem uma extensão do conteúdo de campos da teoria.

### 2. Oscilação de Neutrinos e a Matriz PMNS

Os autoestados de sabor, produzidos e detectados via interações de corrente carregada, relacionam-se aos autoestados de massa através da matriz unitária PMNS:

$$\left|\nu_\alpha\right\rangle = \sum_{i=1}^{3} U_{\alpha i}^{*} \left|\nu_i\right\rangle, \qquad \alpha = e, \mu, \tau$$

A propagação de cada autoestado de massa $\nu_i$ acumula uma fase dependente de sua energia e, portanto, de sua massa $m_i$, dando origem a uma probabilidade de transição entre sabores que oscila em função da razão $L/E$ (distância percorrida sobre energia do neutrino) e dos parâmetros $\Delta m^2_{ij} = m_i^2 - m_j^2$. É precisamente por depender apenas dessas diferenças de quadrados de massa que a oscilação, embora comprove a existência de massa, é cega à escala absoluta e à natureza (Dirac ou Majorana) dessa massa.

### 3. Dirac vs. Majorana: Duas Naturezas Possíveis para a Massa

A distinção entre as duas hipóteses está na estrutura do termo de massa admitido pela teoria de campos:

- **Massa de Dirac:** exige a introdução de neutrinos right-handed estéreis $\nu_R$ (singletos de isospin fraco, sem carga sob o grupo de gauge do Modelo Padrão) e gera a massa via o acoplamento de Yukawa usual com o campo de Higgs, $\mathcal{L}_D = -y_\nu \, \bar{L}\, \tilde{\phi}\, \nu_R + \text{h.c.}$, resultando em um termo $m_D\, \bar{\nu}_L \nu_R$. Nesse cenário, neutrino e antineutrino permanecem estados distintos, distinguidos por número leptônico $L = +1$ e $L = -1$, e a pequenez da massa observada exigiria acoplamentos de Yukawa extraordinariamente pequenos ($y_\nu \sim 10^{-12}$), sem explicação estrutural dentro do modelo.
- **Massa de Majorana:** explora o fato de que um férmion eletricamente neutro admite um termo de massa que conecta o campo à sua própria conjugação de carga, $\mathcal{L}_M = -\tfrac{1}{2} m_M\, \overline{\nu^c}\, \nu + \text{h.c.}$ Esse termo não é permitido para férmions carregados (violaria conservação de carga elétrica), mas é perfeitamente consistente para o neutrino. Nesse cenário, $\nu \equiv \nu^c$: a partícula é sua própria antipartícula, e o número leptônico deixa de ser uma simetria conservada. Massas de Majorana pequenas surgem naturalmente de mecanismos como o **seesaw**, em que a leveza dos neutrinos observados é suprimida pela razão entre a escala eletrofraca e uma escala de nova física muito mais alta.

### 4. Violação do Número Leptônico e a Assimetria Matéria-Antimatéria

A confirmação da natureza de Majorana implica diretamente a violação da conservação do número leptônico total ($\Delta L = 2$) em processos fundamentais. Essa violação, combinada à violação de CP nas fases da matriz PMNS, fornece os três ingredientes das condições de Sakharov necessários para gerar dinamicamente uma assimetria entre matéria e antimatéria a partir de um universo primordial simétrico. O mecanismo de **leptogênese** — no qual um excesso de número leptônico gerado no universo primordial é parcialmente convertido em excesso de número bariônico por processos eletrofracos (esfalerons) — depende crucialmente da existência de neutrinos de Majorana pesados, conectando a fenomenologia de baixas energias estudada neste projeto à cosmologia do universo primordial.

### 5. Decaimento Duplo Beta sem Neutrinos e a Massa Efetiva de Majorana

O canal fenomenológico mais promissor para testar a hipótese de Majorana em laboratório é a busca pelo **decaimento duplo beta sem emissão de neutrinos** ($0\nu\beta\beta$):

$$(A, Z) \rightarrow (A, Z+2) + 2e^{-}$$

Diferentemente do decaimento duplo beta padrão (permitido no Modelo Padrão e já observado, $2\nu\beta\beta$, que emite dois antineutrinos), o processo $0\nu\beta\beta$ não emite neutrinos no estado final — um antineutrino virtual emitido em um dos vértices é absorvido como neutrino no segundo vértice, o que só é cinematicamente possível se a partícula trocada for idêntica à sua antipartícula, isto é, se o neutrino for um férmion de Majorana. A taxa de decaimento é proporcional ao quadrado da chamada **massa efetiva de Majorana**:

$$m_{\beta\beta} = \left| \sum_{i=1}^{3} U_{ei}^2\, m_i \right| = \left| m_1 |U_{e1}|^2 + m_2 |U_{e2}|^2 e^{i\alpha_1} + m_3 |U_{e3}|^2 e^{i\alpha_2} \right|$$

Note-se que $m_{\beta\beta}$ depende explicitamente das fases de Majorana $\alpha_1, \alpha_2$ — que não são acessíveis por experimentos de oscilação, precisamente porque estes são insensíveis à natureza de Dirac ou Majorana da massa. A observação de $0\nu\beta\beta$ estabeleceria, portanto, não apenas a natureza de Majorana dos neutrinos, mas forneceria também uma medida da escala absoluta de massa e um vínculo direto sobre suas fases de violação de CP.
