# PROTOCOLO DE BUSCA — INSPIRE-HEP

Documento normativo. Todo bloco de coleta (B01–B51) segue exatamente estas regras.

## 1. Endpoint

```
https://inspirehep.net/api/literature?size=<N>&fields=<lista>&q=<query>
```

Campos padrão a pedir:
`titles,earliest_date,citation_count,citation_count_without_self_citations,author_count,dois,arxiv_eprints,document_type`

## 2. Restrição crítica de transporte

O host `inspirehep.net` está **bloqueado para `curl`/`python requests`** no container
(política de egresso da organização — HTTP 403 no CONNECT). A única via válida é a
ferramenta **`WebFetch`**. Duas limitações medidas empiricamente:

1. **URL acima de ~250 caracteres → HTTP 403 do proxy.** Mantenha a URL curta:
   peça só os campos necessários.
2. **Consultas em lote (`q=arxiv:a+or+arxiv:b+or+...`) são NÃO CONFIÁVEIS.** Com 3 IDs
   funcionam; com 5 ou mais o parser do INSPIRE devolve registros arbitrários e sem
   relação com a consulta (testado e reprovado). **Proibido usar lote.**

3. **O resumidor do `WebFetch` corrompe JSON grande.** Em papers de colaboracoes grandes
   (centenas de autores) ele trunca a resposta e ocasionalmente devolve titulo trocado ou
   confunde o numero do artigo do DOI com o `inspire_id` (observado nos blocos B09 e B10).
   Mitigacao: peca o MINIMO de campos —
   `titles,earliest_date,citation_count,citation_count_without_self_citations` — e tire
   `authors`, que e o campo que estoura o JSON. Preencha `primeiro_autor` e `journal` a
   partir do texto bruto da referencia (registre em `obs`). Se um titulo vier estranho,
   reconsulte por `recid:<id>` com esses quatro campos.
4. **O `WebFetch` tem limite de sessao.** Ao bater o limite ele responde
   "You've hit your session limit - resets <hora> (UTC)". Nao insista: grave o parcial,
   marque os uids restantes como `ERRO_FETCH` e retome depois do reset.

**Regra:** *uma referência = uma chamada `WebFetch`*. Vinte chamadas por bloco.

## 3. Cadeia de identificação (em ordem; pare no primeiro sucesso)

| Ordem | Condição | Query | Exemplo |
|---|---|---|---|
| 1 | tem `arxiv` | `q=arxiv:<id>` | `q=arxiv:hep-ph/9606388` |
| 2 | tem `doi` | `q=doi:<doi>` | `q=doi:10.1103/PhysRevD.17.2369` |
| 3 | tem `journal` (`rev\|vol\|pag`) | `q=j+<Rev>,<vol>,<pag>` | `q=j+Phys.Rev.Lett.,44,912` |
| 4 | resto | `q=t+<palavras+do+titulo>` e, se ambíguo, `+and+a+<sobrenome>` | `q=t+neutrino+mass+and+a+minkowski` |
| 5 | nada bate | registrar `status=NAO_ENCONTRADO` com a query tentada | — |

Notas de sintaxe:
- Busca por autor+ano exige o token literal `date`: `q=a+majorana+and+date+1937` funciona;
  `q=a+majorana+and+1937` devolve TOTAL=0 **em silencio** (descoberto no bloco B25). Nunca
  conclua "nao indexado" a partir da forma sem `date`.
- Cobertura pre-1950 do INSPIRE e parcial e verificada: Fermi 1934, Majorana 1937, Racah 1937,
  Furry 1938, Dirac 1928, Chadwick 1932, Goeppert-Mayer 1935 e Pauli 1930 ESTAO indexados;
  Rutherford 1920, Chadwick 1933 (Bakerian), Heisenberg 1932 partes II/III, Majorana 1933,
  Stueckelberg 1932, Fireman 1948 e Touschek 1948 NAO estao, nem por journal nem por autor+date.
  `NAO_ENCONTRADO` nesses casos e o resultado correto, nao uma falha de busca.
- `Nature Phys.` no INSPIRE e `Nat.Phys.` (nao `Nature.Phys.`). Ja para a `Nature` propriamente,
  a busca por coordenada (`j+Nature,568,53`) devolve TOTAL=0 mesmo para registros indexados —
  use titulo para artigos da Nature.
- Abreviaturas de revista sem espaços: `Phys.Rev.Lett.`, `Phys.Rev.D`, `Nucl.Phys.B`,
  `Phys.Lett.B`, `Prog.Theor.Phys.`, `Rev.Mod.Phys.`, `JHEP`, `JCAP`, `Eur.Phys.J.C`.
- Volume com letra colada no PDG (`Phys. Lett. 67B, 421`) → tente `j+Phys.Lett.B,67,421`
  e, se falhar, `j+Phys.Lett.,67B,421`.
- Erratum entre colchetes no texto bruto **não** é a referência: use sempre a citação principal.

## 4. Validação obrigatória de cada resultado

Antes de gravar a linha, confira **duas** âncoras independentes:
- `earliest_date` bate com o ano da referência (tolerância de ±1 ano; para preprints
  antigos anteriores a 1991, ±2 anos);
- primeiro autor **ou** título bate com o texto bruto da referência.

Se só uma âncora bate → `status=DUVIDOSO` e explique em `obs`.
Se `TOTAL` > 1 e os registros são diferentes → escolha o que bate nas duas âncoras;
se nenhum bater, `status=AMBIGUO`.

**Nunca invente números de citação.** Não há valor plausível: só o que o JSON devolveu.
Se o `WebFetch` responder com prosa em vez da linha pedida, repita a chamada uma vez
com a instrução de formato reforçada; se falhar de novo, `status=ERRO_FETCH`.

## 5. Saída

`resultados/<BLOCO>.csv`, cabeçalho idêntico a `resultados/_schema.csv`:

```
uid,status,inspire_id,titulo_inspire,primeiro_autor,n_autores,ano_inspire,data_inspire,arxiv,doi,journal,citacoes,citacoes_sem_auto,tipo_doc,query_usada,obs
```

- `status` ∈ `OK` | `DUVIDOSO` | `AMBIGUO` | `NAO_ENCONTRADO` | `ERRO_FETCH`
- `ano_inspire` = os 4 primeiros dígitos de `earliest_date`; `data_inspire` = valor cru.
- Campos com vírgula vão entre aspas duplas.
- Uma linha por `uid` do bloco — **20 linhas** (o bloco B47 tem 2). Nem mais, nem menos.

## 6. Encerramento do bloco

1. Rodar `python3 scripts/inspire/validar_bloco.py <BLOCO>` — falha ⇒ o bloco não está pronto.
2. Atualizar `tarefas/indice_blocos.json` (`status`: `pendente` → `concluido`, com data e contagens).
3. Gravar o CSV na pasta do João (`device_commit_files`).
4. Reportar em 3 linhas: quantos OK, quantos precisam de revisão manual, e a citação
   mais alta encontrada no bloco.
