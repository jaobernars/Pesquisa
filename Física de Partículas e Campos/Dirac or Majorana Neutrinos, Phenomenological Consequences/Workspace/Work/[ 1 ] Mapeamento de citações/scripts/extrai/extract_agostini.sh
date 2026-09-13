#!/bin/bash
# Rode a partir da pasta "[ 1 ] Mapeamento de citações" (caminhos relativos).
PDF="Citações das Referências/[1] AGOSTINI, Referências.pdf"
OUT="dados/ref/_agostini_cols.txt"
: > "$OUT"
for p in $(seq 1 20); do
  pdftotext -layout -f $p -l $p -x 0   -y 0 -W 310 -H 792 "$PDF" - >> "$OUT"
  pdftotext -layout -f $p -l $p -x 302 -y 0 -W 310 -H 792 "$PDF" - >> "$OUT"
done
wc -l "$OUT"
