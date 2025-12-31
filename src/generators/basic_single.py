from ..data_loader import WineDataLoader
from ..text_processor import TextProcessor
from ..generators.base import BaseWordCloudGenerator
from wordcloud import WordCloud
from ..config import get_config


class BasicSingleGenerator(BaseWordCloudGenerator):
    def __init__(self, csv_path: str):
        super().__init__()
        self.data_loader = WineDataLoader(csv_path)
        self.variant_config = self.config.variants.get("basic_single", {})

    def generate(self) -> WordCloud:
        df = self.data_loader.load_csv()

        text = df.description[0]

        max_words = self.variant_config.get("max_words", 100)
        max_font_size = self.variant_config.get("max_font_size", 50)
        background_color = self.config.wordcloud.get("background_color", "black")

        wordcloud = self._create_wordcloud(
            text=text,
            max_words=max_words,
            max_font_size=max_font_size,
            background_color=background_color,
        )

        return wordcloud
