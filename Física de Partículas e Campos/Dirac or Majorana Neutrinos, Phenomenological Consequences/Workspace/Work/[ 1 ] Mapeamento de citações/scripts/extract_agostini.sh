#!/bin/bash
PDF="/root/.claude/uploads/9e61252c-ae46-59f8-a689-7a8d08e03155/3410fb29-1_AGOSTINI_Refer_ncias.pdf"
OUT=/home/claude/proj/data/agostini_cols.txt
: > $OUT
for p in $(seq 1 20); do
  pdftotext -layout -f $p -l $p -x 0   -y 0 -W 310 -H 792 "$PDF" - >> $OUT
  pdftotext -layout -f $p -l $p -x 302 -y 0 -W 310 -H 792 "$PDF" - >> $OUT
done
wc -l $OUT
