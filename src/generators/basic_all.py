from ..data_loader import WineDataLoader
from ..text_processor import TextProcessor
from ..generators.base import BaseWordCloudGenerator
from wordcloud import WordCloud
from ..config import get_config


class BasicAllGenerator(BaseWordCloudGenerator):
    def __init__(self, csv_path: str):
        super().__init__()
        self.data_loader = WineDataLoader(csv_path)
        self.text_processor = TextProcessor()
        self.variant_config = self.config.variants.get("basic_all", {})

    def generate(self) -> WordCloud:
        df = self.data_loader.load_csv()

        text = self.text_processor.join_descriptions(df)

        max_words = self.variant_config.get("max_words", 200)
        background_color = self.config.wordcloud.get("background_color", "black")

        stopwords = None
        if self.variant_config.get("use_stopwords", False):
            stopwords = self.text_processor.load_stopwords()

        wordcloud = self._create_wordcloud(
            text=text,
            max_words=max_words,
            background_color=background_color,
            stopwords=stopwords,
        )

        return wordcloud
