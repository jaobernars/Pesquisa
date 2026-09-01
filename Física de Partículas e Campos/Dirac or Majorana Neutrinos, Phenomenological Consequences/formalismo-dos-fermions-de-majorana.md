# Formalismo dos Férmions de Majorana

**Review Lecture — Física de Partículas e Campos**

*Um tratamento autocontido da construção de campos fermiônicos autoconjugados: da álgebra de Clifford e da matriz de conjugação de carga até os mecanismos de geração de massa, as fases de Majorana e a fenomenologia da violação de número leptônico.*

---

## Resumo

Um férmion de Majorana é um campo espinorial que satisfaz a condição de realidade $\psi = \psi^{c}$, onde $\psi^{c} = C\bar{\psi}^{T}$ é o conjugado de carga. A imposição dessa condição reduz pela metade o conteúdo de graus de liberdade da representação de Dirac, elimina a simetria $U(1)$ global associada ao número fermiônico e torna o campo incapaz de carregar qualquer carga conservada. Este documento desenvolve a estrutura completa: (i) a base algébrica — álgebra de Clifford, representações do grupo de Lorentz, teorema de Pauli, existência e propriedades da matriz $C$; (ii) a condição de Majorana em suas formulações de quatro e de duas componentes, a lagrangiana com o fator $1/2$, a quantização canônica, os propagadores anômalos e as regras de Feynman com fluxo fermiônico contínuo; (iii) simetrias discretas, a paridade intrínseca imaginária, as identidades de bilineares e o anulamento da corrente vetorial, com sua consequência direta sobre os momentos eletromagnéticos; (iv) a matriz de massa Dirac–Majorana geral, a diagonalização de Takagi–Autonne e os mecanismos de geração de massa (operador de Weinberg, seesaw I/II/III, seesaw inverso e linear, modelos radiativos); (v) a fenomenologia — fases de Majorana na matriz PMNS, decaimento duplo beta sem neutrinos, teorema de Schechter–Valle, assinaturas em colisores, leptogênese, momentos eletromagnéticos e o teorema da confusão prática Dirac–Majorana. Seis apêndices consolidam convenções, o dicionário $4\leftrightarrow2$ componentes, a estrutura de $C$ em $D$ dimensões, identidades de Fierz, o cálculo variacional de Grassmann e as regras de Feynman detalhadas.

---

## Sumário

**Parte 0 — Convenções**
- [0. Convenções, unidades e notação](#0-convenções-unidades-e-notação)

**Parte I — Fundamentos Algébricos**
- [1. Introdução: o problema físico](#1-introdução-o-problema-físico)
- [2. Álgebra de Clifford e representações do grupo de Lorentz](#2-álgebra-de-clifford-e-representações-do-grupo-de-lorentz)
- [3. Conjugação de carga e a matriz $C$](#3-conjugação-de-carga-e-a-matriz-c)

**Parte II — A Condição de Majorana**
- [4. A condição de Majorana](#4-a-condição-de-majorana)
- [5. Lagrangiana, o fator $1/2$ e equações de movimento](#5-lagrangiana-o-fator-12-e-equações-de-movimento)
- [6. Quantização canônica](#6-quantização-canônica)
- [7. Propagadores e regras de Feynman](#7-propagadores-e-regras-de-feynman)

**Parte III — Estrutura de Simetrias**
- [8. Simetrias discretas: $C$, $P$, $T$ e $CPT$](#8-simetrias-discretas-c-p-t-e-cpt)
- [9. Bilineares de Majorana e o anulamento da corrente vetorial](#9-bilineares-de-majorana-e-o-anulamento-da-corrente-vetorial)
- [10. Momentos eletromagnéticos e o momento anapolar](#10-momentos-eletromagnéticos-e-o-momento-anapolar)

**Parte IV — Massa**
- [11. Massa de Dirac versus massa de Majorana](#11-massa-de-dirac-versus-massa-de-majorana)
- [12. Diagonalização: o teorema de Takagi–Autonne](#12-diagonalização-o-teorema-de-takagiautonne)
- [13. Mecanismos de geração de massa](#13-mecanismos-de-geração-de-massa)

**Parte V — Fenomenologia**
- [14. Mistura leptônica e as fases de Majorana](#14-mistura-leptônica-e-as-fases-de-majorana)
- [15. Decaimento duplo beta sem neutrinos](#15-decaimento-duplo-beta-sem-neutrinos)
- [16. Violação de número leptônico em colisores](#16-violação-de-número-leptônico-em-colisores)
- [17. Leptogênese](#17-leptogênese)
- [18. O teorema da confusão prática Dirac–Majorana](#18-o-teorema-da-confusão-prática-diracmajorana)
- [19. Férmions de Majorana além dos neutrinos](#19-férmions-de-majorana-além-dos-neutrinos)
- [20. Síntese](#20-síntese)

**Apêndices**
- [A. Representações explícitas das matrizes de Dirac](#apêndice-a--representações-explícitas-das-matrizes-de-dirac)
- [B. Notação de duas componentes e o dicionário $4\leftrightarrow2$](#apêndice-b--notação-de-duas-componentes-van-der-waerden)
- [C. A matriz $C$ em $D$ dimensões e a condição de Majorana–Weyl](#apêndice-c--a-matriz-c-em-d-dimensões)
- [D. Identidades de Fierz para bilineares de Majorana](#apêndice-d--identidades-de-fierz)
- [E. Variação da ação com variáveis de Grassmann](#apêndice-e--variação-da-ação-com-variáveis-de-grassmann)
- [F. Regras de Feynman com fluxo fermiônico contínuo](#apêndice-f--regras-de-feynman-com-fluxo-fermiônico-contínuo)
- [G. Cálculo da amplitude de $0\nu\beta\beta$](#apêndice-g--cálculo-da-amplitude-de-0νββ)
- [Referências](#referências)

---

# Parte 0 — Convenções

## 0. Convenções, unidades e notação

Adotamos $\hbar = c = 1$ e a métrica de assinatura *mostly minus*:

$$\eta_{\mu\nu} = \operatorname{diag}(+1,-1,-1,-1).\tag{0.1}$$

Índices gregos $\mu,\nu,\ldots$ correm de $0$ a $3$; índices latinos $i,j,k$ de $1$ a $3$. A convenção de soma de Einstein é usada em toda parte. As matrizes de Dirac obedecem

$$\{\gamma^{\mu},\gamma^{\nu}\} = 2\eta^{\mu\nu}\mathbb{1}_{4},\qquad \gamma^{\mu\dagger} = \gamma^{0}\gamma^{\mu}\gamma^{0},\tag{0.2}$$

de modo que $\gamma^{0\dagger}=\gamma^{0}$ e $\gamma^{i\dagger}=-\gamma^{i}$. Definimos

$$\gamma^{5} \equiv i\gamma^{0}\gamma^{1}\gamma^{2}\gamma^{3},\qquad (\gamma^{5})^{2}=\mathbb{1},\qquad \{\gamma^{5},\gamma^{\mu}\}=0,\tag{0.3}$$

$$P_{L} = \frac{1-\gamma^{5}}{2},\qquad P_{R}=\frac{1+\gamma^{5}}{2},\qquad P_{L}+P_{R}=\mathbb{1},\qquad P_{L}P_{R}=0,\tag{0.4}$$

$$\sigma^{\mu\nu} \equiv \frac{i}{2}[\gamma^{\mu},\gamma^{\nu}].\tag{0.5}$$

O adjunto de Dirac é $\bar\psi \equiv \psi^{\dagger}\gamma^{0}$; para uma matriz $M$ qualquer no espaço espinorial, $\overline{M\psi} = \bar\psi\,\gamma^{0}M^{\dagger}\gamma^{0}$. A notação *slash* é $\displaystyle \not{a} \equiv a_{\mu}\gamma^{\mu}$. Usamos $\varepsilon^{0123}=+1$.

Campos fermiônicos são variáveis de Grassmann: $\psi_{a}(x)\psi_{b}(y) = -\psi_{b}(y)\psi_{a}(x)$ no nível clássico, e satisfazem relações de anticomutação canônicas após a quantização. Essa propriedade é usada de forma essencial ao longo do texto, e sua omissão é a origem mais comum de erros de sinal no formalismo de Majorana.

A convenção específica para a matriz de conjugação de carga é fixada em §3 e mantida em todo o documento:

$$C\gamma^{\mu T}C^{-1} = -\gamma^{\mu},\qquad C^{T}=-C,\qquad C^{\dagger}=C^{-1}.\tag{0.6}$$

Em bases nas quais $\gamma^{0}$ é real e simétrica (Dirac e quiral), uma escolha explícita compatível é $C = i\gamma^{2}\gamma^{0}$.

> **Observação sobre convenções.** Boa parte da literatura difere na fase de $C$, no sinal da métrica e na definição de $\gamma^{5}$. Nenhuma quantidade física depende dessas escolhas, mas *sinais intermediários dependem*. Todos os resultados abaixo são internamente consistentes com (0.1)–(0.6); ao comparar com outras fontes, verifique primeiro qual convenção de $C$ está em uso.

---

# Parte I — Fundamentos Algébricos

## 1. Introdução: o problema físico

### 1.1 O contexto histórico

A equação de Dirac (1928) foi construída como uma equação de primeira ordem cuja iteração reproduz a relação de dispersão relativística $p^{2}=m^{2}$. Sua solução exige espinores de quatro componentes complexas e prevê estados de energia negativa, reinterpretados por Dirac como antipartículas. A estrutura resultante é intrinsecamente complexa: a equação

$$(i\gamma^{\mu}\partial_{\mu}-m)\psi=0\tag{1.1}$$

possui coeficientes $i\gamma^{\mu}$ que, nas representações usuais, não são reais, e a lagrangiana associada possui uma simetria global $U(1)$

$$\psi \to e^{i\alpha}\psi,\qquad \bar\psi \to e^{-i\alpha}\bar\psi,\tag{1.2}$$

cuja corrente de Noether $j^{\mu}=\bar\psi\gamma^{\mu}\psi$ é conservada e define o número fermiônico. É essa carga que distingue partícula de antipartícula.

Em 1937, Ettore Majorana observou que se pode escolher uma representação das matrizes de Dirac na qual todas as $\gamma^{\mu}$ são puramente imaginárias, de modo que $i\gamma^{\mu}$ seja real e (1.1) se torne uma equação diferencial **real**. Nessa representação é consistente impor que o campo seja real,

$$\psi^{*}=\psi \quad\text{(na representação de Majorana)},\tag{1.3}$$

o que reduz o conteúdo de quatro componentes complexas (oito graus reais) para quatro componentes reais. O preço é a destruição da simetria (1.2): um campo real não admite transformação de fase global e, portanto, **não pode carregar nenhuma carga conservada**. Partícula e antipartícula deixam de ser estados distintos.

### 1.2 A questão física em jogo

A pergunta "o neutrino é de Dirac ou de Majorana?" é a pergunta sobre se o número leptônico $L$ é uma simetria exata da natureza ou apenas uma simetria acidental do setor renormalizável do Modelo Padrão. No Modelo Padrão mínimo — sem neutrinos de mão direita — o neutrino é exatamente sem massa e $B-L$ é conservado a nível perturbativo. A observação de oscilações de neutrinos estabelece $m_{\nu}\neq0$ e exige extensão. Existem exatamente duas classes de extensão mínima:

1. **Dirac.** Adiciona-se $\nu_{R}$ singleto e impõe-se $L$ como simetria exata *ad hoc*, com acoplamento de Yukawa $y_{\nu}\lesssim10^{-12}$.
2. **Majorana.** Permite-se o operador efetivo de dimensão cinco $\mathcal{O}_{5}\sim (LH)(LH)/\Lambda$ — o **único** operador de dimensão cinco compatível com as simetrias de gauge do Modelo Padrão — que viola $L$ em duas unidades e produz massa $m_{\nu}\sim v^{2}/\Lambda$.

A segunda alternativa é, do ponto de vista da teoria efetiva de campos, a explicação *genérica*: ela é o primeiro termo da expansão em $1/\Lambda$ e é automaticamente pequena. Sua assinatura observacional definitiva é a violação de $L$ em dois, cuja manifestação mais acessível é o decaimento duplo beta sem neutrinos ($0\nu\beta\beta$).

Este documento constrói o formalismo necessário para formular essa alternativa com precisão.

---

## 2. Álgebra de Clifford e representações do grupo de Lorentz

### 2.1 A álgebra de Clifford $\mathcal{C}\ell_{1,3}$

Seja $V$ o espaço de Minkowski quadridimensional com métrica $\eta$. A álgebra de Clifford $\mathcal{C}\ell_{1,3}(\mathbb{R})$ é a álgebra associativa gerada por elementos $\gamma^{\mu}$ sujeitos a

$$\gamma^{\mu}\gamma^{\nu}+\gamma^{\nu}\gamma^{\mu} = 2\eta^{\mu\nu}.\tag{2.1}$$

Uma base do espaço vetorial subjacente é dada pelos $2^{4}=16$ produtos antissimetrizados

$$\Gamma^{A} \in \{\mathbb{1},\;\gamma^{\mu},\;\sigma^{\mu\nu},\;\gamma^{\mu}\gamma^{5},\;\gamma^{5}\},\tag{2.2}$$

com multiplicidades $1+4+6+4+1=16$. Esses são os **bilineares covariantes**: escalar (S), vetor (V), tensor (T), axial-vetor (A) e pseudoescalar (P). Vale a relação de ortogonalidade

$$\operatorname{tr}\!\left(\Gamma^{A}\Gamma_{B}\right)=4\,\delta^{A}_{B},\tag{2.3}$$

onde $\Gamma_{B}$ denota a base dual (com índices abaixados pela métrica e fator de normalização apropriado nos tensores). Essa relação é a base de todas as identidades de Fierz (Apêndice D).

### 2.2 Teorema de Pauli

**Teorema (Pauli, 1936).** Sejam $\{\gamma^{\mu}\}$ e $\{\gamma'^{\mu}\}$ dois conjuntos de matrizes $4\times4$ satisfazendo (2.1). Então existe uma matriz $S$, não singular e **única a menos de um fator multiplicativo complexo**, tal que

$$\gamma'^{\mu} = S\,\gamma^{\mu}\,S^{-1}.\tag{2.4}$$

*Esboço da demonstração.* A representação de dimensão $4$ da álgebra é irredutível em $D=4$ (as $16$ matrizes $\Gamma^{A}$ são linearmente independentes e geram toda a álgebra $\mathrm{Mat}_{4}(\mathbb{C})$, que é simples). Construa $S = \sum_{A}\Gamma'^{A} F \Gamma_{A}$ para uma matriz arbitrária $F$; usando (2.1) para ambos os conjuntos mostra-se $\gamma'^{\mu}S = S\gamma^{\mu}$. A não singularidade de $S$ para algum $F$ segue de irredutibilidade (lema de Schur), que também garante unicidade a menos de escala. $\blacksquare$

**Este teorema é a pedra angular de todo o formalismo de Majorana.** Aplicado ao conjunto $\{-\gamma^{\mu T}\}$ — que satisfaz (2.1) porque a transposição inverte a ordem dos produtos e o sinal duplo se cancela — ele garante a *existência* da matriz de conjugação de carga $C$. Aplicado a $\{\gamma^{\mu *}\}$, garante a existência da representação de Majorana.

### 2.3 Geradores de Lorentz e as representações $(\tfrac12,0)\oplus(0,\tfrac12)$

Os geradores da representação espinorial do grupo de Lorentz são

$$S^{\mu\nu} = \frac{1}{2}\sigma^{\mu\nu} = \frac{i}{4}[\gamma^{\mu},\gamma^{\nu}],\tag{2.5}$$

satisfazendo a álgebra $\mathfrak{so}(1,3)$:

$$[S^{\mu\nu},S^{\rho\sigma}] = i\left(\eta^{\nu\rho}S^{\mu\sigma}-\eta^{\mu\rho}S^{\nu\sigma}-\eta^{\nu\sigma}S^{\mu\rho}+\eta^{\mu\sigma}S^{\nu\rho}\right).\tag{2.6}$$

Definindo $J^{i}=\tfrac12\varepsilon^{ijk}S^{jk}$ (rotações) e $K^{i}=S^{0i}$ (boosts), e formando as combinações complexas

$$A^{i}=\tfrac12(J^{i}+iK^{i}),\qquad B^{i}=\tfrac12(J^{i}-iK^{i}),\tag{2.7}$$

obtém-se duas álgebras $\mathfrak{su}(2)$ comutantes. A representação de Dirac decompõe-se como

$$\left(\tfrac12,0\right)\oplus\left(0,\tfrac12\right),\tag{2.8}$$

que é precisamente a decomposição em quiralidade: $\psi_{L}=P_{L}\psi$ transforma-se como $(\tfrac12,0)$ e $\psi_{R}=P_{R}\psi$ como $(0,\tfrac12)$. Como $\gamma^{5}$ comuta com $S^{\mu\nu}$,

$$[\gamma^{5},\sigma^{\mu\nu}]=0,\tag{2.9}$$

a quiralidade é um invariante de Lorentz e a decomposição (2.8) é preservada por transformações do grupo de Lorentz próprio ortócrono.

### 2.4 Espinores de Weyl

Na base quiral (Apêndice A.2), $\gamma^{5}=\operatorname{diag}(-\mathbb{1}_{2},+\mathbb{1}_{2})$ e o espinor de Dirac se escreve

$$\psi = \begin{pmatrix}\chi_{\alpha}\\ \bar\xi^{\dot\alpha}\end{pmatrix},\tag{2.10}$$

onde $\chi_{\alpha}$ é um espinor de Weyl de mão esquerda ($\alpha=1,2$) e $\bar\xi^{\dot\alpha}$ de mão direita. A equação de Dirac se desacopla em

$$i\bar\sigma^{\mu}\partial_{\mu}\chi = m\,\bar\xi,\qquad i\sigma^{\mu}\partial_{\mu}\bar\xi = m\,\chi,\tag{2.11}$$

com $\sigma^{\mu}=(\mathbb{1},\vec\sigma)$ e $\bar\sigma^{\mu}=(\mathbb{1},-\vec\sigma)$. Para $m=0$ os dois espinores de Weyl são completamente independentes: um espinor de Weyl é a representação irredutível mínima do grupo de Lorentz em $D=4$, com **dois** graus de liberdade complexos.

O ponto central da construção de Majorana pode ser antecipado aqui: em $D=4$ as representações $(\tfrac12,0)$ e $(0,\tfrac12)$ são **conjugadas complexas uma da outra**. Isso significa que $\bar\chi^{\dot\alpha} \equiv (\chi_{\alpha})^{*}$ transforma-se exatamente como $\bar\xi^{\dot\alpha}$. Logo, a escolha $\bar\xi = \bar\chi$ em (2.10) é Lorentz-covariante — e essa escolha *é* a condição de Majorana. Um férmion de Majorana é, portanto, o mesmo objeto que um único espinor de Weyl massivo.

---

## 3. Conjugação de carga e a matriz $C$

### 3.1 Existência e propriedades

Como notado em §2.2, o conjunto $\{-\gamma^{\mu T}\}$ satisfaz a álgebra de Clifford (2.1). Pelo teorema de Pauli existe $C$ tal que

$$C\,\gamma^{\mu T}\,C^{-1} = -\gamma^{\mu} \quad\Longleftrightarrow\quad C^{-1}\gamma^{\mu}C = -\gamma^{\mu T}.\tag{3.1}$$

**Propriedades de simetria.** Aplicando (3.1) duas vezes obtém-se $C^{-T}C$ comutando com todas as $\gamma^{\mu}$, logo (Schur) $C^{T}=\lambda C$ com $\lambda^{2}=1$. Em $D=4$ prova-se que $\lambda=-1$: para isso, note que as matrizes $C\Gamma^{A}$ têm simetria definida sob transposição, e a contagem de matrizes simétricas ($10$) e antissimétricas ($6$) em $\mathrm{Mat}_{4}$ só é consistente com

$$\boxed{\;C^{T}=-C\;}\tag{3.2}$$

Explicitamente, com $\lambda=-1$: $C$, $C\gamma^{5}$ e $C\gamma^{\mu}\gamma^{5}$ são antissimétricas ($1+1+4=6$), enquanto $C\gamma^{\mu}$ e $C\sigma^{\mu\nu}$ são simétricas ($4+6=10$). Essa tabela de simetrias é o que produz os sinais das identidades bilineares de §9.

**Unitariedade.** A fase de $C$ é convencional. Fixamos $C^{\dagger}C=\mathbb{1}$, de modo que $C^{-1}=C^{\dagger}=-C^{*}$ (usando (3.2)), e portanto

$$C^{*}C = -\mathbb{1},\qquad C^{2}=-\mathbb{1}\ \text{(em bases onde }C\text{ é real)}.\tag{3.3}$$

**Relação com $\gamma^{5}$.** De (3.1) segue diretamente

$$C\,\gamma^{5T}\,C^{-1} = +\gamma^{5},\qquad C\,\sigma^{\mu\nu T}\,C^{-1}=-\sigma^{\mu\nu}.\tag{3.4}$$

O sinal $+$ em $\gamma^{5}$ é o motivo pelo qual a conjugação de carga **preserva** a quiralidade em sua ação sobre índices matriciais, mas a **inverte** quando aplicada a campos — ver (3.9).

### 3.2 Formas explícitas

Nas bases de Dirac e quiral, onde $\gamma^{0}$ é real simétrica, $\gamma^{1},\gamma^{3}$ são reais e $\gamma^{2}$ é imaginária, uma escolha padrão é

$$C = i\gamma^{2}\gamma^{0}.\tag{3.5}$$

*Verificação de (3.1) para $\mu=0$:* como $C^{-1}=-C$ nessa convenção,
$$C^{-1}\gamma^{0}C = -(i\gamma^{2}\gamma^{0})\gamma^{0}(i\gamma^{2}\gamma^{0}) = \gamma^{2}\gamma^{2}\gamma^{0} = -\gamma^{0} = -\gamma^{0T}.\ \checkmark$$

Na representação de Majorana (Apêndice A.3), onde todas as $\gamma^{\mu}_{M}$ são puramente imaginárias e $\gamma^{0}_{M}$ é hermitiana, tem-se simplesmente

$$C_{M} = \gamma^{0}_{M} \quad\text{(a menos de fase)},\tag{3.6}$$

o que torna a operação de conjugação de carga equivalente à conjugação complexa — daí a simplicidade da condição (1.3) nessa base.

### 3.3 O campo conjugado de carga

Define-se

$$\boxed{\;\psi^{c} \equiv C\,\bar\psi^{T} = C\gamma^{0T}\psi^{*}\;}\tag{3.7}$$

Nas bases de Dirac e quiral, com $\gamma^{0T}=\gamma^{0}$ e (3.5), isso se reduz a $\psi^{c} = i\gamma^{2}\psi^{*}$.

**Propriedade fundamental — involutividade.** Aplicando (3.7) duas vezes e usando (3.2)–(3.3):

$$(\psi^{c})^{c} = \psi.\tag{3.8}$$

*Demonstração.* $\overline{\psi^{c}} = (\psi^{c})^{\dagger}\gamma^{0} = (C\gamma^{0T}\psi^{*})^{\dagger}\gamma^{0} = \psi^{T}\gamma^{0*}C^{\dagger}\gamma^{0}$. Usando $C^{\dagger}=C^{-1}$ e (3.1) para reordenar, obtém-se a identidade compacta

$$\overline{\psi^{c}} = -\psi^{T}C^{-1}\qquad\Longleftrightarrow\qquad \psi^{T} = -\overline{\psi^{c}}\,C.\tag{3.9}$$

Então $(\psi^{c})^{c} = C\,\overline{\psi^{c}}^{\,T} = C\,(-\psi^{T}C^{-1})^{T} = -C\,C^{-T}\psi = -C(-C^{-1})\psi = \psi$. $\blacksquare$

A identidade (3.9) — que reaparecerá como a *definição operacional* da regra de contração de Majorana em §7 — é uma das relações mais usadas de todo o formalismo. É útil registrar também sua forma para campos genéricos:

$$\overline{\psi} = -(\psi^{c})^{T}C^{-1}.\tag{3.9'}$$

**Ação sobre a quiralidade.** De (3.4) e (3.7):

$$(\psi_{L})^{c} = (\psi^{c})_{R},\qquad (\psi_{R})^{c}=(\psi^{c})_{L}.\tag{3.10}$$

*Demonstração.* $(P_{L}\psi)^{c} = C\,\overline{P_{L}\psi}^{T} = C(\bar\psi P_{R})^{T} = C P_{R}^{T}\bar\psi^{T} = (C P_{R}^{T}C^{-1})C\bar\psi^{T} = P_{R}\,\psi^{c}$, onde usamos $C\gamma^{5T}C^{-1}=\gamma^{5}$. $\blacksquare$

Este resultado é essencial: o conjugado de carga de um campo canhoto é um campo destro. É exatamente por isso que $\overline{(\nu_{L})^{c}}\,\nu_{L}$ é um termo de massa Lorentz-invariante construído *apenas* com o campo canhoto do Modelo Padrão — e é exatamente esse termo que viola $L$ em duas unidades.

### 3.4 A operação de conjugação de carga sobre bilineares

Para dois campos quaisquer $\psi_{1},\psi_{2}$ e $\Gamma$ na base (2.2), vale

$$\overline{\psi_{1}^{c}}\,\Gamma\,\psi_{2}^{c} = \eta_{\Gamma}\;\overline{\psi_{2}}\,\Gamma\,\psi_{1},\tag{3.11}$$

com os sinais

| $\Gamma$ | $\mathbb{1}$ | $\gamma^{5}$ | $\gamma^{\mu}$ | $\gamma^{\mu}\gamma^{5}$ | $\sigma^{\mu\nu}$ |
|:---|:---:|:---:|:---:|:---:|:---:|
| $\eta_{\Gamma}$ | $+1$ | $+1$ | $-1$ | $+1$ | $-1$ |

*Demonstração.* Usando (3.7) e (3.9),
$$\overline{\psi_{1}^{c}}\,\Gamma\,\psi_{2}^{c} = (-\psi_{1}^{T}C^{-1})\,\Gamma\,(C\bar\psi_{2}^{T}) = -\psi_{1}^{T}\left(C^{-1}\Gamma C\right)\bar\psi_{2}^{T}.$$
De (3.1) e (3.4), $C^{-1}\Gamma C = \eta_{\Gamma}\Gamma^{T}$ com os sinais tabelados. Assim a expressão vale $-\eta_{\Gamma}\,\psi_{1}^{T}\Gamma^{T}\bar\psi_{2}^{T} = -\eta_{\Gamma}(\bar\psi_{2}\Gamma\psi_{1})^{T}$. Como $\bar\psi_{2}\Gamma\psi_{1}$ é um número (matriz $1\times1$), a transposição é trivial, mas a reordenação dos campos de Grassmann introduz um fator $(-1)$. Logo o resultado é $+\eta_{\Gamma}\,\bar\psi_{2}\Gamma\psi_{1}$. $\blacksquare$

O sinal $\eta_{\gamma^{\mu}}=-1$ é a razão pela qual a corrente vetorial troca de sinal sob $C$ — o conteúdo físico da conjugação de carga — e, quando $\psi_{1}=\psi_{2}=\psi$ com $\psi^{c}=\psi$, a razão pela qual essa corrente **se anula identicamente** (§9).

---

# Parte II — A Condição de Majorana

## 4. A condição de Majorana

### 4.1 Enunciado

Um campo espinorial $\psi$ é de **Majorana** se satisfaz a condição de autoconjugação

$$\boxed{\;\psi^{c} = \lambda\,\psi,\qquad |\lambda|=1\;}\tag{4.1}$$

onde $\lambda$ é a chamada *fase de criação* (*creation phase*). A involutividade (3.8) impõe uma restrição sobre $\lambda$:

$$\psi = (\psi^{c})^{c} = (\lambda\psi)^{c} = \lambda^{*}\psi^{c} = \lambda^{*}\lambda\,\psi = |\lambda|^{2}\psi,\tag{4.2}$$

o que é automaticamente satisfeito para qualquer $|\lambda|=1$ — note que a conjugação de carga é **antilinear** em $\psi$ (contém $\psi^{*}$), daí o $\lambda^{*}$. Consequentemente $\lambda$ não é fixado pela consistência.

**A fase $\lambda$ é não física.** Sob a redefinição $\psi\to e^{i\theta}\psi$ tem-se $\psi^{c}\to e^{-i\theta}\psi^{c}$, logo $\lambda\to e^{-2i\theta}\lambda$. Escolhendo $\theta=\tfrac12\arg\lambda$ pode-se sempre levar $\lambda\to1$. Adotamos daqui em diante a forma canônica

$$\psi^{c}=\psi \quad\Longleftrightarrow\quad \psi = C\bar\psi^{T} \quad\Longleftrightarrow\quad \bar\psi = -\psi^{T}C^{-1}.\tag{4.3}$$

> **Advertência.** Em teorias com várias famílias, a liberdade de redefinição de fase é usada para tornar as *massas* reais e positivas, e então as fases $\lambda_{i}$ **não podem** ser simultaneamente eliminadas. Os sinais relativos remanescentes são as paridades CP relativas dos autoestados de Majorana, e ressurgem fisicamente como as **fases de Majorana** da matriz de mistura (§14). Este é o ponto onde a "não fisicalidade" de $\lambda$ deixa de valer.

### 4.2 A representação de Majorana: a equação de Dirac como equação real

Pelo teorema de Pauli aplicado ao conjunto $\{\gamma^{\mu*}\}$ (que satisfaz (2.1) porque a métrica é real), existe uma matriz $S$ com $\gamma^{\mu*}=S\gamma^{\mu}S^{-1}$. Uma escolha explícita de base em que

$$\gamma^{\mu}_{M}\ \text{é puramente imaginária para todo }\mu\tag{4.4}$$

é dada no Apêndice A.3. Nessa base, $i\gamma^{\mu}_{M}$ é **real**, e a equação de Dirac

$$(i\gamma^{\mu}_{M}\partial_{\mu}-m)\psi=0\tag{4.5}$$

é uma equação diferencial de coeficientes reais. Consequentemente, se $\psi$ é solução, $\psi^{*}$ também é, e a condição de realidade

$$\psi^{*}=\psi\tag{4.6}$$

é compatível com a dinâmica. Nessa base, $C_{M}=\gamma^{0}_{M}$ e (4.3) reduz-se exatamente a (4.6). Duas observações:

- A representação de Majorana **não** é uma teoria diferente; é a *mesma* teoria em outra base espinorial. A condição de Majorana em uma base arbitrária é (4.3), não (4.6).
- Não existe nenhuma base em que a condição (4.6) possa ser imposta sobre um campo *carregado*, porque a derivada covariante $D_{\mu}=\partial_{\mu}-iqA_{\mu}$ reintroduz um $i$ explícito, quebrando a realidade da equação. Isso é a manifestação estrutural do fato de que **férmions de Majorana não podem ter carga**.

### 4.3 Contagem de graus de liberdade

| | Dirac | Majorana | Weyl |
|:---|:---:|:---:|:---:|
| Componentes complexas do campo | 4 | 4 (com vínculo) | 2 |
| Graus reais off-shell | 8 | 4 | 4 |
| Graus físicos on-shell | 4 | 2 | 2 |
| Estados de uma partícula | $\nu_{\uparrow},\nu_{\downarrow},\bar\nu_{\uparrow},\bar\nu_{\downarrow}$ | $\nu_{\uparrow},\nu_{\downarrow}$ | $\nu_{L},\bar\nu_{R}$ |
| Massa permitida | $m\,\bar\psi\psi$ | $\tfrac{m}{2}\bar\psi\psi$ | $0$ |
| Simetria $U(1)$ | sim | **não** | sim |

O ponto crucial da terceira linha: um férmion **de Majorana massivo** e um férmion **de Weyl sem massa** têm o mesmo número de graus de liberdade. Isso é consistente porque, como estabelecido em §2.4, ambos são o mesmo objeto de $D=4$: a representação $(\tfrac12,0)$, com ou sem termo de massa. O termo de massa de Majorana é o *único* termo de massa que se pode escrever com uma única representação irredutível de Weyl.

### 4.4 Formulação em duas componentes

Na base quiral, escrevendo o espinor de Dirac como em (2.10), a condição (4.3) com $C=i\gamma^{2}\gamma^{0}$ atua como

$$\psi^{c} = \begin{pmatrix}\;\epsilon\,\bar\xi^{*}\;\\ \;-\epsilon\,\chi^{*}\;\end{pmatrix},\qquad \epsilon = i\sigma^{2}=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\tag{4.7}$$

de modo que $\psi^{c}=\psi$ força $\bar\xi = \bar\chi \equiv \epsilon\,\chi^{*}$ (a menos das convenções de índices pontuados; ver Apêndice B). O espinor de Majorana é portanto

$$\boxed{\;\psi_{M} = \begin{pmatrix}\chi_{\alpha}\\[2pt] \bar\chi^{\dot\alpha}\end{pmatrix}\;}\tag{4.8}$$

com **um único** espinor de Weyl independente $\chi$. Equivalentemente, em notação de quatro componentes,

$$\psi_{M} = \nu_{L} + (\nu_{L})^{c},\tag{4.9}$$

que é a forma mais usada em fenomenologia de neutrinos: dado o campo canhoto do Modelo Padrão $\nu_{L}$, o campo de Majorana correspondente é a soma dele com seu conjugado de carga. Verifica-se imediatamente $\psi_{M}^{c}=(\nu_{L})^{c}+\nu_{L}=\psi_{M}$ usando (3.8) e (3.10). $\checkmark$

Duas identidades úteis que seguem de (4.9) e das projeções quirais:

$$P_{L}\psi_{M}=\nu_{L},\qquad P_{R}\psi_{M}=(\nu_{L})^{c},\qquad \overline{\psi_{M}}P_{L}=\overline{(\nu_{L})^{c}}\,P_{L}.\tag{4.10}$$

### 4.5 Independência de base e o significado invariante

A pergunta "este campo é de Majorana?" é bem posta apenas relativamente a uma escolha de $C$, ou seja, a uma escolha de o que significa "antipartícula". A formulação invariante do enunciado é:

> Um campo fermiônico descreve partículas de Majorana se e somente se não existe nenhuma simetria $U(1)$ contínua exata sob a qual o campo seja carregado — equivalentemente, se e somente se não há número quântico conservado que distinga partícula de antipartícula.

Essa é a razão pela qual "Majorana" e "violação de número leptônico" são, no contexto de neutrinos, enunciados equivalentes. Formalmente: se $L$ é exatamente conservado, os autoestados de massa se organizam em pares degenerados com $L=\pm1$ que se combinam em espinores de Dirac; se $L$ é violado, essa degenerescência é quebrada e os autoestados são de Majorana. O caso limite — degenerescência quase exata com violação minúscula — é o férmion **pseudo-Dirac** (§11.5).

---

## 5. Lagrangiana, o fator $1/2$ e equações de movimento

### 5.1 A lagrangiana de Majorana

$$\boxed{\;\mathcal{L}_{M} = \frac{1}{2}\,\bar\psi\left(i\gamma^{\mu}\partial_{\mu}-m\right)\psi\;}\tag{5.1}$$

com $\psi$ satisfazendo o vínculo (4.3). Em forma explicitamente hermitiana (a menos de derivada total),

$$\mathcal{L}_{M} = \frac{i}{4}\left(\bar\psi\gamma^{\mu}\partial_{\mu}\psi - \partial_{\mu}\bar\psi\,\gamma^{\mu}\psi\right)-\frac{m}{2}\bar\psi\psi.\tag{5.2}$$

**Por que o fator $1/2$.** A justificativa não é estética; ela é imposta pela consistência da normalização canônica. Como $\bar\psi$ não é independente de $\psi$ — está fixado por (4.3) —, a variação da ação com respeito às componentes independentes de $\psi$ recebe *duas* contribuições (uma via $\psi$, outra via $\bar\psi=\bar\psi[\psi]$), que são iguais. Sem o $1/2$, a equação de movimento resultante seria a equação de Dirac com massa $2m$, e o hamiltoniano teria autovalores $2E_{p}$. O fator $1/2$ é o análogo fermiônico exato do fator $1/2$ na lagrangiana de um campo escalar **real** comparada à de um escalar complexo.

Uma verificação limpa: escrevendo $\psi_{M}=\nu_{L}+(\nu_{L})^{c}$ e usando (4.10),

$$\frac{1}{2}\bar\psi_{M}\,i\not{\partial}\,\psi_{M} = \frac{1}{2}\left[\overline{\nu_{L}}\,i\not{\partial}\,\nu_{L} + \overline{(\nu_{L})^{c}}\,i\not{\partial}\,(\nu_{L})^{c}\right] = \overline{\nu_{L}}\,i\not{\partial}\,\nu_{L} + \text{(derivada total)},\tag{5.3}$$

onde o último passo usa a identidade $\overline{(\nu_{L})^{c}}\,\gamma^{\mu}\,(\nu_{L})^{c} = -\overline{\nu_{L}}\gamma^{\mu}\nu_{L}$ (de (3.11)) combinada com uma integração por partes. O termo cinético canônico de $\nu_{L}$ é recuperado com coeficiente $1$. $\checkmark$

### 5.2 O termo de massa

$$-\frac{m}{2}\bar\psi_{M}\psi_{M} = -\frac{m}{2}\left[\overline{\nu_{L}}\,(\nu_{L})^{c} + \overline{(\nu_{L})^{c}}\,\nu_{L}\right] = -\frac{m}{2}\left[\overline{(\nu_{L})^{c}}\,\nu_{L}+\text{h.c.}\right],\tag{5.4}$$

usando $\overline{\nu_{L}}(\nu_{L})^{c} = \overline{(\nu_{L})^{c}}\nu_{L}$ (identidade $\eta_{\mathbb{1}}=+1$ de (3.11)). Este é o **termo de massa de Majorana**. Suas propriedades definidoras:

1. É construído *apenas* com o campo canhoto — não requer $\nu_{R}$.
2. Viola número leptônico em $\Delta L=2$: sob $\nu_{L}\to e^{i\alpha}\nu_{L}$, tem-se $\overline{(\nu_{L})^{c}}\nu_{L}\to e^{2i\alpha}\overline{(\nu_{L})^{c}}\nu_{L}$.
3. No Modelo Padrão, $\nu_{L}$ é componente do dubleto $L=(\nu_{L},e_{L})^{T}$ com hipercarga $Y=-1/2$; o operador $\overline{(\nu_{L})^{c}}\nu_{L}$ tem $Y=+1$ e isospin fraco $T=1$ ou $T=0$ na decomposição $2\otimes2 = 3\oplus1$, sendo o singleto antissimétrico proibido pela estatística. Logo **não é invariante de gauge** e não pode aparecer na lagrangiana renormalizável. É por isso que a massa de Majorana para neutrinos ativos exige nova física — o assunto de §13.

### 5.3 Formulação em duas componentes

Em notação de Weyl (Apêndice B), a lagrangiana (5.1) é

$$\boxed{\;\mathcal{L}_{M} = i\,\bar\chi\,\bar\sigma^{\mu}\partial_{\mu}\chi - \frac{m}{2}\left(\chi\chi + \bar\chi\bar\chi\right)\;}\tag{5.5}$$

onde $\chi\chi \equiv \chi^{\alpha}\chi_{\alpha} = \epsilon^{\alpha\beta}\chi_{\beta}\chi_{\alpha}$ e $\bar\chi\bar\chi \equiv \bar\chi_{\dot\alpha}\bar\chi^{\dot\alpha}$. Note que $\chi\chi\neq0$ apesar da antissimetria de $\epsilon$, precisamente porque $\chi$ é anticomutante: $\epsilon^{\alpha\beta}\chi_{\beta}\chi_{\alpha}$ é simétrico no produto de dois objetos antissimétricos. A generalização a $n$ sabores é imediata:

$$\mathcal{L} = i\,\bar\chi_{j}\bar\sigma^{\mu}\partial_{\mu}\chi_{j} - \frac{1}{2}\left(M_{jk}\,\chi_{j}\chi_{k} + \text{h.c.}\right),\tag{5.6}$$

com $M$ uma matriz **complexa simétrica** $n\times n$ — a simetria sendo consequência de $\chi_{j}\chi_{k}=\chi_{k}\chi_{j}$ (dois sinais negativos: um da anticomutação, outro de $\epsilon$). Essa simetria de $M$ é o fato estrutural central da Parte IV.

### 5.4 Equações de movimento

Variando (5.1) com respeito às componentes independentes de $\psi$ (Apêndice E para o tratamento Grassmann cuidadoso) obtém-se a equação de Dirac usual,

$$(i\gamma^{\mu}\partial_{\mu}-m)\psi=0,\tag{5.7}$$

que é *compatível* com o vínculo (4.3): tomando o conjugado de carga de (5.7),
$$C\overline{\left[(i\not{\partial}-m)\psi\right]}^{\,T} = C\left(-i\partial_{\mu}\gamma^{\mu T}-m\right)\bar\psi^{T} = \left(i\gamma^{\mu}\partial_{\mu}-m\right)\psi^{c},$$
usando (3.1). Logo $\psi^{c}$ satisfaz a mesma equação — a condição de Majorana é preservada pela evolução temporal. $\checkmark$

Em duas componentes, (5.5) fornece

$$i\bar\sigma^{\mu}\partial_{\mu}\chi = m\,\bar\chi,\tag{5.8}$$

cuja iteração dá $\Box\chi + m^{2}\chi = 0$ (usando $\sigma^{\mu}\bar\sigma^{\nu}+\sigma^{\nu}\bar\sigma^{\mu}=2\eta^{\mu\nu}$). Compare com (2.11): a equação de Majorana é a equação de Dirac com $\bar\xi\to\bar\chi$, isto é, com os dois espinores de Weyl identificados.

### 5.5 Simetrias contínuas da lagrangiana de Majorana

Para $m=0$, (5.5) possui a simetria $U(1)$ quiral $\chi\to e^{i\alpha}\chi$. Para $m\neq0$, essa simetria é explicitamente quebrada pelo termo de massa: **a lagrangiana de Majorana massiva não possui nenhuma simetria de fase contínua**. A corrente de Noether correspondente,

$$j^{\mu} = \bar\chi\bar\sigma^{\mu}\chi \;\longleftrightarrow\; \frac{1}{2}\bar\psi_{M}\gamma^{\mu}\gamma^{5}\psi_{M},\tag{5.9}$$

satisfaz $\partial_{\mu}j^{\mu} = 2im(\chi\chi - \bar\chi\bar\chi)\neq0$. Note que a corrente sobrevivente é **axial**, não vetorial — a corrente vetorial $\bar\psi_{M}\gamma^{\mu}\psi_{M}$ é identicamente nula (§9). Para $n$ sabores com $M=0$, a simetria é $U(n)$; ligar $M$ a quebra completamente exceto por eventuais subgrupos discretos.

---

## 6. Quantização canônica

### 6.1 Expansão em modos

O ponto de partida é a solução geral de (5.7) sujeita a (4.3). Para o campo de Dirac, a expansão é

$$\psi_{D}(x) = \int\!\!\frac{d^{3}p}{(2\pi)^{3}2E_{p}}\sum_{s=\pm}\left[\,b_{s}(\mathbf{p})\,u_{s}(p)\,e^{-ip\cdot x} + d_{s}^{\dagger}(\mathbf{p})\,v_{s}(p)\,e^{+ip\cdot x}\right],\tag{6.1}$$

com $E_{p}=\sqrt{|\mathbf{p}|^{2}+m^{2}}$, $b$ aniquilando partículas e $d^{\dagger}$ criando antipartículas. Os espinores satisfazem

$$(\not{p} - m)u_{s}(p)=0,\qquad (\not{p}+m)v_{s}(p)=0,\tag{6.2}$$

e a relação chave que conecta os dois conjuntos é

$$v_{s}(p) = C\,\bar u_{s}(p)^{T},\qquad u_{s}(p)=C\,\bar v_{s}(p)^{T}.\tag{6.3}$$

*Verificação:* aplicando $C\overline{(\cdot)}^{T}$ à primeira de (6.2) e usando (3.1), obtém-se $(\not{p}+m)C\bar u^{T}=0$, que é a segunda equação. $\checkmark$

Impondo agora $\psi = \psi^{c}$ sobre (6.1):

$$\psi^{c} = \int\!\!\frac{d^{3}p}{(2\pi)^{3}2E_{p}}\sum_{s}\left[b_{s}^{\dagger}\,C\bar u_{s}^{T}\,e^{+ipx} + d_{s}\,C\bar v_{s}^{T}\,e^{-ipx}\right] = \int\!\!\frac{d^{3}p}{(2\pi)^{3}2E_{p}}\sum_{s}\left[d_{s}\,u_{s}\,e^{-ipx}+b_{s}^{\dagger}\,v_{s}\,e^{+ipx}\right],$$

onde (6.3) foi usada. Comparando com (6.1), a condição de Majorana equivale a

$$\boxed{\;d_{s}(\mathbf{p}) = b_{s}(\mathbf{p})\;}\tag{6.4}$$

**Partícula e antipartícula são o mesmo estado.** A expansão de Majorana é portanto

$$\psi_{M}(x)=\int\!\!\frac{d^{3}p}{(2\pi)^{3}2E_{p}}\sum_{s=\pm}\left[\,a_{s}(\mathbf{p})\,u_{s}(p)\,e^{-ip\cdot x} + a^{\dagger}_{s}(\mathbf{p})\,v_{s}(p)\,e^{+ip\cdot x}\right].\tag{6.5}$$

Se a fase $\lambda$ de (4.1) não tivesse sido normalizada a $1$, o resultado seria $d_{s}=\lambda^{*}b_{s}$; a fase é reabsorvível na definição de $a_{s}$, confirmando §4.1.

### 6.2 Relações de anticomutação e o espaço de Fock

Impondo

$$\{a_{r}(\mathbf{p}),a^{\dagger}_{s}(\mathbf{p}')\}=(2\pi)^{3}\,2E_{p}\,\delta^{3}(\mathbf{p}-\mathbf{p}')\,\delta_{rs},\qquad \{a,a\}=\{a^{\dagger},a^{\dagger}\}=0,\tag{6.6}$$

e usando as relações de completude

$$\sum_{s}u_{s}(p)\bar u_{s}(p)=\not{p}+m,\qquad \sum_{s}v_{s}(p)\bar v_{s}(p)=\not{p} - m,\tag{6.7}$$

obtém-se o anticomutador a tempos iguais

$$\{\psi_{a}(t,\mathbf{x}),\psi^{\dagger}_{b}(t,\mathbf{y})\}=\delta_{ab}\,\delta^{3}(\mathbf{x}-\mathbf{y}).\tag{6.8}$$

Aqui aparece a diferença estrutural com o caso de Dirac: para um campo de Majorana também

$$\{\psi_{a}(t,\mathbf{x}),\psi_{b}(t,\mathbf{y})\}=(C\gamma^{0T})_{ab}\,\delta^{3}(\mathbf{x}-\mathbf{y})\;\neq\;0,\tag{6.9}$$

ao passo que para Dirac esse objeto é identicamente nulo. É essa relação — consequência direta de (4.3) — que gera os **propagadores anômalos** de §7.2.

**Momento canonicamente conjugado.** De (5.2), $\pi = \partial\mathcal{L}/\partial\dot\psi = \tfrac{i}{2}\psi^{\dagger}$. O fator $1/2$ implica que o parêntese de Dirac (e não o de Poisson) deve ser usado, pois o vínculo $\pi-\tfrac{i}{2}\psi^{\dagger}\approx0$ é de segunda classe. O resultado do procedimento de Dirac reproduz exatamente (6.8) — mais uma confirmação da necessidade do fator $1/2$ em (5.1).

### 6.3 Hamiltoniano e momento

Substituindo (6.5) em $H=\int d^{3}x\,\left(\pi\dot\psi - \mathcal{L}\right)$ e ordenando normalmente:

$$H = \int\!\!\frac{d^{3}p}{(2\pi)^{3}2E_{p}}\;E_{p}\sum_{s}a^{\dagger}_{s}(\mathbf{p})a_{s}(\mathbf{p}),\qquad \mathbf{P}=\int\!\!\frac{d^{3}p}{(2\pi)^{3}2E_{p}}\;\mathbf{p}\sum_{s}a^{\dagger}_{s}a_{s}.\tag{6.10}$$

A energia de ponto zero de um campo de Majorana é **metade** da de um campo de Dirac de mesma massa — resultado relevante em cálculos de correções radiativas e em supersimetria, onde o cancelamento entre graus bosônicos e fermiônicos exige exatamente essa contagem.

### 6.4 Estados de uma partícula e helicidade

Os estados $|\mathbf{p},s\rangle = a^{\dagger}_{s}(\mathbf{p})|0\rangle$ formam um multipleto de **dois** estados por momento. Para $m\neq0$ a helicidade não é invariante de Lorentz e ambos os estados são acessíveis. No limite ultrarrelativístico $m/E\to0$, o campo $\nu_{L}=P_{L}\psi_{M}$ produz predominantemente o estado de helicidade negativa, e $(\nu_{L})^{c}=P_{R}\psi_{M}$ o de helicidade positiva; a amplitude de "erro de helicidade" é suprimida por $m/E$. Este é o conteúdo técnico do **teorema da confusão prática** (§18): à medida que $m/E\to0$, os dois estados de Majorana se tornam operacionalmente indistinguíveis do par ($\nu_{L}$, $\bar\nu_{R}$) de Dirac.

---

## 7. Propagadores e regras de Feynman

### 7.1 O propagador ordinário

$$\langle 0|T\,\psi(x)\bar\psi(y)|0\rangle = S_{F}(x-y)=\int\!\!\frac{d^{4}p}{(2\pi)^{4}}\;\frac{i(\not{p}+m)}{p^{2}-m^{2}+i\varepsilon}\,e^{-ip\cdot(x-y)},\tag{7.1}$$

**idêntico** ao de Dirac. A diferença entre Dirac e Majorana **não** está neste propagador.

### 7.2 Propagadores anômalos

A relação (4.3), na forma $\psi^{T}=-\bar\psi C$ e $\bar\psi^{T}=C^{-1}\psi$, permite construir dois contratores adicionais que são identicamente nulos para campos de Dirac:

$$\boxed{\;\langle0|T\,\psi(x)\,\psi^{T}(y)|0\rangle = -\,S_{F}(x-y)\,C\;}\tag{7.2}$$

$$\boxed{\;\langle0|T\,\bar\psi^{T}(x)\,\bar\psi(y)|0\rangle = C^{-1}\,S_{F}(x-y)\;}\tag{7.3}$$

*Demonstração de (7.2).* $\langle T\psi(x)\psi^{T}(y)\rangle = \langle T\psi(x)\,[-\bar\psi(y)C]\rangle = -\langle T\psi(x)\bar\psi(y)\rangle C = -S_{F}(x-y)C$. $\blacksquare$

Estes são os **propagadores de violação de número leptônico**. No espaço de momentos, (7.2) contribui com o fator

$$\frac{i(\not{p} + m)}{p^{2}-m^{2}}\,C \;\xrightarrow{\ \text{parte dominante}\ }\; \frac{i\,m\,C}{p^{2}-m^{2}},\tag{7.4}$$

onde a parte $\propto\not{p}$ tipicamente se anula ao ser contraída com projetores quirais idênticos nos dois vértices. **A amplitude de violação de $L$ é proporcional à massa de Majorana** — o resultado que estrutura toda a fenomenologia de $0\nu\beta\beta$ (§15).

### 7.3 A ambiguidade de fluxo fermiônico

Em diagramas de Feynman com férmions de Dirac, a seta na linha fermiônica representa simultaneamente (i) a direção do fluxo de número fermiônico e (ii) a ordem de contração dos índices espinoriais. Para Majorana, (i) não existe. A ambiguidade resultante é resolvida pelo esquema de **fluxo fermiônico contínuo** de Denner, Eck, Hahn e Küblbeck (1992):

1. Escolha, para cada cadeia fermiônica aberta ou fechada, uma **direção arbitrária** de fluxo (a *fermion flow*). O resultado final é independente dessa escolha.
2. Percorra cada cadeia **contra** a direção do fluxo escolhido, escrevendo os fatores da esquerda para a direita.
3. Onde o fluxo escolhido é oposto à seta natural do vértice, substitua o vértice $\Gamma$ pelo vértice **invertido**
$$\Gamma' \equiv C\,\Gamma^{T}\,C^{-1},\tag{7.5}$$
cujos valores explícitos, por (3.1) e (3.4), são
$$\mathbb{1}'=\mathbb{1},\quad(\gamma^{5})'=\gamma^{5},\quad(\gamma^{\mu})'=-\gamma^{\mu},\quad(\gamma^{\mu}\gamma^{5})'=+\gamma^{\mu}\gamma^{5},\quad(\sigma^{\mu\nu})'=-\sigma^{\mu\nu}.$$
4. Propagadores: alinhado com o fluxo, use (7.1); anti-alinhado, use (7.2)/(7.3) com os fatores $C$ apropriados. Na prática, os fatores $C$ dos propagadores e dos vértices invertidos se cancelam mutuamente, e o algoritmo se reduz a: *use os propagadores e vértices usuais de Dirac, com a substituição (7.5) nos vértices anti-alinhados.*
5. **Sinais relativos.** Diagramas que diferem por uma permutação ímpar de linhas fermiônicas externas idênticas recebem sinal relativo $-1$; laços fermiônicos fechados recebem $(-1)$ e traço.
6. **Fatores de simetria.** Como partícula e antipartícula coincidem, o número de contrações de Wick distintas duplica em certos diagramas. Concretamente: (a) para um férmion de Majorana em um laço, existe um fator combinatório adicional relativo ao caso de Dirac; (b) para estados finais com $n$ férmions de Majorana idênticos, inclui-se $1/n!$ no espaço de fase.

A regra prática mais útil: **um férmion de Majorana em uma linha interna admite duas contrações (as duas "orientações"), e a soma delas é o que produz a amplitude de $\Delta L=2$.** Um tratamento completo com todos os fatores está no Apêndice F.

### 7.4 Exemplo mínimo: a inserção de massa

Considere o acoplamento $\mathcal{L}_{\rm int} = g\,\bar\ell\,\gamma^{\mu}P_{L}\,\psi_{M}\,W_{\mu} + \text{h.c.}$ e o processo com dois vértices de corrente carregada ligados por uma linha interna de Majorana. A amplitude contém

$$\left[\bar u_{\ell}\gamma^{\mu}P_{L}\right]\;\underbrace{\frac{i(\not{p}+m)}{p^{2}-m^{2}}}_{\text{propagador}}\;\left[\gamma^{\nu}P_{L}\right]^{T}\!\!\cdots\tag{7.6}$$

Como $P_{L}(\not{p} + m)P_{L}^{T}\!$-contraído gera $P_{L}\not{p}\,P_{R}\to0$ e $P_{L}\,m\,P_{L}\to m\,P_{L}$, sobrevive apenas o termo de massa:

$$\mathcal{M}\;\propto\;\frac{m}{p^{2}-m^{2}}\;\times\;\left[\bar u_{\ell_{1}}\gamma^{\mu}P_{L}\,C\,\gamma^{\nu T}P_{L}^{T}\,\bar u_{\ell_{2}}^{T}\right],\tag{7.7}$$

uma amplitude com **dois léptons de mesma carga** no estado final: $\Delta L = 2$. Se $m\to0$, a amplitude se anula, e o processo é proibido — como deve ser, já que $m=0$ restaura a simetria $U(1)$ de $L$. Este é o esqueleto de todo processo de violação de número leptônico induzido por massa de Majorana.

---

# Parte III — Estrutura de Simetrias

## 8. Simetrias discretas: $C$, $P$, $T$ e $CPT$

### 8.1 Conjugação de carga

Por construção, o operador $\mathcal{C}$ atua como $\mathcal{C}\psi\mathcal{C}^{-1}=\eta_{C}\,\psi^{c}$. Para um campo de Majorana com a normalização (4.3),

$$\mathcal{C}\,\psi_{M}\,\mathcal{C}^{-1} = \psi_{M},\qquad \mathcal{C}\,|\mathbf{p},s\rangle = |\mathbf{p},s\rangle.\tag{8.1}$$

O estado de uma partícula de Majorana é autoestado de $\mathcal{C}$ com autovalor $+1$ (na convenção $\lambda=1$). Estritamente, porém, $\mathcal{C}$ isolada só é uma simetria se a interação a preservar; o enunciado invariante é sobre $CP$ e $CPT$.

### 8.2 Paridade: a paridade intrínseca é imaginária

Para um campo de Dirac, $\mathcal{P}\psi(t,\mathbf{x})\mathcal{P}^{-1} = \eta_{P}\gamma^{0}\psi(t,-\mathbf{x})$ com $\eta_{P}$ uma fase arbitrária, convencionalmente $\pm1$. Para Majorana, a condição (4.3) restringe $\eta_{P}$.

**Teorema.** A paridade intrínseca de um férmion de Majorana é $\eta_{P}=\pm i$.

*Demonstração.* Seja $\psi'=\eta_{P}\gamma^{0}\psi$. Calculamos $(\psi')^{c}$. Primeiro, $\overline{\eta_{P}\gamma^{0}\psi}=\eta_{P}^{*}\,\bar\psi\,\gamma^{0}\gamma^{0\dagger}\gamma^{0}=\eta_{P}^{*}\bar\psi\gamma^{0}$. Então

$$(\psi')^{c}=C\left(\eta_{P}^{*}\bar\psi\gamma^{0}\right)^{T}=\eta_{P}^{*}\,C\,\gamma^{0T}\,\bar\psi^{T}=\eta_{P}^{*}\left(C\gamma^{0T}C^{-1}\right)C\bar\psi^{T}=\eta_{P}^{*}\left(-\gamma^{0}\right)\psi^{c},$$

usando (3.1). Impondo que $\psi'$ também satisfaça a condição de Majorana, $\psi'=(\psi')^{c}$:

$$\eta_{P}\,\gamma^{0}\psi = -\eta_{P}^{*}\,\gamma^{0}\psi \;\;\Longrightarrow\;\; \eta_{P}=-\eta_{P}^{*} \;\;\Longrightarrow\;\; \eta_{P}\in i\mathbb{R},\quad|\eta_{P}|=1 \;\;\Longrightarrow\;\; \eta_{P}=\pm i. \;\blacksquare\tag{8.2}$$

**Consequências.**
- $\eta_{P}^{2}=-1$: um par de férmions de Majorana idênticos tem paridade **negativa**, ao contrário do caso de Dirac (onde $\eta_{P}\eta_{\bar P}=-1$ é a paridade relativa fermião–antifermião, mas $\eta_{P}^{2}=+1$).
- A paridade relativa entre dois férmions de Majorana **distintos** $i,j$ é $\eta_{i}\eta_{j}^{*}=\pm1$, e esse sinal é **fisicamente observável**. Em uma base onde as massas são reais e positivas, esse sinal é a *paridade CP relativa* dos autoestados. Ele é o resíduo discreto das fases de Majorana no limite de conservação de CP — o elo formal entre §4.1 e §14.

### 8.3 Reversão temporal e $CPT$

Sob $\mathcal{T}$ (antiunitária), $\mathcal{T}\psi(t,\mathbf{x})\mathcal{T}^{-1}=\eta_{T}\,T\,\psi(-t,\mathbf{x})$ com $T=i\gamma^{1}\gamma^{3}$ na base de Dirac. A condição de Majorana é preservada para $\eta_{T}$ real, sem restrição adicional forte. O produto $CPT$ atua sempre de modo consistente: como o teorema $CPT$ vale para qualquer teoria local, hermitiana e Lorentz-invariante, e como para Majorana partícula = antipartícula, o teorema $CPT$ implica que a massa e o tempo de vida são automaticamente idênticos para "partícula e antipartícula" — enunciado vazio, mas consistente.

O conteúdo não trivial é o seguinte: para férmions de Majorana, a **violação de CP** não pode ser atribuída a diferenças entre partícula e antipartícula, mas apenas a **interferências entre diferentes autoestados de massa** — o que exige $n\geq2$ sabores. Esse é o mecanismo de leptogênese (§17).

### 8.4 Tabela resumida

| Operação | Dirac | Majorana |
|:---|:---|:---|
| $\mathcal{C}\psi\mathcal{C}^{-1}$ | $\eta_{C}\,C\bar\psi^{T}$, $\eta_{C}$ livre | $\psi$ (autoestado, $\eta_{C}=+1$) |
| $\eta_{P}$ | $\pm1$ | $\pm i$ |
| $\eta_{P}^{2}$ (par idêntico) | $+1$ | $-1$ |
| Simetria $U(1)$ | sim | não |
| Momento magnético diagonal | permitido | **proibido** |
| $CP$ violação com $n=1$ | possível (com fases) | impossível |

---

## 9. Bilineares de Majorana e o anulamento da corrente vetorial

### 9.1 Identidades gerais de simetria

Sejam $\lambda,\chi$ dois campos de Majorana quaisquer (possivelmente iguais). Então

$$\boxed{\;\bar\lambda\,\Gamma\,\chi = \eta_{\Gamma}^{\,\rm M}\;\bar\chi\,\Gamma\,\lambda\;}\tag{9.1}$$

com

| $\Gamma$ | $\mathbb{1}$ | $\gamma^{5}$ | $\gamma^{\mu}$ | $\gamma^{\mu}\gamma^{5}$ | $\sigma^{\mu\nu}$ | $\sigma^{\mu\nu}\gamma^{5}$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| $\eta_{\Gamma}^{\rm M}$ | $+1$ | $+1$ | $-1$ | $+1$ | $-1$ | $-1$ |

*Demonstração.* Como $\lambda,\chi$ são de Majorana, $\bar\lambda = -\lambda^{T}C^{-1}$ e $\chi = C\bar\chi^{T}$. Logo

$$\bar\lambda\Gamma\chi = -\lambda^{T}\,C^{-1}\Gamma C\,\bar\chi^{T} = -\eta_{\Gamma}\,\lambda^{T}\Gamma^{T}\bar\chi^{T} = -\eta_{\Gamma}\left(\bar\chi\,\Gamma\,\lambda\right)^{T}.$$

O objeto entre parênteses é um escalar; sua transposição é trivial. Mas ao escrevê-lo na ordem $\bar\chi\Gamma\lambda$, os campos de Grassmann foram permutados, gerando um sinal $(-1)$. Portanto $\bar\lambda\Gamma\chi = +\eta_{\Gamma}\,\bar\chi\Gamma\lambda$, com $\eta_{\Gamma}$ tabelado em (3.11). $\blacksquare$

*(Equivalentemente, o sinal $\eta_{\Gamma}^{\rm M}$ é exatamente a simetria da matriz $C\Gamma$ sob transposição, conforme a contagem $10+6$ de §3.1: $C\Gamma$ simétrica $\Rightarrow\eta^{\rm M}=-1$; antissimétrica $\Rightarrow\eta^{\rm M}=+1$.)*

### 9.2 O anulamento da corrente vetorial e do tensor

Tomando $\lambda=\chi=\psi$ em (9.1) com $\eta^{\rm M}=-1$:

$$\boxed{\;\bar\psi\,\gamma^{\mu}\,\psi = 0,\qquad \bar\psi\,\sigma^{\mu\nu}\,\psi=0,\qquad \bar\psi\,\sigma^{\mu\nu}\gamma^{5}\,\psi=0\;}\tag{9.2}$$

**identicamente, como identidade de operadores.** Os únicos bilineares diagonais não nulos de um férmion de Majorana são

$$\bar\psi\psi,\qquad \bar\psi\gamma^{5}\psi,\qquad \bar\psi\gamma^{\mu}\gamma^{5}\psi.\tag{9.3}$$

**Verificação direta em duas componentes.** Usando o dicionário do Apêndice B, $\bar\psi_{M}\gamma^{\mu}\psi_{M} = \bar\chi\bar\sigma^{\mu}\chi - \chi\sigma^{\mu}\bar\chi$. Mas $\chi\sigma^{\mu}\bar\chi = \bar\chi\bar\sigma^{\mu}\chi$ é uma identidade elementar de espinores anticomutantes de duas componentes. Logo a diferença é nula. $\checkmark$

### 9.3 Consequências físicas imediatas

1. **Nenhuma carga conservada.** Qualquer acoplamento de gauge $U(1)$ tem a forma $q A_{\mu}\bar\psi\gamma^{\mu}\psi$, que se anula. Um férmion de Majorana é necessariamente **neutro** sob toda simetria $U(1)$ — eletromagnética, número bariônico, número leptônico. Este é o teorema estrutural mais importante do formalismo.

2. **Sem momento magnético ou elétrico de dipolo diagonal.** Ver §10.

3. **Acoplamento vetorial ao $Z$ suprimido.** Um férmion de Majorana acopla-se ao $Z^{0}$ apenas via a corrente axial $\bar\psi\gamma^{\mu}\gamma^{5}\psi$. Como no limite não relativístico $\bar\psi\gamma^{\mu}\gamma^{5}\psi$ é uma corrente de spin (componente espacial $\sim\vec{S}$, componente temporal suprimida por $v/c$), a aniquilação $\chi\chi\to f\bar f$ via troca de $Z$ em onda $s$ é **suprimida por helicidade**, $\sigma v\propto m_{f}^{2}/m_{\chi}^{2}$. Esta é uma das propriedades mais consequentes em fenomenologia de matéria escura (§19.2).

4. **Autoacoplamento.** Termos como $(\bar\psi\psi)^{2}$ e $(\bar\psi\gamma^{\mu}\gamma^{5}\psi)^{2}$ são não nulos e são os operadores efetivos relevantes; termos vetoriais são identicamente nulos.

### 9.4 Bilineares de transição (não diagonais)

Para $i\neq j$, as identidades (9.1) **não** anulam nada: $\bar\psi_{i}\gamma^{\mu}\psi_{j}$ é não nulo, apenas antissimétrico sob $i\leftrightarrow j$:

$$\bar\psi_{i}\gamma^{\mu}\psi_{j}=-\bar\psi_{j}\gamma^{\mu}\psi_{i}.\tag{9.4}$$

Em uma teoria com $n$ férmions de Majorana, a matriz de correntes vetoriais é uma matriz **antissimétrica** $n\times n$, e a de correntes axiais é **simétrica**. Isso tem consequências diretas: por exemplo, no MSSM os neutralinos (Majorana) acoplam-se ao $Z$ com estrutura $Z\tilde\chi_{i}^{0}\tilde\chi_{j}^{0}$ que é puramente axial na diagonal e possui parte vetorial antissimétrica fora dela.

---

## 10. Momentos eletromagnéticos e o momento anapolar

### 10.1 O vértice eletromagnético mais geral

Para um férmion neutro de spin $1/2$, o vértice efetivo com um fóton de momento $q$ compatível com Lorentz-invariância, hermiticidade e conservação da corrente ($q_{\mu}\Gamma^{\mu}=0$) é

$$\Gamma^{\mu}(q) = F_{Q}(q^{2})\,\gamma^{\mu} + F_{M}(q^{2})\,i\sigma^{\mu\nu}q_{\nu} + F_{E}(q^{2})\,\sigma^{\mu\nu}q_{\nu}\gamma^{5} + F_{A}(q^{2})\left(q^{2}\gamma^{\mu}-\not{q}\,q^{\mu}\right)\gamma^{5},\tag{10.1}$$

com $F_{Q}$ = carga (fator de forma de carga), $F_{M}$ = momento magnético de dipolo, $F_{E}$ = momento elétrico de dipolo (viola $P$ e $T$), $F_{A}$ = **momento anapolar** (toroidal).

### 10.2 O teorema de anulamento

Para um férmion de Majorana, os bilineares $\bar\psi\gamma^{\mu}\psi$, $\bar\psi\sigma^{\mu\nu}\psi$ e $\bar\psi\sigma^{\mu\nu}\gamma^{5}\psi$ são identicamente nulos por (9.2). Portanto:

$$\boxed{\;F_{Q}=F_{M}=F_{E}=0;\qquad \text{apenas } F_{A}\ \text{sobrevive.}\;}\tag{10.2}$$

**Um férmion de Majorana possui exatamente um momento eletromagnético: o momento anapolar.** O anapolo, introduzido por Zel'dovich (1958), corresponde a uma distribuição de corrente toroidal; ele só é observável em interações de contato ($q^{2}\neq0$ com fóton fora da camada de massa) e não gera campo eletromagnético estático no exterior.

### 10.3 Momentos de transição

Para $i\neq j$, os momentos magnético e elétrico de **transição** são permitidos, mas com estrutura restrita pela antissimetria (9.4): a matriz de momentos de transição $\mu_{ij}$ de férmions de Majorana é **antissimétrica**,

$$\mu_{ij}=-\mu_{ji},\qquad \mu_{ii}=0,\tag{10.3}$$

ao passo que para férmions de Dirac ela é hermitiana com diagonal real não nula. Essa é uma diferença *estrutural* entre os dois casos e, em princípio, uma via de discriminação experimental.

### 10.4 Ordem de grandeza no Modelo Padrão estendido

Para um neutrino de Dirac com massa $m_{\nu}$ no Modelo Padrão mínimo estendido com $\nu_{R}$, o momento magnético gerado a um laço é

$$\mu_{\nu}\simeq \frac{3\,e\,G_{F}\,m_{\nu}}{8\sqrt{2}\,\pi^{2}} \approx 3.2\times10^{-19}\,\mu_{B}\left(\frac{m_{\nu}}{1\ \mathrm{eV}}\right),\tag{10.4}$$

com $\mu_{B}=e/2m_{e}$ o magnéton de Bohr. Para $m_{\nu}\sim0.05$ eV isso dá $\mu_{\nu}\sim10^{-20}\mu_{B}$ — cerca de nove ordens de grandeza abaixo dos limites experimentais atuais ($\mu_{\nu}\lesssim$ alguns $\times10^{-12}\mu_{B}$ de experimentos de espalhamento $\nu$–$e$ e $\lesssim10^{-12}\mu_{B}$ de argumentos astrofísicos de gigantes vermelhas). Consequentemente, **a medida do momento magnético não é uma via realista para distinguir Dirac de Majorana** dentro do Modelo Padrão mínimo: qualquer sinal observável exigiria nova física, e nesse caso a interpretação seria ambígua.

Há um argumento adicional importante (Bell *et al.*, 2005): um momento magnético grande de neutrino de Dirac induz, via correções radiativas, uma contribuição à massa $\delta m_{\nu}\sim\Lambda^{2}\mu_{\nu}/(m_{e})$, o que impõe $\mu_{\nu}\lesssim10^{-14}\mu_{B}$ para $\Lambda\sim1$ TeV. Para Majorana, a antissimetria (10.3) enfraquece esse vínculo em várias ordens de grandeza — de modo que a **observação** de um momento magnético de transição grande favoreceria, indiretamente, a natureza de Majorana.

---

# Parte IV — Massa

## 11. Massa de Dirac versus massa de Majorana

### 11.1 Os dois tipos de termo

Dados os campos quirais $\nu_{L}$ e $N_{R}$ (este último um singleto de gauge, se existir), há exatamente três estruturas bilineares de massa Lorentz-invariantes:

$$\mathcal{L}_{D} = -m_{D}\left(\overline{\nu_{L}}\,N_{R} + \text{h.c.}\right),\tag{11.1}$$

$$\mathcal{L}_{L} = -\frac{1}{2}m_{L}\left(\overline{(\nu_{L})^{c}}\,\nu_{L} + \text{h.c.}\right),\tag{11.2}$$

$$\mathcal{L}_{R} = -\frac{1}{2}m_{R}\left(\overline{(N_{R})^{c}}\,N_{R} + \text{h.c.}\right).\tag{11.3}$$

Suas propriedades sob as simetrias do Modelo Padrão:

| Termo | $\Delta L$ | $SU(2)_{L}\times U(1)_{Y}$ | Origem |
|:---|:---:|:---|:---|
| $m_{D}$ | $0$ | invariante (via Yukawa $\bar L\tilde\Phi N_{R}$) | $m_{D}=y_{\nu}v/\sqrt2$ |
| $m_{L}$ | $2$ | **não invariante** ($T=1$, $Y=+1$) | operador de dim. 5 ou tripleto escalar |
| $m_{R}$ | $2$ | invariante (singleto total) | escala arbitrária, $\sim\Lambda_{\rm NP}$ |

O ponto decisivo: $m_{R}$ é permitido pelas simetrias de gauge com **qualquer** valor, inclusive $\gg v$, porque $N_{R}$ é singleto completo. É essa assimetria estrutural que gera o mecanismo de balanço (*seesaw*).

### 11.2 A matriz de massa geral

Definindo o vetor de campos canhotos

$$n_{L} \equiv \begin{pmatrix}\nu_{L}\\ (N_{R})^{c}\end{pmatrix},\tag{11.4}$$

toda a lagrangiana de massa se compacta em

$$\boxed{\;\mathcal{L}_{\rm massa} = -\frac{1}{2}\,\overline{(n_{L})^{c}}\;\mathcal{M}\;n_{L} + \text{h.c.},\qquad \mathcal{M}=\begin{pmatrix} m_{L} & m_{D}\\ m_{D}^{T} & m_{R}\end{pmatrix}\;}\tag{11.5}$$

A matriz $\mathcal{M}$ é **complexa simétrica** (não hermitiana!). A simetria é obrigatória, não uma escolha: de (9.1) com $\eta^{\rm M}_{\mathbb{1}}=+1$, o bilinear $\overline{(n_{L,i})^{c}}\,n_{L,j}$ é simétrico em $i\leftrightarrow j$, de modo que a parte antissimétrica de $\mathcal{M}$ não contribui. Este é o mesmo fato registrado em (5.6).

Para $n_{g}$ gerações e $n_{R}$ singletos, $\mathcal{M}$ é $(n_{g}+n_{R})\times(n_{g}+n_{R})$ complexa simétrica.

### 11.3 O caso $2\times2$ com uma geração

Tome $m_{L},m_{D},m_{R}$ reais e $\mathcal{M}=\begin{pmatrix}m_{L}&m_{D}\\ m_{D}&m_{R}\end{pmatrix}$. Diagonalizando com rotação ortogonal de ângulo $\theta$:

$$\tan2\theta = \frac{2m_{D}}{m_{R}-m_{L}},\tag{11.6}$$

$$m_{1,2} = \frac{1}{2}\left|\,(m_{L}+m_{R}) \mp \sqrt{(m_{R}-m_{L})^{2}+4m_{D}^{2}}\,\right|.\tag{11.7}$$

Os autoestados são **dois** campos de Majorana $\psi_{1},\psi_{2}$, e o valor absoluto em (11.7) é necessário porque o autovalor "$m_{1}$" pode sair negativo; um autovalor negativo é convertido em positivo pela redefinição $\psi_{1}\to i\gamma^{5}\psi_{1}$, que **inverte a paridade CP relativa** do estado — recuperando o conteúdo de §8.2.

Casos limites:

- **$m_{L}=m_{R}=0$ (Dirac puro).** $\theta=\pi/4$, $m_{1}=m_{2}=m_{D}$. Dois estados de Majorana **exatamente degenerados** e com paridades CP opostas, que se recombinam em um único férmion de Dirac com massa $m_{D}$. *Um férmion de Dirac é um par de férmions de Majorana degenerados com CP oposto.*
- **$m_{L}=0$, $m_{R}\gg m_{D}$ (seesaw tipo I).** $$m_{1}\simeq\frac{m_{D}^{2}}{m_{R}},\qquad m_{2}\simeq m_{R},\qquad \theta\simeq\frac{m_{D}}{m_{R}}\ll1.\tag{11.8}$$ Um estado leve, quase puramente $\nu_{L}$, e um pesado, quase puramente $N_{R}$. A supressão da massa leve é o *seesaw*.
- **$m_{L},m_{R}\ll m_{D}$ (pseudo-Dirac).** Dois estados quase degenerados, $m_{1,2}\simeq m_{D}\mp\tfrac12(m_{L}+m_{R})$, com separação $\delta m = m_{L}+m_{R}$, e mistura ainda máxima. A violação de $L$ é minúscula mas não nula, e se manifesta em oscilações de comprimento $\propto 1/\delta m^{2}$ — relevante em fenomenologia de neutrinos estéreis e em oscilações de longa distância.

### 11.4 Verificação da estrutura seesaw por blocos

Para $\mathcal{M}$ com blocos $m_{L}=0$, a diagonalização por blocos até ordem $\mathcal{O}(m_{D}/m_{R})^{2}$ usa a matriz unitária aproximada

$$U \simeq \begin{pmatrix}\mathbb{1}-\tfrac12\Theta\Theta^{\dagger} & \Theta\\ -\Theta^{\dagger} & \mathbb{1}-\tfrac12\Theta^{\dagger}\Theta\end{pmatrix},\qquad \Theta = m_{D}\,m_{R}^{-1},\tag{11.9}$$

que fornece

$$U^{T}\mathcal{M}\,U = \begin{pmatrix} -m_{D}m_{R}^{-1}m_{D}^{T} & 0\\ 0& m_{R}\end{pmatrix} + \mathcal{O}(\Theta^{3}).\tag{11.10}$$

Portanto

$$\boxed{\;m_{\nu} = -\,m_{D}\,m_{R}^{-1}\,m_{D}^{T}\;}\tag{11.11}$$

que é a **fórmula do seesaw tipo I**. Note: (i) $m_{\nu}$ é automaticamente simétrica, como exigido; (ii) o sinal global é absorvível por redefinição de fase; (iii) o resultado é o mesmo que se obteria integrando $N_{R}$ pelas equações de movimento na teoria efetiva, e o operador resultante é exatamente o de Weinberg (§13.1).

Um efeito colateral importante de (11.9): a matriz de mistura dos neutrinos leves **não é exatamente unitária**, com desvios $\mathcal{O}(\Theta\Theta^{\dagger})=\mathcal{O}(m_{D}^{2}/m_{R}^{2})\sim m_{\nu}/m_{R}$. Isso é o que se busca em testes de "unitariedade da PMNS" e em violação de universalidade leptônica.

### 11.5 Contagem de parâmetros físicos

Para $n_{g}$ gerações de neutrinos de Majorana, a matriz $m_{\nu}$ complexa simétrica tem $n_{g}(n_{g}+1)/2$ entradas complexas $=n_{g}(n_{g}+1)$ parâmetros reais. As redefinições de fase disponíveis são apenas as dos campos de léptons carregados, $n_{g}$ fases. Logo o número de parâmetros físicos é

$$n_{g}(n_{g}+1)-n_{g} = n_{g}^{2}.\tag{11.12}$$

Decompondo: $n_{g}$ massas, $n_{g}(n_{g}-1)/2$ ângulos de mistura, e

$$n_{\rm fases}^{\rm Maj} = \frac{n_{g}(n_{g}-1)}{2}\tag{11.13}$$

fases físicas. Para $n_{g}=3$: $3$ massas, $3$ ângulos, $3$ fases. Compare com o caso de Dirac, onde $m_{\nu}$ é uma matriz complexa geral mas há $2n_{g}-1$ redefinições de fase, resultando em

$$n^{\rm Dirac}_{\rm fases}=\frac{(n_{g}-1)(n_{g}-2)}{2}=1\quad (n_{g}=3).\tag{11.14}$$

**A diferença $3-1=2$ é exatamente o número de fases de Majorana.** Elas são o excesso de estrutura de CP que a natureza de Majorana introduz — e, como veremos em §14.3, são invisíveis em oscilações.

---

## 12. Diagonalização: o teorema de Takagi–Autonne

### 12.1 Enunciado

A diagonalização de $\mathcal{M}$ **não** é a diagonalização usual por transformação de similaridade, porque $\mathcal{M}$ é simétrica e não hermitiana, e porque o campo à esquerda em (11.5) é $\overline{(n_{L})^{c}}$, não $\overline{n_{L}}$. Sob $n_{L}=U\,\hat n_{L}$ com $U$ unitária, tem-se $\overline{(n_{L})^{c}}=\overline{(\hat n_{L})^{c}}\,U^{T}$, de modo que

$$\overline{(n_{L})^{c}}\,\mathcal{M}\,n_{L} \;\longrightarrow\; \overline{(\hat n_{L})^{c}}\left(U^{T}\mathcal{M}\,U\right)\hat n_{L}.\tag{12.1}$$

A transformação relevante é **congruência** $\mathcal{M}\to U^{T}\mathcal{M}U$, não similaridade.

**Teorema (Takagi 1925; Autonne 1915).** Toda matriz complexa simétrica $\mathcal{M}$ admite a decomposição

$$\boxed{\;\mathcal{M} = U^{*}\,\hat{m}\,U^{\dagger}\qquad\Longleftrightarrow\qquad U^{T}\mathcal{M}\,U = \hat m = \operatorname{diag}(m_{1},\ldots,m_{n}),\;m_{i}\geq0\;}\tag{12.2}$$

com $U$ unitária e $m_{i}$ reais **não negativos** — os *valores singulares* de $\mathcal{M}$.

*Demonstração (construtiva).* A matriz $\mathcal{M}^{\dagger}\mathcal{M}$ é hermitiana semidefinida positiva; seja $V$ unitária tal que $V^{\dagger}\mathcal{M}^{\dagger}\mathcal{M}V=\hat m^{2}$ com $\hat m\geq0$. Defina $W = \hat m^{-1}V^{T}\mathcal{M}V$ no subespaço de autovalores não nulos. Usando $\mathcal{M}^{T}=\mathcal{M}$, verifica-se $W^{T}=W$ e $W^{\dagger}W=\mathbb{1}$, ou seja, $W$ é unitária simétrica. Toda unitária simétrica admite raiz quadrada unitária simétrica $W=S^{2}$ com $S^{T}=S$. Então $U\equiv VS^{*}$ satisfaz $U^{T}\mathcal{M}U=\hat m$. $\blacksquare$

Consequências práticas:

$$\hat m^{2} = U^{\dagger}\,\mathcal{M}^{\dagger}\mathcal{M}\,U,\tag{12.3}$$

isto é: **os quadrados das massas de Majorana são os autovalores de $\mathcal{M}^{\dagger}\mathcal{M}$**, e $U$ é a matriz que diagonaliza $\mathcal{M}^{\dagger}\mathcal{M}$ — a menos das fases residuais, que são fixadas exigindo $m_{i}\geq0$ em (12.2). Essas fases residuais **são** as fases de Majorana.

### 12.2 Os campos de massa

Após a diagonalização, os autoestados de massa são os campos de Majorana

$$\psi_{i} = \hat n_{L,i} + (\hat n_{L,i})^{c},\qquad \psi_{i}^{c}=\psi_{i},\tag{12.4}$$

e a lagrangiana de massa é

$$\mathcal{L}_{\rm massa}=-\frac{1}{2}\sum_{i} m_{i}\,\bar\psi_{i}\psi_{i},\qquad m_{i}\geq0.\tag{12.5}$$

**Alternativa com massas de sinal.** Pode-se, em vez disso, usar uma matriz **ortogonal real** $O$ quando $\mathcal{M}$ é real, aceitando autovalores $\varepsilon_{i}m_{i}$ com $\varepsilon_{i}=\pm1$ e $m_{i}>0$. O sinal $\varepsilon_{i}$ é então a **paridade CP** do estado $i$ (cf. §8.2). As duas descrições são equivalentes: a transformação $\psi_{i}\to i\gamma^{5}\psi_{i}$ converte $\varepsilon_{i}=-1$ em $+1$ ao custo de uma fase de Majorana $\pi$. Em cálculos de $0\nu\beta\beta$, é frequentemente mais transparente usar a convenção de sinais.

### 12.3 Exemplo explícito: seesaw $2\times2$ complexo

Para $\mathcal{M}=\begin{pmatrix}0& m_{D}\\ m_{D}& M\end{pmatrix}$ com $m_{D},M$ complexos:

$$\mathcal{M}^{\dagger}\mathcal{M}=\begin{pmatrix}|m_{D}|^{2} & m_{D}^{*}M\\ M^{*}m_{D}& |m_{D}|^{2}+|M|^{2}\end{pmatrix},$$

cujos autovalores, para $|M|\gg|m_{D}|$, são

$$m_{1}^{2}\simeq\frac{|m_{D}|^{4}}{|M|^{2}},\qquad m_{2}^{2}\simeq|M|^{2}+2|m_{D}|^{2},\tag{12.6}$$

confirmando $m_{1}\simeq|m_{D}|^{2}/|M|$. A fase de $m_{1}$ — isto é, $\arg(m_{D}^{2}/M)$ — não é removível quando há mais de um sabor, e é a origem da violação de CP em leptogênese.

---

## 13. Mecanismos de geração de massa

### 13.1 O operador de Weinberg: teoria efetiva

Trate o Modelo Padrão como uma teoria efetiva válida abaixo de uma escala $\Lambda$ e expanda em operadores de dimensão crescente:

$$\mathcal{L}_{\rm eff} = \mathcal{L}_{\rm SM}^{(4)} + \frac{1}{\Lambda}\sum_{i}c_{i}\,\mathcal{O}_{i}^{(5)} + \frac{1}{\Lambda^{2}}\sum_{j}c_{j}\,\mathcal{O}_{j}^{(6)} + \ldots\tag{13.1}$$

**Teorema (Weinberg, 1979).** Existe um **único** operador de dimensão cinco invariante sob $SU(3)_{c}\times SU(2)_{L}\times U(1)_{Y}$ construído com os campos do Modelo Padrão:

$$\boxed{\;\mathcal{O}_{5} = \frac{c_{\alpha\beta}}{\Lambda}\left(\overline{L^{c}_{\alpha}}\,\tilde\Phi^{*}\right)\left(\tilde\Phi^{\dagger}L_{\beta}\right) + \text{h.c.},\qquad \tilde\Phi = i\tau_{2}\Phi^{*}\;}\tag{13.2}$$

Equivalentemente, em notação de componentes de isospin, $\mathcal{O}_{5}\propto (L^{T}_{\alpha}\,C\,i\tau_{2}\Phi)(\Phi^{T} i\tau_{2}\,C\,L_{\beta})$. As propriedades:

- $\Delta L = 2$: viola número leptônico em duas unidades.
- Após a quebra eletrofraca, $\langle\Phi^{0}\rangle=v/\sqrt2$ com $v\simeq246$ GeV, produz $$m^{\nu}_{\alpha\beta}=c_{\alpha\beta}\,\frac{v^{2}}{\Lambda}.\tag{13.3}$$
- É simétrico em $\alpha\beta$ (pela mesma identidade bilinear de §11.2). $\checkmark$
- Para $m_{\nu}\sim0.05$ eV e $c\sim1$: $\Lambda\sim 10^{14}$–$10^{15}$ GeV — próximo da escala de grande unificação.

**A interpretação estrutural é forte:** o operador de Weinberg é o *líder* da expansão em nova física. Se existe qualquer nova física acima da escala eletrofraca que não conserve $L$, ela gera $\mathcal{O}_{5}$, e neutrinos de Majorana leves são a consequência genérica. A massa de neutrino é, nesse sentido, o primeiro sinal esperado de física além do Modelo Padrão.

### 13.2 Seesaw tipo I: singletos fermiônicos

$$\mathcal{L}_{\rm I} = -y_{\alpha i}\,\overline{L_{\alpha}}\,\tilde\Phi\,N_{i} - \frac{1}{2}M_{i}\,\overline{N_{i}^{c}}\,N_{i} + \text{h.c.},\qquad N_{i}\sim(1,1,0).\tag{13.4}$$

Integrando os $N_{i}$ (massa $M_{i}\gg v$) obtém-se (13.2) com

$$\frac{c_{\alpha\beta}}{\Lambda}=\sum_{i}\frac{y_{\alpha i}y_{\beta i}}{M_{i}}\qquad\Longrightarrow\qquad m_{\nu}=-\,m_{D}M_{R}^{-1}m_{D}^{T},\quad m_{D}=\frac{y\,v}{\sqrt2}.\tag{13.5}$$

**Parametrização de Casas–Ibarra.** Dadas $m_{\nu}$ (medida) e $M_{R}$ (livre), a matriz de Yukawa mais geral compatível é

$$y = \frac{\sqrt2}{v}\,U^{*}\,\sqrt{\hat m_{\nu}}\;R^{T}\,\sqrt{M_{R}},\tag{13.6}$$

com $R$ uma matriz **complexa ortogonal** arbitrária ($R^{T}R=\mathbb{1}$). Os parâmetros de $R$ são precisamente os graus de liberdade do setor pesado invisíveis à física de baixa energia — e são os que controlam a assimetria CP em leptogênese.

Contagem: para $n_{g}=3$ e $3$ singletos, o setor completo tem $18$ parâmetros físicos ($3$ massas leves + $3$ ângulos + $3$ fases + $3$ massas pesadas + $3$ ângulos e $3$ fases de $R$), dos quais apenas $9$ são acessíveis a baixas energias.

### 13.3 Seesaw tipo II: tripleto escalar

Introduza um escalar $\Delta\sim(1,3,1)$ (na convenção $Q=T_{3}+Y$ com $Y_{\Phi}=1/2$; alguns textos usam $Y_{\Delta}=2$):

$$\mathcal{L}_{\rm II} = -\frac{1}{2}f_{\alpha\beta}\,L_{\alpha}^{T}\,C\,i\tau_{2}\,\Delta\,L_{\beta} - \mu\,\Phi^{T}i\tau_{2}\Delta^{\dagger}\Phi - M_{\Delta}^{2}\operatorname{tr}(\Delta^{\dagger}\Delta) + \text{h.c.}\tag{13.7}$$

O termo $\mu$ é o único que viola $L$ (ao qual se atribui $L(\Delta)=-2$). Minimizando o potencial, $\Delta$ adquire um valor esperado induzido

$$v_{\Delta}\simeq \frac{\mu\,v^{2}}{M_{\Delta}^{2}},\tag{13.8}$$

e a massa de neutrino é **linear** nos acoplamentos:

$$\boxed{\;m_{\nu}^{\rm II} = f\,v_{\Delta} \simeq f\,\frac{\mu\,v^{2}}{M_{\Delta}^{2}}\;}\tag{13.9}$$

**Diferenças em relação ao tipo I:** (i) a estrutura de sabor de $m_{\nu}$ é *diretamente* $f$, sem inversão de matriz — o que torna o modelo mais preditivo; (ii) o dubleto $\Delta^{\pm\pm}$ é duplamente carregado e decai em pares de léptons de mesma carga, $\Delta^{\pm\pm}\to\ell^{\pm}\ell^{\pm}$, com razões de ramificação **diretamente proporcionais** a $|f_{\alpha\beta}|^{2}\propto|m_{\nu,\alpha\beta}|^{2}$: uma assinatura de colisor que mapeia a matriz de massa dos neutrinos; (iii) $v_{\Delta}\lesssim$ GeV é exigido pelo parâmetro $\rho$ eletrofraco.

### 13.4 Seesaw tipo III: tripleto fermiônico

Introduza fermions $\Sigma\sim(1,3,0)$, $\Sigma = \Sigma^{a}\tau^{a}/2$, com $\Sigma^{c}=\Sigma$:

$$\mathcal{L}_{\rm III} = -y_{\Sigma}\,\overline{L}\,\sqrt2\,\Sigma^{\dagger}\,\tilde\Phi - \frac{1}{2}M_{\Sigma}\operatorname{tr}\!\left(\overline{\Sigma^{c}}\Sigma\right)+\text{h.c.}\tag{13.10}$$

$$m_{\nu}^{\rm III} = -\frac{v^{2}}{2}\,y_{\Sigma}\,M_{\Sigma}^{-1}\,y_{\Sigma}^{T}.\tag{13.11}$$

Estruturalmente idêntico ao tipo I, mas $\Sigma$ tem **carga de gauge** ($SU(2)_{L}$), logo é produzido em colisores por interações de gauge — não suprimido por Yukawas minúsculos. Isso torna o tipo III testável no LHC até $M_{\Sigma}\sim1$ TeV, ao contrário do tipo I.

### 13.5 Seesaw inverso e linear

O problema estrutural do seesaw tipo I é que $M_{R}\sim10^{14}$ GeV é inacessível. As variantes de **baixa escala** contornam isso introduzindo um parâmetro pequeno que viola $L$, protegido tecnicamente ('t Hooft): no limite em que ele vai a zero, a simetria $L$ é restaurada, de modo que sua pequenez é natural.

**Seesaw inverso.** Com campos $(\nu_{L}, N^{c}, S)$ e

$$\mathcal{M} = \begin{pmatrix} 0 & m_{D} & 0\\ m_{D}^{T}& 0 & M\\ 0 & M^{T} & \mu\end{pmatrix},\tag{13.12}$$

onde apenas $\mu$ viola $L$:

$$\boxed{\;m_{\nu}^{\rm inv} \simeq m_{D}\,(M^{T})^{-1}\,\mu\,M^{-1}\,m_{D}^{T}\;}\tag{13.13}$$

A massa leve é **linear** em $\mu$ e **quadrática** em $m_{D}/M$. Com $\mu\sim$ keV, $M\sim$ TeV e $m_{D}\sim$ 100 GeV obtém-se $m_{\nu}\sim0.1$ eV com nova física à escala TeV e Yukawas $\mathcal{O}(1)$. Os estados pesados formam pares pseudo-Dirac com separação $\mu$.

**Seesaw linear.** Introduzindo um acoplamento pequeno $m_{L}$ que viola $L$ no bloco $(\nu_{L},S)$:

$$m_{\nu}^{\rm lin}\simeq m_{D}M^{-1}m_{L}^{T} + m_{L}(M^{T})^{-1}m_{D}^{T}.\tag{13.14}$$

Linear em $m_{D}$ — daí o nome.

### 13.6 Massa de Majorana radiativa

Alternativa à supressão por escala: suprimir por laços. Nesses modelos, $\mathcal{O}_{5}$ é proibido a nível de árvore por uma simetria (frequentemente $\mathbb{Z}_{2}$) e gerado apenas radiativamente.

| Modelo | Ordem | Conteúdo novo | Supressão típica |
|:---|:---:|:---|:---|
| **Zee** (1980) | 1 laço | escalar carregado singleto $h^{+}$, segundo dubleto | $\sim\dfrac{f\,\mu\,m_{\ell}^{2}}{16\pi^{2}M^{2}}$ |
| **Zee–Babu** (1988) | 2 laços | $h^{+}$ e $k^{++}$ | $\sim\dfrac{m_{\ell}^{2}}{(16\pi^{2})^{2}M}$ |
| **Escotogênico** (Ma, 2006) | 1 laço | dubleto inerte $\eta$, singletos $N_{i}$, $\mathbb{Z}_{2}$ | $\sim\dfrac{y^{2}\lambda_{5}}{16\pi^{2}}\dfrac{v^{2}}{M_{N}}$ |
| **Krauss–Nasri–Trodden** | 3 laços | $\mathbb{Z}_{2}$, escalares carregados | $\sim(16\pi^{2})^{-3}$ |

O modelo **escotogênico** é particularmente atrativo porque a simetria $\mathbb{Z}_{2}$ que suprime a massa também estabiliza a partícula mais leve do setor escuro, ligando origem da massa de neutrino e matéria escura em uma única estrutura.

### 13.7 Como o mecanismo se torna manifesto na fórmula da massa

Um resumo comparativo útil:

$$m_{\nu}\;\sim\;\underbrace{\frac{y^{2}v^{2}}{M}}_{\rm I,\;III}\;\;\Big|\;\;\underbrace{\frac{f\mu v^{2}}{M_{\Delta}^{2}}}_{\rm II}\;\;\Big|\;\;\underbrace{\frac{y^{2}v^{2}\mu}{M^{2}}}_{\rm inverso}\;\;\Big|\;\;\underbrace{\frac{1}{(16\pi^{2})^{n}}\frac{y^{2}v^{2}}{M}}_{\rm radiativo\ (n\ laços)}\tag{13.15}$$

Em **todos** os casos, o resultado é um termo de massa de Majorana — porque $\mathcal{O}_{5}$ é o único operador de dimensão cinco. A diversidade está no mecanismo de supressão, não na natureza do resultado.

> **Teorema de "caixa preta" antecipado.** Independentemente do mecanismo, a observação de qualquer processo com $\Delta L=2$ implica a existência de uma massa de Majorana para o neutrino — o teorema de Schechter–Valle (§15.5).

---

# Parte V — Fenomenologia

## 14. Mistura leptônica e as fases de Majorana

### 14.1 A matriz PMNS

Na base em que a matriz de massa dos léptons carregados é diagonal, os autoestados de sabor se relacionam aos de massa por

$$\nu_{\alpha L} = \sum_{i=1}^{3} U_{\alpha i}\,\nu_{iL},\qquad \alpha=e,\mu,\tau.\tag{14.1}$$

Para neutrinos de **Dirac**, $U$ é uma matriz unitária $3\times3$ com $3$ ângulos e $1$ fase física. Para neutrinos de **Majorana**, a contagem de §11.5 exige $2$ fases adicionais, e a parametrização padrão é

$$\boxed{\;U_{\rm PMNS} = V(\theta_{12},\theta_{13},\theta_{23},\delta)\;\cdot\;P,\qquad P=\operatorname{diag}\!\left(1,\;e^{i\alpha_{21}/2},\;e^{i\alpha_{31}/2}\right)\;}\tag{14.2}$$

com $V$ na forma padrão de CKM:

$$V=\begin{pmatrix} c_{12}c_{13} & s_{12}c_{13} & s_{13}e^{-i\delta}\\ -s_{12}c_{23}-c_{12}s_{23}s_{13}e^{i\delta} & c_{12}c_{23}-s_{12}s_{23}s_{13}e^{i\delta} & s_{23}c_{13}\\ s_{12}s_{23}-c_{12}c_{23}s_{13}e^{i\delta} & -c_{12}s_{23}-s_{12}c_{23}s_{13}e^{i\delta}& c_{23}c_{13}\end{pmatrix},\tag{14.3}$$

$c_{ij}\equiv\cos\theta_{ij}$, $s_{ij}\equiv\sin\theta_{ij}$. As fases $\alpha_{21},\alpha_{31}$ são as **fases de Majorana**.

**Valores globais (NuFit 6.0, ordenamento normal, com dados atmosféricos de SK):**

| Parâmetro | Melhor ajuste $\pm1\sigma$ | Intervalo $3\sigma$ |
|:---|:---|:---|
| $\sin^{2}\theta_{12}$ | $0.308\pm0.012$ | $0.275\to0.345$ |
| $\sin^{2}\theta_{13}$ | $0.02215^{+0.00056}_{-0.00058}$ | $0.02030\to0.02388$ |
| $\sin^{2}\theta_{23}$ | $0.470^{+0.017}_{-0.013}$ | $0.435\to0.585$ |
| $\delta_{\rm CP}/^{\circ}$ | $177\pm20$ | $96\to422$ |
| $\Delta m^{2}_{21}/10^{-5}\,{\rm eV}^{2}$ | $7.49\pm0.19$ | $6.92\to8.05$ |
| $\Delta m^{2}_{31}/10^{-3}\,{\rm eV}^{2}$ | $+2.534^{+0.025}_{-0.023}$ | $+2.463\to+2.606$ |
| $\alpha_{21},\alpha_{31}$ | **não determinadas** | $[0,2\pi)$ |

### 14.2 Por que exatamente duas fases extras

O argumento é limpo. Comece com $U$ unitária geral: $9$ parâmetros reais ($3$ ângulos $+$ $6$ fases). As redefinições de fase disponíveis são $\ell_{\alpha}\to e^{i\phi_{\alpha}}\ell_{\alpha}$ e $\nu_{i}\to e^{i\varphi_{i}}\nu_{i}$.

- **Dirac:** ambas as redefinições são permitidas, pois o termo de massa $m_{i}\bar\nu_{i}\nu_{i}$ é invariante sob fase de $\nu_{i}$. Total: $3+3-1=5$ fases removíveis (a fase global não conta). Restam $6-5=1$ fase física.
- **Majorana:** o termo $\tfrac12 m_{i}\overline{\nu_{i}^{c}}\nu_{i}$ **não** é invariante sob $\nu_{i}\to e^{i\varphi_{i}}\nu_{i}$: transforma-se com $e^{2i\varphi_{i}}$. Manter $m_{i}$ real e positivo proíbe essas $3$ redefinições. Restam apenas as $3$ dos léptons carregados: $6-3=3$ fases físicas.

$$\Delta n_{\rm fases}=3-1=2.\tag{14.4}$$

**A origem das fases de Majorana é, portanto, exatamente a mesma que a da violação de $L$: a impossibilidade de redefinir a fase do campo de neutrino.**

### 14.3 Teorema: oscilações são cegas às fases de Majorana

**Teorema.** A probabilidade de oscilação no vácuo ou na matéria é independente de $\alpha_{21}$ e $\alpha_{31}$.

*Demonstração.* A amplitude de transição sabor $\alpha\to\beta$ é

$$A_{\alpha\to\beta}=\sum_{i}U^{*}_{\alpha i}\,e^{-i m_{i}^{2}L/2E}\,U_{\beta i}.\tag{14.5}$$

Escrevendo $U_{\alpha i}=V_{\alpha i}\,e^{i\alpha_{i}/2}$ (com $\alpha_{1}\equiv0$),

$$U^{*}_{\alpha i}U_{\beta i}= V^{*}_{\alpha i}\,e^{-i\alpha_{i}/2}\,V_{\beta i}\,e^{+i\alpha_{i}/2} = V^{*}_{\alpha i}V_{\beta i}.\tag{14.6}$$

A fase de Majorana cancela **em cada termo separadamente**, para todo $i$. $\blacksquare$

A razão física: oscilações preservam número leptônico. A amplitude (14.5) envolve o par $U^{*}U$, que é a estrutura de um processo com $\Delta L=0$. Só processos com $\Delta L=2$ — cuja amplitude envolve $U\cdot U$, não $U^{*}\cdot U$ — são sensíveis às fases de Majorana. Este é o conteúdo formal da afirmação "só $0\nu\beta\beta$ (e processos análogos) podem sondar as fases de Majorana".

### 14.4 Invariantes de violação de CP

O invariante de Jarlskog, sensível apenas a $\delta$:

$$J = \operatorname{Im}\!\left(U_{e1}U_{\mu2}U^{*}_{e2}U^{*}_{\mu1}\right)= \frac{1}{8}\sin2\theta_{12}\sin2\theta_{23}\sin2\theta_{13}\cos\theta_{13}\sin\delta.\tag{14.7}$$

Os invariantes de Majorana, sensíveis a $\alpha_{21},\alpha_{31}$:

$$S_{1}=\operatorname{Im}\!\left(U^{*2}_{e1}U^{2}_{e2}\right),\qquad S_{2}=\operatorname{Im}\!\left(U^{*2}_{e1}U^{2}_{e3}\right).\tag{14.8}$$

Note a estrutura $U^{2}$ (não $|U|^{2}$): os invariantes de Majorana são quadráticos no *mesmo* elemento, refletindo o caráter $\Delta L=2$. Se $S_{1}=S_{2}=J=0$, a CP é conservada no setor leptônico.

### 14.5 Ordenamento de massas e escalas absolutas

Definindo $m_{\rm lightest}$, os dois ordenamentos são

- **Normal (NO):** $m_{1}<m_{2}<m_{3}$, com $m_{2}=\sqrt{m_{1}^{2}+\Delta m^{2}_{21}}$, $m_{3}=\sqrt{m_{1}^{2}+\Delta m^{2}_{31}}$.
- **Invertido (IO):** $m_{3}<m_{1}<m_{2}$, com $m_{1}=\sqrt{m_{3}^{2}+|\Delta m^{2}_{31}|}$.

Limites atuais sobre a escala absoluta:

| Observável | Limite | Fonte |
|:---|:---|:---|
| $m_{\beta}=\sqrt{\sum_{i}\lvert U_{ei}\rvert^{2}m_{i}^{2}}$ | $<0.45$ eV (90% C.L.) | KATRIN, 259 dias |
| $\sum_{i}m_{i}$ | $<0.064$ eV (95% C.L.), $\Lambda$CDM | DESI DR2 BAO $+$ CMB |
| $m_{\beta\beta}$ | $<28$–$122$ meV (90% C.L.) | KamLAND-Zen (dep. de NME) |

O limite cosmológico é notavelmente restritivo: $\sum m_{i}<0.064$ eV está em tensão com o mínimo do ordenamento invertido ($\sum m_{i}\gtrsim0.10$ eV), embora o resultado dependa do modelo cosmológico assumido.

---

## 15. Decaimento duplo beta sem neutrinos

### 15.1 O processo

$$(A,Z)\;\longrightarrow\;(A,Z+2) + e^{-} + e^{-},\qquad \Delta L = +2.\tag{15.1}$$

Compare com o decaimento duplo beta padrão, permitido no Modelo Padrão e já observado em uma dúzia de isótopos:

$$(A,Z)\;\longrightarrow\;(A,Z+2)+e^{-}+e^{-}+\bar\nu_{e}+\bar\nu_{e},\qquad \Delta L=0.\tag{15.2}$$

O processo (15.1) é o **teste experimental mais sensível** da natureza de Majorana. Sua assinatura é limpa: como não há neutrinos no estado final, a soma das energias cinéticas dos dois elétrons é fixa e igual ao $Q$-valor, produzindo um pico monoenergético no extremo do espectro contínuo de (15.2).

Isótopos utilizados: $^{76}$Ge ($Q=2039$ keV), $^{136}$Xe ($Q=2458$ keV), $^{130}$Te ($Q=2527$ keV), $^{100}$Mo, $^{82}$Se, $^{116}$Cd, $^{150}$Nd.

### 15.2 A amplitude e a massa efetiva de Majorana

No mecanismo padrão (troca de neutrino leve de Majorana com correntes $V-A$), a amplitude tem a estrutura (cf. §7.4 e Apêndice G): dois vértices de corrente carregada $\propto U_{ei}\gamma^{\mu}P_{L}$ ligados pelo propagador anômalo (7.2). O numerador do propagador contribui apenas com sua parte $\propto m_{i}$, e cada vértice traz um fator $U_{ei}$ — **não** $U_{ei}^{*}U_{ei}$. Logo

$$\mathcal{A}\;\propto\;\sum_{i}U_{ei}^{2}\,\frac{m_{i}}{q^{2}-m_{i}^{2}}\;\simeq\;\frac{1}{\langle q^{2}\rangle}\sum_{i}U_{ei}^{2}\,m_{i},\tag{15.3}$$

onde $\langle q^{2}\rangle\sim(100\ {\rm MeV})^{2}$ é o momento virtual típico dentro do núcleo (fixado pelo tamanho nuclear, $|q|\sim1/R\sim100$ MeV $\gg m_{i}$).

Define-se a **massa efetiva de Majorana**:

$$\boxed{\;m_{\beta\beta}\;\equiv\;\left|\sum_{i=1}^{3}U_{ei}^{2}\,m_{i}\right| = \left|\,c_{12}^{2}c_{13}^{2}m_{1} + s_{12}^{2}c_{13}^{2}m_{2}\,e^{i\alpha_{21}} + s_{13}^{2}m_{3}\,e^{i(\alpha_{31}-2\delta)}\right|\;}\tag{15.4}$$

Observe:
- A soma é **coerente e com sinais**: as fases de Majorana entram diretamente e podem produzir **cancelamentos**.
- $m_{\beta\beta}$ é a única combinação observável das fases de Majorana em experimentos realistas.
- É $U_{ei}^{2}$, não $|U_{ei}|^{2}$ — a estrutura característica de $\Delta L=2$ prevista por §14.3.

### 15.3 A meia-vida

$$\boxed{\;\left[T^{0\nu}_{1/2}\right]^{-1} = G_{0\nu}(Q,Z)\;\big|\mathcal{M}_{0\nu}\big|^{2}\;\frac{m_{\beta\beta}^{2}}{m_{e}^{2}}\;}\tag{15.5}$$

com:
- $G_{0\nu}$ = **fator de espaço de fase**, calculável com precisão de poucos por cento; escala como $\sim Q^{5}$.
- $\mathcal{M}_{0\nu}$ = **elemento de matriz nuclear (NME)**, adimensional. É a maior fonte de incerteza teórica: cálculos com QRPA, *shell model*, IBM-2, EDF e métodos *ab initio* diferem por fatores de $2$–$3$, o que se traduz em fatores de $4$–$9$ em $m_{\beta\beta}$ para um dado $T_{1/2}$.
- $m_{e}$ = massa do elétron (normalização convencional).

### 15.4 Estado experimental

| Experimento | Isótopo | $T^{0\nu}_{1/2}$ (90% C.L.) | $m_{\beta\beta}$ |
|:---|:---|:---|:---|
| **KamLAND-Zen** (conjunto completo) | $^{136}$Xe | $>3.8\times10^{26}$ yr | $28$–$122$ meV |
| **LEGEND-200** $+$ GERDA $+$ MJD | $^{76}$Ge | $>1.9\times10^{26}$ yr | $\sim70$–$200$ meV |
| **CUORE** (2 t·yr) | $^{130}$Te | $>3.5\times10^{25}$ yr | $\sim70$–$240$ meV$^{\ast}$ |

$^{\ast}$ *As faixas de $m_{\beta\beta}$ são intervalos sobre conjuntos de NME; comparações entre experimentos exigem o mesmo conjunto.*

A próxima geração (LEGEND-1000, nEXO, CUPID, SNO+ fase II, KamLAND2-Zen) tem como meta cobrir **toda a região do ordenamento invertido**, $m_{\beta\beta}\gtrsim15$ meV, correspondendo a $T_{1/2}\gtrsim10^{28}$ yr.

**A estrutura dos "lóbulos" de $m_{\beta\beta}$ vs. $m_{\rm lightest}$:**

- **Ordenamento invertido:** $m_{\beta\beta}\in[\,c_{13}^{2}|\cos2\theta_{12}|\sqrt{|\Delta m^{2}_{31}|}\,,\;c_{13}^{2}\sqrt{|\Delta m^{2}_{31}|}\,]\approx[18,48]$ meV para $m_{3}\to0$. **Não há cancelamento possível** — o limite inferior é estritamente positivo. Esta é a razão pela qual a região IO é considerada o alvo definitivo: sua exclusão completa, se o ordenamento for invertido, refutaria o mecanismo padrão de Majorana.
- **Ordenamento normal:** o cancelamento **é** possível. Para $m_{1}\simeq2$–$7$ meV com fases apropriadas, $m_{\beta\beta}$ pode se anular exatamente. Portanto um resultado nulo em NO **não** exclui a natureza de Majorana.
- **Quase degenerado** ($m_{\rm lightest}\gtrsim0.1$ eV): $m_{\beta\beta}\to m_{0}|c_{12}^{2}+s_{12}^{2}e^{i\alpha_{21}}|$, região já fortemente restringida por cosmologia.

### 15.5 O teorema de Schechter–Valle (caixa preta)

**Teorema (Schechter & Valle, 1982).** Se o decaimento $0\nu\beta\beta$ é observado, então o neutrino tem massa de Majorana não nula, **independentemente do mecanismo** que gera o decaimento.

*Argumento.* Qualquer diagrama que produza $0\nu\beta\beta$ pode ser "fechado" ligando os quarks e os elétrons externos por linhas do Modelo Padrão, obtendo um diagrama de quatro laços que contribui para a autoenergia $\overline{\nu^{c}}\nu$ — isto é, para um termo de massa de Majorana. Como não há simetria que force o cancelamento desse diagrama, a massa de Majorana é não nula.

$$\delta m_{\nu}^{\rm SV}\;\sim\;\mathcal{O}\!\left(10^{-24}\ \mathrm{eV}\right).\tag{15.6}$$

**Interpretação correta e limitações.** O teorema é uma afirmação *qualitativa* sobre simetria: estabelece que $\Delta L=2$ observado $\Rightarrow$ neutrino de Majorana, e portanto que a distinção Dirac/Majorana é decidida por $0\nu\beta\beta$ **em princípio**. Mas a magnitude (15.6) é dez ordens de grandeza abaixo da massa observada. Portanto o teorema **não** garante que o mecanismo dominante de $0\nu\beta\beta$ seja a troca de neutrino leve — apenas que, se $0\nu\beta\beta$ ocorre, a massa de Majorana existe. A interpretação quantitativa de $m_{\beta\beta}$ a partir de um sinal medido continua dependendo da hipótese de mecanismo.

### 15.6 Mecanismos alternativos

Se a nova física está à escala TeV, contribuições de "corrente pesada" podem dominar:

1. **Correntes à direita** (modelos $SU(2)_{L}\times SU(2)_{R}\times U(1)_{B-L}$): troca de $W_{R}$ e $N_{R}$ pesado, com amplitude $\propto (m_{W}/m_{W_{R}})^{4}/M_{N}$ — **não** suprimida por $m_{\nu}$.
2. **Operadores de dimensão $9$**: $\mathcal{O}_{9}\sim \bar u\bar u \bar d\bar d\,\bar e\bar e/\Lambda^{5}$, contato de curto alcance.
3. **SUSY com violação de paridade R**: troca de squarks/gluinos.
4. **Neutrinos estéreis** de massa $\sim$ 100 MeV–GeV, ressonantemente favorecidos por $|q|\sim100$ MeV.

Distinguir mecanismos exige medir a **distribuição angular e de energia** dos dois elétrons (que difere entre $0\nu\beta\beta$ de longo e curto alcance) e comparar taxas em **múltiplos isótopos** com dependências de NME distintas.

---

## 16. Violação de número leptônico em colisores

### 16.1 O processo de Keung–Senjanović

Em modelos com $W_{R}$ e $N$ de Majorana à escala TeV:

$$pp \to W_{R}^{\pm}\to \ell^{\pm}\,N \to \ell^{\pm}\,\ell^{\pm}\,jj.\tag{16.1}$$

A assinatura é **dois léptons de mesma carga** sem energia faltante — praticamente livre de fundo do Modelo Padrão. O sinal de "mesma carga" ocorre porque $N$ é de Majorana e decai com igual probabilidade em $\ell^{+}$ ou $\ell^{-}$:

$$\frac{\Gamma(N\to\ell^{+}W^{-})}{\Gamma(N\to\ell^{-}W^{+})}=1 \quad\text{(Majorana)},\qquad =0\ \text{ou}\ \infty\ \text{(Dirac)}.\tag{16.2}$$

A razão $R_{\ell\ell}=\sigma(\ell^{\pm}\ell^{\pm})/\sigma(\ell^{\pm}\ell^{\mp})$ é, portanto, um **discriminador direto** da natureza de Majorana. Limites atuais do LHC excluem $m_{W_{R}}\lesssim4$–$5$ TeV para $m_{N}$ favorável.

### 16.2 Produção de tripleto duplamente carregado

No seesaw tipo II, a produção $pp\to\Delta^{++}\Delta^{--}$ via Drell–Yan seguida de $\Delta^{\pm\pm}\to\ell^{\pm}\ell^{\pm}$ dá quatro léptons com carga total $\pm4$. As razões de ramificação são $\propto|m^{\nu}_{\alpha\beta}|^{2}$, oferecendo acesso direto à estrutura de sabor da matriz de massa dos neutrinos.

### 16.3 O gargalo de sensibilidade

Para o seesaw tipo I mínimo, a mistura ativo-estéril é $\Theta^{2}\sim m_{\nu}/M_{N}\sim10^{-14}(\text{GeV}/M_{N})$, muito abaixo do alcance de colisores. Sinais observáveis exigem cancelamentos na estrutura de sabor (garantidos, por exemplo, por uma simetria $L$ aproximada, como no seesaw inverso), nos quais $\Theta$ pode ser grande e $m_{\nu}$ ainda pequena. **Nesses cenários, porém, a violação de $L$ é suprimida** — a assinatura de mesma carga volta a ser pequena. Existe portanto uma tensão estrutural: grande produção e grande violação de $L$ tendem a ser mutuamente exclusivas em modelos naturais. Cenários com pares pseudo-Dirac quase degenerados podem escapar dessa tensão via oscilações $N_{1}\leftrightarrow N_{2}$ dentro do detector.

---

## 17. Leptogênese

### 17.1 O mecanismo de Fukugita–Yanagida (1986)

Os neutrinos pesados de Majorana do seesaw tipo I decaem fora do equilíbrio no universo primordial:

$$N_{i}\to L\,\Phi\qquad\text{e}\qquad N_{i}\to \bar L\,\Phi^{\dagger}.\tag{17.1}$$

Como $N_{i}$ é de **Majorana**, ambos os canais estão abertos — este é o ponto essencial. A interferência entre as amplitudes de árvore e de laço (vértice e autoenergia) gera uma assimetria CP:

$$\varepsilon_{i}=\frac{\Gamma(N_{i}\to L\Phi)-\Gamma(N_{i}\to\bar L\Phi^{\dagger})}{\Gamma_{\rm total}}.\tag{17.2}$$

Para hierarquia $M_{1}\ll M_{2,3}$,

$$\varepsilon_{1}\simeq -\frac{3}{16\pi}\frac{1}{(y^{\dagger}y)_{11}}\sum_{j\neq1}\operatorname{Im}\!\left[\left(y^{\dagger}y\right)_{1j}^{2}\right]\frac{M_{1}}{M_{j}} \;\lesssim\;\frac{3}{16\pi}\frac{M_{1}\,m_{3}}{v^{2}}\Big|_{v\simeq174\ \mathrm{GeV}},\tag{17.3}$$

o último sendo o **limite de Davidson–Ibarra**, que impõe

$$M_{1}\gtrsim10^{9}\ \mathrm{GeV}\tag{17.4}$$

para gerar a assimetria bariônica observada $\eta_{B}\simeq6\times10^{-10}$.

### 17.2 As três condições de Sakharov

1. **Violação de $B$** (aqui, de $B-L$, convertido em $B$ por processos de esfaleron eletrofracos, que são ativos para $T\gtrsim100$ GeV e convertem $B-L$ em $B$ com fator $\sim28/79$).
2. **Violação de C e CP**: fornecida pelas fases complexas de $y$, que incluem as fases de $R$ (13.6) e, em geral, também as fases de Majorana de baixa energia.
3. **Fora do equilíbrio térmico**: garantida se $\Gamma_{N}<H(T=M_{1})$.

$$\eta_{B}\simeq 10^{-2}\times\varepsilon_{1}\times\kappa,\tag{17.5}$$

com $\kappa\lesssim1$ o fator de eficiência de *washout*, obtido resolvendo as equações de Boltzmann.

### 17.3 Relevância para a distinção Dirac/Majorana

Leptogênese **exige** neutrinos de Majorana: se $L$ fosse exatamente conservado, não haveria assimetria em (17.1) porque os dois canais não coexistiriam. É por isso que a natureza de Majorana está ligada, teoricamente, à explicação da assimetria matéria–antimatéria do universo — um dos argumentos mais fortes, ainda que indiretos, a favor dessa hipótese.

**Variantes.** Leptogênese ressonante (Pilaftsis–Underwood), com $M_{1}\simeq M_{2}$ e $\varepsilon$ amplificado por $M/\Delta M$, viabiliza escalas de TeV; leptogênese via oscilações (Akhmedov–Rubakov–Smirnov, mecanismo ARS) opera com $M_{N}\sim$ GeV, dentro do alcance de experimentos de dumping de feixe (SHiP) e do LHC.

---

## 18. O teorema da confusão prática Dirac–Majorana

### 18.1 Enunciado

**Teorema.** No limite $m_{\nu}\to0$, todas as observáveis calculadas com neutrinos de Dirac e de Majorana coincidem. As diferenças em qualquer processo com neutrinos ultrarrelativísticos são suprimidas por potências de $m_{\nu}/E$.

*Esboço.* Para $m=0$, a quiralidade é conservada e coincide com a helicidade. As interações do Modelo Padrão acoplam-se apenas a $\nu_{L}$ e $\bar\nu_{R}$. No caso de Majorana, os estados produzidos por $\nu_{L}=P_{L}\psi_{M}$ e $(\nu_{L})^{c}=P_{R}\psi_{M}$ são exatamente os que, no caso de Dirac, seriam chamados "$\nu$" e "$\bar\nu$". Como nenhuma medida acessa a componente de quiralidade errada — cuja amplitude é $\propto m/E$ —, os dois casos são operacionalmente idênticos. $\blacksquare$

### 18.2 Estimativas numéricas

Para um neutrino de $m_{\nu}\sim0.05$ eV em um experimento de $E\sim1$ MeV, a supressão é

$$\left(\frac{m_{\nu}}{E}\right)^{2}\sim\left(\frac{5\times10^{-2}\ \mathrm{eV}}{10^{6}\ \mathrm{eV}}\right)^{2}\sim2.5\times10^{-15}.\tag{18.1}$$

Isso é o que torna a questão experimentalmente difícil: **essencialmente nenhum processo com neutrinos relativísticos distingue Dirac de Majorana**.

### 18.3 As exceções — e por que funcionam

A escapatória do teorema é procurar processos cuja amplitude **de ordem dominante** já seja proporcional a $m_{\nu}$, de modo que o fator de supressão seja compensado pela ausência do processo concorrente:

| Sonda | Por que escapa |
|:---|:---|
| **$0\nu\beta\beta$** | O processo concorrente de Dirac tem taxa **zero**. Toda a amplitude é $\propto m_{\beta\beta}$, e o enorme fator de espaço de fase nuclear ($\sim10^{26}$ yr de sensibilidade) compensa a supressão. |
| **Colisores com $N$ pesado** | O neutrino relevante é **não relativístico** ($M_{N}\gtrsim$ TeV), logo $m/E\sim1$. |
| **Captura de neutrinos de relíquia** (PTOLEMY) | $\nu$ cósmicos hoje são não relativísticos ($T_{\nu}\sim1.9$ K $\ll m_{\nu}$). A taxa de captura em $^{3}$H é **duas vezes maior** para Majorana que para Dirac, porque ambas as helicidades contribuem. |
| **Momentos eletromagnéticos de transição** | A estrutura antissimétrica (10.3) difere qualitativamente do caso de Dirac. |
| **Aniquilação de matéria escura** | Se a matéria escura é de Majorana, a supressão de helicidade em onda $s$ é uma assinatura estrutural (§19.2). |

### 18.4 O que oscilações **não** podem dizer

Vale repetir o resultado de §14.3 em linguagem física: oscilações são processos com $\Delta L=0$ e, portanto, medem $|U_{\alpha i}|$ e $\Delta m^{2}_{ij}$, mas são **rigorosamente cegas** às fases de Majorana e à natureza Dirac/Majorana. Nenhum aprimoramento de precisão em experimentos de oscilação (DUNE, Hyper-K, JUNO) pode resolver a questão. Isso não os torna irrelevantes para o problema: eles fixam $\theta_{12},\theta_{13},\Delta m^{2}$ e o ordenamento, que são os *inputs* de (15.4).

---

## 19. Férmions de Majorana além dos neutrinos

### 19.1 Supersimetria: gauginos e neutralinos

Em teorias supersimétricas, os parceiros fermiônicos dos bósons de gauge (gauginos) estão na representação **adjunta**, que é real. Um férmion na representação adjunta pode — e, se a supersimetria é $\mathcal{N}=1$, **deve** — ser de Majorana:

$$\lambda^{a} = (\lambda^{a})^{c},\qquad a=1,\ldots,\dim G.\tag{19.1}$$

No MSSM, os quatro **neutralinos** $\tilde\chi^{0}_{1,\ldots,4}$ — misturas de bino, wino neutro e higgsinos — são férmions de Majorana. Sua matriz de massa é $4\times4$ complexa simétrica, diagonalizada por Takagi (§12), exatamente como a matriz de massa de neutrinos. Toda a estrutura formal desenvolvida aqui se aplica sem modificação.

O gluino $\tilde g$ é um octeto de cor de Majorana; sua natureza autoconjugada é o que permite os processos $pp\to\tilde g\tilde g\to$ *same-sign dileptons*, uma assinatura clássica de SUSY no LHC — o análogo direto de (16.1).

### 19.2 Matéria escura de Majorana

Se a matéria escura $\chi$ é um férmion de Majorana (o caso mais comum: neutralino, singleto escotogênico, WIMP genérico), as identidades (9.2) impõem:

1. **Acoplamento vetorial ao $Z$ nulo:** $\bar\chi\gamma^{\mu}\chi=0$. Isso **elimina** a seção de choque de espalhamento coerente spin-independente via troca de $Z$, que de outro modo já teria sido excluída por experimentos de detecção direta em várias ordens de grandeza. A matéria escura de Majorana é, nesse sentido, "naturalmente escondida".

2. **Supressão de helicidade na aniquilação:** para $\chi\chi\to f\bar f$ via corrente axial em onda $s$,

$$\langle\sigma v\rangle_{s\text{-wave}} \;\propto\; \frac{m_{f}^{2}}{m_{\chi}^{2}}.\tag{19.2}$$

*Razão:* o estado inicial $\chi\chi$ em onda $s$ com dois férmions idênticos de Majorana é forçado, pelo princípio de Pauli e pela antissimetria da função de onda, ao estado $^{1}S_{0}$ ($J^{PC}=0^{-+}$). A conservação de momento angular e a estrutura $V-A$ do estado final exigem então uma inversão de helicidade, penalizada por $m_{f}/m_{\chi}$. A consequência fenomenológica é imediata: a aniquilação é dominada pelo férmion mais pesado cinematicamente acessível ($b\bar b$, $\tau^{+}\tau^{-}$, $t\bar t$), e canais leves são irrelevantes. Processos com emissão de fóton ou glúon no estado inicial (*internal bremsstrahlung*) levantam a supressão e podem dominar, produzindo espectros de raios gama com estrutura característica de borda aguda.

3. **Espalhamento em detecção direta:** o operador dominante é spin-dependente, $\propto\bar\chi\gamma^{\mu}\gamma^{5}\chi\,\bar q\gamma_{\mu}\gamma^{5}q$, cuja seção de choque não recebe a amplificação coerente $\propto A^{2}$.

### 19.3 Modos zero de Majorana em matéria condensada

Uma nota de esclarecimento, porque a nomenclatura gera confusão. Em supercondutores topológicos (cadeia de Kitaev, nanofios de InSb/InAs com acoplamento spin-órbita, estados de vórtice em $p$-wave), aparecem excitações localizadas descritas por operadores hermitianos $\gamma = \gamma^{\dagger}$, com $\gamma^{2}=1$, chamadas **modos zero de Majorana** (MZMs).

Esses objetos:
- **Não** são férmions de Majorana relativísticos. Não há invariância de Lorentz, e eles não constituem um campo espinorial com a estrutura de §4.
- São **quase-partículas** de energia zero em um sistema de muitos corpos, cuja auto-hermiticidade decorre da estrutura de Bogoliubov–de Gennes (mistura partícula-buraco), formalmente análoga à condição (4.3).
- Obedecem estatística **não abeliana** (são anyons de Ising), o que é a base das propostas de computação quântica topológica. Férmions de Majorana relativísticos em $D=4$ obedecem estatística de Fermi–Dirac ordinária.

A analogia formal é real e profunda — a estrutura de Bogoliubov é matematicamente a mesma condição de autoconjugação — mas a identificação física é incorreta. A frase "descobriram o férmion de Majorana em um chip" é, do ponto de vista de física de partículas, uma imprecisão.

---

## 20. Síntese

### 20.1 A cadeia lógica do formalismo

$$\underbrace{\text{Álgebra de Clifford}}_{\S2}\;\Rightarrow\;\underbrace{\exists\,C:\;C\gamma^{\mu T}C^{-1}=-\gamma^{\mu}}_{\S3}\;\Rightarrow\;\underbrace{\psi^{c}=C\bar\psi^{T},\;(\psi^{c})^{c}=\psi}_{\S3.3}\;\Rightarrow\;\underbrace{\psi=\psi^{c}\ \text{é consistente}}_{\S4}$$

$$\Rightarrow\;\underbrace{\bar\psi=-\psi^{T}C^{-1}}_{(4.3)}\;\Rightarrow\;\begin{cases}\underbrace{d_{s}=b_{s}}_{\S6:\;\text{partícula}=\text{antipartícula}}\\[6pt] \underbrace{\langle T\psi\psi^{T}\rangle\neq0}_{\S7:\;\Delta L=2}\\[6pt] \underbrace{\bar\psi\gamma^{\mu}\psi=0}_{\S9:\;\text{sem carga, sem }\mu_{\rm mag}}\\[6pt] \underbrace{\mathcal{M}=\mathcal{M}^{T}}_{\S11:\;\text{Takagi, fases de Majorana}}\end{cases}$$

Tudo o mais — seesaw, $m_{\beta\beta}$, leptogênese, supressão de helicidade na matéria escura — é consequência dessas quatro linhas.

### 20.2 As afirmações centrais, em uma frase cada

1. **Existência.** A matriz $C$ existe pelo teorema de Pauli aplicado a $\{-\gamma^{\mu T}\}$; a condição $\psi=\psi^{c}$ é Lorentz-covariante porque $(\tfrac12,0)^{*}\cong(0,\tfrac12)$ em $D=4$.
2. **Conteúdo.** Um férmion de Majorana massivo tem os mesmos graus de liberdade de um férmion de Weyl sem massa: dois estados por momento, e é o **único** férmion que pode ser massivo com uma só representação irredutível.
3. **Consequência estrutural.** $\bar\psi\gamma^{\mu}\psi\equiv0$ implica ausência de qualquer carga $U(1)$ conservada, de momento magnético e elétrico diagonais, e restringe todo o acoplamento eletromagnético ao momento anapolar.
4. **Massa.** A matriz de massa é complexa simétrica, diagonalizada por congruência (Takagi), e a impossibilidade de redefinir as fases dos campos de neutrino gera $n_{g}(n_{g}-1)/2 = 3$ fases físicas, duas a mais que no caso de Dirac.
5. **Origem.** O operador de Weinberg $(LH)(LH)/\Lambda$ é o único operador de dimensão cinco do Modelo Padrão, e ele produz massa de Majorana; todos os mecanismos (seesaw I/II/III, inverso, radiativo) são realizações UV distintas do mesmo operador.
6. **Assinatura.** A única observável realista é $\Delta L=2$: o decaimento $0\nu\beta\beta$, com $[T_{1/2}]^{-1}=G_{0\nu}|\mathcal{M}_{0\nu}|^{2}m_{\beta\beta}^{2}/m_{e}^{2}$ e $m_{\beta\beta}=|\sum_{i}U_{ei}^{2}m_{i}|$.
7. **Limitação.** O teorema da confusão prática garante que toda diferença Dirac/Majorana em processos relativísticos é $\mathcal{O}(m_{\nu}^{2}/E^{2})\sim10^{-15}$; a questão só é decidível em processos onde a amplitude de Dirac é exatamente nula.

### 20.3 O estado da questão

Do ponto de vista teórico, a hipótese de Majorana é a **genérica**: exige menos estrutura (nenhuma simetria $L$ imposta *ad hoc*), explica naturalmente a pequenez de $m_{\nu}$ via seesaw, e conecta-se à assimetria bariônica via leptogênese. Do ponto de vista experimental, ela permanece **não testada**, com a próxima geração de experimentos de $0\nu\beta\beta$ prestes a cobrir integralmente a região do ordenamento invertido. Um resultado positivo estabeleceria a natureza de Majorana; um resultado nulo, se o ordenamento for normal, deixaria a questão em aberto por causa da possibilidade de cancelamento em (15.4).

---

# Apêndices

## Apêndice A — Representações explícitas das matrizes de Dirac

Em todas as representações abaixo, $\sigma^{i}$ são as matrizes de Pauli e os blocos são $2\times2$. Todas satisfazem (2.1), $\gamma^{0\dagger}=\gamma^{0}$, $\gamma^{i\dagger}=-\gamma^{i}$ (verificado explicitamente).

### A.1 Representação de Dirac (padrão)

$$\gamma^{0}=\begin{pmatrix}\mathbb{1}&0\\0&-\mathbb{1}\end{pmatrix},\qquad \gamma^{i}=\begin{pmatrix}0&\sigma^{i}\\-\sigma^{i}&0\end{pmatrix},\qquad \gamma^{5}=\begin{pmatrix}0&\mathbb{1}\\ \mathbb{1}&0\end{pmatrix}.\tag{A.1}$$

$\gamma^{0}$ diagonal — conveniente no limite não relativístico.

### A.2 Representação quiral (Weyl)

$$\gamma^{0}=\begin{pmatrix}0&\mathbb{1}\\ \mathbb{1}&0\end{pmatrix},\qquad \gamma^{i}=\begin{pmatrix}0&\sigma^{i}\\-\sigma^{i}&0\end{pmatrix},\qquad \gamma^{5}=\begin{pmatrix}-\mathbb{1}&0\\0&\mathbb{1}\end{pmatrix}.\tag{A.2}$$

Compactamente, $\gamma^{\mu}=\begin{pmatrix}0&\sigma^{\mu}\\ \bar\sigma^{\mu}&0\end{pmatrix}$ com $\sigma^{\mu}=(\mathbb{1},\vec\sigma)$, $\bar\sigma^{\mu}=(\mathbb{1},-\vec\sigma)$. $\gamma^{5}$ diagonal — a representação natural para férmions quirais e para a formulação de duas componentes.

### A.3 Representação de Majorana

$$\gamma^{0}_{M}=\begin{pmatrix}0&\sigma^{2}\\ \sigma^{2}&0\end{pmatrix},\quad \gamma^{1}_{M}=\begin{pmatrix}i\sigma^{3}&0\\0&i\sigma^{3}\end{pmatrix},\quad \gamma^{2}_{M}=\begin{pmatrix}0&-\sigma^{2}\\ \sigma^{2}&0\end{pmatrix},\quad \gamma^{3}_{M}=\begin{pmatrix}-i\sigma^{1}&0\\0&-i\sigma^{1}\end{pmatrix}.\tag{A.3}$$

$$\gamma^{5}_{M}=i\gamma^{0}_{M}\gamma^{1}_{M}\gamma^{2}_{M}\gamma^{3}_{M}=\begin{pmatrix}\sigma^{2}&0\\0&-\sigma^{2}\end{pmatrix}.\tag{A.4}$$

**Todas as $\gamma^{\mu}_{M}$ (e também $\gamma^{5}_{M}$) são puramente imaginárias** — verificado explicitamente. Logo $i\gamma^{\mu}_{M}$ é real e a equação de Dirac (4.5) tem coeficientes reais. Nessa base, $C_{M}=\gamma^{0}_{M}$, e $C_{M}\gamma^{\mu T}_{M}C_{M}^{-1}=-\gamma^{\mu}_{M}$, $C_{M}^{T}=-C_{M}$ (verificado).

### A.4 Tabela de simetrias de $C\Gamma^{A}$

Com $C=i\gamma^{2}\gamma^{0}$ nas bases de Dirac e quiral (verificado numericamente em ambas):

| $\Gamma$ | $\mathbb{1}$ | $\gamma^{5}$ | $\gamma^{\mu}$ | $\gamma^{\mu}\gamma^{5}$ | $\sigma^{\mu\nu}$ | $\sigma^{\mu\nu}\gamma^{5}$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| $(C\Gamma)^{T}$ vs. $C\Gamma$ | antissim. | antissim. | **sim.** | antissim. | **sim.** | **sim.** |
| contagem | $1$ | $1$ | $4$ | $4$ | $6$ | — |
| $\eta_{\Gamma}^{\rm M}$ (eq. 9.1) | $+1$ | $+1$ | $-1$ | $+1$ | $-1$ | $-1$ |

Total: $10$ simétricas ($C\gamma^{\mu}$, $C\sigma^{\mu\nu}$) e $6$ antissimétricas ($C$, $C\gamma^{5}$, $C\gamma^{\mu}\gamma^{5}$), consistente com a decomposição $\mathrm{Mat}_{4}=\mathrm{Sym}_{4}\oplus\mathrm{Anti}_{4}$, $16=10+6$. **Esta tabela é a origem de todos os sinais de §9.**

---

## Apêndice B — Notação de duas componentes (van der Waerden)

### B.1 Convenções

Índices não pontuados $\alpha,\beta=1,2$ transformam-se na representação $(\tfrac12,0)$; pontuados $\dot\alpha,\dot\beta$ em $(0,\tfrac12)$. O tensor invariante é

$$\epsilon^{\alpha\beta}=\epsilon^{\dot\alpha\dot\beta}=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad \epsilon_{\alpha\beta}=\epsilon_{\dot\alpha\dot\beta}=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad \epsilon^{\alpha\beta}\epsilon_{\beta\gamma}=\delta^{\alpha}_{\gamma}.\tag{B.1}$$

Subida e descida de índices: $\chi^{\alpha}=\epsilon^{\alpha\beta}\chi_{\beta}$, $\chi_{\alpha}=\epsilon_{\alpha\beta}\chi^{\beta}$. Convenção de contração (NW–SE para não pontuados, SW–NE para pontuados):

$$\chi\eta \equiv \chi^{\alpha}\eta_{\alpha},\qquad \bar\chi\bar\eta\equiv\bar\chi_{\dot\alpha}\bar\eta^{\dot\alpha}.\tag{B.2}$$

Como os campos anticomutam,

$$\chi\eta=\eta\chi,\qquad \bar\chi\bar\eta=\bar\eta\bar\chi,\qquad (\chi\eta)^{\dagger}=\bar\eta\bar\chi.\tag{B.3}$$

Em particular $\chi\chi=\epsilon^{\alpha\beta}\chi_{\beta}\chi_{\alpha}=2\chi_{2}\chi_{1}\neq0$ — o termo de massa de Majorana.

Matrizes sigma: $(\sigma^{\mu})_{\alpha\dot\beta}=(\mathbb{1},\vec\sigma)$, $(\bar\sigma^{\mu})^{\dot\alpha\beta}=(\mathbb{1},-\vec\sigma)$, com

$$\bar\sigma^{\mu\,\dot\alpha\beta}=\epsilon^{\dot\alpha\dot\gamma}\epsilon^{\beta\delta}\sigma^{\mu}_{\delta\dot\gamma},\qquad \sigma^{\mu}\bar\sigma^{\nu}+\sigma^{\nu}\bar\sigma^{\mu}=2\eta^{\mu\nu}.\tag{B.4}$$

### B.2 O dicionário $4\leftrightarrow2$ componentes

Na base quiral (A.2), com $\psi=\begin{pmatrix}\chi_{\alpha}\\ \bar\xi^{\dot\alpha}\end{pmatrix}$ e $\bar\psi=(\xi^{\alpha}\;\;\bar\chi_{\dot\alpha})$:

| Quatro componentes | Duas componentes |
|:---|:---|
| $\bar\psi_{1}P_{L}\psi_{2}$ | $\xi_{1}\chi_{2}$ |
| $\bar\psi_{1}P_{R}\psi_{2}$ | $\bar\chi_{1}\bar\xi_{2}$ |
| $\bar\psi_{1}\gamma^{\mu}P_{L}\psi_{2}$ | $\bar\chi_{1}\bar\sigma^{\mu}\chi_{2}$ |
| $\bar\psi_{1}\gamma^{\mu}P_{R}\psi_{2}$ | $\xi_{1}\sigma^{\mu}\bar\xi_{2}$ |
| $\bar\psi\psi$ (Majorana, $\xi=\chi$) | $\chi\chi+\bar\chi\bar\chi$ |
| $\bar\psi\gamma^{5}\psi$ (Majorana) | $-\chi\chi+\bar\chi\bar\chi$ |
| $\bar\psi\gamma^{\mu}\psi$ (Majorana) | $\bar\chi\bar\sigma^{\mu}\chi-\chi\sigma^{\mu}\bar\chi = 0$ |
| $\bar\psi\gamma^{\mu}\gamma^{5}\psi$ (Majorana) | $\bar\chi\bar\sigma^{\mu}\chi+\chi\sigma^{\mu}\bar\chi=2\bar\chi\bar\sigma^{\mu}\chi$ |

A penúltima linha é a demonstração em duas componentes do anulamento da corrente vetorial (9.2), usando a identidade $\chi\sigma^{\mu}\bar\eta=-\bar\eta\bar\sigma^{\mu}\chi$ para campos anticomutantes (com $\eta=\chi$).

### B.3 Espinor de Majorana e conjugação

$$\psi_{M}=\begin{pmatrix}\chi_{\alpha}\\ \bar\chi^{\dot\alpha}\end{pmatrix},\qquad \bar\psi_{M}=\left(\chi^{\alpha}\;\;\bar\chi_{\dot\alpha}\right).\tag{B.5}$$

A conjugação de carga em quatro componentes corresponde, em duas, simplesmente à conjugação hermitiana com subida/descida de índices por $\epsilon$: $\chi_{\alpha}\to\bar\chi_{\dot\alpha}=(\chi_{\alpha})^{\dagger}$. Isso deixa transparente por que a condição de Majorana é natural em duas componentes: **ela é a afirmação de que existe apenas um $\chi$, não dois campos independentes.**

---

## Apêndice C — A matriz $C$ em $D$ dimensões

### C.1 As duas matrizes de conjugação

Em $D$ dimensões com métrica de assinatura $(1,D-1)$, as matrizes gama têm dimensão $2^{\lfloor D/2\rfloor}$. Pelo teorema de Pauli generalizado, tanto $\{+\gamma^{\mu T}\}$ quanto $\{-\gamma^{\mu T}\}$ satisfazem a álgebra de Clifford, definindo

$$C_{+}\gamma^{\mu}C_{+}^{-1}=+\gamma^{\mu T},\qquad C_{-}\gamma^{\mu}C_{-}^{-1}=-\gamma^{\mu T}.\tag{C.1}$$

- **$D$ par:** ambas existem, e $C_{+}=C_{-}\gamma_{*}$ com $\gamma_{*}$ a matriz de quiralidade.
- **$D$ ímpar:** apenas uma delas existe (a outra é incompatível com a relação $\gamma^{0}\gamma^{1}\cdots\gamma^{D-1}\propto\mathbb{1}$).

Em $D=4$, a matriz relevante para o formalismo padrão é $C\equiv C_{-}$ (nossa eq. (3.1)).

### C.2 Simetria de $C$ e periodicidade mod 8

A propriedade de simetria $C_{\pm}^{T}=\varepsilon_{\pm}C_{\pm}$ depende de $D$ módulo $8$:

| $D\ \mathrm{mod}\ 8$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $\varepsilon_{-}$ | $+$ | $+$ | $-$ | $-$ | $-$ | $-$ | $+$ | $+$ |
| $\varepsilon_{+}$ | $+$ | — | $+$ | — | $-$ | — | $-$ | — |

Essa periodicidade mod $8$ é a manifestação, na álgebra de Clifford, da periodicidade de Bott.

### C.3 Existência de espinores de Majorana

A condição de Majorana em $D$ dimensões é $\psi = B\psi^{*}$ com $B = C\gamma^{0T}$ (a menos de convenções). A consistência $(\psi^{c})^{c}=\psi$ exige

$$B^{*}B = +\mathbb{1}.\tag{C.2}$$

Traduzindo (C.2) em termos de $\varepsilon_{\pm}$, obtém-se o resultado clássico:

$$\boxed{\;\text{Espinores de Majorana existem em assinatura }(1,D-1)\ \text{para}\ D\equiv 0,1,2,3,4\ (\mathrm{mod}\ 8).\;}\tag{C.3}$$

$$\boxed{\;\text{Espinores de Majorana–Weyl existem apenas para}\ D\equiv 2\ (\mathrm{mod}\ 8).\;}\tag{C.4}$$

| $D$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Majorana | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| Weyl | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ |
| Majorana–Weyl | ✓ | — | — | — | — | — | — | — | ✓ | — | — |
| Majorana simplético | — | — | — | ✓ | ✓ | ✓ | — | — | — | — | — |

Onde a Majorana ordinária falha ($D\equiv5,6,7$), existe a variante **simplética**, que impõe a condição de realidade sobre um par de espinores usando um tensor invariante antissimétrico de um grupo $SU(2)$ interno.

**Comentários de relevância física:**
- $D=4$: Majorana existe, Majorana–Weyl não. Um férmion de Majorana em $D=4$ tem $4$ componentes reais.
- $D=10$: Majorana–Weyl existe — a razão pela qual a supercorda tipo I e a heterótica são consistentes com $\mathcal{N}=1$ em dez dimensões.
- $D=11$: Majorana existe ($32$ componentes reais) — a base da supergravidade $\mathcal{N}=1$ em $D=11$.
- $D=3$: Majorana existe com $2$ componentes reais — relevante em teorias de Chern–Simons e em modelos efetivos de matéria condensada.

---

## Apêndice D — Identidades de Fierz

### D.1 Relação de completude

A base $\{\Gamma^{A}\}=\{\mathbb{1},\gamma^{\mu},\sigma^{\mu\nu}\;(\mu<\nu),\gamma^{\mu}\gamma^{5},\gamma^{5}\}$ ($16$ elementos) satisfaz $\operatorname{tr}(\Gamma^{A}\Gamma_{B})=4\delta^{A}_{B}$, o que implica

$$\delta_{ad}\,\delta_{cb}=\frac{1}{4}\sum_{A}\left(\Gamma^{A}\right)_{ab}\left(\Gamma_{A}\right)_{cd}.\tag{D.1}$$

### D.2 A matriz de Fierz

Para quatro espinores, a identidade de rearranjo é

$$\left(\bar\psi_{1}\Gamma^{A}\psi_{2}\right)\left(\bar\psi_{3}\Gamma_{A}\psi_{4}\right)=\sum_{B}F_{AB}\left(\bar\psi_{1}\Gamma^{B}\psi_{4}\right)\left(\bar\psi_{3}\Gamma_{B}\psi_{2}\right),\tag{D.2}$$

com (convenção: $T$ soma sobre $\mu<\nu$; verificado por cálculo direto)

$$F=\frac{1}{4}\begin{pmatrix} 1 & 1 & 1 & -1 & 1\\ 4 & -2 & 0 & -2 & -4\\ 6 & 0 & -2 & 0 & 6\\ -4 & -2 & 0 & -2 & 4\\ 1 & -1 & 1 & 1 & 1 \end{pmatrix}\;\begin{matrix}\leftarrow S\\ \leftarrow V\\ \leftarrow T\\ \leftarrow A\\ \leftarrow P\end{matrix}\tag{D.3}$$

*(linhas indexadas por $A$; colunas na ordem $S,V,T,A,P$.)*

**Para campos anticomutantes (o caso físico), multiplique todo o lado direito de (D.2) por $-1$.**

> **Nota de convenção.** Muitos textos usam para $T$ a normalização $\tfrac12\sigma_{\mu\nu}\otimes\sigma^{\mu\nu}$ (soma sobre todos $\mu,\nu$), o que troca as entradas $F_{ST}=F_{PT}=1/4\to1/8$ e $F_{TS}=F_{TP}=6/4\to12/4$. As identidades físicas são as mesmas.

### D.3 Identidades quirais úteis

Restringindo a projetores quirais, as identidades tornam-se muito mais simples. Para campos anticomutantes:

$$\left(\bar\psi_{1}\gamma^{\mu}P_{L}\psi_{2}\right)\left(\bar\psi_{3}\gamma_{\mu}P_{L}\psi_{4}\right)=-\left(\bar\psi_{1}\gamma^{\mu}P_{L}\psi_{4}\right)\left(\bar\psi_{3}\gamma_{\mu}P_{L}\psi_{2}\right),\tag{D.4}$$

$$\left(\bar\psi_{1}P_{L}\psi_{2}\right)\left(\bar\psi_{3}P_{L}\psi_{4}\right)=-\frac{1}{2}\left(\bar\psi_{1}P_{L}\psi_{4}\right)\left(\bar\psi_{3}P_{L}\psi_{2}\right)-\frac{1}{8}\left(\bar\psi_{1}\sigma^{\mu\nu}P_{L}\psi_{4}\right)\left(\bar\psi_{3}\sigma_{\mu\nu}P_{L}\psi_{2}\right).\tag{D.5}$$

A identidade (D.4) — o "milagre quiral" — é o que garante a unicidade da estrutura $V-A$ em correntes de contato e é usada constantemente na redução de operadores efetivos de $0\nu\beta\beta$ e de decaimentos de mésons.

### D.4 Fierz para campos de Majorana

Para quatro campos de Majorana, (D.2) combina-se com (9.1) para produzir vínculos adicionais. Em particular, para um único campo de Majorana $\psi$, a identidade de Grassmann $\psi_{a}\psi_{b}\psi_{c}=$ (antissimetrização) implica que **todos os operadores com mais de quatro potências de $\psi$ em duas componentes se anulam**:

$$\left(\chi\chi\right)^{2}=0\quad\text{para um único espinor de Weyl de duas componentes},\tag{D.6}$$

pois $\chi_{\alpha}$ tem apenas duas componentes de Grassmann. Portanto, o autoacoplamento não trivial de menor ordem de um único férmion de Majorana é $(\bar\psi\psi)^{2}$ em quatro componentes, que em duas componentes é $\chi\chi\,\bar\chi\bar\chi$ — o análogo fermiônico do termo $|\phi|^{4}$.

---

## Apêndice E — Variação da ação com variáveis de Grassmann

### E.1 Regras de diferenciação

Para variáveis de Grassmann $\theta_{i}$ com $\theta_{i}\theta_{j}=-\theta_{j}\theta_{i}$, a derivada à esquerda é definida por

$$\frac{\partial^{L}}{\partial\theta_{i}}\left(\theta_{j}\theta_{k}\right)=\delta_{ij}\theta_{k}-\delta_{ik}\theta_{j}.\tag{E.1}$$

Ao variar uma ação, é essencial mover $\delta\psi$ para a **esquerda** de cada termo antes de fatorá-lo, contando os sinais de anticomutação.

### E.2 O caso de Dirac (referência)

$$S_{D}=\int d^{4}x\;\bar\psi\left(i\not{\partial}-m\right)\psi.\tag{E.2}$$

Aqui $\psi$ e $\bar\psi$ são independentes, e $\delta S/\delta\bar\psi=0$ dá imediatamente $(i\not{\partial}-m)\psi=0$.

### E.3 O caso de Majorana

$$S_{M}=\frac{1}{2}\int d^{4}x\;\bar\psi\left(i\not{\partial}-m\right)\psi,\qquad \bar\psi=-\psi^{T}C^{-1}.\tag{E.3}$$

Substituindo o vínculo,

$$S_{M}=-\frac{1}{2}\int d^{4}x\;\psi^{T}C^{-1}\left(i\not{\partial}-m\right)\psi \equiv -\frac{1}{2}\int d^{4}x\;\psi^{T}\,\mathcal{D}\,\psi,\qquad \mathcal{D}\equiv C^{-1}(i\not{\partial} - m).\tag{E.4}$$

A variação é

$$\delta S_{M}=-\frac{1}{2}\int d^{4}x\left[\delta\psi^{T}\mathcal{D}\psi+\psi^{T}\mathcal{D}\,\delta\psi\right].\tag{E.5}$$

O segundo termo pode ser reescrito transpondo (um número é igual a sua transposta) e contando o sinal de Grassmann:

$$\psi^{T}\mathcal{D}\,\delta\psi = -\left(\delta\psi\right)^{T}\mathcal{D}^{T}\psi\times(-1)_{\rm Grassmann} = \delta\psi^{T}\,\mathcal{D}^{T}\,\psi.\tag{E.6}$$

Agora o ponto essencial: usando $C^{T}=-C$ e $C^{-1}\gamma^{\mu}C=-\gamma^{\mu T}$,

$$\mathcal{D}^{T}=\left[C^{-1}(i\not{\partial}-m)\right]^{T}=\left(i\gamma^{\mu T}\partial_{\mu}-m\right)C^{-T}= \mathcal{D}\;\;\text{(a menos de derivada total)}.\tag{E.7}$$

Ou seja, $\mathcal{D}$ é **simétrica** no sentido relevante, os dois termos de (E.5) são iguais, e

$$\delta S_{M}=-\int d^{4}x\;\delta\psi^{T}\,C^{-1}\left(i\not{\partial}-m\right)\psi.\tag{E.8}$$

$$\Longrightarrow\quad \left(i\not{\partial} - m\right)\psi = 0.\tag{E.9}$$

**O fator $2$ vindo da igualdade dos dois termos é exatamente o que cancela o $1/2$ da lagrangiana**, entregando a equação de Dirac com a massa correta $m$ (e não $2m$). Esta é a demonstração formal da afirmação de §5.1.

---

## Apêndice F — Regras de Feynman com fluxo fermiônico contínuo

Algoritmo de Denner–Eck–Hahn–Küblbeck (*Nucl. Phys. B* **387** (1992) 467). Válido para teorias com férmions de Dirac e Majorana simultaneamente.

### F.1 Procedimento

1. **Desenhe** todos os diagramas topologicamente distintos, ignorando setas.
2. **Oriente** cada cadeia fermiônica (aberta ou fechada) com uma direção arbitrária de *fermion flow*. Marque-a com uma seta fina, distinta da seta de número fermiônico (que só existe para linhas de Dirac).
3. **Leia** cada cadeia **contra** o fluxo escolhido, escrevendo os fatores da esquerda para a direita.
4. **Vértices:** se o fluxo escolhido coincide com a orientação natural do vértice, use $\Gamma$; caso contrário use
$$\Gamma'=C\Gamma^{T}C^{-1}:\qquad \mathbb{1}'=\mathbb{1},\;\;(\gamma^{5})'=\gamma^{5},\;\;(\gamma^{\mu})'=-\gamma^{\mu},\;\;(\gamma^{\mu}\gamma^{5})'=\gamma^{\mu}\gamma^{5},\;\;(\sigma^{\mu\nu})'=-\sigma^{\mu\nu}.$$
Em particular, para o vértice quiral $\gamma^{\mu}P_{L}$: $\left(\gamma^{\mu}P_{L}\right)'=-\gamma^{\mu}P_{L}$.
5. **Propagadores internos:**
$$\text{alinhado: }\;\frac{i(\not{p}+m)}{p^{2}-m^{2}+i\varepsilon},\qquad \text{anti-alinhado: }\;\frac{i(-\not{p}+m)}{p^{2}-m^{2}+i\varepsilon}.$$
(Os fatores $C$ cancelam-se sistematicamente contra os dos vértices invertidos.)
6. **Espinores externos:** para Majorana, $u$ e $v$ são intercambiáveis via (6.3); a escolha é ditada pelo fluxo. Concretamente, um férmion de Majorana externo entrando contribui com $u(p)$ se o fluxo aponta para dentro e $v(p)$ se aponta para fora.
7. **Sinais relativos:** dois diagramas cujas linhas fermiônicas externas diferem por uma permutação **ímpar** têm sinal relativo $-1$. Laços fechados: fator $(-1)$ e traço.
8. **Fatores de simetria:** $1/n!$ para $n$ férmions de Majorana idênticos no estado final; nas larguras de decaimento e seções de choque, isso evita a dupla contagem de estados idênticos.

**Independência da escolha de fluxo.** Trocar a orientação de uma cadeia inteira substitui cada vértice por $\Gamma'$ e inverte o sentido de leitura; o resultado é a transposta da amplitude anterior multiplicada pelos fatores $C$, que se cancelam. Como a amplitude é um número, ela é invariante. Isso fornece uma verificação computacional útil.

### F.2 Regras específicas de vértices típicos

| Interação | Vértice | Vértice invertido $\Gamma'$ |
|:---|:---|:---|
| Yukawa escalar $g\,\phi\,\bar\psi\psi$ | $-ig$ | $-ig$ |
| Yukawa pseudoescalar $ig\,\phi\,\bar\psi\gamma^{5}\psi$ | $g\gamma^{5}$ | $g\gamma^{5}$ |
| Corrente carregada $\frac{g}{\sqrt2}W_{\mu}\bar\ell\gamma^{\mu}P_{L}\nu$ | $\frac{ig}{\sqrt2}\gamma^{\mu}P_{L}$ | $-\frac{ig}{\sqrt2}\gamma^{\mu}P_{L}$ |
| Corrente neutra $\frac{g}{2c_{W}}Z_{\mu}\bar\nu\gamma^{\mu}P_{L}\nu$ | $\frac{ig}{2c_{W}}\gamma^{\mu}P_{L}$ | $-\frac{ig}{2c_{W}}\gamma^{\mu}P_{L}$ |

### F.3 Exemplo: $Z\to\nu_{i}\nu_{j}$ com neutrinos de Majorana

Como $\bar\psi_{i}\gamma^{\mu}\psi_{j}$ é antissimétrico e $\bar\psi_{i}\gamma^{\mu}\gamma^{5}\psi_{j}$ simétrico (§9.4), o acoplamento diagonal $Z\nu_{i}\nu_{i}$ é **puramente axial**. A largura resultante, incluindo o fator de simetria $1/2!$ para os dois férmions idênticos e a supressão de espaço de fase, é

$$\Gamma(Z\to\nu_{i}\nu_{i})=\frac{G_{F}m_{Z}^{3}}{12\pi\sqrt2}\left(1-\frac{4m_{i}^{2}}{m_{Z}^{2}}\right)^{3/2},\tag{F.1}$$

onde o expoente $3/2$ (em vez de $1/2$ no caso vetorial) é a assinatura do acoplamento puramente axial. Para $m_{i}\ll m_{Z}$ recupera-se exatamente o resultado de Dirac — mais uma instância do teorema da confusão prática (§18).

---

## Apêndice G — Cálculo da amplitude de 0νββ

### G.1 A lagrangiana efetiva de corrente carregada

$$\mathcal{L}_{\rm CC}=-\frac{G_{F}}{\sqrt2}\,J^{\mu\dagger}_{\rm had}\,j_{\mu,\rm lep}+\text{h.c.},\qquad j_{\mu,\rm lep}=\sum_{i}\bar e\,\gamma_{\mu}(1-\gamma^{5})\,U_{ei}\,\nu_{i}.\tag{G.1}$$

### G.2 A amplitude leptônica

O processo (15.1) requer **dois** vértices de (G.1), ambos criando um elétron. A linha de neutrino interna deve, portanto, ser contraída consigo mesma na configuração "anômala" (7.2). A parte leptônica da amplitude é

$$\mathcal{A}^{\rm lep}_{\mu\nu}=\sum_{i}U_{ei}^{2}\;\bar u(p_{1})\,\gamma_{\mu}(1-\gamma^{5})\;\frac{i(\not{q}+m_{i})}{q^{2}-m_{i}^{2}}\;C\;\left[\gamma_{\nu}(1-\gamma^{5})\right]^{T}\,\bar u^{T}(p_{2})\;-\;(p_{1}\leftrightarrow p_{2}).\tag{G.2}$$

O termo $(p_{1}\leftrightarrow p_{2})$ com sinal negativo implementa a antissimetrização exigida pela estatística dos dois elétrons idênticos.

**A seleção do termo de massa.** Escrevendo $(1-\gamma^{5})=2P_{L}$ e usando $P_{L}\gamma^{\alpha}=\gamma^{\alpha}P_{R}$:

$$P_{L}\left(\not{q} + m_{i}\right)\left[\gamma_{\nu}P_{L}\right]^{T}\;\longrightarrow\; \underbrace{P_{L}\not{q}\,\gamma_{\nu}^{T}P_{L}^{T}}_{\text{contém }P_{L}P_{R}=0}\;+\;m_{i}\,P_{L}\gamma_{\nu}^{T}P_{L}^{T}.\tag{G.3}$$

O termo $\propto\not{q}$ envolve a projeção $P_{L}\cdots P_{R}$ na cadeia espinorial e se anula identicamente. **Apenas o termo de massa sobrevive**, confirmando quantitativamente §7.2:

$$\mathcal{A}^{\rm lep}\;\propto\;\sum_{i}U_{ei}^{2}\,\frac{m_{i}}{q^{2}-m_{i}^{2}}.\tag{G.4}$$

### G.3 A expansão de impulso e $m_{\beta\beta}$

O momento virtual do neutrino é fixado pela escala nuclear: $|\vec q|\sim1/R\sim p_{F}\sim100$ MeV, com $R\simeq1.2\,A^{1/3}$ fm. Para os neutrinos leves, $m_{i}\lesssim0.1$ eV $\ll|q|$, de modo que

$$\frac{m_{i}}{q^{2}-m_{i}^{2}}\;\simeq\;\frac{m_{i}}{q^{2}},\tag{G.5}$$

e a dependência de sabor fatora completamente:

$$\mathcal{A}^{\rm lep}\;\propto\;\frac{1}{q^{2}}\sum_{i}U_{ei}^{2}m_{i}\;\equiv\;\frac{m_{\beta\beta}}{q^{2}}\quad\text{(a menos de fase global)}.\tag{G.6}$$

Este é o passo que define $m_{\beta\beta}$ e que justifica sua interpretação como *o* parâmetro de violação de $L$ acessível ao experimento. Note que a fatoração requer $m_{i}\ll|q|$; para neutrinos estéreis pesados ($m_{N}\gg|q|$) o propagador se torna $\propto1/m_{N}$ e a dependência se inverte — daí a existência de um máximo ressonante em $m_{N}\sim100$ MeV.

### G.4 A parte nuclear e o resultado final

A parte hadrônica gera o elemento de matriz nuclear

$$\mathcal{M}_{0\nu}= \mathcal{M}_{GT}-\frac{g_{V}^{2}}{g_{A}^{2}}\mathcal{M}_{F}+\mathcal{M}_{T},\tag{G.7}$$

soma das contribuições de Gamow–Teller, Fermi e tensorial, cada uma envolvendo o *potencial de neutrino*

$$H(r)\;\simeq\;\frac{2R}{\pi r}\int_{0}^{\infty}\frac{\sin(qr)}{q+\langle E\rangle}\,dq,\tag{G.8}$$

que é de **longo alcance** ($\sim1/r$), em contraste com o caráter de contato dos mecanismos de curta distância. Integrando o espaço de fase dos dois elétrons:

$$\left[T_{1/2}^{0\nu}\right]^{-1}=G_{0\nu}\left|\mathcal{M}_{0\nu}\right|^{2}\frac{m_{\beta\beta}^{2}}{m_{e}^{2}},\tag{G.9}$$

que é (15.5). Ordens de grandeza para $^{136}$Xe: $G_{0\nu}\simeq1.5\times10^{-14}\ {\rm yr}^{-1}$, $|\mathcal{M}_{0\nu}|\simeq1.5$–$4$, e $T_{1/2}>3.8\times10^{26}$ yr $\Rightarrow$ $m_{\beta\beta}<28$–$122$ meV.

### G.5 Diagnóstico do mecanismo

O caráter de longo alcance de (G.8) versus o de contato dos operadores de dimensão nove produz **distribuições angulares distintas** dos dois elétrons:

$$\frac{d\Gamma}{d\cos\theta_{12}}\propto 1 + k(\varepsilon_{1},\varepsilon_{2})\cos\theta_{12},\tag{G.10}$$

com $k<0$ para o mecanismo de massa (longo alcance) e $k>0$ para vários mecanismos de curto alcance. Experimentos com rastreamento (SuperNEMO, NEXT) podem, em princípio, medir $k$ e discriminar mecanismos — informação inacessível a calorímetros puros.

---

## Referências

**Fundamentos e artigos originais**

1. E. Majorana, *Teoria simmetrica dell'elettrone e del positrone*, Nuovo Cim. **14** (1937) 171.
2. W. Pauli, *Contributions mathématiques à la théorie des matrices de Dirac*, Ann. Inst. H. Poincaré **6** (1936) 109.
3. P. A. M. Dirac, *The Quantum Theory of the Electron*, Proc. Roy. Soc. A **117** (1928) 610.
4. S. Weinberg, *Baryon and Lepton Nonconserving Processes*, Phys. Rev. Lett. **43** (1979) 1566.
5. J. Schechter and J. W. F. Valle, *Neutrinoless Double-β Decay in SU(2)×U(1) Theories*, Phys. Rev. D **25** (1982) 2951.

**Seesaw e geração de massa**

6. P. Minkowski, *μ→eγ at a Rate of One Out of 10⁹ Muon Decays?*, Phys. Lett. B **67** (1977) 421.
7. M. Gell-Mann, P. Ramond, R. Slansky, in *Supergravity*, eds. van Nieuwenhuizen & Freedman (1979) 315.
8. T. Yanagida, in *Proc. Workshop on Unified Theory and Baryon Number in the Universe*, KEK (1979).
9. R. N. Mohapatra and G. Senjanović, *Neutrino Mass and Spontaneous Parity Nonconservation*, Phys. Rev. Lett. **44** (1980) 912.
10. J. Schechter and J. W. F. Valle, *Neutrino Masses in SU(2)×U(1) Theories*, Phys. Rev. D **22** (1980) 2227.
11. R. Foot, H. Lew, X.-G. He, G. C. Joshi, *Seesaw Neutrino Masses Induced by a Triplet of Leptons*, Z. Phys. C **44** (1989) 441.
12. R. N. Mohapatra and J. W. F. Valle, *Neutrino Mass and Baryon Number Nonconservation in Superstring Models*, Phys. Rev. D **34** (1986) 1642. [seesaw inverso]
13. A. Zee, Phys. Lett. B **93** (1980) 389; K. S. Babu, Phys. Lett. B **203** (1988) 132.
14. E. Ma, *Verifiable Radiative Seesaw Mechanism of Neutrino Mass and Dark Matter*, Phys. Rev. D **73** (2006) 077301. [escotogênico]
15. J. A. Casas and A. Ibarra, *Oscillating Neutrinos and μ→eγ*, Nucl. Phys. B **618** (2001) 171.

**Formalismo e técnica de cálculo**

16. A. Denner, H. Eck, O. Hahn, J. Küblbeck, *Feynman Rules for Fermion-Number-Violating Interactions*, Nucl. Phys. B **387** (1992) 467.
17. H. K. Dreiner, H. E. Haber, S. P. Martin, *Two-component spinor techniques and Feynman rules*, Phys. Rept. **494** (2010) 1. [arXiv:0812.1594]
18. P. B. Pal, *Dirac, Majorana and Weyl fermions*, Am. J. Phys. **79** (2011) 485. [arXiv:1006.1718]
19. B. Kayser, *Majorana Neutrinos and Their Electromagnetic Properties*, Phys. Rev. D **26** (1982) 1662.
20. J. F. Nieves, *Electromagnetic Properties of Majorana Neutrinos*, Phys. Rev. D **26** (1982) 3152.

**Revisões**

21. S. M. Bilenky and C. Giunti, *Neutrinoless Double-Beta Decay: A Probe of Physics Beyond the Standard Model*, Int. J. Mod. Phys. A **30** (2015) 1530001.
22. M. J. Dolinski, A. W. P. Poon, W. Rodejohann, *Neutrinoless Double-Beta Decay: Status and Prospects*, Ann. Rev. Nucl. Part. Sci. **69** (2019) 219.
23. J. D. Vergados, H. Ejiri, F. Šimkovic, *Neutrinoless double beta decay and neutrino mass*, Int. J. Mod. Phys. E **25** (2016) 1630007.
24. C. Giunti and A. Studenikin, *Neutrino electromagnetic interactions: a window to new physics*, Rev. Mod. Phys. **87** (2015) 531.
25. S. Davidson, E. Nardi, Y. Nir, *Leptogenesis*, Phys. Rept. **466** (2008) 105.
26. R. N. Mohapatra and A. Y. Smirnov, *Neutrino Mass and New Physics*, Ann. Rev. Nucl. Part. Sci. **56** (2006) 569.

**Dados experimentais e ajustes globais citados**

27. KamLAND-Zen Collaboration, *Search for Majorana Neutrinos with the Complete KamLAND-Zen Dataset*, [arXiv:2406.11438](https://arxiv.org/abs/2406.11438).
28. LEGEND Collaboration, *Results of the LEGEND-200 experiment in the search for neutrinoless double beta decay*, [arXiv:2508.18573](https://arxiv.org/abs/2508.18573).
29. CUORE Collaboration, *Constraints on Lepton Number Violation with the 2 tonne·yr CUORE Dataset*, [arXiv:2404.04453](https://arxiv.org/abs/2404.04453).
30. KATRIN Collaboration, *Direct neutrino-mass measurement based on 259 days of KATRIN data*, Science (2025). [doi:10.1126/science.adq9592](https://www.science.org/doi/10.1126/science.adq9592)
31. I. Esteban *et al.* (NuFit), *NuFit-6.0: Updated global analysis of three-flavor neutrino oscillations*, JHEP **12** (2024) 216, [arXiv:2410.05380](https://arxiv.org/abs/2410.05380).
32. DESI Collaboration, *DESI DR2 Results II: BAO Measurements and Cosmological Constraints*, [arXiv:2503.14738](https://arxiv.org/abs/2503.14738).

**Livros-texto**

33. C. Giunti and C. W. Kim, *Fundamentals of Neutrino Physics and Astrophysics*, Oxford University Press (2007). — a referência mais completa para o formalismo de Majorana em contexto fenomenológico.
34. R. N. Mohapatra and P. B. Pal, *Massive Neutrinos in Physics and Astrophysics*, 3rd ed., World Scientific (2004).
35. M. Fukugita and T. Yanagida, *Physics of Neutrinos and Applications to Astrophysics*, Springer (2003).
36. P. Ramond, *Journeys Beyond the Standard Model*, Perseus (1999). — Apêndice sobre espinores em $D$ dimensões.
37. J. Wess and J. Bagger, *Supersymmetry and Supergravity*, 2nd ed., Princeton (1992). — convenções de duas componentes.

---

*Documento produzido como Review Lecture. Convenções em §0; todas as identidades algébricas (álgebra de Clifford nas três representações, propriedades de $C$, tabela de simetrias de $C\Gamma^{A}$, matriz de Fierz e a fórmula do seesaw) foram verificadas por cálculo simbólico-numérico direto.*
