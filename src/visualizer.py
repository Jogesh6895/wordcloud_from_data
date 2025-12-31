import matplotlib.pyplot as plt
from pathlib import Path
from wordcloud import WordCloud
from typing import Optional
from .config import get_config


class WordCloudVisualizer:
    def __init__(self):
        self.config = get_config()

    def display(self, wordcloud: WordCloud, figsize: tuple = (20, 10)) -> None:
        plt.figure(figsize=figsize)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    def save(self, wordcloud: WordCloud, filename: str) -> str:
        output_dir = Path(self.config.output.get("directory", "output"))
        output_dir.mkdir(parents=True, exist_ok=True)

        filepath = output_dir / f"{filename}.{self.config.output.get('format', 'png')}"
        wordcloud.to_file(str(filepath))
        return str(filepath)

    def save_to_path(self, wordcloud: WordCloud, filepath: str) -> str:
        filepath_path = Path(filepath)
        filepath_path.parent.mkdir(parents=True, exist_ok=True)
        wordcloud.to_file(str(filepath))
        return str(filepath)
