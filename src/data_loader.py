import pandas as pd
from pathlib import Path
from typing import List, Dict, Any


class WineDataLoader:
    def __init__(self, csv_path: str):
        self.csv_path = Path(csv_path)
        self._df: pd.DataFrame = None

    def load_csv(self) -> pd.DataFrame:
        if self._df is None:
            self._df = pd.read_csv(self.csv_path, index_col=0)
        return self._df

    def filter_by_country(self, country: str) -> pd.DataFrame:
        df = self.load_csv()
        return df[df["country"] == country]

    def get_country_list(self) -> List[str]:
        df = self.load_csv()
        return sorted(df["country"].unique().tolist())

    def get_statistics(self) -> Dict[str, Any]:
        df = self.load_csv()
        return {
            "observations": df.shape[0],
            "features": df.shape[1],
            "countries": len(df.country.unique()),
            "varieties": len(df.variety.unique()),
        }

    @property
    def data(self) -> pd.DataFrame:
        return self.load_csv()
