import os
from typing import Literal
import pandas as pd
from pathlib import Path
from src import generate_metadata


def ingest_directory(
    src_dir,
    output_path,
    layer,
    catalog_manager,
    description,
    target_format: Literal[".csv", ".parquet"],
    output_format: Literal[".csv", ".parquet"],
    observations,
):
    """Varre um diretório e registra tudo no catálogo."""
    files = os.listdir(src_dir)
    for file in files:
        if file.endswith(target_format):
            path = os.path.join(src_dir, file)
            df = pd.read_csv(path) if target_format == ".csv" else pd.read_parquet(path)
            meta = generate_metadata(
                df=df,
                filename=Path(path).stem,
                layer=layer,
                output_path=output_path,
                file_format=output_format,
                description=description,
                observations=observations,
                src=src_dir,
            )
            catalog_manager.update_catalog(meta)

    print(
        f"✅ {len(files)} Dados de '{src_dir}' processados digeridos para' '{output_path}' no formato {output_format}"
    )


def save_and_catalog(
    df,
    filename,
    layer,
    output_path,
    description,
    observations,
    catalog_manager,
    src="Pipeline",
    file_format=".parquet",
):
    """
    1. Salva o DataFrame no formato escolhido[cite: 26, 121, 221].
    2. Gera o metadado JSON[cite: 105, 150].
    3. Atualiza o catálogo central[cite: 138, 148].
    """
    os.makedirs(output_path, exist_ok=True)
    file_path = os.path.join(output_path, f"{filename}{file_format}")

    if file_format == ".parquet":
        df.to_parquet(file_path, index=False)
    else:
        df.to_csv(file_path, index=False)

    meta = generate_metadata(
        df=df,
        description=description,
        src=src,
        output_path=output_path,
        file_format=file_format,
        filename=filename,
        layer=layer,
        observations=observations,
    )
    catalog_manager.update_catalog(meta)
    print(f"✅ Dataset {filename} processado com sucesso na camada {layer}.")
