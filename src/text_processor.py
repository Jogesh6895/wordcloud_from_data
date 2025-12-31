from typing import List, Set, Dict
import pandas as pd
from wordcloud import STOPWORDS
from .config import get_config


class TextProcessor:
    def __init__(self):
        self.config = get_config()
        self._stopwords: Set[str] = set(STOPWORDS)
        self._load_default_stopwords()

    def _load_default_stopwords(self) -> None:
        default_stopwords = self.config.text.get("default_stopwords", [])
        self._stopwords.update(default_stopwords)

    def join_descriptions(self, df: pd.DataFrame) -> str:
        return " ".join(review for review in df.description)

    def load_stopwords(self) -> Set[str]:
        return self._stopwords

    def add_stopwords(self, words: List[str]) -> None:
        self._stopwords.update(words)

    def clear_stopwords(self) -> None:
        self._stopwords = set(STOPWORDS)
        self._load_default_stopwords()

    def get_text_stats(self, text: str) -> Dict[str, int]:
        return {"word_count": len(text)}
