# O Formalismo da Teoria Quântica de Campos

**Review Lecture — Física de Partículas e Campos**

*Construção sistemática do formalismo: da teoria clássica de campos e do teorema de Noether à quantização canônica, à matriz S, às integrais de trajetória, à renormalização e ao grupo de renormalização, com uma parte dedicada aos campos fermiônicos e um apêndice que conecta a estrutura geral ao formalismo dos férmions de Majorana.*

---

## Resumo

A teoria quântica de campos é a estrutura que resulta de exigir simultaneamente mecânica quântica, invariância de Lorentz e localidade. Este documento constrói essa estrutura em oito partes. **Parte I** estabelece a base clássica: princípio de ação, teorema de Noether em suas duas formas, tensor energia-momento de Belinfante, e a classificação de Wigner das representações unitárias irredutíveis do grupo de Poincaré — que é o que define, a priori, o que pode ser uma partícula. **Parte II** quantiza canonicamente os campos escalar e vetorial, estabelece o espaço de Fock, deduz a estrutura de propagadores e prova microcausalidade. **Parte III** é dedicada aos campos fermiônicos: representação espinorial, equação de Dirac, a necessidade dos anticomutadores, o teorema spin-estatística, variáveis de Grassmann, regras de Feynman fermiônicas e a anomalia quiral. **Parte IV** constrói a teoria de perturbação — quadro de interação, teorema de Wick, diagramas, redução LSZ, unitariedade e teorema óptico. **Parte V** reformula tudo por integrais de trajetória, chegando ao funcional gerador, à ação efetiva, ao procedimento de Faddeev–Popov e à simetria BRST. **Parte VI** trata da renormalização: contagem de potências, regularização dimensional, contratermos, grupo de renormalização e teoria efetiva de campos. **Parte VII** cobre quebra espontânea de simetria, mecanismo de Higgs, teorias de Yang–Mills e anomalias de gauge. Sete apêndices consolidam convenções, integrais de laço, integração de Berezin, teoria de grupos, a representação de Källén–Lehmann e as regras de Feynman de referência. O **Apêndice G** conecta explicitamente todo o formalismo ao caso de Majorana — incluindo o resultado de que a integral funcional de um campo de Majorana produz um **Pfaffiano** onde a de Dirac produz um determinante, o que é a origem estrutural do célebre fator $1/2$.

---

## Sumário

**Parte 0**
- [0. Convenções e notação](#0-convenções-e-notação)

**Parte I — Fundamentos Clássicos e Simetrias**
- [1. Por que teoria quântica de campos](#1-por-que-teoria-quântica-de-campos)
- [2. Teoria clássica de campos](#2-teoria-clássica-de-campos)
- [3. O teorema de Noether](#3-o-teorema-de-noether)
- [4. O grupo de Poincaré e a classificação de Wigner](#4-o-grupo-de-poincaré-e-a-classificação-de-wigner)

**Parte II — Quantização Canônica**
- [5. O campo escalar real](#5-o-campo-escalar-real)
- [6. O campo escalar complexo e a carga](#6-o-campo-escalar-complexo-e-a-carga)
- [7. Causalidade, comutadores e propagadores](#7-causalidade-comutadores-e-propagadores)
- [8. O campo vetorial](#8-o-campo-vetorial)

**Parte III — Campos Fermiônicos**
- [9. A representação espinorial do grupo de Lorentz](#9-a-representação-espinorial-do-grupo-de-lorentz)
- [10. A equação de Dirac e suas soluções](#10-a-equação-de-dirac-e-suas-soluções)
- [11. Quantização do campo de Dirac](#11-quantização-do-campo-de-dirac)
- [12. O propagador fermiônico](#12-o-propagador-fermiônico)
- [13. Bilineares, correntes e quiralidade](#13-bilineares-correntes-e-quiralidade)
- [14. O teorema spin-estatística](#14-o-teorema-spin-estatística)
- [15. Férmions no formalismo funcional](#15-férmions-no-formalismo-funcional)
- [16. Regras de Feynman fermiônicas e o teorema de Furry](#16-regras-de-feynman-fermiônicas-e-o-teorema-de-furry)
- [17. A anomalia quiral](#17-a-anomalia-quiral)

**Parte IV — Teoria de Perturbação e a Matriz S**
- [18. Quadro de interação e série de Dyson](#18-quadro-de-interação-e-série-de-dyson)
- [19. O teorema de Wick](#19-o-teorema-de-wick)
- [20. Diagramas de Feynman](#20-diagramas-de-feynman)
- [21. A redução LSZ](#21-a-redução-lsz)
- [22. Unitariedade e o teorema óptico](#22-unitariedade-e-o-teorema-óptico)
- [23. Observáveis: seções de choque e larguras](#23-observáveis-seções-de-choque-e-larguras)

**Parte V — Integrais de Trajetória**
- [24. Da mecânica quântica à integral funcional](#24-da-mecânica-quântica-à-integral-funcional)
- [25. Funcional gerador e ação efetiva](#25-funcional-gerador-e-ação-efetiva)
- [26. Campos de gauge: o procedimento de Faddeev–Popov](#26-campos-de-gauge-o-procedimento-de-faddeevpopov)
- [27. BRST e identidades de Ward–Takahashi](#27-brst-e-identidades-de-wardtakahashi)

**Parte VI — Renormalização**
- [28. Divergências e contagem de potências](#28-divergências-e-contagem-de-potências)
- [29. Regularização](#29-regularização)
- [30. Contratermos e esquemas de renormalização](#30-contratermos-e-esquemas-de-renormalização)
- [31. O grupo de renormalização](#31-o-grupo-de-renormalização)
- [32. Teoria efetiva de campos](#32-teoria-efetiva-de-campos)

**Parte VII — Simetrias Quebradas e Teorias de Gauge**
- [33. Quebra espontânea de simetria e o teorema de Goldstone](#33-quebra-espontânea-de-simetria-e-o-teorema-de-goldstone)
- [34. O mecanismo de Higgs](#34-o-mecanismo-de-higgs)
- [35. Teorias de Yang–Mills](#35-teorias-de-yangmills)
- [36. Anomalias de gauge e seu cancelamento](#36-anomalias-de-gauge-e-seu-cancelamento)

**Parte VIII**
- [37. Síntese](#37-síntese)

**Apêndices**
- [A. Convenções, unidades naturais e matrizes gama](#apêndice-a--convenções-unidades-naturais-e-matrizes-gama)
- [B. Integrais de laço e regularização dimensional](#apêndice-b--integrais-de-laço-e-regularização-dimensional)
- [C. Álgebra de Grassmann e integração de Berezin](#apêndice-c--álgebra-de-grassmann-e-integração-de-berezin)
- [D. Grupos de Lie, representações e fatores de cor](#apêndice-d--grupos-de-lie-representações-e-fatores-de-cor)
- [E. A representação de Källén–Lehmann](#apêndice-e--a-representação-de-källénlehmann)
- [F. Regras de Feynman de referência](#apêndice-f--regras-de-feynman-de-referência)
- [G. Do formalismo geral aos férmions de Majorana](#apêndice-g--do-formalismo-geral-aos-férmions-de-majorana)
- [Referências](#referências)

---

# Parte 0

## 0. Convenções e notação

Este documento usa **exatamente as mesmas convenções** do documento companheiro *Formalismo dos Férmions de Majorana*, de modo que os dois possam ser lidos em conjunto sem tradução de sinais.

$$\hbar=c=1,\qquad \eta_{\mu\nu}=\operatorname{diag}(+1,-1,-1,-1),\qquad \varepsilon^{0123}=+1.\tag{0.1}$$

$$\{\gamma^{\mu},\gamma^{\nu}\}=2\eta^{\mu\nu},\qquad \gamma^{\mu\dagger}=\gamma^{0}\gamma^{\mu}\gamma^{0},\qquad \gamma^{5}=i\gamma^{0}\gamma^{1}\gamma^{2}\gamma^{3},\tag{0.2}$$

$$P_{L}=\frac{1-\gamma^{5}}{2},\qquad P_{R}=\frac{1+\gamma^{5}}{2},\qquad \sigma^{\mu\nu}=\frac{i}{2}[\gamma^{\mu},\gamma^{\nu}],\qquad \bar\psi=\psi^{\dagger}\gamma^{0}.\tag{0.3}$$

$$C\gamma^{\mu T}C^{-1}=-\gamma^{\mu},\qquad C^{T}=-C,\qquad C^{\dagger}=C^{-1},\qquad C=i\gamma^{2}\gamma^{0}\ \text{(bases de Dirac e quiral)}.\tag{0.4}$$

**Medidas e normalizações.** Usamos a normalização covariante para estados de uma partícula:

$$|p\rangle = \sqrt{2E_{p}}\;a^{\dagger}_{\mathbf{p}}|0\rangle,\qquad \langle p|q\rangle = (2\pi)^{3}\,2E_{p}\,\delta^{3}(\mathbf{p}-\mathbf{q}),\tag{0.5}$$

$$\int\!\widetilde{dp}\;\equiv\;\int\!\frac{d^{3}p}{(2\pi)^{3}\,2E_{p}}=\int\!\frac{d^{4}p}{(2\pi)^{4}}\,2\pi\,\delta(p^{2}-m^{2})\,\theta(p^{0}),\tag{0.6}$$

esta última sendo manifestamente invariante de Lorentz.

**Transformada de Fourier.** $\displaystyle f(x)=\int\!\frac{d^{4}p}{(2\pi)^{4}}\,e^{-ip\cdot x}\tilde f(p)$, com $p\cdot x = p^{0}x^{0}-\mathbf{p}\cdot\mathbf{x}$.

**Dimensões em unidades naturais.** $[\text{massa}]=[\text{energia}]=[\text{momento}]=[\text{comprimento}]^{-1}=[\text{tempo}]^{-1}$. Em $D=4$: $[\mathcal{L}]=4$, $[\phi]=1$, $[\psi]=3/2$, $[A_{\mu}]=1$, $[\partial_{\mu}]=1$. Um acoplamento associado a um operador de dimensão $d$ tem dimensão $4-d$.

**Convenção de índices.** Repetidos somam-se. Índices de sabor/cor são explicitados quando necessário. $\partial_{\mu}\equiv\partial/\partial x^{\mu}$, $\Box \equiv \partial_{\mu}\partial^{\mu}$.

---

# Parte I — Fundamentos Clássicos e Simetrias

## 1. Por que teoria quântica de campos

### 1.1 O fracasso da mecânica quântica relativística de partícula única

Tentar quantizar uma única partícula relativística leva a três obstruções que não são técnicas, mas estruturais.

**(i) Estados de energia negativa.** A relação $E^{2}=\mathbf{p}^{2}+m^{2}$ tem duas raízes. Em uma teoria de partícula única, $E=-\sqrt{\mathbf{p}^{2}+m^{2}}$ não pode ser descartada: as interações induzem transições para esses estados, e o espectro é ilimitado por baixo. O "mar de Dirac" resolve o problema para férmions ao custo de introduzir infinitas partículas — ou seja, ao custo de abandonar a teoria de partícula única.

**(ii) Não conservação do número de partículas.** Para $E>2m$, o processo $a\to a+b\bar b$ é cinematicamente permitido. Nenhuma teoria com espaço de Hilbert de dimensão fixa em número de partículas pode descrevê-lo. O espaço de estados correto é a soma direta

$$\mathcal{F}=\bigoplus_{n=0}^{\infty}\mathcal{H}^{(n)},\tag{1.1}$$

o **espaço de Fock**.

**(iii) Causalidade.** A amplitude de propagação de uma partícula livre relativística entre pontos separados tipo espaço,

$$\langle \mathbf{x}|e^{-iHt}|\mathbf{y}\rangle \;\sim\; e^{-m\sqrt{|\mathbf{x}-\mathbf{y}|^{2}-t^{2}}},\tag{1.2}$$

é exponencialmente pequena mas **não nula**. A causalidade só é recuperada quando a contribuição de "partícula indo de $y$ a $x$" cancela a de "antipartícula indo de $x$ a $y$" — o que exige que ambas existam com a mesma massa. **A existência de antipartículas é uma consequência da causalidade, não uma hipótese adicional.**

### 1.2 A resolução

A teoria quântica de campos resolve os três problemas simultaneamente ao promover o campo — e não a posição da partícula — ao status de variável dinâmica fundamental:

- O campo $\phi(x)$ é um **operador** definido em cada ponto do espaço-tempo; $x$ é um rótulo, não um observável.
- Os estados de partícula são excitações do vácuo: $|p\rangle\propto a^{\dagger}_{p}|0\rangle$, com $n$ partículas obtidas por aplicações repetidas.
- A localidade é implementada como **microcausalidade**: $[\mathcal{O}(x),\mathcal{O}(y)]=0$ para $(x-y)^{2}<0$ (§7.2).

### 1.3 O que a estrutura impõe

Três resultados são consequências puramente estruturais e serão demonstrados adiante:

| Resultado | Onde | Conteúdo |
|:---|:---|:---|
| Existência de antipartículas | §6, §7.2 | Exigida pela microcausalidade |
| Teorema spin-estatística | §14 | Spin inteiro $\Rightarrow$ Bose; semi-inteiro $\Rightarrow$ Fermi |
| Teorema $CPT$ | §14.4 | Toda TQC local, hermitiana e Lorentz-invariante é $CPT$-invariante |

---

## 2. Teoria clássica de campos

### 2.1 Ação e equações de campo

Um campo é uma aplicação $\phi^{a}:\mathbb{R}^{1,3}\to V$, com $V$ o espaço-alvo carregando uma representação do grupo de Lorentz. A dinâmica é gerada pela ação

$$S[\phi]=\int d^{4}x\;\mathcal{L}\!\left(\phi^{a},\partial_{\mu}\phi^{a}\right).\tag{2.1}$$

A restrição de $\mathcal{L}$ a depender apenas do campo e de suas **primeiras** derivadas, no mesmo ponto, é a implementação da **localidade**; a exigência de que $\mathcal{L}$ seja um escalar de Lorentz é a implementação da **invariância relativística**.

Exigindo $\delta S=0$ com $\delta\phi=0$ na fronteira:

$$\delta S = \int d^{4}x\left[\frac{\partial\mathcal{L}}{\partial\phi^{a}}\delta\phi^{a}+\frac{\partial\mathcal{L}}{\partial(\partial_{\mu}\phi^{a})}\partial_{\mu}\delta\phi^{a}\right] = \int d^{4}x\left[\frac{\partial\mathcal{L}}{\partial\phi^{a}}-\partial_{\mu}\frac{\partial\mathcal{L}}{\partial(\partial_{\mu}\phi^{a})}\right]\delta\phi^{a},\tag{2.2}$$

$$\boxed{\;\partial_{\mu}\frac{\partial\mathcal{L}}{\partial(\partial_{\mu}\phi^{a})}-\frac{\partial\mathcal{L}}{\partial\phi^{a}}=0\;}\tag{2.3}$$

**Exemplos canônicos.**

$$\mathcal{L}_{\rm KG}=\frac{1}{2}\partial_{\mu}\phi\,\partial^{\mu}\phi-\frac{1}{2}m^{2}\phi^{2}\;\;\Longrightarrow\;\;\left(\Box+m^{2}\right)\phi=0,\tag{2.4}$$

$$\mathcal{L}_{\rm Dirac}=\bar\psi\left(i\gamma^{\mu}\partial_{\mu}-m\right)\psi\;\;\Longrightarrow\;\;\left(i\not{\partial}-m\right)\psi=0,\tag{2.5}$$

$$\mathcal{L}_{\rm Maxwell}=-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}\;\;\Longrightarrow\;\;\partial_{\mu}F^{\mu\nu}=0,\qquad F_{\mu\nu}=\partial_{\mu}A_{\nu}-\partial_{\nu}A_{\mu}.\tag{2.6}$$

### 2.2 Formalismo hamiltoniano

$$\pi_{a}(x)=\frac{\partial\mathcal{L}}{\partial\dot\phi^{a}(x)},\qquad \mathcal{H}=\pi_{a}\dot\phi^{a}-\mathcal{L},\qquad H=\int d^{3}x\;\mathcal{H}.\tag{2.7}$$

Os parênteses de Poisson a tempos iguais,

$$\left\{\phi^{a}(t,\mathbf{x}),\pi_{b}(t,\mathbf{y})\right\}_{\rm PB}=\delta^{a}_{b}\,\delta^{3}(\mathbf{x}-\mathbf{y}),\tag{2.8}$$

são o que a quantização canônica promove a comutadores (bósons) ou anticomutadores (férmions). O formalismo hamiltoniano **quebra a covariância manifesta** ao singularizar $t$ — o preço de ter uma estrutura de espaço de Hilbert explícita. A covariância é recuperada no fim (as amplitudes são invariantes), e o formalismo funcional da Parte V a mantém manifesta o tempo todo.

> **Vínculos.** Quando (2.7) não é invertível para $\dot\phi$ — o caso de campos de gauge, em que $\pi^{0}=\partial\mathcal{L}/\partial\dot A_{0}=0$ identicamente — o sistema é **vinculado** e requer o procedimento de Dirac (classificação em vínculos de primeira e segunda classe, parênteses de Dirac). Isso é tratado em §8.2 para Maxwell e resolvido de forma mais econômica pelo método de Faddeev–Popov em §26.

### 2.3 O tensor energia-momento

Sob translações $x^{\mu}\to x^{\mu}+a^{\mu}$, a corrente de Noether (§3) é o tensor energia-momento canônico

$$T^{\mu\nu}_{\rm can} = \frac{\partial\mathcal{L}}{\partial(\partial_{\mu}\phi^{a})}\,\partial^{\nu}\phi^{a}-\eta^{\mu\nu}\mathcal{L},\qquad \partial_{\mu}T^{\mu\nu}_{\rm can}=0.\tag{2.9}$$

Este tensor tem dois defeitos: em geral **não é simétrico** ($T^{\mu\nu}\neq T^{\nu\mu}$) e, para campos de gauge, não é invariante de gauge. Ambos são corrigidos pela **melhoria de Belinfante**: como $T^{\mu\nu}$ só é fisicamente definido a menos de um termo identicamente conservado,

$$T^{\mu\nu}_{B}=T^{\mu\nu}_{\rm can}+\partial_{\lambda}K^{\lambda\mu\nu},\qquad K^{\lambda\mu\nu}=-K^{\mu\lambda\nu},\tag{2.10}$$

a antissimetria de $K$ garante $\partial_{\mu}\partial_{\lambda}K^{\lambda\mu\nu}\equiv0$ e as cargas $P^{\nu}=\int d^{3}x\,T^{0\nu}$ não mudam. Existe sempre uma escolha de $K$ tornando $T^{\mu\nu}_{B}$ simétrico e invariante de gauge; $T^{\mu\nu}_{B}$ é o tensor que acopla à gravitação.

**Verificação em Maxwell.** $T^{\mu\nu}_{\rm can}=-F^{\mu\lambda}\partial^{\nu}A_{\lambda}+\tfrac14\eta^{\mu\nu}F^{2}$ não é simétrico nem invariante de gauge. Com $K^{\lambda\mu\nu}=F^{\mu\lambda}A^{\nu}$:

$$T^{\mu\nu}_{B}=-F^{\mu\lambda}F^{\nu}{}_{\lambda}+\frac{1}{4}\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta},\tag{2.11}$$

simétrico, invariante de gauge e com traço nulo (refletindo a invariância conforme de Maxwell em $D=4$), com $T^{00}_{B}=\tfrac12(\mathbf{E}^{2}+\mathbf{B}^{2})$ — a densidade de energia correta. $\checkmark$

---

## 3. O teorema de Noether

### 3.1 Primeiro teorema: simetrias globais

**Teorema.** Seja $\phi^{a}\to\phi^{a}+\epsilon\,\Delta^{a}(\phi,\partial\phi)$ uma transformação infinitesimal contínua que deixa a ação invariante, no sentido de que a lagrangiana muda no máximo por uma derivada total,

$$\delta\mathcal{L}=\epsilon\,\partial_{\mu}\mathcal{J}^{\mu}.\tag{3.1}$$

Então a corrente

$$\boxed{\;j^{\mu}=\frac{\partial\mathcal{L}}{\partial(\partial_{\mu}\phi^{a})}\,\Delta^{a}-\mathcal{J}^{\mu}\;}\tag{3.2}$$

é conservada, $\partial_{\mu}j^{\mu}=0$, e a carga $Q=\int d^{3}x\,j^{0}$ é constante no tempo.

*Demonstração.* Calculando $\delta\mathcal{L}$ diretamente da variação do campo,

$$\delta\mathcal{L}=\epsilon\left[\frac{\partial\mathcal{L}}{\partial\phi^{a}}\Delta^{a}+\frac{\partial\mathcal{L}}{\partial(\partial_{\mu}\phi^{a})}\partial_{\mu}\Delta^{a}\right] = \epsilon\left\{\underbrace{\left[\frac{\partial\mathcal{L}}{\partial\phi^{a}}-\partial_{\mu}\frac{\partial\mathcal{L}}{\partial(\partial_{\mu}\phi^{a})}\right]}_{=\,0\ \text{on-shell}}\Delta^{a}+\partial_{\mu}\!\left[\frac{\partial\mathcal{L}}{\partial(\partial_{\mu}\phi^{a})}\Delta^{a}\right]\right\}.$$

Igualando a (3.1): $\partial_{\mu}\left[\frac{\partial\mathcal{L}}{\partial(\partial_{\mu}\phi^{a})}\Delta^{a}-\mathcal{J}^{\mu}\right]=0$. $\blacksquare$

**Observação essencial.** A conservação vale **on-shell**, isto é, sobre soluções das equações de movimento. Na teoria quântica isso se traduz nas identidades de Ward, que valem como identidades entre funções de Green a menos de termos de contato (§27).

### 3.2 Exemplos

| Simetria | $\Delta$ | Corrente | Carga |
|:---|:---|:---|:---|
| Translação $x\to x+a$ | $\Delta^{a}_{\nu}=\partial_{\nu}\phi^{a}$ | $T^{\mu}{}_{\nu}$ | $P^{\nu}$ (energia-momento) |
| Lorentz $x\to\Lambda x$ | $\Delta\ \text{orbital}+\text{spin}$ | $M^{\mu\rho\sigma}$ | $J^{\rho\sigma}$ (momento angular) |
| $U(1)$: $\phi\to e^{i\alpha}\phi$ | $i\phi$ | $j^{\mu}=i(\phi^{*}\partial^{\mu}\phi-\phi\,\partial^{\mu}\phi^{*})$ | $Q$ (carga) |
| Quiral: $\psi\to e^{i\alpha\gamma^{5}}\psi$ | $i\gamma^{5}\psi$ | $j^{\mu5}=\bar\psi\gamma^{\mu}\gamma^{5}\psi$ | $Q_{5}$ (quiral) |

A corrente de momento angular contém uma parte orbital e uma parte de **spin** intrínseca:

$$M^{\mu\rho\sigma}=x^{\rho}T^{\mu\sigma}-x^{\sigma}T^{\mu\rho}+\frac{\partial\mathcal{L}}{\partial(\partial_{\mu}\phi^{a})}\left(\Sigma^{\rho\sigma}\right)^{a}{}_{b}\,\phi^{b},\tag{3.3}$$

com $\Sigma^{\rho\sigma}$ os geradores da representação de Lorentz sob a qual $\phi$ se transforma. Para um campo escalar $\Sigma=0$; para Dirac, $\Sigma^{\rho\sigma}=\tfrac12\sigma^{\rho\sigma}$.

### 3.3 Segundo teorema: simetrias locais

Quando o parâmetro da simetria é uma função arbitrária $\epsilon(x)$ — uma **simetria de gauge** —, o teorema de Noether produz não uma lei de conservação nova, mas **identidades entre as equações de movimento**. Para $\delta A_{\mu}=\partial_{\mu}\epsilon(x)$ em eletrodinâmica:

$$\partial_{\nu}\!\left(\frac{\delta S}{\delta A_{\nu}}\right)\equiv 0,\tag{3.4}$$

identicamente, sem usar as equações de movimento. Consequências:

1. As equações de movimento **não são todas independentes** — há uma relação diferencial entre elas. Concretamente, $\partial_{\mu}F^{\mu\nu}=j^{\nu}$ só é consistente se $\partial_{\nu}j^{\nu}=0$: **a invariância de gauge implica conservação de carga**.
2. O sistema é **vinculado**: a lei de Gauss $\nabla\cdot\mathbf{E}=\rho$ não contém $\ddot A$ e é um vínculo, não uma equação de evolução.
3. Uma simetria de gauge **não é uma simetria física** — é uma redundância de descrição. Estados relacionados por gauge são o mesmo estado físico. Isso é o que torna a quantização de campos de gauge não trivial (§8.2, §26).

---

## 4. O grupo de Poincaré e a classificação de Wigner

### 4.1 A álgebra

O grupo de Poincaré $\mathcal{P}=\mathbb{R}^{1,3}\rtimes SO(1,3)^{\uparrow}_{+}$ tem geradores $P^{\mu}$ (translações) e $M^{\mu\nu}$ (Lorentz), com

$$[P^{\mu},P^{\nu}]=0,\tag{4.1}$$

$$[M^{\mu\nu},P^{\rho}]=i\left(\eta^{\nu\rho}P^{\mu}-\eta^{\mu\rho}P^{\nu}\right),\tag{4.2}$$

$$[M^{\mu\nu},M^{\rho\sigma}]=i\left(\eta^{\nu\rho}M^{\mu\sigma}-\eta^{\mu\rho}M^{\nu\sigma}-\eta^{\nu\sigma}M^{\mu\rho}+\eta^{\mu\sigma}M^{\nu\rho}\right).\tag{4.3}$$

### 4.2 Os Casimires

$$C_{1}=P^{2}=P_{\mu}P^{\mu},\qquad C_{2}=W^{2}=W_{\mu}W^{\mu},\qquad W^{\mu}\equiv-\frac{1}{2}\varepsilon^{\mu\nu\rho\sigma}P_{\nu}M_{\rho\sigma},\tag{4.4}$$

com $W^{\mu}$ o **vetor de Pauli–Lubanski**. Ambos comutam com todos os geradores; por Schur, são múltiplos da identidade em cada representação irredutível. Seus autovalores rotulam as representações.

### 4.3 O método do pequeno grupo (Wigner, 1939)

O procedimento de Wigner para construir as representações unitárias irredutíveis de $\mathcal{P}$:

1. Escolha um momento de referência $k^{\mu}$ em cada órbita de $P^{2}$.
2. Identifique o **pequeno grupo** (*little group*) $G_{k}$: o subgrupo de Lorentz que deixa $k$ invariante.
3. As representações irredutíveis de $\mathcal{P}$ são induzidas pelas representações irredutíveis de $G_{k}$.

| Órbita | $k^{\mu}$ de referência | Pequeno grupo | Rótulos | Realização física |
|:---|:---|:---|:---|:---|
| $P^{2}=m^{2}>0$, $p^{0}>0$ | $(m,0,0,0)$ | $SO(3)\simeq SU(2)$ | $m,\;s=0,\tfrac12,1,\ldots$ | partícula massiva, $2s+1$ estados |
| $P^{2}=0$, $p^{0}>0$ | $(E,0,0,E)$ | $ISO(2)$ | $h=0,\pm\tfrac12,\pm1,\ldots$ | partícula sem massa, $2$ estados ($\pm h$) |
| $P^{2}=0$, $P^{\mu}=0$ | $0$ | $SO(1,3)$ | — | vácuo |
| $P^{2}<0$ | $(0,0,0,\kappa)$ | $SO(1,2)$ | — | táquions (excluídos) |

Para o caso massivo, $W^{2}=-m^{2}s(s+1)$; para o caso sem massa, $W^{2}=0$ e $W^{\mu}=h\,P^{\mu}$, com $h$ a **helicidade**.

**O ponto central.** A classificação de Wigner define o que uma partícula *é*, do ponto de vista de simetria: uma representação unitária irredutível do grupo de Poincaré. O conteúdo de uma teoria quântica de campos é, no fim, o conjunto de tais representações que seu espectro realiza.

### 4.4 Campos versus estados

Existe uma distinção que causa confusão constante:

- **Estados** de uma partícula formam representações **unitárias** de $\mathcal{P}$ — necessariamente de dimensão infinita (o grupo é não compacto), com os rótulos discretos $(m,s)$ acima.
- **Campos** $\phi^{a}(x)$ transformam-se em representações de **dimensão finita** e **não unitárias** do grupo de Lorentz:
$$U(\Lambda)\,\phi^{a}(x)\,U(\Lambda)^{-1}=D^{a}{}_{b}(\Lambda^{-1})\,\phi^{b}(\Lambda x),\tag{4.5}$$
classificadas por $(j_{-},j_{+})$ com $j_{\pm}$ semi-inteiros (§9.1): escalar $(0,0)$, Weyl $(\tfrac12,0)$ e $(0,\tfrac12)$, vetor $(\tfrac12,\tfrac12)$, Dirac $(\tfrac12,0)\oplus(0,\tfrac12)$.

O papel do campo é servir de **intertwiner**: um objeto local que, agindo no vácuo, cria os estados da representação unitária. A relação entre a representação finita do campo e o spin dos estados que ele cria é o conteúdo do teorema spin-estatística (§14) e da contagem de graus de liberdade (§8.3).

Uma consequência importante e frequentemente subestimada: **para partículas sem massa de helicidade $|h|\geq1$, não existe campo local que se transforme covariantemente e crie apenas os estados físicos.** É por isso que o fóton exige um campo $A_{\mu}$ com graus de liberdade espúrios e uma simetria de gauge para removê-los — a invariância de gauge é a resposta a uma obstrução de teoria de representações, não uma escolha estética.

---

# Parte II — Quantização Canônica

## 5. O campo escalar real

### 5.1 Quantização

$$\mathcal{L}=\frac{1}{2}\partial_{\mu}\phi\partial^{\mu}\phi-\frac{1}{2}m^{2}\phi^{2},\qquad \pi=\dot\phi,\qquad \mathcal{H}=\frac{1}{2}\pi^{2}+\frac{1}{2}(\nabla\phi)^{2}+\frac{1}{2}m^{2}\phi^{2}.\tag{5.1}$$

A quantização canônica promove (2.8) a comutadores a tempos iguais:

$$\left[\phi(t,\mathbf{x}),\pi(t,\mathbf{y})\right]=i\,\delta^{3}(\mathbf{x}-\mathbf{y}),\qquad [\phi,\phi]=[\pi,\pi]=0.\tag{5.2}$$

### 5.2 Expansão em modos e o espaço de Fock

Resolvendo a equação de Klein–Gordon e impondo hermiticidade $\phi=\phi^{\dagger}$:

$$\boxed{\;\phi(x)=\int\!\widetilde{dp}\;\left[a_{\mathbf{p}}\,e^{-ip\cdot x}+a^{\dagger}_{\mathbf{p}}\,e^{+ip\cdot x}\right]_{p^{0}=E_{p}}\;}\tag{5.3}$$

$$\left[a_{\mathbf{p}},a^{\dagger}_{\mathbf{q}}\right]=(2\pi)^{3}\,2E_{p}\,\delta^{3}(\mathbf{p}-\mathbf{q}),\qquad [a,a]=[a^{\dagger},a^{\dagger}]=0.\tag{5.4}$$

**Verificação de consistência.** Substituindo (5.3) em (5.2) e usando (5.4) reproduz-se $i\delta^{3}$; e reciprocamente, (5.4) segue de (5.2) por inversão de Fourier. As duas formulações são equivalentes.

O espaço de Fock é gerado a partir do vácuo $a_{\mathbf{p}}|0\rangle=0$:

$$|p_{1}\ldots p_{n}\rangle = a^{\dagger}_{\mathbf{p}_{1}}\cdots a^{\dagger}_{\mathbf{p}_{n}}|0\rangle,\tag{5.5}$$

automaticamente **simétrico** sob troca de quaisquer dois momentos, por (5.4) — a estatística de Bose–Einstein é uma consequência da escolha de comutadores.

### 5.3 Hamiltoniano, momento e ordenamento normal

$$H=\int\!\widetilde{dp}\;E_{p}\,a^{\dagger}_{\mathbf{p}}a_{\mathbf{p}}\;+\;\underbrace{\frac{1}{2}\int\! d^{3}p\;\frac{E_{p}}{(2\pi)^{3}}\,\delta^{3}(0)\cdot\ldots}_{\text{energia de vácuo}}.\tag{5.6}$$

A energia de vácuo é duplamente divergente: $\delta^{3}(0)\propto V$ (volume, divergência infravermelha) e $\int d^{3}p\,E_{p}$ (ultravioleta). O **ordenamento normal** $:\!\mathcal{O}\!:$ — todos os $a^{\dagger}$ à esquerda de todos os $a$ — a remove por definição:

$$:\!H\!:\;=\int\!\widetilde{dp}\;E_{p}\,a^{\dagger}_{\mathbf{p}}a_{\mathbf{p}},\qquad :\!\mathbf{P}\!:\;=\int\!\widetilde{dp}\;\mathbf{p}\,a^{\dagger}_{\mathbf{p}}a_{\mathbf{p}}.\tag{5.7}$$

**Isso é legítimo?** Sim, com duas ressalvas. (i) Apenas *diferenças* de energia são observáveis em uma teoria sem gravitação; o ordenamento normal é a escolha de origem $E_{\rm vac}=0$. (ii) Quando a energia de vácuo é *modulada* por condições de contorno, a diferença é observável: é o **efeito Casimir**,

$$\frac{E}{A}=-\frac{\pi^{2}}{720\,a^{3}}\qquad\text{(duas placas condutoras separadas por }a\text{)},\tag{5.8}$$

medido experimentalmente. (iii) Acoplada à gravitação, a energia absoluta de vácuo importa, e a discrepância de $\sim10^{120}$ com a constante cosmológica observada é o problema da constante cosmológica — não resolvido, e um sinal claro de que o formalismo é incompleto nesse setor.

### 5.4 Estados de uma partícula e normalização

$$\phi(x)|0\rangle=\int\!\widetilde{dp}\;e^{ip\cdot x}\,|p\rangle\quad\text{com}\quad |p\rangle=a^{\dagger}_{\mathbf{p}}|0\rangle,\tag{5.9}$$

$$\langle0|\phi(x)|p\rangle = e^{-ip\cdot x}.\tag{5.10}$$

A relação (5.10) é a definição operacional de "o campo cria a partícula" e é o ponto de partida da fórmula de redução LSZ (§21). A normalização covariante (0.5) garante que $\langle p|q\rangle$ se transforma como escalar; a medida (0.6) é o elemento de volume invariante no hiperboloide de massa.

---

## 6. O campo escalar complexo e a carga

$$\mathcal{L}=\partial_{\mu}\phi^{*}\partial^{\mu}\phi-m^{2}|\phi|^{2},\qquad \phi\neq\phi^{\dagger}.\tag{6.1}$$

A lagrangiana tem simetria global $U(1)$: $\phi\to e^{i\alpha}\phi$, com corrente de Noether

$$j^{\mu}=i\left(\phi^{*}\partial^{\mu}\phi-\phi\,\partial^{\mu}\phi^{*}\right),\qquad Q=\int d^{3}x\;j^{0}.\tag{6.2}$$

A expansão em modos agora requer **dois** conjuntos independentes de operadores:

$$\phi(x)=\int\!\widetilde{dp}\left[a_{\mathbf{p}}e^{-ipx}+b^{\dagger}_{\mathbf{p}}e^{+ipx}\right],\qquad \phi^{\dagger}(x)=\int\!\widetilde{dp}\left[b_{\mathbf{p}}e^{-ipx}+a^{\dagger}_{\mathbf{p}}e^{+ipx}\right].\tag{6.3}$$

$$:\!Q\!:\;=\int\!\widetilde{dp}\left(a^{\dagger}_{\mathbf{p}}a_{\mathbf{p}}-b^{\dagger}_{\mathbf{p}}b_{\mathbf{p}}\right).\tag{6.4}$$

**Interpretação.** $a^{\dagger}$ cria quanta de carga $+1$; $b^{\dagger}$ cria quanta de carga $-1$ e mesma massa: **antipartículas**. A estrutura (6.3) é forçada: um campo que aniquila carga $+1$ deve também criar carga $-1$, para que $\phi$ tenha carga definida $-1$ e o hamiltoniano de interação seja neutro.

**O caso real como limite.** Impor $\phi=\phi^{\dagger}$ em (6.3) força $b_{\mathbf{p}}=a_{\mathbf{p}}$: partícula e antipartícula coincidem, e $Q\equiv0$ por (6.4). Esta é **exatamente** a estrutura que reaparece, no setor fermiônico, como a condição de Majorana ($d_{s}=b_{s}$, cf. Apêndice G): um campo autoconjugado não pode carregar carga.

---

## 7. Causalidade, comutadores e propagadores

### 7.1 As funções de dois pontos

Definimos, para o campo escalar real,

$$\Delta^{+}(x-y)\equiv\langle0|\phi(x)\phi(y)|0\rangle=\int\!\widetilde{dp}\;e^{-ip\cdot(x-y)}\qquad\text{(função de Wightman)},\tag{7.1}$$

$$\Delta(x-y)\equiv\left[\phi(x),\phi(y)\right]=\Delta^{+}(x-y)-\Delta^{+}(y-x)\qquad\text{(função de Pauli–Jordan)}.\tag{7.2}$$

### 7.2 Microcausalidade

**Teorema.** $\Delta(x-y)=0$ para $(x-y)^{2}<0$ (separação tipo espaço).

*Demonstração.* $\Delta$ é um invariante de Lorentz — cada termo em (7.2) é integrado com a medida invariante (0.6). Para separação tipo espaço existe uma transformação de Lorentz **própria e ortócrona** que leva $x-y\to-(x-y)$ (basta uma rotação de $\pi$ em torno de um eixo perpendicular, na origem apropriada). Logo $\Delta(x-y)=\Delta(y-x)$. Mas de (7.2), $\Delta(x-y)=-\Delta(y-x)$. Portanto $\Delta=0$. $\blacksquare$

Note onde a demonstração falha para separação **tipo tempo**: nesse caso a inversão $x-y\to-(x-y)$ trocaria a ordem temporal e exigiria uma transformação não ortócrona, fora do grupo de Lorentz próprio. Assim $\Delta\neq0$ para separação tipo tempo — e é exatamente isso que permite propagação causal de sinais.

**O papel da antipartícula.** O cancelamento em (7.2) é entre a amplitude de uma partícula ir de $y$ a $x$ e a de uma antipartícula ir de $x$ a $y$. Para o campo complexo, o comutador relevante é $[\phi(x),\phi^{\dagger}(y)]$, e o cancelamento só ocorre porque $a$ e $b$ têm **a mesma massa**. Este é o argumento anunciado em §1.1(iii): *a causalidade exige a existência de antipartículas com massa igual*. O teorema $CPT$ (§14.4) é a versão geral deste enunciado.

### 7.3 O propagador de Feynman

$$D_{F}(x-y)\equiv\langle0|T\,\phi(x)\phi(y)|0\rangle = \theta(x^{0}-y^{0})\Delta^{+}(x-y)+\theta(y^{0}-x^{0})\Delta^{+}(y-x),\tag{7.3}$$

$$\boxed{\;D_{F}(x-y)=\int\!\frac{d^{4}p}{(2\pi)^{4}}\;\frac{i}{p^{2}-m^{2}+i\varepsilon}\;e^{-ip\cdot(x-y)}\;}\tag{7.4}$$

**A prescrição $i\varepsilon$.** Os polos de $1/(p^{2}-m^{2})$ estão em $p^{0}=\pm E_{p}$; o $+i\varepsilon$ os desloca para $p^{0}=\pm(E_{p}-i\varepsilon)$. Fechando o contorno por baixo para $x^{0}>y^{0}$ captura o polo em $+E_{p}$ (frequências positivas propagando para o futuro); por cima para $x^{0}<y^{0}$ captura $-E_{p}$. Isto é exatamente a estrutura (7.3). Outras prescrições dão outras funções de Green:

| Prescrição | Função | Suporte |
|:---|:---|:---|
| $p^{2}-m^{2}+i\varepsilon$ | Feynman $D_{F}$ | ambos os cones |
| $(p^{0}+i\varepsilon)^{2}-\mathbf{p}^{2}-m^{2}$ | retardada $D_{R}$ | cone de luz futuro |
| $(p^{0}-i\varepsilon)^{2}-\mathbf{p}^{2}-m^{2}$ | avançada $D_{A}$ | cone de luz passado |

$D_{F}$ é a que aparece na teoria de perturbação (§19), porque o produto ordenado no tempo é o que emerge da série de Dyson. $D_{R}$ e $D_{A}$ são as relevantes para problemas de valor inicial clássicos.

**Equação satisfeita.** $\left(\Box_{x}+m^{2}\right)D_{F}(x-y)=-i\,\delta^{4}(x-y)$: $D_{F}$ é uma função de Green do operador de Klein–Gordon.

### 7.4 Representação de Källén–Lehmann

Na teoria interagente, a função de dois pontos exata admite a representação espectral

$$\langle\Omega|T\phi(x)\phi(y)|\Omega\rangle=\int_{0}^{\infty}\frac{d\mu^{2}}{2\pi}\;\rho(\mu^{2})\;D_{F}(x-y;\mu^{2}),\tag{7.5}$$

$$\rho(\mu^{2})=2\pi\,Z\,\delta(\mu^{2}-m^{2}_{\rm phys})+\text{(contínuo de multipartículas, }\mu^{2}\geq(2m)^{2}),\tag{7.6}$$

com $\rho\geq0$ garantida pela positividade da métrica do espaço de Hilbert. Consequências estruturais (detalhes no Apêndice E):

- O propagador exato tem um **polo simples** em $p^{2}=m^{2}_{\rm phys}$ com resíduo $iZ$, onde $Z=|\langle\Omega|\phi(0)|p\rangle|^{2}$ é a **constante de renormalização de função de onda**, com $0\leq Z\leq1$.
- $m_{\rm phys}$ é a massa física (polo), em geral diferente do parâmetro $m$ da lagrangiana.
- Como $\rho\geq0$, o propagador exato não pode decair mais rápido que $1/p^{2}$ no ultravioleta — o que proíbe, em teorias unitárias, propagadores "melhorados" do tipo $1/p^{4}$ que ingenuamente resolveriam as divergências.

---

## 8. O campo vetorial

### 8.1 O campo de Proca (massivo)

$$\mathcal{L}_{\rm Proca}=-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}+\frac{1}{2}m^{2}A_{\mu}A^{\mu}\;\Longrightarrow\;\partial_{\mu}F^{\mu\nu}+m^{2}A^{\nu}=0.\tag{8.1}$$

Tomando $\partial_{\nu}$ da equação de movimento e usando a antissimetria de $F$:

$$m^{2}\,\partial_{\nu}A^{\nu}=0\;\;\Longrightarrow\;\; \partial_{\nu}A^{\nu}=0\quad(m\neq0),\tag{8.2}$$

o que **não é uma escolha de gauge**, mas uma consequência dinâmica. O vínculo elimina uma das quatro componentes, deixando $3=2s+1$ com $s=1$ — correto para uma partícula massiva de spin 1, conforme a classificação de Wigner (§4.3). O propagador é

$$D^{\mu\nu}_{F}(p)=\frac{-i\left(\eta^{\mu\nu}-p^{\mu}p^{\nu}/m^{2}\right)}{p^{2}-m^{2}+i\varepsilon}.\tag{8.3}$$

O termo $p^{\mu}p^{\nu}/m^{2}$ cresce com o momento e é a origem do mau comportamento ultravioleta de teorias com vetores massivos não originados de quebra espontânea (§34).

### 8.2 O campo de Maxwell (sem massa) e o problema do gauge

Para $m=0$, (8.1) adquire a invariância de gauge $A_{\mu}\to A_{\mu}+\partial_{\mu}\lambda(x)$, e a quantização canônica enfrenta duas obstruções:

1. $\pi^{0}=\partial\mathcal{L}/\partial\dot A_{0}=0$ **identicamente** — um vínculo primário. $A_{0}$ não é uma variável dinâmica.
2. A lei de Gauss $\nabla\cdot\mathbf{E}=0$ é um vínculo secundário.

Existem três estratégias padrão:

**(a) Gauge de radiação (Coulomb).** Impõe-se $A^{0}=0$ e $\nabla\cdot\mathbf{A}=0$. Restam dois graus de liberdade transversais — o resultado fisicamente correto (helicidades $\pm1$), mas a covariância de Lorentz é sacrificada e deve ser reverificada a cada passo.

**(b) Gupta–Bleuler.** Adiciona-se um termo de fixação de gauge covariante,

$$\mathcal{L}=-\frac{1}{4}F^{2}-\frac{1}{2\xi}\left(\partial_{\mu}A^{\mu}\right)^{2},\tag{8.4}$$

quantizam-se as quatro componentes covariantemente, ao custo de uma **métrica indefinida** no espaço de estados: $[a^{0}_{\mathbf{p}},a^{0\dagger}_{\mathbf{q}}]=-(2\pi)^{3}2E_{p}\delta^{3}$, com norma negativa. Os estados físicos são definidos pela condição

$$\partial_{\mu}A^{\mu(+)}(x)\,|\psi\rangle=0,\tag{8.5}$$

que seleciona um subespaço de norma semidefinida positiva; os estados de norma nula (combinações de temporais e longitudinais) são identificados a zero pela relação de equivalência. O resultado líquido: dois estados físicos. O propagador é

$$D^{\mu\nu}_{F}(p)=\frac{-i}{p^{2}+i\varepsilon}\left[\eta^{\mu\nu}-(1-\xi)\frac{p^{\mu}p^{\nu}}{p^{2}}\right],\tag{8.6}$$

com $\xi=1$ (Feynman) e $\xi=0$ (Landau) as escolhas usuais. **A independência das amplitudes físicas em relação a $\xi$ é uma verificação computacional essencial.**

**(c) Faddeev–Popov.** O método funcional (§26), que generaliza (b) para o caso não abeliano — onde Gupta–Bleuler falha e fantasmas são obrigatórios.

### 8.3 Contagem de graus de liberdade

| Campo | Componentes | Vínculos/gauge | Físicos on-shell | Little group |
|:---|:---:|:---|:---:|:---|
| Escalar real | 1 | — | 1 | trivial |
| Escalar complexo | 2 | — | 2 (partícula + antipartícula) | trivial |
| Weyl | 2 (complexas) | eq. de movimento | 2 | $ISO(2)$ / $SU(2)$ |
| Dirac | 4 (complexas) | eq. de movimento | 4 | $SU(2)$, $s=\tfrac12$ |
| Proca | 4 | $\partial\!\cdot\!A=0$ | 3 | $SU(2)$, $s=1$ |
| Maxwell | 4 | $\partial\!\cdot\!A=0$ + gauge residual | 2 | $ISO(2)$, $h=\pm1$ |
| Gráviton | 10 | difeomorfismos | 2 | $ISO(2)$, $h=\pm2$ |

**A descontinuidade $m\to0$.** Proca tem $3$ graus; Maxwell tem $2$. O limite não é contínuo: o grau longitudinal não desaparece suavemente. Em teorias em que o vetor massivo vem de quebra espontânea, esse grau é o bóson de Goldstone "comido" (§34), e o limite é bem comportado — outra razão pela qual o mecanismo de Higgs, e não um termo de massa explícito, é a maneira consistente de dar massa a bósons de gauge.

---

# Parte III — Campos Fermiônicos

> *Esta é a parte dedicada aos férmions. Ela é autocontida: constrói a representação espinorial, quantiza o campo, estabelece a estatística, desenvolve o formalismo de Grassmann e chega às regras de Feynman e à anomalia quiral, com referências para frente às Partes IV–VI onde a maquinaria geral é desenvolvida. O Apêndice G estende tudo ao caso de Majorana.*

## 9. A representação espinorial do grupo de Lorentz

### 9.1 A estrutura $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$

Partindo da álgebra de Lorentz (4.3), defina $J^{i}=\tfrac12\varepsilon^{ijk}M^{jk}$ (rotações) e $K^{i}=M^{0i}$ (boosts), e forme

$$A^{i}=\frac{1}{2}\left(J^{i}+iK^{i}\right),\qquad B^{i}=\frac{1}{2}\left(J^{i}-iK^{i}\right).\tag{9.1}$$

Um cálculo direto a partir de (4.3) dá

$$[A^{i},A^{j}]=i\varepsilon^{ijk}A^{k},\qquad [B^{i},B^{j}]=i\varepsilon^{ijk}B^{k},\qquad [A^{i},B^{j}]=0.\tag{9.2}$$

Ou seja, $\mathfrak{so}(1,3)_{\mathbb{C}}\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$. As representações de dimensão finita são portanto rotuladas por um par $(j_{-},j_{+})$ de spins de $SU(2)$, com dimensão $(2j_{-}+1)(2j_{+}+1)$ e spin total decomposto por $j_{-}\otimes j_{+}$.

> **Ressalva importante.** $A$ e $B$ **não** são hermitianos separadamente (os boosts $K$ entram com $i$), de modo que essas representações são de dimensão finita mas **não unitárias**. Isso é consistente com §4.4: campos usam representações não unitárias; estados usam as unitárias de dimensão infinita de Wigner.

| $(j_{-},j_{+})$ | dim | Objeto | Spin |
|:---|:---:|:---|:---|
| $(0,0)$ | 1 | escalar | 0 |
| $(\tfrac12,0)$ | 2 | espinor de Weyl canhoto $\chi_{\alpha}$ | $\tfrac12$ |
| $(0,\tfrac12)$ | 2 | espinor de Weyl destro $\bar\xi^{\dot\alpha}$ | $\tfrac12$ |
| $(\tfrac12,0)\oplus(0,\tfrac12)$ | 4 | espinor de Dirac | $\tfrac12$ |
| $(\tfrac12,\tfrac12)$ | 4 | vetor $A^{\mu}$ | $0\oplus1$ |
| $(1,0)\oplus(0,1)$ | 6 | tensor antissimétrico $F_{\mu\nu}$ | — |

### 9.2 Os geradores na representação de Dirac

$$S^{\mu\nu}=\frac{1}{2}\sigma^{\mu\nu}=\frac{i}{4}\left[\gamma^{\mu},\gamma^{\nu}\right],\tag{9.3}$$

que satisfazem (4.3) como consequência direta da álgebra de Clifford $\{\gamma^{\mu},\gamma^{\nu}\}=2\eta^{\mu\nu}$ (verificado explicitamente por cálculo matricial). A transformação finita de um espinor é

$$\psi(x)\;\longrightarrow\;S(\Lambda)\,\psi(\Lambda^{-1}x),\qquad S(\Lambda)=\exp\!\left(-\frac{i}{4}\omega_{\mu\nu}\sigma^{\mu\nu}\right).\tag{9.4}$$

Como $\gamma^{5}$ comuta com $\sigma^{\mu\nu}$, a decomposição $\psi=P_{L}\psi+P_{R}\psi$ é **invariante de Lorentz**: a quiralidade é um bom número quântico do grupo próprio ortócrono, embora seja trocada por paridade.

**Duas propriedades que serão usadas constantemente:**

$$S(\Lambda)^{-1}\gamma^{\mu}S(\Lambda)=\Lambda^{\mu}{}_{\nu}\gamma^{\nu}\qquad\text{(covariância de }\gamma^{\mu}),\tag{9.5}$$

$$\gamma^{0}S(\Lambda)^{\dagger}\gamma^{0}=S(\Lambda)^{-1}\qquad\Longrightarrow\qquad \bar\psi\psi\ \text{é escalar},\;\;\bar\psi\gamma^{\mu}\psi\ \text{é vetor}.\tag{9.6}$$

A relação (9.6) é a razão de ser do adjunto de Dirac $\bar\psi=\psi^{\dagger}\gamma^{0}$: $\psi^{\dagger}\psi$ **não** é escalar, porque $S(\Lambda)$ não é unitária para boosts.

### 9.3 Existência: a álgebra de Clifford

A construção acima pressupõe a existência de matrizes $\gamma^{\mu}$ satisfazendo $\{\gamma^{\mu},\gamma^{\nu}\}=2\eta^{\mu\nu}$. Em $D=4$ existem, com dimensão mínima $4$, e a representação é **única a menos de similaridade** (teorema de Pauli). Três bases explícitas — Dirac, quiral e Majorana — estão no Apêndice A.3.

---

## 10. A equação de Dirac e suas soluções

### 10.1 A equação

$$\mathcal{L}_{\rm Dirac}=\bar\psi\left(i\gamma^{\mu}\partial_{\mu}-m\right)\psi\;\;\Longrightarrow\;\;\left(i\not{\partial}-m\right)\psi=0,\qquad \bar\psi\left(i\overleftarrow{\not{\partial}}+m\right)=0.\tag{10.1}$$

Aplicando $(i\not{\partial}+m)$ à esquerda e usando $\not{\partial}\not{\partial}=\Box$:

$$\left(\Box+m^{2}\right)\psi=0,\tag{10.2}$$

de modo que cada componente satisfaz Klein–Gordon e a relação de dispersão $p^{2}=m^{2}$ é automática. **A equação de Dirac é uma "raiz quadrada" da equação de Klein–Gordon**, e essa fatoração é precisamente o que a álgebra de Clifford torna possível.

### 10.2 Soluções de onda plana

Escrevendo $\psi=u(p)e^{-ip\cdot x}$ e $\psi=v(p)e^{+ip\cdot x}$ com $p^{0}=E_{p}>0$:

$$\left(\not{p}-m\right)u^{s}(p)=0,\qquad \left(\not{p}+m\right)v^{s}(p)=0,\qquad s=1,2.\tag{10.3}$$

Na base de Dirac, com $\xi^{s}$ espinores de duas componentes normalizados ($\xi^{r\dagger}\xi^{s}=\delta^{rs}$):

$$u^{s}(p)=\begin{pmatrix}\sqrt{p\cdot\sigma}\;\xi^{s}\\ \sqrt{p\cdot\bar\sigma}\;\xi^{s}\end{pmatrix},\qquad v^{s}(p)=\begin{pmatrix}\sqrt{p\cdot\sigma}\;\eta^{s}\\ -\sqrt{p\cdot\bar\sigma}\;\eta^{s}\end{pmatrix}\quad\text{(base quiral)}.\tag{10.4}$$

**Normalizações e relações de completude** (com a convenção covariante $\bar u u = 2m$):

$$\bar u^{r}(p)u^{s}(p)=2m\,\delta^{rs},\qquad \bar v^{r}(p)v^{s}(p)=-2m\,\delta^{rs},\qquad \bar u^{r}v^{s}=\bar v^{r}u^{s}=0,\tag{10.5}$$

$$u^{r\dagger}(p)u^{s}(p)=2E_{p}\,\delta^{rs},\qquad v^{r\dagger}(p)v^{s}(p)=2E_{p}\,\delta^{rs},\tag{10.6}$$

$$\boxed{\;\sum_{s}u^{s}(p)\bar u^{s}(p)=\not{p}+m,\qquad \sum_{s}v^{s}(p)\bar v^{s}(p)=\not{p}-m\;}\tag{10.7}$$

As relações (10.7) — verificadas explicitamente por cálculo matricial — são as mais usadas de toda a Parte III: elas convertem somas sobre spins em traços de matrizes gama (§16.3).

**Projetores de energia e de spin.**

$$\Lambda_{\pm}(p)=\frac{\pm\not{p}+m}{2m},\qquad \Lambda_{\pm}^{2}=\Lambda_{\pm},\qquad \Lambda_{+}+\Lambda_{-}=\mathbb{1},\tag{10.8}$$

$$\Sigma(s)=\frac{1+\gamma^{5}\not{s}}{2},\qquad s\cdot p=0,\;\;s^{2}=-1,\tag{10.9}$$

com $s^{\mu}$ o quadrivetor de polarização. No referencial de repouso $s^{\mu}=(0,\hat{\mathbf{s}})$ e $\Sigma$ projeta sobre spin ao longo de $\hat{\mathbf{s}}$.

### 10.3 Helicidade e quiralidade

$$h=\frac{\boldsymbol{\Sigma}\cdot\hat{\mathbf{p}}}{2},\qquad \boldsymbol{\Sigma}^{i}=\begin{pmatrix}\sigma^{i}&0\\0&\sigma^{i}\end{pmatrix}\quad\text{(base quiral)}.\tag{10.10}$$

- **Helicidade** é a projeção do spin no momento. É conservada para partículas livres, mas **não é invariante de Lorentz** se $m\neq0$: um observador que ultrapassa a partícula vê a helicidade invertida.
- **Quiralidade** é o autovalor de $\gamma^{5}$. É invariante de Lorentz sempre, mas **não é conservada** se $m\neq0$: o termo de massa $m\bar\psi\psi=m(\bar\psi_{L}\psi_{R}+\bar\psi_{R}\psi_{L})$ conecta as duas quiralidades.

$$\text{Para }m=0:\quad \text{helicidade}=\text{quiralidade},\quad\text{ambas invariantes e conservadas.}\tag{10.11}$$

Para $m\neq0$, os dois conceitos coincidem apenas até correções $\mathcal{O}(m/E)$. Esta é a origem técnica de toda "supressão de helicidade" em física de partículas: $\pi\to e\nu$ suprimido em relação a $\pi\to\mu\nu$, aniquilação de matéria escura de Majorana em onda $s$, e a dificuldade de distinguir neutrinos de Dirac e de Majorana.

---

## 11. Quantização do campo de Dirac

### 11.1 Por que anticomutadores são obrigatórios

Suponha, para argumentar, que se imponham **comutadores** canônicos. De $\pi=\partial\mathcal{L}/\partial\dot\psi=i\psi^{\dagger}$,

$$\left[\psi_{a}(t,\mathbf{x}),\psi^{\dagger}_{b}(t,\mathbf{y})\right]\overset{?}{=}\delta_{ab}\,\delta^{3}(\mathbf{x}-\mathbf{y}).\tag{11.1}$$

Expandindo em modos, obtém-se $[b,b^{\dagger}]\sim+1$ e $[d,d^{\dagger}]\sim-1$, e o hamiltoniano fica

$$H\;\sim\;\int\!\widetilde{dp}\;E_{p}\left(b^{\dagger}b-d^{\dagger}d\right),\tag{11.2}$$

**ilimitado por baixo**: criar antipartículas abaixa a energia indefinidamente. Não há vácuo estável. Alternativamente, se em vez disso se redefine $d\leftrightarrow d^{\dagger}$ para consertar o sinal da energia, obtêm-se estados de **norma negativa**. Nenhuma das duas patologias é removível.

Com **anticomutadores**, ambos os problemas desaparecem de uma vez: o sinal de $H$ é corrigido *e* a norma permanece positiva. Este é o conteúdo do teorema spin-estatística (§14) visto de baixo para cima; a versão "de cima para baixo", a partir da microcausalidade, está em §14.2.

### 11.2 A quantização correta

$$\boxed{\;\left\{\psi_{a}(t,\mathbf{x}),\psi^{\dagger}_{b}(t,\mathbf{y})\right\}=\delta_{ab}\,\delta^{3}(\mathbf{x}-\mathbf{y}),\qquad \{\psi,\psi\}=\{\psi^{\dagger},\psi^{\dagger}\}=0\;}\tag{11.3}$$

$$\psi(x)=\int\!\widetilde{dp}\;\sum_{s}\left[b^{s}_{\mathbf{p}}\,u^{s}(p)\,e^{-ip\cdot x}+d^{s\dagger}_{\mathbf{p}}\,v^{s}(p)\,e^{+ip\cdot x}\right],\tag{11.4}$$

$$\left\{b^{r}_{\mathbf{p}},b^{s\dagger}_{\mathbf{q}}\right\}=\left\{d^{r}_{\mathbf{p}},d^{s\dagger}_{\mathbf{q}}\right\}=(2\pi)^{3}\,2E_{p}\,\delta^{rs}\,\delta^{3}(\mathbf{p}-\mathbf{q}),\tag{11.5}$$

com todos os demais anticomutadores nulos. $b^{\dagger}$ cria férmions, $d^{\dagger}$ cria antiférmions.

### 11.3 Observáveis

$$:\!H\!:\;=\int\!\widetilde{dp}\;E_{p}\sum_{s}\left(b^{s\dagger}_{\mathbf{p}}b^{s}_{\mathbf{p}}+d^{s\dagger}_{\mathbf{p}}d^{s}_{\mathbf{p}}\right)\;\geq\;0,\tag{11.6}$$

$$:\!Q\!:\;=\int\!\widetilde{dp}\;\sum_{s}\left(b^{s\dagger}_{\mathbf{p}}b^{s}_{\mathbf{p}}-d^{s\dagger}_{\mathbf{p}}d^{s}_{\mathbf{p}}\right),\qquad j^{\mu}=\bar\psi\gamma^{\mu}\psi.\tag{11.7}$$

**A energia de vácuo fermiônica tem sinal oposto à bosônica** (o ordenamento normal de operadores anticomutantes introduz um sinal). Em teorias supersimétricas, os cancelamentos entre os dois setores são exatos, e a energia de vácuo se anula — a motivação original da supersimetria como solução do problema da hierarquia.

### 11.4 O espaço de Fock fermiônico e o princípio de exclusão

De $\{b^{\dagger},b^{\dagger}\}=0$ segue imediatamente

$$\left(b^{s\dagger}_{\mathbf{p}}\right)^{2}=0,\tag{11.8}$$

isto é, **nenhum estado pode conter dois férmions idênticos com os mesmos números quânticos**. O princípio de exclusão de Pauli não é um postulado adicional: é uma consequência algébrica da quantização com anticomutadores, que por sua vez é obrigatória pela consistência relativística. E o estado de duas partículas

$$|p_{1}s_{1};p_{2}s_{2}\rangle=b^{s_{1}\dagger}_{\mathbf{p}_{1}}b^{s_{2}\dagger}_{\mathbf{p}_{2}}|0\rangle=-\,|p_{2}s_{2};p_{1}s_{1}\rangle\tag{11.9}$$

é automaticamente antissimétrico. Toda a estrutura da matéria — a tabela periódica, a estabilidade das anãs brancas — decorre de (11.8).

---

## 12. O propagador fermiônico

$$S_{F}(x-y)\equiv\langle0|T\,\psi(x)\bar\psi(y)|0\rangle,\qquad T\,\psi(x)\bar\psi(y)\equiv\theta(x^{0}-y^{0})\psi(x)\bar\psi(y)-\theta(y^{0}-x^{0})\bar\psi(y)\psi(x).\tag{12.1}$$

**O sinal menos na definição do produto ordenado é obrigatório** para campos fermiônicos: sem ele, $S_{F}$ não satisfaz a equação de Green nem tem as propriedades de transformação corretas. Ele é a semente de todos os sinais relativos entre diagramas de Feynman (§16.2).

Calculando com (11.4)–(11.5) e (10.7):

$$\boxed{\;S_{F}(x-y)=\int\!\frac{d^{4}p}{(2\pi)^{4}}\;\frac{i\left(\not{p}+m\right)}{p^{2}-m^{2}+i\varepsilon}\;e^{-ip\cdot(x-y)}=\int\!\frac{d^{4}p}{(2\pi)^{4}}\;\frac{i}{\not{p}-m+i\varepsilon}\;e^{-ip\cdot(x-y)}\;}\tag{12.2}$$

usando $(\not{p}-m)(\not{p}+m)=p^{2}-m^{2}$. Ele satisfaz

$$\left(i\not{\partial}_{x}-m\right)S_{F}(x-y)=i\,\delta^{4}(x-y).\tag{12.3}$$

**Microcausalidade fermiônica.** O objeto que se anula fora do cone de luz é o **anti**comutador:

$$\left\{\psi(x),\bar\psi(y)\right\}=\left(i\not{\partial}_{x}+m\right)\Delta(x-y)=0\quad\text{para}\quad (x-y)^{2}<0,\tag{12.4}$$

com $\Delta$ a função de Pauli–Jordan (7.2). Observáveis físicos são **bilineares** nos campos fermiônicos (§13) e, portanto, comutam a separações tipo espaço — que é o enunciado fisicamente relevante da causalidade. Campos fermiônicos individuais não são observáveis.

---

## 13. Bilineares, correntes e quiralidade

### 13.1 A base de bilineares

Os $16$ produtos independentes de matrizes gama formam a base $\Gamma^{A}=\{\mathbb{1},\gamma^{\mu},\sigma^{\mu\nu},\gamma^{\mu}\gamma^{5},\gamma^{5}\}$, com $\operatorname{tr}(\Gamma^{A}\Gamma_{B})=4\delta^{A}_{B}$. Os bilineares correspondentes e suas propriedades de transformação:

| Bilinear | Tipo | $P$ | $C$ | $T$ | $CPT$ |
|:---|:---|:---:|:---:|:---:|:---:|
| $\bar\psi\psi$ | escalar (S) | $+$ | $+$ | $+$ | $+$ |
| $i\bar\psi\gamma^{5}\psi$ | pseudoescalar (P) | $-$ | $+$ | $-$ | $+$ |
| $\bar\psi\gamma^{\mu}\psi$ | vetor (V) | $(-1)^{\mu}$ | $-$ | $(-1)^{\mu}$ | $-$ |
| $\bar\psi\gamma^{\mu}\gamma^{5}\psi$ | axial (A) | $-(-1)^{\mu}$ | $+$ | $(-1)^{\mu}$ | $-$ |
| $\bar\psi\sigma^{\mu\nu}\psi$ | tensor (T) | $(-1)^{\mu}(-1)^{\nu}$ | $-$ | $-(-1)^{\mu}(-1)^{\nu}$ | $+$ |

(onde $(-1)^{\mu}=+1$ para $\mu=0$ e $-1$ para $\mu=1,2,3$.)

Toda interação local de férmions é construída a partir dessa base. Em particular, o Modelo Padrão usa apenas $V$ e $A$ nos acoplamentos de gauge, e $S$ e $P$ nos acoplamentos de Yukawa.

### 13.2 Correntes conservadas e correntes anômalas

**Corrente vetorial.** A simetria $\psi\to e^{i\alpha}\psi$ dá

$$j^{\mu}=\bar\psi\gamma^{\mu}\psi,\qquad \partial_{\mu}j^{\mu}=0\quad\text{exatamente (para qualquer }m).\tag{13.1}$$

**Corrente axial.** A simetria $\psi\to e^{i\alpha\gamma^{5}}\psi$ é uma simetria de $\mathcal{L}$ apenas para $m=0$; classicamente,

$$j^{\mu5}=\bar\psi\gamma^{\mu}\gamma^{5}\psi,\qquad \partial_{\mu}j^{\mu5}=2im\,\bar\psi\gamma^{5}\psi.\tag{13.2}$$

**Mas essa equação é falsa na teoria quântica**, mesmo para $m=0$: a corrente axial é **anômala** (§17). Este é um dos resultados mais profundos da TQC — uma simetria clássica destruída pela quantização.

### 13.3 Decomposição quiral e a estrutura de massa

$$\psi=\psi_{L}+\psi_{R},\qquad \psi_{L,R}=P_{L,R}\psi.\tag{13.3}$$

$$\bar\psi\,i\not{\partial}\,\psi=\bar\psi_{L}\,i\not{\partial}\,\psi_{L}+\bar\psi_{R}\,i\not{\partial}\,\psi_{R},\qquad m\bar\psi\psi=m\left(\bar\psi_{L}\psi_{R}+\bar\psi_{R}\psi_{L}\right).\tag{13.4}$$

**O termo cinético não mistura quiralidades; o termo de massa mistura.** Esta é a observação estrutural que organiza toda a física de sabor:

1. Para $m=0$, as duas quiralidades são campos **independentes**, e a teoria tem simetria $U(1)_{L}\times U(1)_{R}$ (ou $U(n)_{L}\times U(n)_{R}$ com $n$ sabores).
2. Um termo de massa exige a existência de **ambas** as quiralidades — ou a construção de um objeto de quiralidade oposta a partir da mesma, que é exatamente o que a conjugação de carga faz e o que abre a porta para a massa de Majorana (Apêndice G).
3. Como as interações fracas acoplam-se apenas a $\psi_{L}$, um termo de massa nu $m\bar\psi\psi$ **não é invariante de gauge** no Modelo Padrão. Toda massa de férmion precisa vir do mecanismo de Higgs via acoplamento de Yukawa.

$$\mathcal{L}_{\rm Yukawa}=-y\,\bar\psi_{L}\,\Phi\,\psi_{R}+\text{h.c.}\;\;\xrightarrow{\;\langle\Phi\rangle=v/\sqrt2\;}\;\;-\frac{yv}{\sqrt2}\,\bar\psi\psi.\tag{13.5}$$

---

## 14. O teorema spin-estatística

### 14.1 Enunciado

**Teorema (Pauli, 1940; Lüders–Zumino, Burgoyne).** Em qualquer teoria quântica de campos que seja (i) invariante sob o grupo de Lorentz próprio ortócrono, (ii) local, com um espaço de Hilbert de métrica **positiva definida**, e (iii) dotada de um espectro de energia limitado por baixo com vácuo único e invariante, vale:

$$\boxed{\;\text{spin inteiro}\;\Longrightarrow\;\text{comutadores (Bose–Einstein)};\qquad \text{spin semi-inteiro}\;\Longrightarrow\;\text{anticomutadores (Fermi–Dirac)}.\;}$$

### 14.2 O argumento por microcausalidade

Considere primeiro o caso **errado** para um campo escalar: quantizar com anticomutadores. Então

$$\left\{\phi(x),\phi(y)\right\}=\Delta^{+}(x-y)+\Delta^{+}(y-x),\tag{14.1}$$

que, ao contrário de (7.2), é uma **soma** e não uma diferença. Como $\Delta^{+}(x-y)=\Delta^{+}(y-x)$ para separação tipo espaço (pelo mesmo argumento de invariância de §7.2), a soma é $2\Delta^{+}\neq0$: **microcausalidade violada**.

Agora o caso **errado** para um campo espinorial: quantizar com comutadores. Então o objeto que se anularia fora do cone de luz seria $[\psi,\bar\psi]=(i\not{\partial}+m)\left[\Delta^{+}(x-y)+\Delta^{+}(y-x)\right]$, novamente uma soma, que não se anula.

O fator estrutural que decide o caso é a **paridade do número de índices espinoriais**: um campo de spin semi-inteiro adquire um sinal $(-1)$ sob a rotação de $2\pi$ implícita na inversão $x-y\to-(x-y)$, e é exatamente esse sinal que exige a troca comutador $\to$ anticomutador para preservar a antissimetria de (7.2). $\blacksquare$ (esboço)

### 14.3 A tabela das patologias

| Campo | Estatística imposta | Patologia |
|:---|:---|:---|
| Spin $0$ | Fermi | Microcausalidade violada (14.1) |
| Spin $\tfrac12$ | Bose | $H$ ilimitado por baixo (11.2) **ou** normas negativas |
| Spin $1$ (massivo) | Fermi | Microcausalidade violada |
| Spin $\tfrac12$ | Fermi | ✓ consistente |

### 14.4 O teorema $CPT$

**Teorema.** Toda teoria quântica de campos local, hermitiana, invariante de Lorentz e com espectro limitado por baixo é invariante sob $\Theta=CPT$.

Consequências verificáveis:

1. Partícula e antipartícula têm **exatamente** a mesma massa e o mesmo tempo de vida total.
2. Seus momentos magnéticos são iguais em módulo e opostos em sinal.
3. Violação de $CP$ $\Longleftrightarrow$ violação de $T$.

O melhor teste experimental é a diferença relativa de massa no sistema $K^{0}$–$\bar K^{0}$, limitada a $|m_{K^{0}}-m_{\bar K^{0}}|/m_{K^{0}}\lesssim10^{-18}$ — o vínculo mais preciso sobre qualquer princípio da física.

$CPT$ e spin-estatística são, num sentido preciso, o **mesmo** teorema: ambos decorrem da possibilidade de continuar analiticamente as funções de Wightman para tempos euclidianos, onde $CPT$ é uma rotação de $\pi$ no plano $(t_{E},z)$.

---

## 15. Férmions no formalismo funcional

### 15.1 Por que Grassmann

No formalismo de integrais de trajetória (Parte V), os campos são variáveis de integração **clássicas**, não operadores. Para reproduzir os anticomutadores (11.3) no limite clássico, essas variáveis devem anticomutar:

$$\theta_{i}\theta_{j}=-\theta_{j}\theta_{i},\qquad \theta_{i}^{2}=0.\tag{15.1}$$

São **variáveis de Grassmann**. A álgebra gerada por $n$ delas tem dimensão $2^{n}$, e qualquer função é um polinômio que termina: $f(\theta)=a+b\theta$ para uma única variável.

### 15.2 Integração de Berezin

A integral de Grassmann é definida algebricamente pelas regras (Apêndice C)

$$\int d\theta\;1=0,\qquad \int d\theta\;\theta=1.\tag{15.2}$$

A propriedade extraordinária dessa definição é que **integração e diferenciação coincidem**, e o jacobiano aparece **invertido**: sob $\theta\to M\theta$, $\;d^{n}\theta\to(\det M)^{-1}d^{n}\theta$.

### 15.3 A integral gaussiana fermiônica

Para variáveis de Grassmann complexas independentes $\bar\theta,\theta$ e uma matriz $M$:

$$\boxed{\;\int d\bar\theta\,d\theta\;e^{-\bar\theta_{i}M_{ij}\theta_{j}}=\det M\;}\tag{15.3}$$

comparada com o caso bosônico $\int d\bar z\,dz\;e^{-\bar z M z}\propto(\det M)^{-1}$. **A inversão da potência do determinante é a manifestação funcional da estatística de Fermi** — e é a origem do fator $(-1)$ associado a cada laço fermiônico fechado (§16.2), bem como dos cancelamentos supersimétricos.

Para variáveis de Grassmann **reais** (o caso de Majorana) com $M$ antissimétrica:

$$\int d^{2n}\theta\;e^{\frac{1}{2}\theta^{T}M\theta}=\operatorname{Pf}(M),\qquad \left[\operatorname{Pf}(M)\right]^{2}=\det M.\tag{15.4}$$

O **Pfaffiano** é literalmente a raiz quadrada do determinante. Este resultado é a formulação funcional exata do fator $1/2$ da lagrangiana de Majorana — desenvolvido no Apêndice G.

### 15.4 O funcional gerador fermiônico

$$Z[\bar\eta,\eta]=\int\mathcal{D}\bar\psi\,\mathcal{D}\psi\;\exp\left\{i\!\int d^{4}x\left[\bar\psi\left(i\not{\partial}-m\right)\psi+\bar\eta\psi+\bar\psi\eta\right]\right\},\tag{15.5}$$

com fontes $\eta,\bar\eta$ também de Grassmann. Completando o quadrado,

$$Z[\bar\eta,\eta]=Z[0,0]\;\exp\left\{-i\!\int d^{4}x\,d^{4}y\;\bar\eta(x)\,S_{F}(x-y)\,\eta(y)\right\},\tag{15.6}$$

e as funções de Green se obtêm por derivadas funcionais **à esquerda**, com atenção aos sinais:

$$\langle0|T\,\psi(x)\bar\psi(y)|0\rangle = \left.\frac{1}{Z}\left(\frac{1}{i}\frac{\delta}{\delta\bar\eta(x)}\right)\left(i\frac{\delta}{\delta\eta(y)}\right)Z\right|_{\eta=\bar\eta=0}=S_{F}(x-y).\tag{15.7}$$

O propagador (12.2) é recuperado exatamente. $\checkmark$

---

## 16. Regras de Feynman fermiônicas e o teorema de Furry

### 16.1 As regras

Tomando QED como exemplo mestre, $\mathcal{L}_{\rm int}=-e\,\bar\psi\gamma^{\mu}\psi A_{\mu}$:

| Elemento | Fator |
|:---|:---|
| Propagador fermiônico | $\dfrac{i\left(\not{p}+m\right)}{p^{2}-m^{2}+i\varepsilon}$ |
| Propagador do fóton (gauge $\xi$) | $\dfrac{-i}{p^{2}+i\varepsilon}\left[\eta^{\mu\nu}-(1-\xi)\dfrac{p^{\mu}p^{\nu}}{p^{2}}\right]$ |
| Vértice | $-ie\gamma^{\mu}$ |
| Férmion entrando / saindo | $u^{s}(p)$ / $\bar u^{s}(p)$ |
| Antiférmion entrando / saindo | $\bar v^{s}(p)$ / $v^{s}(p)$ |
| Fóton externo | $\epsilon_{\mu}(p)$ / $\epsilon^{*}_{\mu}(p)$ |
| Laço | $\displaystyle\int\!\frac{d^{4}\ell}{(2\pi)^{4}}$ |
| Laço fermiônico fechado | fator $(-1)$ e traço $\operatorname{tr}[\cdots]$ |

**Ordem de leitura:** cada cadeia fermiônica é escrita **contra** o sentido da seta, começando por $\bar u$ (ou $\bar v$) e terminando em $u$ (ou $v$). Essa convenção garante que as matrizes se multipliquem na ordem correta.

### 16.2 Os sinais fermiônicos

Três fontes de sinal, todas rastreáveis ao produto ordenado (12.1) e à álgebra de Grassmann:

1. **Laço fechado:** fator $(-1)$, consequência direta de (15.3) — o determinante no numerador.
2. **Troca de férmions externos idênticos:** diagramas relacionados por permutação **ímpar** de linhas externas fermiônicas têm sinal relativo $(-1)$. Exemplo: espalhamento Møller $e^{-}e^{-}\to e^{-}e^{-}$, canais $t$ e $u$.
3. **Ordenamento normal:** já absorvido nas regras acima.

Apenas os sinais **relativos** entre diagramas importam; o sinal global é convenção.

### 16.3 Traços de matrizes gama

As relações de completude (10.7) convertem $\sum_{\rm spins}|\mathcal{M}|^{2}$ em traços. As identidades essenciais (verificadas por cálculo matricial direto):

$$\operatorname{tr}\mathbb{1}=4,\qquad \operatorname{tr}\left(\text{número ímpar de }\gamma\right)=0,\qquad \operatorname{tr}\gamma^{5}=0,\tag{16.1}$$

$$\operatorname{tr}\left(\gamma^{\mu}\gamma^{\nu}\right)=4\eta^{\mu\nu},\tag{16.2}$$

$$\operatorname{tr}\left(\gamma^{\mu}\gamma^{\nu}\gamma^{\rho}\gamma^{\sigma}\right)=4\left(\eta^{\mu\nu}\eta^{\rho\sigma}-\eta^{\mu\rho}\eta^{\nu\sigma}+\eta^{\mu\sigma}\eta^{\nu\rho}\right),\tag{16.3}$$

$$\operatorname{tr}\left(\gamma^{5}\gamma^{\mu}\gamma^{\nu}\right)=0,\qquad \operatorname{tr}\left(\gamma^{5}\gamma^{\mu}\gamma^{\nu}\gamma^{\rho}\gamma^{\sigma}\right)=-4i\,\varepsilon^{\mu\nu\rho\sigma}.\tag{16.4}$$

Identidades de contração em $D=4$:

$$\gamma^{\mu}\gamma_{\mu}=4,\quad \gamma^{\mu}\gamma^{\nu}\gamma_{\mu}=-2\gamma^{\nu},\quad \gamma^{\mu}\gamma^{\nu}\gamma^{\rho}\gamma_{\mu}=4\eta^{\nu\rho},\quad \gamma^{\mu}\gamma^{\nu}\gamma^{\rho}\gamma^{\sigma}\gamma_{\mu}=-2\gamma^{\sigma}\gamma^{\rho}\gamma^{\nu}.\tag{16.5}$$

Em $D=4-\epsilon$ dimensões essas identidades adquirem correções $\mathcal{O}(\epsilon)$ (por exemplo $\gamma^{\mu}\gamma_{\mu}=D$), que são essenciais em cálculos a um laço — e $\gamma^{5}$ torna-se genuinamente problemático, pois não existe extensão de $\gamma^{5}$ a $D$ dimensões que preserve simultaneamente $\{\gamma^{5},\gamma^{\mu}\}=0$ e a ciclicidade do traço. Este é o eco técnico da anomalia quiral (§17).

### 16.4 O teorema de Furry

**Teorema.** Em QED, qualquer diagrama contendo um laço fermiônico fechado com um número **ímpar** de vértices de fóton se anula identicamente.

*Demonstração.* Sob conjugação de carga, $\mathcal{C}A_{\mu}\mathcal{C}^{-1}=-A_{\mu}$ e $\mathcal{C}\,\bar\psi\gamma^{\mu}\psi\,\mathcal{C}^{-1}=-\bar\psi\gamma^{\mu}\psi$. QED é $C$-invariante, logo qualquer amplitude com um número ímpar de fótons externos ligados a um laço fermiônico deve ser igual a menos ela mesma, e portanto nula. Alternativamente, sem invocar simetria: as duas orientações do laço (percorrido nos dois sentidos) dão contribuições que diferem por $(-1)^{n}$ para $n$ vértices, cancelando-se para $n$ ímpar. $\blacksquare$

**Consequências.** (i) O processo luz-por-luz é dominado pelo laço de **quatro** fótons, não três. (ii) A ausência de correções de três fótons é o que garante a estabilidade das relações de QED a baixas ordens. (iii) A anomalia triangular (§17) **escapa** ao teorema de Furry porque um dos vértices é axial ($\gamma^{\mu}\gamma^{5}$, que é $C$-par), invertendo a contagem de sinais.

---

## 17. A anomalia quiral

### 17.1 O fenômeno

Classicamente, para $m=0$, a corrente axial é conservada: $\partial_{\mu}j^{\mu5}=0$. Quanticamente, ela **não é**:

$$\boxed{\;\partial_{\mu}j^{\mu5}=2im\,\bar\psi\gamma^{5}\psi+\frac{e^{2}}{16\pi^{2}}\,\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\;}\tag{17.1}$$

O segundo termo — a **anomalia de Adler–Bell–Jackiw** — sobrevive mesmo em $m=0$. Equivalentemente, $\partial_{\mu}j^{\mu5}=\frac{e^{2}}{2\pi^{2}}\mathbf{E}\cdot\mathbf{B}$ para $m=0$.

### 17.2 Três derivações, três leituras

**(a) Diagrama triangular (Adler; Bell–Jackiw, 1969).** O diagrama com um vértice axial e dois vetoriais é linearmente divergente. Não existe regularização que preserve **simultaneamente** a conservação da corrente vetorial e da axial. A escolha física — preservar a corrente vetorial, porque ela está acoplada ao fóton e sua conservação é exigida pela invariância de gauge — força a anomalia para o setor axial.

**(b) Medida funcional (Fujikawa, 1979).** Sob uma transformação quiral $\psi\to e^{i\alpha\gamma^{5}}\psi$, a **medida** da integral de trajetória não é invariante:

$$\mathcal{D}\bar\psi\mathcal{D}\psi\;\longrightarrow\;\mathcal{D}\bar\psi\mathcal{D}\psi\;\exp\left[-2i\!\int d^{4}x\;\alpha(x)\,\mathcal{A}(x)\right],\tag{17.2}$$

com o jacobiano $\mathcal{A}$ dado, após regularização, exatamente pelo termo anômalo. Esta é a leitura mais transparente: **a anomalia é um fracasso da medida funcional em respeitar a simetria clássica**.

**(c) Índice topológico.** O termo anômalo integrado é

$$\int d^{4}x\;\frac{e^{2}}{16\pi^{2}}\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\;=\;2\,\nu\;\in\;2\mathbb{Z},\tag{17.3}$$

um invariante topológico (número de enrolamento / carga de Pontryagin). Pelo **teorema do índice de Atiyah–Singer**, $\nu = n_{+}-n_{-}$, a diferença entre o número de modos zero de quiralidade positiva e negativa do operador de Dirac. A anomalia é, portanto, um enunciado sobre topologia do espaço de configurações de gauge.

### 17.3 O caráter exato: teorema de não renormalização

**Teorema (Adler–Bardeen).** O coeficiente da anomalia é dado **exatamente** pelo diagrama de um laço; correções de ordem superior se cancelam a todas as ordens em teoria de perturbação.

Isso torna a anomalia uma das poucas quantidades exatamente calculáveis em TQC interagente, e é o que permite usá-la como vínculo rigoroso sobre o conteúdo de partículas de uma teoria (§36).

### 17.4 Consequências físicas

1. **$\pi^{0}\to\gamma\gamma$.** A taxa é fixada pela anomalia:
$$\Gamma\left(\pi^{0}\to\gamma\gamma\right)=\frac{\alpha^{2}m_{\pi}^{3}}{64\pi^{3}f_{\pi}^{2}}N_{c}^{2}\left(Q_{u}^{2}-Q_{d}^{2}\right)^{2}\approx7.8\ \mathrm{eV},\tag{17.4}$$
em excelente acordo com a medida — e o resultado **exige $N_{c}=3$**. Este é historicamente um dos argumentos mais fortes pela existência de três cores.
2. **O problema $U(1)_{A}$.** A ausência de um nono pseudo-bóson de Goldstone leve na QCD (o $\eta'$ é pesado) é explicada pela anomalia: $U(1)_{A}$ nunca foi uma simetria genuína.
3. **Violação de $B+L$ no Modelo Padrão.** As correntes bariônica e leptônica são anômalas em relação a $SU(2)_{L}$; $B+L$ é violado por esfalerons, enquanto $B-L$ permanece conservado. Este é o mecanismo que converte assimetria leptônica em bariônica.
4. **Vínculo sobre teorias de gauge.** As anomalias em correntes de **gauge** destroem a unitariedade e devem cancelar. É o que fixa o conteúdo de hipercarga do Modelo Padrão (§36).

---

# Parte IV — Teoria de Perturbação e a Matriz S

## 18. Quadro de interação e série de Dyson

### 18.1 O quadro de interação

Separe $H=H_{0}+H_{\rm int}$, com $H_{0}$ livre. No quadro de interação, os campos evoluem com $H_{0}$ e os estados com $H_{\rm int}$:

$$\phi_{I}(t,\mathbf{x})=e^{iH_{0}(t-t_{0})}\phi(t_{0},\mathbf{x})e^{-iH_{0}(t-t_{0})},\qquad i\frac{d}{dt}|\psi(t)\rangle_{I}=H_{I}(t)\,|\psi(t)\rangle_{I}.\tag{18.1}$$

A vantagem decisiva: $\phi_{I}$ satisfaz a equação de movimento **livre** e admite a expansão em modos (5.3), com todos os resultados da Parte II válidos.

### 18.2 O operador de evolução e a série de Dyson

$$U(t,t_{0})=T\exp\left[-i\int_{t_{0}}^{t}dt'\;H_{I}(t')\right]=\sum_{n=0}^{\infty}\frac{(-i)^{n}}{n!}\int\!dt_{1}\cdots dt_{n}\;T\left\{H_{I}(t_{1})\cdots H_{I}(t_{n})\right\}.\tag{18.2}$$

O ordenamento temporal $T$ é o que torna a exponencial bem definida para operadores que não comutam em tempos diferentes; o fator $1/n!$ compensa a sobrecontagem das ordenações.

### 18.3 A matriz S

$$S\equiv U(+\infty,-\infty)=T\exp\left[-i\int d^{4}x\;\mathcal{H}_{I}(x)\right]=T\exp\left[i\int d^{4}x\;\mathcal{L}_{\rm int}(x)\right],\tag{18.3}$$

a última igualdade valendo quando $\mathcal{L}_{\rm int}$ não contém derivadas. A amplitude de um processo é

$$S_{fi}=\langle f|S|i\rangle = \delta_{fi}+i(2\pi)^{4}\delta^{4}\!\left(\textstyle\sum p_{i}-\sum p_{f}\right)\mathcal{M}_{fi},\tag{18.4}$$

com $\mathcal{M}$ a **amplitude invariante**, o objeto que os diagramas de Feynman calculam.

> **A hipótese adiabática e suas limitações.** A construção (18.3) supõe que os estados assintóticos $|i\rangle,|f\rangle$ sejam os do hamiltoniano livre, com a interação "desligada" em $t\to\pm\infty$. Isso falha em três situações fisicamente importantes: (i) teorias com estados ligados, cujos assintóticos não estão no espaço de Fock livre; (ii) teorias confinantes como a QCD, onde os quarks nunca são assintóticos; (iii) partículas sem massa, onde divergências infravermelhas exigem tratamento inclusivo (teorema de Kinoshita–Lee–Nauenberg). A fórmula LSZ (§21) fornece a base mais sólida, ao definir a matriz S diretamente a partir das funções de Green da teoria interagente.

---

## 19. O teorema de Wick

### 19.1 Contrações

Defina a **contração** de dois campos como o propagador de Feynman correspondente:

$$\overline{\phi(x)\,\phi(y)}\;\equiv\;\langle0|T\,\phi(x)\phi(y)|0\rangle=D_{F}(x-y).\tag{19.1}$$

**Teorema de Wick.** O produto ordenado no tempo de $n$ campos livres é a soma do produto ordenado normalmente com todas as contrações possíveis:

$$T\left\{\phi_{1}\cdots\phi_{n}\right\}=\;:\!\phi_{1}\cdots\phi_{n}\!:\;+\;\sum_{\text{1 contração}}:\!\cdots\!:\;+\;\sum_{\text{2 contrações}}:\!\cdots\!:\;+\;\cdots\tag{19.2}$$

Para $n$ **par**, o último termo é a soma sobre todos os emparelhamentos completos, e é o único que sobrevive no valor esperado no vácuo (pois $\langle0|:\!\mathcal{O}\!:|0\rangle=0$):

$$\langle0|T\left\{\phi_{1}\cdots\phi_{2n}\right\}|0\rangle=\sum_{\text{emparelhamentos}}\;\prod D_{F}.\tag{19.3}$$

Para $n$ ímpar, o valor esperado é nulo.

### 19.2 A versão fermiônica

Para campos fermiônicos, cada permutação necessária para colocar os campos contraídos lado a lado introduz um sinal:

$$\langle0|T\left\{\psi_{1}\bar\psi_{2}\psi_{3}\bar\psi_{4}\right\}|0\rangle=S_{F}(1-2)S_{F}(3-4)-S_{F}(1-4)S_{F}(3-2),\tag{19.4}$$

o sinal relativo sendo a paridade da permutação. Este é o mecanismo microscópico dos sinais fermiônicos de §16.2.

### 19.3 Por que Wick é o teorema central da teoria de perturbação

O teorema de Wick converte um problema de **operadores** (produtos ordenados no tempo de campos quantizados) em um problema **combinatório** (somar emparelhamentos), cujos termos são funções ordinárias (propagadores). Os diagramas de Feynman são, literalmente, a notação gráfica para os emparelhamentos de (19.3). Toda a Parte IV é um desdobramento disso.

---

## 20. Diagramas de Feynman

### 20.1 Da expansão às regras

Combinando (18.3), (19.2) e a expansão de $\mathcal{L}_{\rm int}$, cada termo da série perturbativa corresponde a um diagrama. Para $\mathcal{L}_{\rm int}=-\frac{\lambda}{4!}\phi^{4}$, as regras no espaço de momentos são:

| Elemento | Fator |
|:---|:---|
| Propagador interno | $\dfrac{i}{p^{2}-m^{2}+i\varepsilon}$ |
| Vértice | $-i\lambda$ |
| Linha externa | $1$ |
| Laço | $\displaystyle\int\!\frac{d^{4}\ell}{(2\pi)^{4}}$ |
| Conservação de momento | em cada vértice |
| Fator de simetria | $1/S$ |

A amplitude $i\mathcal{M}$ é a soma de todos os diagramas **amputados e conexos**.

### 20.2 Fatores de simetria

$S$ é a ordem do grupo de automorfismos do diagrama: o número de permutações de linhas e vértices internos que deixam o diagrama invariante. Os casos mais comuns:

| Diagrama | $S$ |
|:---|:---:|
| Laço "tadpole" (linha que se fecha sobre si) | $2$ |
| Bolha simples entre dois vértices | $2$ |
| Bolha dupla ("sunset") | $6$ |
| Diagramas de árvore genéricos | $1$ |

Fatores de simetria são a fonte de erro mais frequente em cálculos manuais. **No formalismo funcional (Parte V) eles emergem automaticamente**, sem contagem combinatória explícita — uma das vantagens práticas daquele formalismo.

### 20.3 Conexos, amputados e o papel do vácuo

Três reduções sucessivas organizam a expansão:

1. **Diagramas de vácuo se fatoram.** $\langle0|T\{\cdots\}|0\rangle = \left(\text{conexos}\right)\times\exp\left(\sum\text{diagramas de vácuo}\right)$, e a exponencial cancela na normalização $Z[J]/Z[0]$. Diagramas de vácuo nunca contribuem para amplitudes de espalhamento.
2. **Apenas conexos.** A parte desconexa de $S$ é $\delta_{fi}$ e não contribui para o espalhamento propriamente dito.
3. **Amputação.** Os propagadores das pernas externas são removidos e substituídos por espinores/polarizações, conforme a fórmula LSZ (§21).

---

## 21. A redução LSZ

### 21.1 O enunciado

**Fórmula de Lehmann–Symanzik–Zimmermann.** Para um campo escalar com $\langle\Omega|\phi(0)|p\rangle=\sqrt{Z}$:

$$\langle p_{1}\cdots p_{n}|S|k_{1}\cdots k_{m}\rangle = \left[\prod_{i}\frac{1}{\sqrt{Z}}\!\int\! d^{4}x_{i}\,e^{ip_{i}x_{i}}\!\left(\Box_{i}+m^{2}\right)\right]\left[\prod_{j}\frac{1}{\sqrt{Z}}\!\int\! d^{4}y_{j}\,e^{-ik_{j}y_{j}}\!\left(\Box_{j}+m^{2}\right)\right]\times$$
$$\times\;\langle\Omega|T\,\phi(x_{1})\cdots\phi(y_{m})|\Omega\rangle.\tag{21.1}$$

Em linguagem de momentos, a fórmula diz:

> A amplitude de espalhamento é o **resíduo do polo múltiplo** da função de Green exata, quando todos os momentos externos vão à camada de massa física, dividido por $\sqrt{Z}$ para cada perna.

### 21.2 O conteúdo estrutural

Três leituras da fórmula, todas importantes:

1. **Amputação.** O operador $(\Box+m^{2})$ cancela exatamente o polo do propagador da perna externa. A "amputação" de §20.3 é isso.
2. **Independência da escolha de campo interpolante.** Qualquer operador local $\mathcal{O}$ com $\langle\Omega|\mathcal{O}|p\rangle\neq0$ serve. As amplitudes físicas não dependem de qual campo se usa para criar o estado — o que justifica redefinições de campo $\phi\to\phi+c\phi^{3}$, cruciais em teoria efetiva (§32).
3. **Onde $Z$ entra.** O fator $Z^{-1/2}$ por perna é o que torna as amplitudes finitas: a renormalização de função de onda (§30) é exatamente a compensação desse fator.

### 21.3 A versão fermiônica

$$\langle p,s|S|\cdots\rangle\;\supset\;\frac{1}{\sqrt{Z_{2}}}\int d^{4}x\;e^{ipx}\;\bar u^{s}(p)\left(i\not{\partial}_{x}-m\right)\left\langle\Omega\right|T\,\psi(x)\cdots\left|\Omega\right\rangle,\tag{21.2}$$

com $Z_{2}$ a constante de renormalização de função de onda fermiônica. Os espinores $u,\bar u,v,\bar v$ das regras de §16.1 têm sua origem precisamente aqui.

---

## 22. Unitariedade e o teorema óptico

### 22.1 De $S^{\dagger}S=1$ ao teorema óptico

A conservação de probabilidade exige $S^{\dagger}S=\mathbb{1}$. Escrevendo $S=\mathbb{1}+iT$:

$$-i\left(T-T^{\dagger}\right)=T^{\dagger}T.\tag{22.1}$$

Tomando elementos de matriz entre estados $|i\rangle$ e $|f\rangle$ e inserindo um conjunto completo de estados intermediários:

$$\boxed{\;-i\left[\mathcal{M}(i\to f)-\mathcal{M}^{*}(f\to i)\right]=\sum_{X}\int d\Pi_{X}\;\mathcal{M}^{*}(f\to X)\,\mathcal{M}(i\to X)\;}\tag{22.2}$$

Para o caso $i=f$ (espalhamento para frente):

$$2\,\mathrm{Im}\,\mathcal{M}(i\to i)=\sum_{X}\int d\Pi_{X}\left|\mathcal{M}(i\to X)\right|^{2}=2E_{\rm cm}p_{\rm cm}\,\sigma_{\rm tot},\tag{22.3}$$

o **teorema óptico**: a parte imaginária da amplitude de espalhamento para frente é a seção de choque total.

### 22.2 Regras de corte de Cutkosky

O teorema óptico tem uma tradução diagramática exata: a parte imaginária de um diagrama a $n$ laços é obtida **cortando** o diagrama de todas as maneiras possíveis, substituindo cada propagador cortado por

$$\frac{i}{p^{2}-m^{2}+i\varepsilon}\;\longrightarrow\;2\pi\,\delta\!\left(p^{2}-m^{2}\right)\theta(p^{0}),\tag{22.4}$$

e somando. As **regras de Cutkosky** conectam laços a espaços de fase e são a ferramenta padrão para verificar unitariedade em cálculos de ordem superior.

### 22.3 Consequências estruturais

1. **Positividade.** O lado direito de (22.3) é uma soma de módulos ao quadrado, logo $\mathrm{Im}\,\mathcal{M}\geq0$ — um vínculo forte sobre teorias efetivas ("positivity bounds").
2. **Larguras de ressonância.** O propagador de uma partícula instável adquire parte imaginária, $1/(p^{2}-m^{2}+im\Gamma)$, com $\Gamma$ fixada pela unitariedade.
3. **Violação de unitariedade como sinal de nova física.** Amplitudes que crescem com a energia, como no espalhamento $W_{L}W_{L}$ sem Higgs, violam o vínculo de unitariedade a uma escala definida ($\sim1.2$ TeV neste caso). Foi esse argumento que garantiu, antes de 2012, que algo teria de aparecer no LHC.

---

## 23. Observáveis: seções de choque e larguras

### 23.1 Espaço de fase invariante

$$d\Pi_{n}=(2\pi)^{4}\,\delta^{4}\!\left(P-\sum_{f}p_{f}\right)\prod_{f=1}^{n}\frac{d^{3}p_{f}}{(2\pi)^{3}\,2E_{f}}.\tag{23.1}$$

### 23.2 Seção de choque $2\to n$

$$d\sigma=\frac{1}{4\,E_{A}E_{B}\left|v_{A}-v_{B}\right|}\;\overline{\left|\mathcal{M}\right|^{2}}\;d\Pi_{n},\tag{23.2}$$

com o fator de fluxo $4E_{A}E_{B}|v_{A}-v_{B}|=4\sqrt{(p_{A}\cdot p_{B})^{2}-m_{A}^{2}m_{B}^{2}}$ escrito de forma invariante. A barra indica média sobre estados iniciais e soma sobre finais.

**Caso $2\to2$ no centro de massa:**

$$\frac{d\sigma}{d\Omega}=\frac{1}{64\pi^{2}s}\,\frac{\left|\mathbf{p}_{f}\right|}{\left|\mathbf{p}_{i}\right|}\;\overline{\left|\mathcal{M}\right|^{2}},\qquad s=(p_{A}+p_{B})^{2}.\tag{23.3}$$

### 23.3 Largura de decaimento

$$d\Gamma=\frac{1}{2M}\;\overline{\left|\mathcal{M}\right|^{2}}\;d\Pi_{n},\qquad \tau=\frac{1}{\Gamma_{\rm tot}},\qquad \mathrm{BR}(i)=\frac{\Gamma_{i}}{\Gamma_{\rm tot}}.\tag{23.4}$$

**Caso $1\to2$:**

$$\Gamma=\frac{\left|\mathbf{p}\right|}{8\pi M^{2}}\;\overline{\left|\mathcal{M}\right|^{2}},\qquad \left|\mathbf{p}\right|=\frac{\sqrt{\lambda(M^{2},m_{1}^{2},m_{2}^{2})}}{2M},\tag{23.5}$$

com $\lambda(a,b,c)=a^{2}+b^{2}+c^{2}-2ab-2ac-2bc$ a função triangular de Källén.

### 23.4 Partículas idênticas

Para $n$ partículas idênticas no estado final, o espaço de fase recebe um fator $1/n!$, evitando dupla contagem de configurações que diferem apenas por rótulos. Este ponto reaparece de forma crítica no caso de Majorana, onde partícula e antipartícula são idênticas e o fator se aplica a situações em que, no caso de Dirac, não se aplicaria (Apêndice G.5).

### 23.5 Variáveis de Mandelstam

$$s=(p_{1}+p_{2})^{2},\quad t=(p_{1}-p_{3})^{2},\quad u=(p_{1}-p_{4})^{2},\qquad s+t+u=\sum_{i=1}^{4}m_{i}^{2}.\tag{23.6}$$

A **simetria de cruzamento** (*crossing*) afirma que a mesma função analítica $\mathcal{M}(s,t,u)$ descreve $12\to34$, $1\bar3\to\bar24$ e $1\bar4\to\bar23$, em regiões diferentes do plano complexo. É uma consequência direta da analiticidade das funções de Green e do fato de que criar uma partícula de momento $p$ e aniquilar uma antipartícula de momento $-p$ são a mesma operação.

---

# Parte V — Integrais de Trajetória

## 24. Da mecânica quântica à integral funcional

### 24.1 O propagador como soma sobre trajetórias

Dividindo o intervalo temporal em $N$ fatias e inserindo conjuntos completos de estados de posição e momento:

$$\left\langle q_{f},t_{f}\middle| q_{i},t_{i}\right\rangle=\int\mathcal{D}q(t)\;e^{iS[q]},\qquad S[q]=\int_{t_{i}}^{t_{f}}dt\;L(q,\dot q).\tag{24.1}$$

A medida $\mathcal{D}q$ é o limite $N\to\infty$ de $\prod_{k}dq_{k}$ com normalização apropriada. O limite clássico $\hbar\to0$ emerge por fase estacionária: as trajetórias que dominam são as que extremizam $S$.

### 24.2 A generalização para campos

$$\boxed{\;Z=\int\mathcal{D}\phi\;e^{iS[\phi]},\qquad \left\langle\Omega\right|T\,\phi(x_{1})\cdots\phi(x_{n})\left|\Omega\right\rangle=\frac{1}{Z}\int\mathcal{D}\phi\;\phi(x_{1})\cdots\phi(x_{n})\,e^{iS[\phi]}\;}\tag{24.2}$$

**Vantagens sobre o formalismo canônico:**

1. **Covariância manifesta** em todos os passos — nenhuma escolha de tempo privilegiado.
2. **Simetrias** são propriedades da ação e da medida, e portanto transparentes. As anomalias (§17.2b) aparecem como não invariância da medida.
3. **Fatores de simetria** e sinais fermiônicos emergem automaticamente da combinatória funcional.
4. **Teorias de gauge** são tratáveis (Faddeev–Popov, §26) de um modo que a quantização canônica torna extremamente pesado.
5. **Métodos não perturbativos** (instantons, rede, semiclássica) são naturais.

**Desvantagens:** a unitariedade e a positividade do espaço de Hilbert não são manifestas (são manifestas no formalismo canônico), e a medida $\mathcal{D}\phi$ não é rigorosamente definida em dimensão $>1$.

### 24.3 Rotação de Wick

A substituição $t\to-i\tau$ leva $e^{iS}\to e^{-S_{E}}$, com $S_{E}$ a ação euclidiana definida positiva. A integral funcional torna-se uma **medida de probabilidade** — a conexão formal entre TQC e mecânica estatística:

$$Z_{\rm TQC}\;\longleftrightarrow\;Z_{\rm estatística}=\sum_{\rm config}e^{-\beta E}.\tag{24.3}$$

É essa correspondência que fundamenta a QCD na rede, a teoria de fenômenos críticos e a leitura do grupo de renormalização como fluxo em espaço de teorias (§31).

---

## 25. Funcional gerador e ação efetiva

### 25.1 A hierarquia $Z\to W\to\Gamma$

$$Z[J]=\int\mathcal{D}\phi\;\exp\left\{i\left(S[\phi]+\int d^{4}x\;J\phi\right)\right\}\qquad\text{(todas as funções de Green)},\tag{25.1}$$

$$W[J]=-i\ln Z[J]\qquad\text{(funções de Green \textbf{conexas})},\tag{25.2}$$

$$\Gamma[\phi_{c}]=W[J]-\int d^{4}x\;J\,\phi_{c},\qquad \phi_{c}(x)\equiv\frac{\delta W}{\delta J(x)}\qquad\text{(a \textbf{ação efetiva})}.\tag{25.3}$$

A passagem $W\to\Gamma$ é uma **transformada de Legendre**, exatamente como na termodinâmica ($F\to G$).

### 25.2 O significado de $\Gamma$

$$\frac{\delta\Gamma}{\delta\phi_{c}(x)}=-J(x)\qquad\Longrightarrow\qquad \left.\frac{\delta\Gamma}{\delta\phi_{c}}\right|_{J=0}=0.\tag{25.4}$$

**A ação efetiva é a ação clássica corrigida por todos os efeitos quânticos:** suas equações de movimento são as equações exatas para os valores esperados dos campos. Suas propriedades:

1. As derivadas funcionais de $\Gamma$ são as **funções de vértice 1PI** (irredutíveis de uma partícula), $\Gamma^{(n)}$.
2. $\Gamma^{(2)}$ é o inverso do propagador exato: os polos de $[\Gamma^{(2)}]^{-1}$ dão o espectro físico.
3. O mínimo de $\Gamma$ determina o vácuo — é o objeto correto para estudar quebra espontânea de simetria (§33).

### 25.3 O potencial efetivo e a expansão em laços

Para campos constantes, $\Gamma[\phi_{c}]=-V_{\rm eff}(\phi_{c})\int d^{4}x$. A um laço (potencial de Coleman–Weinberg):

$$V_{\rm eff}(\phi)=V_{\rm cl}(\phi)+\frac{1}{2}\int\!\frac{d^{4}k_{E}}{(2\pi)^{4}}\,\ln\left[k_{E}^{2}+V''_{\rm cl}(\phi)\right]+\cdots\tag{25.5}$$

$$=V_{\rm cl}(\phi)+\frac{1}{64\pi^{2}}\sum_{i}(-1)^{2s_{i}}(2s_{i}+1)\,m_{i}^{4}(\phi)\left[\ln\frac{m_{i}^{2}(\phi)}{\mu^{2}}-c_{i}\right]+\cdots\tag{25.6}$$

O sinal $(-1)^{2s_{i}}$ é a assinatura de §15.3: bósons contribuem com $+$, férmions com $-$ (determinante no numerador). Este sinal relativo é a base tanto dos cancelamentos supersimétricos quanto do problema de estabilidade do vácuo eletrofraco, onde o laço do quark top (fermiônico, negativo) empurra $\lambda(\mu)$ para valores negativos em escalas altas.

**A expansão em laços é uma expansão em $\hbar$**, não em acoplamento: restaurando $\hbar$, um diagrama com $L$ laços vem com $\hbar^{L-1}$. Por isso $\Gamma$ a zero laços é $S$.

---

## 26. Campos de gauge: o procedimento de Faddeev–Popov

### 26.1 O problema

A integral $\int\mathcal{D}A\;e^{iS[A]}$ com $S$ invariante de gauge diverge: integra-se infinitas vezes sobre cada órbita de gauge $\{A^{\alpha}_{\mu}\}$, todas com o mesmo peso. O volume infinito do grupo de gauge deve ser fatorado.

### 26.2 O truque de Faddeev–Popov

Insira a identidade

$$1=\Delta_{\rm FP}[A]\int\mathcal{D}\alpha\;\delta\!\left(G(A^{\alpha})\right),\qquad \Delta_{\rm FP}[A]=\det\!\left(\frac{\delta G(A^{\alpha})}{\delta\alpha}\right),\tag{26.1}$$

onde $G(A)=0$ é a condição de fixação de gauge (por exemplo $\partial^{\mu}A_{\mu}-\omega(x)=0$). Fatorando $\int\mathcal{D}\alpha$ (que é o volume do grupo, uma constante que cancela na normalização) e integrando sobre $\omega$ com peso gaussiano de largura $\xi$:

$$Z=\int\mathcal{D}A\;\det\!\left(\frac{\delta G}{\delta\alpha}\right)\exp\left\{i\!\int d^{4}x\left[\mathcal{L}_{\rm YM}-\frac{1}{2\xi}\left(\partial^{\mu}A^{a}_{\mu}\right)^{2}\right]\right\}.\tag{26.2}$$

### 26.3 Fantasmas

O determinante em (26.2) é exponenciado como uma integral de Grassmann, por (15.3):

$$\det\!\left(\frac{\delta G}{\delta\alpha}\right)=\int\mathcal{D}\bar c\,\mathcal{D}c\;\exp\left\{i\!\int d^{4}x\;\bar c^{a}\left(-\partial^{\mu}D_{\mu}^{ac}\right)c^{c}\right\}.\tag{26.3}$$

Os campos $c,\bar c$ são os **fantasmas de Faddeev–Popov**: escalares (spin 0) mas anticomutantes — eles violam o teorema spin-estatística deliberadamente, e por isso **não podem ser estados assintóticos físicos**. Sua função é precisamente cancelar as contribuições dos graus de liberdade não físicos (temporal e longitudinal) do campo de gauge nos laços.

**No caso abeliano** (QED), $D_{\mu}=\partial_{\mu}$ para os fantasmas, o determinante é independente de $A$ e os fantasmas se desacoplam — razão pela qual Gupta–Bleuler basta para QED, mas não para Yang–Mills.

$$\mathcal{L}_{\rm total}=-\frac{1}{4}F^{a}_{\mu\nu}F^{a\,\mu\nu}-\frac{1}{2\xi}\left(\partial^{\mu}A^{a}_{\mu}\right)^{2}+\bar c^{a}\left(-\partial^{\mu}D^{ac}_{\mu}\right)c^{c}.\tag{26.4}$$

### 26.4 A ambiguidade de Gribov

O procedimento supõe que $G(A^{\alpha})=0$ tem **exatamente uma** solução por órbita. Isso é verdade perturbativamente, mas falso globalmente em teorias não abelianas: existem **cópias de Gribov**, configurações distintas satisfazendo a mesma condição de gauge. A restrição da integração à "região fundamental de Gribov" é essencial em tratamentos não perturbativos, mas irrelevante em teoria de perturbação.

---

## 27. BRST e identidades de Ward–Takahashi

### 27.1 A simetria BRST

A lagrangiana completa (26.4) perdeu a invariância de gauge, mas adquiriu uma simetria global fermiônica — a **simetria BRST** (Becchi–Rouet–Stora–Tyutin):

$$s\,A^{a}_{\mu}=D^{ab}_{\mu}c^{b},\qquad s\,c^{a}=-\frac{g}{2}f^{abc}c^{b}c^{c},\qquad s\,\bar c^{a}=B^{a},\qquad s\,B^{a}=0,\tag{27.1}$$

com $B^{a}$ o campo auxiliar de Nakanishi–Lautrup. A propriedade fundamental é a **nilpotência**:

$$\boxed{\;s^{2}=0\;}\tag{27.2}$$

que segue da identidade de Jacobi para $f^{abc}$.

### 27.2 O que BRST resolve

1. **Definição do espaço físico.** Os estados físicos são a **cohomologia** de $s$: estados fechados ($s|\psi\rangle=0$) módulo exatos ($|\psi\rangle=s|\chi\rangle$). Isso generaliza a condição de Gupta–Bleuler (8.5) para o caso não abeliano.
2. **Unitariedade.** O teorema de Kugo–Ojima mostra que os estados de norma negativa (fantasmas e polarizações não físicas) formam quartetos que se cancelam na cohomologia, garantindo unitariedade no subespaço físico.
3. **Renormalizabilidade.** A simetria BRST é preservada pela renormalização, e as identidades de Slavnov–Taylor que ela gera garantem que a estrutura de contratermos respeite a invariância de gauge a todas as ordens (teorema de 't Hooft–Veltman).
4. **Independência de gauge.** Como $\partial\Gamma/\partial\xi$ é $s$-exato, as amplitudes físicas não dependem de $\xi$.

### 27.3 Identidades de Ward–Takahashi

Em QED, a versão abeliana das identidades de Slavnov–Taylor:

$$q_{\mu}\,\Gamma^{\mu}(p',p)=S^{-1}(p')-S^{-1}(p),\qquad q=p'-p,\tag{27.3}$$

com $\Gamma^{\mu}$ o vértice exato e $S$ o propagador exato. Consequências:

1. **$Z_{1}=Z_{2}$.** As renormalizações do vértice e da função de onda do elétron são iguais, o que implica que a renormalização da carga vem **somente** da polarização do vácuo:
$$e_{\rm ren}=e_{0}\,\frac{Z_{2}}{Z_{1}}\sqrt{Z_{3}}=e_{0}\sqrt{Z_{3}}.\tag{27.4}$$
**Isso é o que garante a universalidade da carga elétrica**: elétron e próton, com dinâmicas completamente diferentes, têm cargas exatamente opostas, porque a renormalização depende apenas do fóton.
2. **Transversalidade da polarização do vácuo.** $q_{\mu}\Pi^{\mu\nu}(q)=0$, logo $\Pi^{\mu\nu}=(q^{2}\eta^{\mu\nu}-q^{\mu}q^{\nu})\Pi(q^{2})$: **o fóton permanece sem massa a todas as ordens**.
3. **Desacoplamento de fótons longitudinais.** $q_{\mu}\mathcal{M}^{\mu}=0$ para amplitudes com fótons externos — uma verificação computacional padrão.

---

# Parte VI — Renormalização

## 28. Divergências e contagem de potências

### 28.1 A origem das divergências

Um laço de momento não restrito produz $\int d^{4}\ell\,f(\ell)$, que diverge no ultravioleta sempre que $f$ cai lentamente. Fisicamente, a divergência reflete a hipótese — não verificada — de que a teoria continua válida a distâncias arbitrariamente curtas. A renormalização é o procedimento sistemático que torna as **predições** independentes dessa hipótese.

### 28.2 Grau superficial de divergência

Para um diagrama com $L$ laços, $I_{B}$ propagadores bosônicos e $I_{F}$ fermiônicos internos:

$$D = 4L - 2I_{B} - I_{F}.\tag{28.1}$$

Usando as relações topológicas ($L=I-V+1$, contagem de pernas nos vértices), obtém-se a forma útil, que depende apenas do **conteúdo externo** e das dimensões dos acoplamentos:

$$\boxed{\;D = 4 - E_{B} - \frac{3}{2}E_{F} - \sum_{i}V_{i}\,\delta_{i},\qquad \delta_{i}\equiv 4-d_{i}\;}\tag{28.2}$$

com $d_{i}$ a dimensão de massa do $i$-ésimo operador de interação e $V_{i}$ o número de vértices desse tipo. O diagrama diverge se $D\geq0$ (logaritmicamente se $D=0$).

### 28.3 A classificação das teorias

| $\delta_{i}=4-d_{i}$ | Dimensão do acoplamento | Classe | Comportamento |
|:---|:---|:---|:---|
| $>0$ | positiva | **super-renormalizável** | número **finito** de diagramas divergentes |
| $=0$ | adimensional | **renormalizável** | número finito de **tipos** de divergência |
| $<0$ | negativa | **não renormalizável** | infinitos tipos; teoria efetiva (§32) |

Exemplos: $\phi^{3}$ em $D=4$ é super-renormalizável; $\phi^{4}$, QED, Yang–Mills e Yukawa são renormalizáveis; a interação de Fermi ($G_{F}$, dimensão $-2$) e a gravitação ($1/M_{\rm Pl}^{2}$) são não renormalizáveis.

### 28.4 Divergências em QED

De (28.2) com $\delta=0$: $D=4-E_{\gamma}-\tfrac32 E_{e}$. Os diagramas superficialmente divergentes são:

| $(E_{\gamma},E_{e})$ | $D$ | Objeto | Divergência efetiva |
|:---|:---:|:---|:---|
| $(2,0)$ | $2$ | polarização do vácuo $\Pi^{\mu\nu}$ | log (a quadrática é morta pela identidade de Ward) |
| $(0,2)$ | $1$ | autoenergia do elétron $\Sigma$ | log (a linear é morta pela simetria quiral) |
| $(1,2)$ | $0$ | vértice $\Gamma^{\mu}$ | log |
| $(3,0)$ | $1$ | — | nula pelo **teorema de Furry** (§16.4) |
| $(4,0)$ | $0$ | luz-por-luz | finita pela identidade de Ward |

**Apenas três estruturas divergem**, e cada uma corresponde a um parâmetro da lagrangiana ($m$, $e$, normalização dos campos). Esta é a essência da renormalizabilidade: **o número de divergências é finito e igual ao número de parâmetros disponíveis**.

**Observação sobre a "divergência efetiva".** Os graus superficiais em (28.4) superestimam as divergências reais. As simetrias reduzem-nas: a identidade de Ward (27.3) força $\Pi^{\mu\nu}=(q^{2}\eta^{\mu\nu}-q^{\mu}q^{\nu})\Pi(q^{2})$, extraindo dois potências de $q$ e transformando divergência quadrática em logarítmica — **o que é o que impede a geração radiativa de massa para o fóton**. Analogamente, a simetria quiral protege a massa do elétron: $\delta m_{e}\propto m_{e}\ln\Lambda$, e não $\Lambda$. Este é o conceito de **naturalidade técnica** de 't Hooft: *um parâmetro pequeno é natural se pô-lo a zero aumenta a simetria da teoria*. A massa do Higgs, sem tal proteção, é o problema da hierarquia.

---

## 29. Regularização

Regularizar é tornar as integrais temporariamente finitas com um parâmetro auxiliar, de modo a manipulá-las com rigor. **Nenhum resultado físico pode depender do regulador.**

| Método | Parâmetro | Preserva Lorentz | Preserva gauge | Observações |
|:---|:---|:---:|:---:|:---|
| Corte de momento | $\Lambda$ | não | **não** | intuitivo; quebra a identidade de Ward |
| Pauli–Villars | $M$ | sim | sim (abeliano) | falha em não abeliano |
| Rede | $a$ | não | sim | não perturbativo; problema com férmions quirais |
| **Dimensional** | $d=4-\epsilon$ | sim | **sim** | padrão; problema com $\gamma^{5}$ |

### 29.1 Regularização dimensional

Continua-se analiticamente a dimensão do espaço-tempo para $d=4-\epsilon$. As divergências logarítmicas aparecem como polos simples $1/\epsilon$. A fórmula mestra (Apêndice B):

$$\int\!\frac{d^{d}\ell}{(2\pi)^{d}}\;\frac{1}{\left(\ell^{2}-\Delta+i\varepsilon\right)^{n}}=\frac{(-1)^{n}\,i}{(4\pi)^{d/2}}\;\frac{\Gamma\!\left(n-\tfrac{d}{2}\right)}{\Gamma(n)}\;\left(\frac{1}{\Delta}\right)^{n-d/2}.\tag{29.1}$$

Para manter a dimensão do acoplamento fixa em $d\neq4$, introduz-se a escala arbitrária $\mu$:

$$\lambda\;\to\;\lambda\,\mu^{\epsilon},\qquad e\;\to\;e\,\mu^{\epsilon/2}.\tag{29.2}$$

**A escala $\mu$ é o gérmen de todo o grupo de renormalização** (§31): ela é arbitrária, e a exigência de que a física não dependa dela gera as equações de fluxo.

### 29.2 O problema de $\gamma^{5}$

Não existe definição de $\gamma^{5}$ em $d$ dimensões que satisfaça simultaneamente $\{\gamma^{5},\gamma^{\mu}\}=0$ e a ciclicidade do traço com $\operatorname{tr}(\gamma^{5}\gamma^{\mu}\gamma^{\nu}\gamma^{\rho}\gamma^{\sigma})=-4i\varepsilon^{\mu\nu\rho\sigma}$. O esquema de 't Hooft–Veltman quebra o anticomutador nas dimensões "extras", ao custo de exigir contratermos que restaurem a simetria quiral. **Isso não é um defeito técnico: é o reflexo, na regularização, da anomalia quiral (§17)** — nenhum regulador pode preservar uma simetria que a teoria genuinamente não tem.

---

## 30. Contratermos e esquemas de renormalização

### 30.1 A lagrangiana nua e a renormalizada

Escreva a lagrangiana em termos de campos e parâmetros **nus** (divergentes) e reescreva-a em termos de renormalizados:

$$\phi_{0}=\sqrt{Z}\,\phi,\qquad m_{0}=Z_{m}m,\qquad \lambda_{0}=Z_{\lambda}\lambda\,\mu^{\epsilon},\tag{30.1}$$

$$\mathcal{L}=\underbrace{\frac{1}{2}(\partial\phi)^{2}-\frac{1}{2}m^{2}\phi^{2}-\frac{\lambda}{4!}\phi^{4}}_{\text{renormalizada}}+\underbrace{\frac{\delta_{Z}}{2}(\partial\phi)^{2}-\frac{\delta_{m}}{2}\phi^{2}-\frac{\delta_{\lambda}}{4!}\phi^{4}}_{\text{contratermos}}.\tag{30.2}$$

Os contratermos $\delta_{i}=Z_{i}-1$ são fixados ordem a ordem para cancelar as divergências. **Nada foi "jogado fora"**: os parâmetros nus nunca foram observáveis, e a divergência apenas expressa que eles são infinitos na teoria idealizada sem escala de corte.

### 30.2 Esquemas

| Esquema | Condição | Uso típico |
|:---|:---|:---|
| **On-shell** | polo do propagador em $p^{2}=m_{\rm fis}^{2}$ com resíduo $i$; $\Gamma^{\mu}(q\to0)=\gamma^{\mu}$ | QED, física de baixa energia |
| **$\overline{\rm MS}$** | subtrai-se $\dfrac{1}{\bar\epsilon}=\dfrac{1}{\epsilon}-\gamma_{E}+\ln4\pi$ | QCD, cálculos de altas ordens |
| **Momento (MOM)** | fixa-se em $p^{2}=-\mu^{2}$ euclidiano | rede, esquemas não perturbativos |

Esquemas diferentes definem parâmetros diferentes (a "massa $\overline{\rm MS}$" do quark top difere da massa de polo por $\sim$ 10 GeV). **Relações entre observáveis são independentes de esquema**; valores de parâmetros não.

### 30.3 O teorema BPHZ

**Teorema (Bogoliubov–Parasiuk–Hepp–Zimmermann).** Em uma teoria renormalizável, a **fórmula floresta** de Zimmermann define uma subtração recursiva que remove todas as divergências, incluindo subdivergências aninhadas e sobrepostas, a todas as ordens em teoria de perturbação, com um número finito de contratermos locais.

Este é o teorema que estabelece a renormalização como um procedimento matematicamente completo, e não uma prescrição ordem a ordem. Combinado com as identidades de Slavnov–Taylor (§27.2), ele garante a renormalizabilidade das teorias de gauge — o resultado de 't Hooft e Veltman (1971) que tornou o Modelo Padrão uma teoria calculável.

### 30.4 Exemplo: renormalização a um laço em QED

$$Z_{2}=1-\frac{e^{2}}{16\pi^{2}}\frac{1}{\bar\epsilon}+\cdots,\qquad Z_{3}=1-\frac{e^{2}}{12\pi^{2}}\frac{1}{\bar\epsilon}+\cdots,\qquad Z_{1}=Z_{2}\ \text{(Ward)},\tag{30.3}$$

$$e_{0}=e\,\mu^{\epsilon/2}\,Z_{3}^{-1/2}\qquad\Longrightarrow\qquad \text{só }Z_{3}\text{ renormaliza a carga}.\tag{30.4}$$

O resultado finito mais célebre desse setor é o momento magnético anômalo do elétron:

$$a_{e}=\frac{g-2}{2}=\frac{\alpha}{2\pi}+\mathcal{O}(\alpha^{2})\approx0.00116,\tag{30.5}$$

calculado hoje até $\mathcal{O}(\alpha^{5})$ e concordando com a medida em mais de dez algarismos significativos — a predição mais precisa de toda a física.

---

## 31. O grupo de renormalização

### 31.1 A equação de Callan–Symanzik

A escala $\mu$ introduzida em (29.2) é arbitrária. As funções de Green **nuas** não dependem dela; as renormalizadas dependem, mas de forma compensada pela variação dos acoplamentos:

$$\boxed{\;\left[\mu\frac{\partial}{\partial\mu}+\beta(\lambda)\frac{\partial}{\partial\lambda}+n\,\gamma(\lambda)\right]G^{(n)}\!\left(x_{1},\ldots,x_{n};\lambda,\mu\right)=0\;}\tag{31.1}$$

$$\beta(\lambda)\equiv\mu\frac{d\lambda}{d\mu},\qquad \gamma\equiv\frac{1}{2}\mu\frac{d\ln Z}{d\mu}\quad\text{(dimensão anômala)}.\tag{31.2}$$

**Leitura física:** mudar a escala de observação é equivalente a mudar os acoplamentos. Um "acoplamento constante" não existe; existe uma **trajetória** no espaço de acoplamentos, parametrizada pela energia.

### 31.2 Funções beta de referência (um laço)

$$\beta(\lambda)_{\phi^{4}}=\frac{3\lambda^{2}}{16\pi^{2}},\qquad \beta(e)_{\rm QED}=\frac{e^{3}}{12\pi^{2}},\tag{31.3}$$

$$\beta(g)_{\rm SU(N)}=-\frac{g^{3}}{16\pi^{2}}\left(\frac{11}{3}N-\frac{2}{3}n_{f}\right).\tag{31.4}$$

### 31.3 As duas classes de comportamento

**Liberdade infravermelha / polo de Landau ($\beta>0$).** Para QED,

$$\alpha(\mu)=\frac{\alpha(m_{e})}{1-\dfrac{2\alpha(m_{e})}{3\pi}\ln\dfrac{\mu}{m_{e}}},\tag{31.5}$$

que diverge em $\mu_{\rm Landau}\sim10^{286}$ GeV. Longe de ser um problema prático, isso sinaliza que QED é uma **teoria efetiva**: está embutida no Modelo Padrão eletrofraco muito antes dessa escala. O crescimento observado é real: $\alpha(m_{Z})\approx1/128$ contra $\alpha(0)\approx1/137$.

**Liberdade assintótica ($\beta<0$).** Para $SU(3)$ com $n_{f}<17$, o coeficiente em (31.4) é positivo e $\beta<0$:

$$\alpha_{s}(Q^{2})=\frac{12\pi}{\left(33-2n_{f}\right)\ln\!\left(Q^{2}/\Lambda_{\rm QCD}^{2}\right)},\qquad \Lambda_{\rm QCD}\approx200\ \mathrm{MeV}.\tag{31.6}$$

O acoplamento **decresce** com a energia: quarks são quase livres a curtas distâncias (permitindo cálculo perturbativo em processos duros) e fortemente acoplados a longas distâncias (confinamento). Gross, Politzer e Wilczek (1973); Nobel 2004.

**A origem do sinal.** O termo $+11N/3$ vem da autointeração dos glúons (antiscreening — só existe no caso não abeliano); o termo $-2n_{f}/3$ vem dos laços de férmions (screening, como em QED). A liberdade assintótica é, portanto, uma consequência direta da estrutura não abeliana.

### 31.4 Pontos fixos e universalidade

Zeros de $\beta$ são **pontos fixos**: a teoria torna-se invariante de escala (e tipicamente conforme). Perto de um ponto fixo, os operadores classificam-se por sua dimensão $\Delta$:

| Classe | $\Delta$ | Comportamento no infravermelho |
|:---|:---|:---|
| **relevante** | $\Delta<4$ | cresce; domina a física de baixa energia |
| **marginal** | $\Delta=4$ | fluxo logarítmico; decide-se em ordem superior |
| **irrelevante** | $\Delta>4$ | decai como $(E/\Lambda)^{\Delta-4}$ |

**Universalidade.** Como os operadores irrelevantes decaem, teorias microscopicamente muito diferentes convergem para o mesmo comportamento de longa distância. É por isso que a física a baixas energias é descrita por poucos parâmetros, e por que sistemas fisicamente díspares (um ferromagneto, um fluido no ponto crítico) compartilham expoentes críticos. Esta é, em uma frase, a razão pela qual a física funciona por escalas.

---

## 32. Teoria efetiva de campos

### 32.1 O princípio

Toda teoria quântica de campos é uma **teoria efetiva** válida abaixo de uma escala $\Lambda$. A prescrição:

1. Identifique os graus de liberdade leves e as simetrias em baixa energia.
2. Escreva **todos** os operadores locais compatíveis com essas simetrias.
3. Organize-os por dimensão:

$$\mathcal{L}_{\rm eff}=\sum_{d\leq4}c_{i}\,\mathcal{O}_{i}^{(d)}+\sum_{d>4}\frac{c_{i}}{\Lambda^{d-4}}\,\mathcal{O}_{i}^{(d)}.\tag{32.1}$$

Os operadores de $d>4$ são suprimidos por potências de $E/\Lambda$, e a expansão é sistemática e **preditiva** a qualquer ordem desejada.

### 32.2 O teorema de desacoplamento

**Teorema (Appelquist–Carazzone).** Em um esquema de massa física, os efeitos de uma partícula pesada de massa $M$ em processos de energia $E\ll M$ são ou (i) absorvíveis na redefinição dos parâmetros da teoria leve, ou (ii) suprimidos por potências de $E/M$.

**Exceções importantes:** partículas cuja massa vem da quebra de simetria (o quark top no Modelo Padrão) **não desacoplam** — seus efeitos crescem com a massa. É por isso que o top domina as correções radiativas eletrofracas.

### 32.3 Exemplos canônicos

| Teoria efetiva | $\Lambda$ | Operador líder |
|:---|:---|:---|
| Fermi (decaimento $\beta$) | $m_{W}$ | $\dfrac{G_{F}}{\sqrt2}(\bar p n)(\bar e\nu)$, $d=6$ |
| Euler–Heisenberg | $m_{e}$ | $(F_{\mu\nu}F^{\mu\nu})^{2}$, $d=8$ |
| Quiral (píons) | $4\pi f_{\pi}$ | $\dfrac{f_{\pi}^{2}}{4}\operatorname{tr}\partial_{\mu}U\partial^{\mu}U^{\dagger}$ |
| Gravitação | $M_{\rm Pl}$ | $R$, com $R^{2}$ suprimido |
| **SMEFT** | $\Lambda_{\rm NP}$ | **operador de Weinberg $\dfrac{(LH)(LH)}{\Lambda}$, $d=5$** |

A última linha é o ponto de contato direto com o documento companheiro: no Modelo Padrão, **existe exatamente um operador de dimensão cinco**, e ele gera massa de Majorana para os neutrinos. Sendo o operador de menor dimensão acima de quatro, é o *primeiro* efeito esperado de qualquer nova física — e sua supressão por $1/\Lambda$ explica naturalmente a pequenez de $m_{\nu}$. Isso é desenvolvido no Apêndice G.6.

---

# Parte VII — Simetrias Quebradas e Teorias de Gauge

## 33. Quebra espontânea de simetria e o teorema de Goldstone

### 33.1 O conceito

Uma simetria é **espontaneamente quebrada** quando a ação é invariante mas o **vácuo** não:

$$\left[Q,H\right]=0\qquad\text{mas}\qquad Q\,|\Omega\rangle\neq0.\tag{33.1}$$

O exemplo mínimo é o potencial "chapéu mexicano":

$$V(\phi)=-\mu^{2}|\phi|^{2}+\lambda|\phi|^{4},\qquad \mu^{2}>0\;\;\Longrightarrow\;\;|\langle\phi\rangle|=v/\sqrt2=\sqrt{\mu^{2}/2\lambda}.\tag{33.2}$$

A escolha de fase do vácuo quebra $U(1)$; os vácuos degenerados formam a órbita do grupo.

### 33.2 O teorema de Goldstone

**Teorema (Goldstone, 1961; Goldstone–Salam–Weinberg, 1962).** Para cada gerador **global** e contínuo espontaneamente quebrado, o espectro contém um bóson escalar sem massa.

*Demonstração.* Expanda o potencial em torno do mínimo $\phi_{0}$:
$$V(\phi)=V(\phi_{0})+\frac{1}{2}\left.\frac{\partial^{2}V}{\partial\phi^{a}\partial\phi^{b}}\right|_{\phi_{0}}\!\!\delta\phi^{a}\delta\phi^{b}+\cdots,\qquad M^{2}_{ab}\equiv\left.\partial_{a}\partial_{b}V\right|_{\phi_{0}}.$$
A invariância $V(\phi)=V(\phi+\epsilon\,T^{A}\phi)$ diferenciada duas vezes e avaliada em $\phi_{0}$ dá
$$M^{2}_{ab}\left(T^{A}\phi_{0}\right)^{b}=0.\tag{33.3}$$
Logo, para cada gerador **quebrado** ($T^{A}\phi_{0}\neq0$), o vetor $T^{A}\phi_{0}$ é um autovetor de $M^{2}$ com autovalor zero: um bóson sem massa. Para geradores **não quebrados** ($T^{A}\phi_{0}=0$), (33.3) é vazia. $\blacksquare$

**Contagem:** $\dim G-\dim H$ bósons de Goldstone, com $H\subset G$ o subgrupo não quebrado (o *little group* do vácuo).

### 33.3 Realização em correntes e o teorema de Nambu

Existe uma formulação equivalente e mais robusta (independente de teoria de perturbação): se $\partial_{\mu}j^{\mu A}=0$ e $\langle\Omega|j^{\mu A}(x)|\pi^{B}(p)\rangle=i f\,p^{\mu}\delta^{AB}e^{-ipx}\neq0$, então a conservação da corrente exige $p^{2}=0$. A constante $f$ (para píons, $f_{\pi}\approx93$ MeV) mede a intensidade da quebra.

### 33.4 Aplicações

| Sistema | $G\to H$ | Goldstones |
|:---|:---|:---|
| Ferromagneto | $SO(3)\to SO(2)$ | 2 magnons |
| QCD (2 sabores leves) | $SU(2)_{L}\times SU(2)_{R}\to SU(2)_{V}$ | 3 píons (pseudo-Goldstones) |
| Supercondutor | $U(1)$ | "comido" (Higgs; §34) |
| Eletrofraco | $SU(2)_{L}\times U(1)_{Y}\to U(1)_{\rm em}$ | 3 "comidos" $\to$ $W^{\pm}_{L},Z_{L}$ |

Os píons são **pseudo**-Goldstones: a simetria quiral é apenas aproximada (quebrada explicitamente pelas massas dos quarks), o que dá $m_{\pi}^{2}\propto m_{q}$ — a relação de Gell-Mann–Oakes–Renner.

---

## 34. O mecanismo de Higgs

### 34.1 A escapatória do teorema de Goldstone

Quando a simetria quebrada é **local** (de gauge), o teorema de Goldstone não se aplica: sua demonstração usa a existência de uma carga conservada bem definida, que em gauge covariante requer estados de norma indefinida. O que acontece em vez disso é:

$$\boxed{\;\text{bóson de Goldstone} + \text{bóson de gauge sem massa}\;\longrightarrow\;\text{bóson de gauge massivo}\;}$$

A contagem de graus de liberdade é preservada: $1+2=3$. O Goldstone torna-se a polarização longitudinal — ele foi "comido".

### 34.2 O caso abeliano

$$\mathcal{L}=-\frac{1}{4}F^{2}+\left|D_{\mu}\phi\right|^{2}-V(\phi),\qquad D_{\mu}=\partial_{\mu}-igA_{\mu}.\tag{34.1}$$

Escrevendo $\phi=\frac{1}{\sqrt2}\left(v+h(x)\right)e^{i\theta(x)/v}$ e usando a liberdade de gauge para eliminar $\theta$ (**gauge unitário**):

$$\left|D_{\mu}\phi\right|^{2}=\frac{1}{2}(\partial h)^{2}+\frac{1}{2}g^{2}v^{2}A_{\mu}A^{\mu}\left(1+\frac{h}{v}\right)^{2}.\tag{34.2}$$

O bóson de gauge adquire $m_{A}=gv$, e sobra um escalar físico $h$ com $m_{h}=\sqrt{2\lambda}\,v$ — o **bóson de Higgs**. O acoplamento $h$–$A$–$A$ é $\propto m_{A}^{2}/v$: **o Higgs acopla-se proporcionalmente à massa**, a assinatura experimental decisiva.

### 34.3 O caso eletrofraco

Com $\Phi$ um dubleto de $SU(2)_{L}$ de hipercarga $Y=1/2$ e $\langle\Phi\rangle=(0,v/\sqrt2)^{T}$:

$$SU(2)_{L}\times U(1)_{Y}\;\longrightarrow\;U(1)_{\rm em},\qquad 4-1=3\ \text{geradores quebrados}.\tag{34.3}$$

$$m_{W}=\frac{gv}{2},\qquad m_{Z}=\frac{v\sqrt{g^{2}+g'^{2}}}{2}=\frac{m_{W}}{\cos\theta_{W}},\qquad m_{\gamma}=0,\tag{34.4}$$

$$\rho\equiv\frac{m_{W}^{2}}{m_{Z}^{2}\cos^{2}\theta_{W}}=1\quad\text{a nível de árvore},\tag{34.5}$$

esta última sendo consequência de uma simetria **custodial** $SU(2)_{V}$ acidental do potencial do Higgs, e um dos testes de precisão mais bem verificados do Modelo Padrão. Com $v\simeq246$ GeV e $m_{h}\simeq125$ GeV, tem-se $\lambda\simeq0.13$.

### 34.4 Gauge unitário versus $R_{\xi}$

| Gauge | Propagador do vetor | Goldstones | Uso |
|:---|:---|:---|:---|
| **Unitário** | $\dfrac{-i(\eta^{\mu\nu}-k^{\mu}k^{\nu}/m^{2})}{k^{2}-m^{2}}$ | ausentes | espectro físico manifesto |
| **$R_{\xi}$** | $\dfrac{-i}{k^{2}-m^{2}}\left[\eta^{\mu\nu}-(1-\xi)\dfrac{k^{\mu}k^{\nu}}{k^{2}-\xi m^{2}}\right] $ | presentes, massa $\sqrt{\xi}\,m$ | renormalizabilidade manifesta |

No gauge unitário o propagador não decai no ultravioleta e a renormalizabilidade fica oculta; no gauge $R_{\xi}$ ela é manifesta, ao custo de manter os Goldstones (não físicos) como campos internos. A equivalência dos dois é uma verificação padrão, e foi ao demonstrar a renormalizabilidade em $R_{\xi}$ que 't Hooft estabeleceu a consistência do Modelo Padrão.

---

## 35. Teorias de Yang–Mills

### 35.1 A construção

Promova uma simetria global $G$ a local, $\psi\to U(x)\psi$ com $U=e^{i\alpha^{a}(x)T^{a}}$. A derivada usual não é covariante; introduza a **derivada covariante** e o campo de gauge:

$$D_{\mu}=\partial_{\mu}-igA^{a}_{\mu}T^{a},\qquad A_{\mu}\to UA_{\mu}U^{\dagger}-\frac{i}{g}\left(\partial_{\mu}U\right)U^{\dagger},\tag{35.1}$$

$$F^{a}_{\mu\nu}=\partial_{\mu}A^{a}_{\nu}-\partial_{\nu}A^{a}_{\mu}+g\,f^{abc}A^{b}_{\mu}A^{c}_{\nu},\qquad \left[D_{\mu},D_{\nu}\right]=-igF^{a}_{\mu\nu}T^{a},\tag{35.2}$$

$$\mathcal{L}_{\rm YM}=-\frac{1}{4}F^{a}_{\mu\nu}F^{a\,\mu\nu}+\bar\psi\left(i\not{D}-m\right)\psi.\tag{35.3}$$

### 35.2 O que é novo em relação ao caso abeliano

1. **Autointeração.** O termo $gf^{abc}A^{b}A^{c}$ em $F$ produz vértices de três e quatro glúons. Os bósons de gauge carregam a própria carga que mediam.
2. **Fantasmas obrigatórios.** Como visto em §26.3, o determinante de Faddeev–Popov depende de $A$ e não se desacopla.
3. **Liberdade assintótica.** A autointeração produz o termo $+11N/3$ em (31.4), com sinal oposto ao dos férmions.
4. **Estrutura topológica.** Instantons, o termo $\theta$ e o problema forte de $CP$.
5. **Confinamento.** Fenômeno não perturbativo, sem demonstração analítica (um dos problemas do milênio).

### 35.3 Um termo que não se pode escrever no caso abeliano

$$\mathcal{L}_{\theta}=\theta\,\frac{g^{2}}{32\pi^{2}}\,\varepsilon^{\mu\nu\rho\sigma}F^{a}_{\mu\nu}F^{a}_{\rho\sigma}.\tag{35.4}$$

É uma derivada total e não afeta as equações de movimento clássicas, mas contribui não perturbativamente (setores de instanton) e viola $P$ e $CP$. O limite experimental sobre o momento de dipolo elétrico do nêutron impõe $|\bar\theta|\lesssim10^{-10}$ — o **problema forte de $CP$**, cuja solução mais popular (Peccei–Quinn) prevê o áxion.

---

## 36. Anomalias de gauge e seu cancelamento

### 36.1 Por que anomalias de gauge são fatais

Uma anomalia em uma corrente **global** (como a axial, §17) é um fato físico interessante. Uma anomalia em uma corrente de **gauge** é uma inconsistência: ela quebra as identidades de Ward–Slavnov–Taylor, reintroduz os estados de norma negativa no espectro físico e destrói a unitariedade e a renormalizabilidade.

$$\boxed{\;\text{As anomalias de gauge \textbf{devem} cancelar. Isso é um vínculo sobre o conteúdo de partículas.}\;}$$

### 36.2 A condição de cancelamento

A anomalia triangular com três correntes de gauge é proporcional ao invariante simétrico

$$\mathcal{A}^{abc}=\operatorname{tr}\left[T^{a}\left\{T^{b},T^{c}\right\}\right]_{L}-\operatorname{tr}\left[T^{a}\left\{T^{b},T^{c}\right\}\right]_{R}.\tag{36.1}$$

Casos em que se anula automaticamente: teorias **vetoriais** (QED, QCD — os conteúdos $L$ e $R$ são idênticos) e grupos "seguros" ($SU(2)$, cujas representações são pseudo-reais, e $SO(N)$ para $N\neq6$, $Sp(N)$, $E_{6,7,8}$, $G_{2}$, $F_{4}$).

### 36.3 O Modelo Padrão

O Modelo Padrão é **quiral** ($L$ e $R$ têm conteúdos diferentes) e a condição (36.1) é não trivial. Escrevendo todos os férmions como canhotos, com hipercarga na convenção $Q=T_{3}+Y$:

| Campo | $SU(3)_{c}$ | $SU(2)_{L}$ | $Y$ | multiplicidade |
|:---|:---:|:---:|:---:|:---:|
| $Q_{L}$ | $\mathbf{3}$ | $\mathbf{2}$ | $+1/6$ | $6$ |
| $u^{c}_{L}$ | $\bar{\mathbf{3}}$ | $\mathbf{1}$ | $-2/3$ | $3$ |
| $d^{c}_{L}$ | $\bar{\mathbf{3}}$ | $\mathbf{1}$ | $+1/3$ | $3$ |
| $L_{L}$ | $\mathbf{1}$ | $\mathbf{2}$ | $-1/2$ | $2$ |
| $e^{c}_{L}$ | $\mathbf{1}$ | $\mathbf{1}$ | $+1$ | $1$ |

As quatro condições, verificadas explicitamente por geração:

$$\left[SU(3)\right]^{2}U(1):\quad 2\!\left(\tfrac16\right)+\left(-\tfrac23\right)+\left(\tfrac13\right)=\tfrac13-\tfrac23+\tfrac13=0\;\checkmark\tag{36.2}$$

$$\left[SU(2)\right]^{2}U(1):\quad 3\!\left(\tfrac16\right)+1\!\left(-\tfrac12\right)=\tfrac12-\tfrac12=0\;\checkmark\tag{36.3}$$

$$\left[U(1)\right]^{3}:\quad 6\!\left(\tfrac16\right)^{3}+3\!\left(-\tfrac23\right)^{3}+3\!\left(\tfrac13\right)^{3}+2\!\left(-\tfrac12\right)^{3}+1\!\left(1\right)^{3}=\tfrac{1}{36}-\tfrac{32}{36}+\tfrac{4}{36}-\tfrac{9}{36}+\tfrac{36}{36}=0\;\checkmark\tag{36.4}$$

$$\text{grav}^{2}U(1):\quad 6\!\left(\tfrac16\right)+3\!\left(-\tfrac23\right)+3\!\left(\tfrac13\right)+2\!\left(-\tfrac12\right)+1\!\left(1\right)=1-2+1-1+1=0\;\checkmark\tag{36.5}$$

**Todas se anulam — mas apenas quando quarks e léptons são contados juntos.** Nenhum dos dois setores é anômalo-livre isoladamente. As anomalias exigem, portanto, que as gerações sejam **completas**: o quark top foi previsto por esse argumento após a descoberta do $\tau$. E o cancelamento fixa a quantização da hipercarga, explicando por que $|Q_{e}|=|Q_{p}|$ exatamente.

### 36.4 A anomalia de Witten

Além das anomalias triangulares (perturbativas), existe uma obstrução **global**: uma teoria com $SU(2)$ e um número **ímpar** de dubletos de Weyl é inconsistente ($\pi_{4}(SU(2))=\mathbb{Z}_{2}$). O Modelo Padrão tem, por geração, $3$ (cores) $+1$ (leptônico) $=4$ dubletos — par. $\checkmark$ Este é um vínculo topológico que a análise perturbativa não capta.

---

# Parte VIII

## 37. Síntese

### 37.1 A cadeia lógica

$$\underbrace{\text{MQ}+\text{Lorentz}+\text{localidade}}_{\S1}\;\Rightarrow\;\underbrace{\text{espaço de Fock},\;\text{antipartículas}}_{\S5\text{–}\S7}\;\Rightarrow\;\underbrace{\text{spin-estatística},\;CPT}_{\S14}$$

$$\underbrace{\text{classificação de Wigner}}_{\S4}\;\Rightarrow\;\underbrace{\text{campos como representações}}_{\S9}\;\Rightarrow\;\underbrace{\text{invariância de gauge para } |h|\geq1}_{\S4.4,\;\S8,\;\S35}$$

$$\underbrace{\text{Dyson}+\text{Wick}}_{\S18\text{–}\S19}\;\Rightarrow\;\underbrace{\text{Feynman}+\text{LSZ}}_{\S20\text{–}\S21}\;\Rightarrow\;\underbrace{\text{divergências}}_{\S28}\;\Rightarrow\;\underbrace{\text{renormalização}+\text{RG}}_{\S30\text{–}\S31}\;\Rightarrow\;\underbrace{\text{teoria efetiva}}_{\S32}$$

### 37.2 As afirmações centrais, em uma frase cada

1. **Estrutura.** A TQC é a única maneira conhecida de reconciliar mecânica quântica, relatividade especial e localidade; o espaço de Fock, as antipartículas e a criação/aniquilação de quanta são consequências, não postulados.
2. **Simetria.** A classificação de Wigner define o que uma partícula é; campos são intertwiners locais em representações não unitárias, e a invariância de gauge é a resposta a uma obstrução de teoria de representações para $|h|\geq1$.
3. **Estatística.** O teorema spin-estatística é forçado pela microcausalidade combinada com positividade da métrica e espectro limitado por baixo; o princípio de Pauli é o corolário algébrico $(b^{\dagger})^{2}=0$.
4. **Cálculo.** O teorema de Wick converte produtos ordenados de operadores em combinatória de propagadores; LSZ define as amplitudes a partir das funções de Green exatas; unitariedade as vincula via teorema óptico.
5. **Funcional.** A integral de trajetória torna covariância e simetrias manifestas, produz automaticamente sinais e fatores de simetria, e revela as anomalias como não invariância da medida. Para férmions, a integral gaussiana dá $\det M$ — e $\operatorname{Pf}(M)$ no caso de Majorana.
6. **Renormalização.** As divergências são reabsorvidas em um número finito de parâmetros quando os acoplamentos têm dimensão $\geq0$; o grupo de renormalização transforma isso na afirmação positiva de que acoplamentos correm e teorias fluem.
7. **Efetividade.** Toda TQC é efetiva; a expansão em operadores de dimensão crescente organiza sistematicamente os efeitos de física desconhecida, e o operador de menor dimensão acima de quatro é o primeiro sinal esperado dela.

### 37.3 O que o formalismo não resolve

Registrar honestamente os limites é parte de expor o formalismo:

- **A medida $\mathcal{D}\phi$** não tem definição matematicamente rigorosa em $D=4$ para teorias interagentes; a construção axiomática de uma TQC quadridimensional não trivial é um problema em aberto (Yang–Mills e o gap de massa é um problema do milênio).
- **A série perturbativa é assintótica**, não convergente: os coeficientes crescem como $n!$ e existem singularidades (renormalons) que limitam a precisão alcançável.
- **Gravitação** não é renormalizável; a TQC como formulada aqui é necessariamente uma teoria efetiva abaixo de $M_{\rm Pl}$.
- **A energia de vácuo** (§5.3) é predita com erro de $\sim10^{120}$ quando confrontada com a constante cosmológica.
- **Confinamento, quebra quiral e o espectro hadrônico** são inacessíveis perturbativamente.

---

# Apêndices

## Apêndice A — Convenções, unidades naturais e matrizes gama

### A.1 Unidades naturais

Com $\hbar=c=1$, toda quantidade tem dimensão de uma potência de massa:

$$[\text{comprimento}]=[\text{tempo}]=[\text{massa}]^{-1}.\tag{A.1}$$

| Grandeza | Dimensão | Conversão útil |
|:---|:---:|:---|
| $\phi$ (escalar), $A_{\mu}$ | $1$ | $1\ \mathrm{GeV}^{-1}=0.1973\ \mathrm{fm}$ |
| $\psi$ (espinor) | $3/2$ | $1\ \mathrm{GeV}^{-2}=0.3894\ \mathrm{mb}$ |
| $\mathcal{L}$ | $4$ | $1\ \mathrm{GeV}^{-1}=6.582\times10^{-25}\ \mathrm{s}$ |
| $\lambda$ ($\phi^{4}$), $e$, $g$ | $0$ | |
| $y$ (Yukawa) | $0$ | |
| $G_{F}$ | $-2$ | $G_{F}=1.1664\times10^{-5}\ \mathrm{GeV}^{-2}$ |
| $G_{N}$ | $-2$ | $M_{\rm Pl}=1.22\times10^{19}$ GeV |

### A.2 Álgebra de Clifford — identidades essenciais

$$\{\gamma^{\mu},\gamma^{\nu}\}=2\eta^{\mu\nu},\qquad \not{a}\not{b}=a\cdot b-i\,\sigma^{\mu\nu}a_{\mu}b_{\nu},\qquad \not{a}\not{a}=a^{2}.\tag{A.2}$$

$$\gamma^{5}=i\gamma^{0}\gamma^{1}\gamma^{2}\gamma^{3}=-\frac{i}{4!}\varepsilon_{\mu\nu\rho\sigma}\gamma^{\mu}\gamma^{\nu}\gamma^{\rho}\gamma^{\sigma},\qquad \sigma^{\mu\nu}\gamma^{5}=\frac{i}{2}\varepsilon^{\mu\nu\rho\sigma}\sigma_{\rho\sigma}.\tag{A.3}$$

Traços e contrações estão em (16.1)–(16.5).

### A.3 Representações explícitas

**Base de Dirac** ($\gamma^{0}$ diagonal):
$$\gamma^{0}=\begin{pmatrix}\mathbb{1}&0\\0&-\mathbb{1}\end{pmatrix},\qquad \gamma^{i}=\begin{pmatrix}0&\sigma^{i}\\-\sigma^{i}&0\end{pmatrix},\qquad \gamma^{5}=\begin{pmatrix}0&\mathbb{1}\\ \mathbb{1}&0\end{pmatrix}.\tag{A.4}$$

**Base quiral (Weyl)** ($\gamma^{5}$ diagonal):
$$\gamma^{\mu}=\begin{pmatrix}0&\sigma^{\mu}\\ \bar\sigma^{\mu}&0\end{pmatrix},\quad \sigma^{\mu}=(\mathbb{1},\vec\sigma),\quad\bar\sigma^{\mu}=(\mathbb{1},-\vec\sigma),\quad \gamma^{5}=\begin{pmatrix}-\mathbb{1}&0\\0&\mathbb{1}\end{pmatrix}.\tag{A.5}$$

**Base de Majorana** (todas as $\gamma^{\mu}$ puramente imaginárias):
$$\gamma^{0}_{M}=\begin{pmatrix}0&\sigma^{2}\\ \sigma^{2}&0\end{pmatrix},\;\gamma^{1}_{M}=\begin{pmatrix}i\sigma^{3}&0\\0&i\sigma^{3}\end{pmatrix},\;\gamma^{2}_{M}=\begin{pmatrix}0&-\sigma^{2}\\ \sigma^{2}&0\end{pmatrix},\;\gamma^{3}_{M}=\begin{pmatrix}-i\sigma^{1}&0\\0&-i\sigma^{1}\end{pmatrix}.\tag{A.6}$$

As três bases satisfazem (A.2), $\gamma^{0\dagger}=\gamma^{0}$ e $\gamma^{i\dagger}=-\gamma^{i}$ (verificado por cálculo matricial direto). Elas são relacionadas por transformações de similaridade, conforme o teorema de Pauli.

### A.4 A matriz de conjugação de carga

$$C\gamma^{\mu T}C^{-1}=-\gamma^{\mu},\qquad C^{T}=-C,\qquad C^{\dagger}=C^{-1},\qquad C\gamma^{5T}C^{-1}=+\gamma^{5},\tag{A.7}$$

com $C=i\gamma^{2}\gamma^{0}$ nas bases de Dirac e quiral, e $C_{M}=\gamma^{0}_{M}$ na base de Majorana. As propriedades de simetria de $C\Gamma^{A}$ ($10$ simétricas, $6$ antissimétricas) estão no Apêndice G.2 e no documento companheiro.

---

## Apêndice B — Integrais de laço e regularização dimensional

### B.1 Parametrização de Feynman

$$\frac{1}{AB}=\int_{0}^{1}\!dx\;\frac{1}{\left[xA+(1-x)B\right]^{2}},\tag{B.1}$$

$$\frac{1}{A_{1}\cdots A_{n}}=\int_{0}^{1}\!dx_{1}\cdots dx_{n}\;\delta\!\left(\textstyle\sum_{i}x_{i}-1\right)\frac{(n-1)!}{\left[\sum_{i}x_{i}A_{i}\right]^{n}},\tag{B.2}$$

$$\frac{1}{A^{m}B^{n}}=\int_{0}^{1}\!dx\;\frac{x^{m-1}(1-x)^{n-1}}{\left[xA+(1-x)B\right]^{m+n}}\,\frac{\Gamma(m+n)}{\Gamma(m)\Gamma(n)}.\tag{B.3}$$

### B.2 Fórmulas mestras (após rotação de Wick e deslocamento $\ell\to\ell+\Delta$)

$$\int\!\frac{d^{d}\ell}{(2\pi)^{d}}\;\frac{1}{\left(\ell^{2}-\Delta\right)^{n}}=\frac{(-1)^{n}\,i}{(4\pi)^{d/2}}\;\frac{\Gamma\!\left(n-\tfrac{d}{2}\right)}{\Gamma(n)}\;\Delta^{\,d/2-n},\tag{B.4}$$

$$\int\!\frac{d^{d}\ell}{(2\pi)^{d}}\;\frac{\ell^{2}}{\left(\ell^{2}-\Delta\right)^{n}}=\frac{(-1)^{n-1}\,i}{(4\pi)^{d/2}}\;\frac{d}{2}\;\frac{\Gamma\!\left(n-\tfrac{d}{2}-1\right)}{\Gamma(n)}\;\Delta^{\,d/2-n+1},\tag{B.5}$$

$$\int\!\frac{d^{d}\ell}{(2\pi)^{d}}\;\frac{\ell^{\mu}\ell^{\nu}}{\left(\ell^{2}-\Delta\right)^{n}}=\frac{(-1)^{n-1}\,i}{(4\pi)^{d/2}}\;\frac{\eta^{\mu\nu}}{2}\;\frac{\Gamma\!\left(n-\tfrac{d}{2}-1\right)}{\Gamma(n)}\;\Delta^{\,d/2-n+1}.\tag{B.6}$$

Integrandos com um número ímpar de $\ell^{\mu}$ anulam-se por simetria.

### B.3 Expansão em torno de $d=4$

Com $d=4-\epsilon$:

$$\Gamma\!\left(\frac{\epsilon}{2}\right)=\frac{2}{\epsilon}-\gamma_{E}+\mathcal{O}(\epsilon),\qquad \gamma_{E}\approx0.5772,\tag{B.7}$$

$$\left(\frac{4\pi\mu^{2}}{\Delta}\right)^{\epsilon/2}=1+\frac{\epsilon}{2}\ln\frac{4\pi\mu^{2}}{\Delta}+\mathcal{O}(\epsilon^{2}),\tag{B.8}$$

$$\Longrightarrow\quad \frac{i}{16\pi^{2}}\left[\frac{2}{\epsilon}-\gamma_{E}+\ln4\pi-\ln\frac{\Delta}{\mu^{2}}\right]\;\equiv\;\frac{i}{16\pi^{2}}\left[\frac{2}{\bar\epsilon}-\ln\frac{\Delta}{\mu^{2}}\right].\tag{B.9}$$

O esquema $\overline{\rm MS}$ subtrai o colchete $\tfrac{2}{\bar\epsilon}$ inteiro, absorvendo $-\gamma_{E}+\ln4\pi$ — uma escolha de conveniência, sem conteúdo físico.

### B.4 Álgebra de Dirac em $d$ dimensões

$$\eta^{\mu}{}_{\mu}=d,\qquad \gamma^{\mu}\gamma_{\mu}=d,\qquad \gamma^{\mu}\gamma^{\nu}\gamma_{\mu}=-(d-2)\gamma^{\nu},\tag{B.10}$$

$$\gamma^{\mu}\gamma^{\nu}\gamma^{\rho}\gamma_{\mu}=4\eta^{\nu\rho}-(4-d)\gamma^{\nu}\gamma^{\rho},\qquad \operatorname{tr}\mathbb{1}=4\ \text{(convenção)}.\tag{B.11}$$

Os termos $\mathcal{O}(\epsilon)$ nessas identidades **contribuem** para a parte finita quando multiplicados por polos $1/\epsilon$ — omiti-los é um erro comum.

---

## Apêndice C — Álgebra de Grassmann e integração de Berezin

### C.1 A álgebra

Geradores $\theta_{1},\ldots,\theta_{n}$ com $\{\theta_{i},\theta_{j}\}=0$ (logo $\theta_{i}^{2}=0$). A álgebra tem dimensão $2^{n}$ com base $\{1,\theta_{i},\theta_{i}\theta_{j},\ldots\}$. Toda função é um polinômio finito.

### C.2 Cálculo

$$\frac{\partial}{\partial\theta_{i}}\theta_{j}=\delta_{ij},\qquad \left\{\frac{\partial}{\partial\theta_{i}},\frac{\partial}{\partial\theta_{j}}\right\}=0,\qquad \left\{\frac{\partial}{\partial\theta_{i}},\theta_{j}\right\}=\delta_{ij}.\tag{C.1}$$

$$\int d\theta\;1=0,\qquad \int d\theta\;\theta=1\qquad\Longrightarrow\qquad \int d\theta \;\equiv\; \frac{\partial}{\partial\theta}.\tag{C.2}$$

**Mudança de variáveis.** Sob $\theta_{i}=M_{ij}\theta'_{j}$:

$$d^{n}\theta = \left(\det M\right)^{-1}d^{n}\theta',\tag{C.3}$$

com o jacobiano **invertido** em relação ao caso comutante. Este único fato é a origem de todos os sinais e determinantes fermiônicos da TQC.

### C.3 Integrais gaussianas

**Complexas** ($\bar\theta,\theta$ independentes, $M$ matriz $n\times n$ arbitrária):

$$\int d^{n}\bar\theta\,d^{n}\theta\;e^{-\bar\theta^{T}M\theta}=\det M.\tag{C.4}$$

Com fontes:

$$\int d^{n}\bar\theta\,d^{n}\theta\;e^{-\bar\theta^{T}M\theta+\bar\eta^{T}\theta+\bar\theta^{T}\eta}=\det M\;\exp\left(\bar\eta^{T}M^{-1}\eta\right).\tag{C.5}$$

**Reais** ($\theta$ real, $A$ **antissimétrica** $2n\times2n$):

$$\boxed{\;\int d^{2n}\theta\;e^{\frac{1}{2}\theta^{T}A\theta}=\operatorname{Pf}(A),\qquad \left[\operatorname{Pf}(A)\right]^{2}=\det A\;}\tag{C.6}$$

com o **Pfaffiano**

$$\operatorname{Pf}(A)=\frac{1}{2^{n}n!}\sum_{\pi\in S_{2n}}\operatorname{sgn}(\pi)\prod_{i=1}^{n}A_{\pi(2i-1)\,\pi(2i)}.\tag{C.7}$$

*(A identidade $\operatorname{Pf}(A)^{2}=\det A$ foi verificada numericamente para matrizes antissimétricas aleatórias.)*

Note que para $A$ antissimétrica de dimensão **ímpar**, $\det A=0$ e $\operatorname{Pf}(A)=0$: uma quantidade ímpar de graus de Majorana reais não admite termo de massa — o análogo algébrico da necessidade de emparelhar modos.

### C.4 Comparação bóson/férmion

| | Bosônico | Fermiônico |
|:---|:---|:---|
| Gaussiana complexa | $(\det M)^{-1}$ | $\det M$ |
| Gaussiana real | $(\det A)^{-1/2}$ | $\operatorname{Pf}(A)=(\det A)^{1/2}$ |
| Laço em $\Gamma$ a um laço | $+\tfrac12\operatorname{tr}\ln$ | $-\operatorname{tr}\ln$ |
| Laço fechado | $+1$ | $-1$ |

A coluna direita é sempre o inverso da esquerda — a razão dos cancelamentos supersimétricos e do sinal em (25.6). **E a linha "gaussiana real" é a linha de Majorana** (Apêndice G.4).

---

## Apêndice D — Grupos de Lie, representações e fatores de cor

### D.1 Generalidades

$$\left[T^{a},T^{b}\right]=i f^{abc}T^{c},\qquad \operatorname{tr}\!\left(T^{a}_{R}T^{b}_{R}\right)=T(R)\,\delta^{ab},\qquad T^{a}_{R}T^{a}_{R}=C_{2}(R)\,\mathbb{1}.\tag{D.1}$$

$$\dim(R)\;C_{2}(R)=T(R)\,\dim(G).\tag{D.2}$$

### D.2 $SU(N)$

| Quantidade | Fundamental $\mathbf{N}$ | Adjunta |
|:---|:---:|:---:|
| $\dim$ | $N$ | $N^{2}-1$ |
| $T(R)$ | $1/2$ | $N$ |
| $C_{2}(R)$ | $\dfrac{N^{2}-1}{2N}$ | $N$ |

Para $SU(3)$: $C_{F}=4/3$, $C_{A}=3$, $T_{F}=1/2$. Identidades úteis:

$$f^{acd}f^{bcd}=N\delta^{ab},\qquad T^{a}_{ij}T^{a}_{kl}=\frac{1}{2}\left(\delta_{il}\delta_{kj}-\frac{1}{N}\delta_{ij}\delta_{kl}\right)\ \text{(identidade de Fierz de cor)}.\tag{D.3}$$

### D.3 O grupo do Modelo Padrão

$$G_{\rm SM}=SU(3)_{c}\times SU(2)_{L}\times U(1)_{Y},\qquad \dim=8+3+1=12\ \text{bósons de gauge}.\tag{D.4}$$

Após a quebra: $8$ glúons sem massa, $W^{\pm},Z$ massivos, $\gamma$ sem massa. O conteúdo de hipercarga que torna a teoria livre de anomalias está tabelado em §36.3.

---

## Apêndice E — A representação de Källén–Lehmann

### E.1 Derivação

Inserindo um conjunto completo de autoestados de momento na função de dois pontos exata e usando invariância de Lorentz:

$$\langle\Omega|\phi(x)\phi(y)|\Omega\rangle=\int_{0}^{\infty}\frac{d\mu^{2}}{2\pi}\;\rho(\mu^{2})\;\Delta^{+}(x-y;\mu^{2}),\tag{E.1}$$

$$\rho(\mu^{2})=(2\pi)\sum_{\lambda}\delta\!\left(\mu^{2}-m_{\lambda}^{2}\right)\left|\langle\Omega|\phi(0)|\lambda_{0}\rangle\right|^{2}\;\geq\;0.\tag{E.2}$$

### E.2 Consequências

$$\tilde D(p^{2})=\int_{0}^{\infty}\frac{d\mu^{2}}{2\pi}\;\rho(\mu^{2})\;\frac{i}{p^{2}-\mu^{2}+i\varepsilon}=\frac{iZ}{p^{2}-m^{2}_{\rm fis}+i\varepsilon}+\text{(corte multipartícula)}.\tag{E.3}$$

1. **Polo simples** em $p^{2}=m^{2}_{\rm fis}$, com resíduo $iZ$; $Z\in[0,1]$ pela normalização $\int d\mu^{2}\rho/2\pi=1$.
2. **Corte** começando em $\mu^{2}=(2m)^{2}$ (limiar de duas partículas), com descontinuidade $\propto\rho$.
3. **$Z=0$** caracteriza um campo que não cria estados de uma partícula — o caso de campos "compostos" e de teorias confinantes.
4. **Comportamento UV.** Como $\rho\geq0$, $\tilde D$ não pode decair mais rápido que $1/p^{2}$: propagadores melhorados do tipo $1/p^{4}$ (que resolveriam as divergências) implicam necessariamente $\rho<0$ em alguma região, isto é, estados de norma negativa e perda de unitariedade. **Este é o argumento estrutural que impede "consertar" a TQC melhorando propagadores** — e a razão pela qual a gravitação quadrática ($R^{2}$), embora renormalizável, não é unitária.

---

## Apêndice F — Regras de Feynman de referência

### F.1 Teoria $\phi^{4}$

$$\mathcal{L}=\frac{1}{2}(\partial\phi)^{2}-\frac{1}{2}m^{2}\phi^{2}-\frac{\lambda}{4!}\phi^{4}$$

Propagador $\dfrac{i}{p^{2}-m^{2}+i\varepsilon}$; vértice $-i\lambda$; fator de simetria $1/S$.

### F.2 QED

$$\mathcal{L}=\bar\psi\left(i\not{D}-m\right)\psi-\frac{1}{4}F^{2}-\frac{1}{2\xi}(\partial\!\cdot\!A)^{2},\qquad D_{\mu}=\partial_{\mu}+ieA_{\mu}$$

| Elemento | Fator |
|:---|:---|
| Propagador do elétron | $\dfrac{i(\not{p}+m)}{p^{2}-m^{2}+i\varepsilon}$ |
| Propagador do fóton | $\dfrac{-i}{p^{2}+i\varepsilon}\left[\eta^{\mu\nu}-(1-\xi)\dfrac{p^{\mu}p^{\nu}}{p^{2}}\right]$ |
| Vértice | $-ie\gamma^{\mu}$ |
| Laço fermiônico | $(-1)\displaystyle\int\!\frac{d^{4}\ell}{(2\pi)^{4}}\operatorname{tr}[\cdots]$ |
| Linhas externas | $u,\bar u,v,\bar v,\epsilon_{\mu},\epsilon^{*}_{\mu}$ |

### F.3 Yang–Mills (gauge $\xi$)

| Elemento | Fator |
|:---|:---|
| Propagador do glúon | $\dfrac{-i\delta^{ab}}{p^{2}+i\varepsilon}\left[\eta^{\mu\nu}-(1-\xi)\dfrac{p^{\mu}p^{\nu}}{p^{2}}\right]$ |
| Propagador do fantasma | $\dfrac{i\delta^{ab}}{p^{2}+i\varepsilon}$ |
| Vértice quark-glúon | $-ig\gamma^{\mu}T^{a}$ |
| Vértice de 3 glúons | $g f^{abc}\left[\eta^{\mu\nu}(k-p)^{\rho}+\eta^{\nu\rho}(p-q)^{\mu}+\eta^{\rho\mu}(q-k)^{\nu}\right]$ |
| Vértice de 4 glúons | $-ig^{2}\left[f^{abe}f^{cde}(\eta^{\mu\rho}\eta^{\nu\sigma}-\eta^{\mu\sigma}\eta^{\nu\rho})+\text{perm.}\right]$ |
| Vértice fantasma-glúon | $-gf^{abc}p^{\mu}$ ($p$ = momento do fantasma que sai) |
| Laço de fantasma | fator $(-1)$ |

### F.4 Somas de polarização

$$\sum_{s}u^{s}\bar u^{s}=\not{p}+m,\qquad \sum_{s}v^{s}\bar v^{s}=\not{p}-m,\tag{F.1}$$

$$\sum_{\lambda}\epsilon^{\mu}_{\lambda}\epsilon^{*\nu}_{\lambda}=-\eta^{\mu\nu}\;\;(\text{fóton, com identidade de Ward}),\qquad =-\eta^{\mu\nu}+\frac{p^{\mu}p^{\nu}}{m^{2}}\;\;(\text{massivo}).\tag{F.2}$$

A substituição $\sum\epsilon\epsilon^{*}\to-\eta^{\mu\nu}$ para fótons só é legítima porque $q_{\mu}\mathcal{M}^{\mu}=0$ (identidade de Ward, §27.3) elimina as contribuições não físicas — em Yang–Mills, ela requer adicionalmente a subtração dos fantasmas.

---

## Apêndice G — Do formalismo geral aos férmions de Majorana

> *Este apêndice conecta a estrutura desenvolvida acima ao formalismo do documento companheiro,* Formalismo dos Férmions de Majorana. *As convenções são idênticas (§0), de modo que todos os resultados se transferem sem tradução de sinais.*

### G.1 Onde o formalismo geral abre espaço para Majorana

Três lugares deste documento contêm, já em forma latente, a estrutura de Majorana:

1. **§6 — o escalar real como limite do complexo.** Impor $\phi=\phi^{\dagger}$ força $b_{\mathbf{p}}=a_{\mathbf{p}}$ e anula a carga $U(1)$. A condição de Majorana é a versão fermiônica exata disso.
2. **§13.3 — a estrutura quiral da massa.** Um termo de massa exige quiralidades opostas. Se apenas $\psi_{L}$ existe, a única maneira de obter um objeto destro a partir dele é a conjugação de carga, $(\psi_{L})^{c}$, que é destro por (3.10) do documento companheiro.
3. **§32 — a expansão em operadores efetivos.** O único operador de dimensão cinco do Modelo Padrão é o de Weinberg, e ele é um termo de massa de Majorana (§G.6).

### G.2 A matriz $C$ dentro da estrutura de §9

O conjunto $\{-\gamma^{\mu T}\}$ satisfaz a mesma álgebra de Clifford (A.2). Pelo **teorema de Pauli** (§9.3), existe $C$ com

$$C\gamma^{\mu T}C^{-1}=-\gamma^{\mu},\qquad C^{T}=-C,\qquad C^{\dagger}=C^{-1}.\tag{G.1}$$

Define-se $\psi^{c}\equiv C\bar\psi^{T}$, que satisfaz $(\psi^{c})^{c}=\psi$ e, o essencial:

$$\psi=\psi^{c}\quad\Longleftrightarrow\quad \bar\psi=-\psi^{T}C^{-1}.\tag{G.2}$$

A tabela de simetrias de $C\Gamma^{A}$ ($C$, $C\gamma^{5}$, $C\gamma^{\mu}\gamma^{5}$ antissimétricas; $C\gamma^{\mu}$, $C\sigma^{\mu\nu}$ simétricas — $6+10=16$) determina todos os sinais dos bilineares, e em particular

$$\bar\psi\gamma^{\mu}\psi\equiv0,\qquad \bar\psi\sigma^{\mu\nu}\psi\equiv0\qquad\text{para }\psi=\psi^{c}.\tag{G.3}$$

**Consequência imediata em linguagem deste documento:** a corrente de Noether de §13.2 se anula identicamente. Um campo de Majorana não tem simetria $U(1)$ e portanto **não pode ser carregado sob nenhum grupo de gauge $U(1)$** — nem eletromagnético, nem de número leptônico. Este é o mesmo enunciado de §6 transposto para férmions.

### G.3 O espaço de Fock

Aplicando (G.2) à expansão em modos (11.4) e usando $v^{s}(p)=C\bar u^{s}(p)^{T}$:

$$\boxed{\;d^{s}_{\mathbf{p}}=b^{s}_{\mathbf{p}}\;}\tag{G.4}$$

Partícula e antipartícula são o mesmo estado. Comparando com (11.6)–(11.7):

$$:\!H\!:\;=\int\!\widetilde{dp}\;E_{p}\sum_{s}b^{s\dagger}b^{s}\quad\text{(metade da de Dirac)},\qquad :\!Q\!:\;\equiv0.\tag{G.5}$$

Cada momento carrega **dois** estados ($s=\pm$), não quatro. Um férmion de Majorana massivo tem o mesmo conteúdo de graus de liberdade que um férmion de Weyl sem massa — consistente com a tabela de §8.3, pois ambos são a representação $(\tfrac12,0)$ de §9.1.

### G.4 A integral funcional: Pfaffiano em vez de determinante

Este é o ponto onde o formalismo funcional (Parte V) fornece a formulação mais limpa da diferença entre Dirac e Majorana.

**Caso de Dirac.** $\psi$ e $\bar\psi$ são variáveis de Grassmann independentes, e por (C.4):

$$Z_{D}=\int\mathcal{D}\bar\psi\,\mathcal{D}\psi\;\exp\left\{i\!\int\!d^{4}x\;\bar\psi\left(i\not{\partial}-m\right)\psi\right\}=\det\!\left(i\not{\partial}-m\right).\tag{G.6}$$

**Caso de Majorana.** O vínculo (G.2) elimina $\bar\psi$ como variável independente. Substituindo na ação com o fator $\tfrac12$:

$$S_{M}=\frac{1}{2}\!\int\! d^{4}x\;\bar\psi\left(i\not{\partial}-m\right)\psi=-\frac{1}{2}\!\int\! d^{4}x\;\psi^{T}\,K\,\psi,\qquad K\equiv C^{-1}\!\left(i\not{\partial}-m\right).\tag{G.7}$$

**O núcleo $K$ é antissimétrico.** Verificação (incluindo os índices de espaço-tempo, com $K(x,y)=C^{-1}(i\not{\partial}_{x}-m)\delta^{4}(x-y)$):

$$K^{T}(x,y)_{ab}=K(y,x)_{ba}=\left[\left(i\gamma^{\mu T}\partial^{y}_{\mu}-m\right)C^{-1\,T}\right]_{ab}\delta^{4}(x-y).$$

Usando $C^{-1T}=(C^{T})^{-1}=-C^{-1}$ e, de (G.1), $\gamma^{\mu T}C^{-1}=-C^{-1}\gamma^{\mu}$:

$$K^{T}=\left[i\,C^{-1}\gamma^{\mu}\partial^{y}_{\mu}+m\,C^{-1}\right]\delta^{4}(x-y)\;\overset{\partial^{y}\delta=-\partial^{x}\delta}{=}\;-C^{-1}\!\left(i\not{\partial}_{x}-m\right)\delta^{4}(x-y)=-K.\;\checkmark$$

Logo, por (C.6), a integral funcional é um **Pfaffiano**:

$$\boxed{\;Z_{M}=\int\mathcal{D}\psi\;e^{iS_{M}}=\operatorname{Pf}(K)=\sqrt{\det K}\;\propto\;\sqrt{Z_{D}}\;}\tag{G.8}$$

**Leitura.** Um campo de Majorana contribui, para a integral funcional, com a *raiz quadrada* do que um campo de Dirac contribui: literalmente "meio férmion de Dirac". Esta é a formulação exata e não perturbativa do fator $\tfrac12$ da lagrangiana de Majorana, e a explicação de por que a energia de vácuo, a contribuição às funções beta e o número de graus de liberdade são todos metade dos correspondentes de Dirac.

> **Nota de consistência.** Na derivação variacional em quatro componentes (Apêndice E do documento companheiro), o núcleo é descrito como "simétrico no sentido relevante", significando que as duas contribuições à variação são iguais. Não há contradição: para variáveis de Grassmann, um núcleo **antissimétrico** é exatamente aquele cujas duas contribuições variacionais se somam em vez de se cancelar. É o mesmo fato enunciado nas duas linguagens.

### G.5 Propagadores e regras de Feynman

O vínculo (G.2) permite duas contrações de Wick adicionais, identicamente nulas no caso de Dirac:

$$\langle0|T\,\psi(x)\bar\psi(y)|0\rangle=S_{F}(x-y)\qquad\text{(idêntico ao de Dirac)},\tag{G.9}$$

$$\langle0|T\,\psi(x)\psi^{T}(y)|0\rangle=-S_{F}(x-y)\,C,\qquad \langle0|T\,\bar\psi^{T}(x)\bar\psi(y)|0\rangle=C^{-1}S_{F}(x-y).\tag{G.10}$$

Estes são os **propagadores anômalos**, que violam número fermiônico em duas unidades. No espaço de momentos, sua parte relevante é

$$\frac{i\left(\not{p}+m\right)C}{p^{2}-m^{2}}\;\xrightarrow{\ \text{entre projetores quirais iguais}\ }\;\frac{i\,m\,C}{p^{2}-m^{2}},\tag{G.11}$$

de modo que **a amplitude de violação de número leptônico é proporcional à massa de Majorana**. Se $m\to0$, o processo desaparece — como deve ser, pois $m=0$ restaura a simetria $U(1)$.

**Regras de Feynman (Denner–Eck–Hahn–Küblbeck).** Como não há seta de número fermiônico, escolhe-se um *fluxo fermiônico* arbitrário por cadeia; nos vértices anti-alinhados, substitui-se $\Gamma\to\Gamma'=C\Gamma^{T}C^{-1}$, isto é

$$\mathbb{1}'=\mathbb{1},\quad (\gamma^{5})'=\gamma^{5},\quad (\gamma^{\mu})'=-\gamma^{\mu},\quad (\gamma^{\mu}\gamma^{5})'=\gamma^{\mu}\gamma^{5},\quad (\sigma^{\mu\nu})'=-\sigma^{\mu\nu}.\tag{G.12}$$

Os fatores $C$ de vértices invertidos e propagadores anômalos se cancelam sistematicamente, e o resultado é independente da escolha de fluxo — uma verificação computacional útil.

**Fatores de simetria.** Aqui §23.4 adquire consequência prática: para $n$ férmions de Majorana idênticos no estado final aplica-se $1/n!$, e um férmion de Majorana em uma linha interna admite **duas** contrações onde um de Dirac admitiria uma. É a soma dessas duas contrações que produz a amplitude de $\Delta L=2$.

### G.6 O operador de Weinberg como o termo $d=5$ da expansão efetiva

Aplicando literalmente a prescrição de teoria efetiva (§32.1) ao Modelo Padrão:

$$\mathcal{L}_{\rm SMEFT}=\mathcal{L}_{\rm SM}^{(4)}+\frac{c_{\alpha\beta}}{\Lambda}\,\mathcal{O}_{5}^{\alpha\beta}+\frac{1}{\Lambda^{2}}\sum_{i}c_{i}\,\mathcal{O}_{i}^{(6)}+\cdots\tag{G.13}$$

$$\mathcal{O}_{5}=\left(\overline{L^{c}}\,\tilde\Phi^{*}\right)\left(\tilde\Phi^{\dagger}L\right),\qquad \tilde\Phi=i\tau_{2}\Phi^{*}.\tag{G.14}$$

**Este é o único operador de dimensão cinco invariante sob $G_{\rm SM}$.** Suas propriedades, em linguagem deste documento:

| Propriedade | Consequência |
|:---|:---|
| $d=5$, coeficiente $\sim1/\Lambda$ | operador **irrelevante** (§31.4); suprimido por $E/\Lambda$ |
| primeiro acima de $d=4$ | **líder** da expansão; primeiro efeito esperado de nova física |
| $\Delta L=2$ | viola número leptônico; gera massa de Majorana |
| após QEB, $m_{\nu}=c\,v^{2}/\Lambda$ | $m_{\nu}\sim0.05$ eV $\Rightarrow$ $\Lambda\sim10^{15}$ GeV |
| simétrico em sabor | matriz de massa complexa simétrica, diagonalizável por Takagi |

O fato de que a massa de neutrino corresponda ao operador de **menor** dimensão acima da renormalizável é o argumento estrutural mais forte, dentro da teoria efetiva de campos, a favor da natureza de Majorana: ela é a predição *genérica* de qualquer nova física acima da escala eletrofraca que não conserve $L$ exatamente.

### G.7 Tabela de correspondência

| Estrutura | Dirac | Majorana |
|:---|:---|:---|
| Campos independentes | $\psi$, $\bar\psi$ | $\psi$ apenas ($\bar\psi=-\psi^{T}C^{-1}$) |
| Lagrangiana | $\bar\psi(i\not{\partial}-m)\psi$ | $\tfrac12\bar\psi(i\not{\partial}-m)\psi$ |
| Integral funcional | $\det K$ | $\operatorname{Pf}(K)=\sqrt{\det K}$ |
| Operadores de escada | $b,d$ independentes | $d=b$ |
| Graus on-shell | $4$ | $2$ |
| Energia de vácuo | $-2\!\int\!E_{p}$ | metade disso |
| Simetria $U(1)$ | sim | **não** |
| $\bar\psi\gamma^{\mu}\psi$ | corrente conservada | $\equiv0$ |
| Momento magnético | permitido | **proibido** (só anapolar) |
| Propagadores | $\langle\psi\bar\psi\rangle$ | $\langle\psi\bar\psi\rangle$ **e** $\langle\psi\psi^{T}\rangle$ |
| Seta de Feynman | fluxo de número fermiônico | escolha arbitrária de fluxo |
| Matriz de massa | complexa geral | complexa **simétrica** |
| Diagonalização | biunitária (SVD) | congruência (Takagi) |
| Fases físicas ($n_{g}=3$) | $1$ | $3$ |
| Termo de massa mínimo | $\psi_{L}$ **e** $\psi_{R}$ | só $\psi_{L}$ |

### G.8 Onde seguir

O desenvolvimento completo do lado direito dessa tabela — condição de Majorana em quatro e duas componentes, paridade intrínseca $\pm i$, matriz de massa Dirac–Majorana e diagonalização de Takagi, mecanismos de seesaw, fases de Majorana na matriz PMNS, decaimento duplo beta sem neutrinos e teorema de Schechter–Valle, leptogênese e o teorema da confusão prática — está no documento companheiro **Formalismo dos Férmions de Majorana**, cujas convenções coincidem exatamente com as deste texto.

---

## Referências

**Livros-texto principais**

1. M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Addison-Wesley (1995). — o padrão; excelente em cálculos explícitos e QED.
2. S. Weinberg, *The Quantum Theory of Fields*, vols. I–III, Cambridge (1995–2000). — o tratamento mais fundamentado; a construção a partir da classificação de Wigner é insuperável.
3. M. Srednicki, *Quantum Field Theory*, Cambridge (2007). — organização impecável; integrais de trajetória desde o início.
4. M. D. Schwartz, *Quantum Field Theory and the Standard Model*, Cambridge (2014). — o mais claro em renormalização e teoria efetiva.
5. A. Zee, *Quantum Field Theory in a Nutshell*, 2nd ed., Princeton (2010). — conceitual e conciso.
6. C. Itzykson and J.-B. Zuber, *Quantum Field Theory*, McGraw-Hill (1980). — clássico; tratamento canônico detalhado.
7. S. Coleman, *Lectures on Quantum Field Theory*, World Scientific (2018). — as notas de Harvard, insubstituíveis em quebra de simetria e aspectos não perturbativos.

**Fundamentos e artigos originais**

8. E. P. Wigner, *On Unitary Representations of the Inhomogeneous Lorentz Group*, Ann. Math. **40** (1939) 149.
9. F. J. Dyson, *The S Matrix in Quantum Electrodynamics*, Phys. Rev. **75** (1949) 1736.
10. G. C. Wick, *The Evaluation of the Collision Matrix*, Phys. Rev. **80** (1950) 268.
11. H. Lehmann, K. Symanzik, W. Zimmermann, Nuovo Cim. **1** (1955) 205. [LSZ]
12. W. Pauli, *The Connection Between Spin and Statistics*, Phys. Rev. **58** (1940) 716.
13. R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That*, Benjamin (1964).
14. L. D. Faddeev and V. N. Popov, *Feynman Diagrams for the Yang–Mills Field*, Phys. Lett. B **25** (1967) 29.
15. C. Becchi, A. Rouet, R. Stora, Ann. Phys. **98** (1976) 287; I. V. Tyutin, Lebedev preprint (1975). [BRST]
16. G. 't Hooft and M. Veltman, *Regularization and Renormalization of Gauge Fields*, Nucl. Phys. B **44** (1972) 189.
17. K. G. Wilson and J. Kogut, *The Renormalization Group and the $\epsilon$ Expansion*, Phys. Rept. **12** (1974) 75.
18. D. J. Gross and F. Wilczek, Phys. Rev. Lett. **30** (1973) 1343; H. D. Politzer, *ibid.* 1346. [liberdade assintótica]
19. S. L. Adler, Phys. Rev. **177** (1969) 2426; J. S. Bell and R. Jackiw, Nuovo Cim. A **60** (1969) 47. [anomalia]
20. K. Fujikawa, *Path-Integral Measure for Gauge-Invariant Fermion Theories*, Phys. Rev. Lett. **42** (1979) 1195.
21. J. Goldstone, A. Salam, S. Weinberg, *Broken Symmetries*, Phys. Rev. **127** (1962) 965.
22. P. W. Higgs, Phys. Rev. Lett. **13** (1964) 508; F. Englert and R. Brout, *ibid.* 321.
23. C. N. Yang and R. L. Mills, Phys. Rev. **96** (1954) 191.
24. T. Appelquist and J. Carazzone, *Infrared Singularities and Massive Fields*, Phys. Rev. D **11** (1975) 2856.
25. S. Weinberg, *Baryon and Lepton Nonconserving Processes*, Phys. Rev. Lett. **43** (1979) 1566. [operador de dimensão 5]
26. E. Witten, *An $SU(2)$ Anomaly*, Phys. Lett. B **117** (1982) 324.

**Formalismo fermiônico e Majorana**

27. A. Denner, H. Eck, O. Hahn, J. Küblbeck, *Feynman Rules for Fermion-Number-Violating Interactions*, Nucl. Phys. B **387** (1992) 467.
28. H. K. Dreiner, H. E. Haber, S. P. Martin, *Two-component spinor techniques and Feynman rules for quantum field theory and supersymmetry*, Phys. Rept. **494** (2010) 1. [arXiv:0812.1594]
29. P. B. Pal, *Dirac, Majorana and Weyl fermions*, Am. J. Phys. **79** (2011) 485. [arXiv:1006.1718]
30. F. A. Berezin, *The Method of Second Quantization*, Academic Press (1966). [integração de Grassmann]

**Documento companheiro**

31. *Formalismo dos Férmions de Majorana* — Review Lecture, mesmas convenções (§0). Desenvolvimento completo da condição de Majorana, matriz de massa Dirac–Majorana, mecanismos de seesaw, fases de Majorana e fenomenologia de $\Delta L=2$.

---

*Documento produzido como Review Lecture, com convenções idênticas às do documento companheiro sobre férmions de Majorana. As identidades algébricas centrais — álgebra de Clifford nas três representações, traços de matrizes gama, relações de completude de espinores, álgebra de Poincaré, a identidade $\operatorname{Pf}(A)^{2}=\det A$, a fórmula mestra de integrais de laço e o cancelamento de anomalias do Modelo Padrão — foram verificadas por cálculo simbólico-numérico direto.*
