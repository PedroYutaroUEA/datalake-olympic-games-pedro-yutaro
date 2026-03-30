import json
import os
from typing import Literal
from datetime import datetime

import pandas as pd


def extract_fields(df: pd.DataFrame) -> list[dict]:
    """
    Extrai informações dos campos do Dataframe.
    """
    fields = []
    for col in df.columns:
        fields.append(
            {
                "name": col,
                "type": str(df[col].dtype),
                "count": int(df[col].notna().sum()),
            }
        )
    return fields


def generate_metadata(
    df: pd.DataFrame,
    filename: str,
    file_format: Literal[".csv", ".parquet"],
    output_path: str,
    description: str,
    layer: str,
    src="Local File",
    observations="Gerado automaticamente pela pipeline.",
    encoding="utf-8",
):
    """
    Gera automaticamente o arquivo JSON de metadados para um DataFrame.
    """

    metadata = {
        "dataset": filename,
        "source": src,
        "description": description,
        "layer": layer,
        "fields": extract_fields(df=df),
        "collected_at": datetime.now().strftime("%Y-%m-%d"),
        "format": file_format,
        "observations": observations,
        "encoding": encoding,
    }

    # Define o caminho do JSON baseado no caminho do arquivo de dados
    os.makedirs(output_path, exist_ok=True)
    json_path = os.path.join(output_path, f"{filename}.json")

    with open(json_path, "w", encoding=encoding) as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)

    return metadata
