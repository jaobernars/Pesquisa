# -*- coding: utf-8 -*-
"""Gera dados/shortlist/shortlist_leitura.xlsx: versao legivel/esquematizada
de 'dados/shortlist/shortlist_leitura.csv' (mesmo esquema de colunas de
dados_citacoes_tema.csv). Nao altera o CSV original.
Nome de saida curto ("shortlist_leitura.xlsx", nao "..._organizado.xlsx")
para nao ultrapassar o limite de 260 caracteres de caminho do Windows/Excel."""
import pandas as pd
from export_refs import formatar_planilha
from export_citacoes import RENOMEIA, ORDEM_BASE, ORDEM_TEMA_EXTRA, WIDTHS, WRAP_COLS

ENTRADA = "dados/shortlist/shortlist_leitura.csv"
SAIDA = "dados/shortlist/shortlist_leitura.xlsx"

def main():
    df = pd.read_csv(ENTRADA, dtype=str).fillna("")
    df = df.rename(columns=RENOMEIA)
    ordem = ORDEM_BASE + ORDEM_TEMA_EXTRA + ["Citação Completa"]
    df = df[ordem]
    with pd.ExcelWriter(SAIDA, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Shortlist", index=False)
        formatar_planilha(writer.sheets["Shortlist"], df, wrap_cols=WRAP_COLS,
                           widths=WIDTHS, freeze="C2")
    print(f"OK -> {SAIDA} ({len(df)} linhas)")

if __name__ == "__main__":
    main()
