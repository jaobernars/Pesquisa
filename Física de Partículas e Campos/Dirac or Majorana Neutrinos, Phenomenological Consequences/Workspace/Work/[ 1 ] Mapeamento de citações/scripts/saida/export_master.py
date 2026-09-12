# -*- coding: utf-8 -*-
"""Gera dados/master ref/master_refs.xlsx: versao legivel/esquematizada
de 'dados/master ref/master_refs.csv' (lista mestre deduplicada, unindo
AGOSTINI e GONZALEZ-GARCIA), com colunas separadas e formatacao.
Nao altera o CSV original usado pelo pipeline (consolidar.py etc).
Nome de saida curto ("master_refs.xlsx", nao "..._organizado.xlsx") para
nao ultrapassar o limite de 260 caracteres de caminho do Windows/Excel."""
import pandas as pd
from export_refs import formatar_planilha

ENTRADA = "dados/master ref/master_refs.csv"
SAIDA = "dados/master ref/master_refs.xlsx"

RENOMEIA = {
    "uid": "ID", "bloco": "Bloco", "metodo": "Método de Casamento",
    "fontes": "Fonte(s)", "ref_ids": "IDs de Referência",
    "autor": "Autor", "ano": "Ano", "arxiv": "arXiv", "doi": "DOI",
    "titulo": "Título", "raw": "Citação Completa",
}
ORDEM = ["ID", "Bloco", "Método de Casamento", "Fonte(s)", "IDs de Referência",
         "Autor", "Ano", "Título", "Periódico", "Volume", "Página",
         "arXiv", "DOI", "Citação Completa"]
WIDTHS = {
    "ID": 9, "Bloco": 8, "Método de Casamento": 14, "Fonte(s)": 20,
    "IDs de Referência": 16, "Autor": 20, "Ano": 8, "Título": 45,
    "Periódico": 22, "Volume": 10, "Página": 10, "arXiv": 16, "DOI": 20,
    "Citação Completa": 70,
}
WRAP_COLS = {"Título", "Citação Completa"}

def montar():
    df = pd.read_csv(ENTRADA, dtype=str).fillna("")
    partes = df["journal"].str.split("|", n=2, expand=True)
    partes = partes.reindex(columns=[0, 1, 2]).fillna("")
    df["Periódico"], df["Volume"], df["Página"] = partes[0], partes[1], partes[2]
    df = df.rename(columns=RENOMEIA)
    return df[ORDEM]

def main():
    df = montar()
    with pd.ExcelWriter(SAIDA, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Master Refs", index=False)
        formatar_planilha(writer.sheets["Master Refs"], df, wrap_cols=WRAP_COLS,
                           widths=WIDTHS, freeze="C2")
    print(f"OK -> {SAIDA} ({len(df)} linhas)")

if __name__ == "__main__":
    main()
