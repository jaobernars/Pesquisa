# -*- coding: utf-8 -*-
"""Gera versoes .xlsx legiveis/esquematizadas de:
dados/dados das citacoes/dados_citacoes.csv
dados/dados das citacoes/dados_citacoes_tema.csv
Colunas renomeadas e reordenadas por grupo (identificacao, autoria, datas,
identificadores, publicacao, citacoes, classificacao tematica, texto bruto).
Nao altera os CSVs originais usados pelo pipeline.
Os .xlsx de saida vao direto em dados/ (nao em dados/dados das citacoes/)
com nomes curtos, porque o caminho completo do projeto ja e muito longo
e ultrapassava o limite de 260 caracteres do Windows/Excel."""
import pandas as pd
from organizar_tabelas import formatar_planilha

PASTA_ENTRADA = "dados/dados das citações"
PASTA_SAIDA = "dados"

RENOMEIA = {
    "uid": "ID", "bloco": "Bloco", "nucleo": "Núcleo Temático",
    "fontes": "Fonte(s)", "citado_por_ambas": "Citado por Ambas",
    "ref_ids": "IDs de Referência", "status": "Status", "duplicata_de": "Duplicata de",
    "autor_ref": "Autor", "primeiro_autor": "Primeiro Autor", "n_autores": "Nº de Autores",
    "ano_ref": "Ano (Referência)", "ano_inspire": "Ano (Inspire)",
    "data_inspire": "Data (Inspire)", "idade_anos": "Idade (anos)",
    "arxiv": "arXiv", "doi": "DOI", "inspire_id": "Inspire ID",
    "journal": "Periódico", "titulo": "Título", "tipo_doc": "Tipo de Documento",
    "citacoes": "Citações", "citacoes_sem_auto": "Citações (sem autocitação)",
    "citacoes_por_ano": "Citações por Ano",
    "eixos": "Eixos Temáticos", "score_tema": "Score do Tema",
    "raw": "Citação Completa",
}

ORDEM_BASE = [
    "ID", "Bloco", "Fonte(s)", "Citado por Ambas", "IDs de Referência",
    "Status", "Duplicata de",
    "Autor", "Primeiro Autor", "Nº de Autores",
    "Ano (Referência)", "Ano (Inspire)", "Data (Inspire)", "Idade (anos)",
    "arXiv", "DOI", "Inspire ID",
    "Periódico", "Título", "Tipo de Documento",
    "Citações", "Citações (sem autocitação)", "Citações por Ano",
]
ORDEM_TEMA_EXTRA = ["Núcleo Temático", "Eixos Temáticos", "Score do Tema"]

WIDTHS = {
    "ID": 9, "Bloco": 8, "Fonte(s)": 14, "Citado por Ambas": 10, "IDs de Referência": 16,
    "Status": 15, "Duplicata de": 12,
    "Autor": 20, "Primeiro Autor": 20, "Nº de Autores": 10,
    "Ano (Referência)": 10, "Ano (Inspire)": 10, "Data (Inspire)": 12, "Idade (anos)": 10,
    "arXiv": 16, "DOI": 20, "Inspire ID": 12,
    "Periódico": 26, "Título": 45, "Tipo de Documento": 12,
    "Citações": 10, "Citações (sem autocitação)": 12, "Citações por Ano": 10,
    "Núcleo Temático": 12, "Eixos Temáticos": 24, "Score do Tema": 10,
    "Citação Completa": 70,
}
WRAP_COLS = {"Título", "Citação Completa", "Eixos Temáticos"}

def carregar(nome_csv, colunas_extra_tema):
    df = pd.read_csv(f"{PASTA_ENTRADA}/{nome_csv}", dtype=str).fillna("")
    df = df.rename(columns=RENOMEIA)
    ordem = ORDEM_BASE + (ORDEM_TEMA_EXTRA if colunas_extra_tema else []) + ["Citação Completa"]
    if not colunas_extra_tema:
        ordem = [c for c in ordem if c not in ORDEM_TEMA_EXTRA]
    return df[ordem]

def salvar(nome_saida, sheet_name, df):
    out_path = f"{PASTA_SAIDA}/{nome_saida}"
    with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        formatar_planilha(writer.sheets[sheet_name], df, wrap_cols=WRAP_COLS, widths=WIDTHS, freeze="C2")
    print(f"OK -> {out_path} ({len(df)} linhas, {len(df.columns)} colunas)")

def main():
    df_base = carregar("dados_citacoes.csv", colunas_extra_tema=False)
    df_tema = carregar("dados_citacoes_tema.csv", colunas_extra_tema=True)
    salvar("citacoes_organizado.xlsx", "Citações", df_base)
    salvar("citacoes_tema_organizado.xlsx", "Citações + Tema", df_tema)

if __name__ == "__main__":
    main()
