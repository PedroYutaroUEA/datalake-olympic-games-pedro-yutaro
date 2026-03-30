import json
from datetime import datetime
import os
from pathlib import Path


class CatalogManager:
    """
    Datalake Catalog Manager
    """

    def __init__(self, catalog_filename="metadata_schema.json"):
        self.root_path = Path(__file__).parent.parent.absolute()
        self.catalog_path = self.root_path / catalog_filename

    def update_catalog(self, new_metadata):
        """
        Adiciona ou atualiza um dataset no catálogo central.
        """
        catalog = self._load()

        catalog["datasets"] = [
            d for d in catalog["datasets"] if d["dataset"] != new_metadata["dataset"]
        ]
        catalog["datasets"].append(new_metadata)
        catalog["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        catalog["version"] = catalog["version"] + 1

        with open(self.catalog_path, "w", encoding="utf-8") as f:
            json.dump(catalog, f, indent=4, ensure_ascii=False)

    def _load(self) -> dict:
        has_catalog = os.path.exists(self.catalog_path)

        if has_catalog:
            with open(self.catalog_path, "r", encoding="utf-8") as f:
                return json.load(f)

        new_catalog = {
            "datalake": "Olympics Data Lake",
            "datasets": [],
            "version": -1,
            "created_at": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        }
        return new_catalog
