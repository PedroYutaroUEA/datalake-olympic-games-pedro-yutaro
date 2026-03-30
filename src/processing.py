import pandas as pd


def clean_history_data(df: pd.DataFrame):
    """Transformações básicas para a camada Bronze."""
    df["season"] = df["edition"].apply(
        lambda x: "Summer" if "Summer" in x else "Winter"
    )
    return df


def clean_paris_data(df: pd.DataFrame):
    """Padroniza colunas do dataset de Paris 2024."""
    return df.rename(
        columns={
            "Gold Medal": "gold",
            "Silver Medal": "silver",
            "Bronze Medal": "bronze",
            "Total": "total",
        }
    )


def normalize_countries(df: pd.DataFrame):
    mapping = {"Soviet Union": "Russia", "Unified Team": "Russia", "ROC": "Russia"}
    if "country" in df.columns:
        df["country"] = df["country"].replace(mapping)
    return df


def aggregate_medal_table(df_combined: pd.DataFrame):
    """Lógica da camada Gold: Agregação final."""
    df_grouped = df_combined.groupby("country")[["gold", "silver", "bronze", "total"]]
    df_total = df_grouped.sum().sort_values("total", ascending=False)
    return df_total
