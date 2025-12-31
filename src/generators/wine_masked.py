from pathlib import Path
from ..data_loader import WineDataLoader
from ..text_processor import TextProcessor
from ..mask_processor import MaskProcessor
from ..generators.base import BaseWordCloudGenerator
from wordcloud import WordCloud
from ..config import get_config


class WineMaskedGenerator(BaseWordCloudGenerator):
    def __init__(self, csv_path: str):
        super().__init__()
        self.data_loader = WineDataLoader(csv_path)
        self.text_processor = TextProcessor()
        self.mask_processor = MaskProcessor()
        self.variant_config = self.config.variants.get("wine_masked", {})

    def generate(self) -> WordCloud:
        df = self.data_loader.load_csv()
        text = self.text_processor.join_descriptions(df)

        max_words = self.variant_config.get("max_words", 1000)
        background_color = self.config.wordcloud.get("background_color", "black")
        contour_width = self.variant_config.get("contour_width", 1)
        contour_color = self.variant_config.get("contour_color", "white")

        mask_file = self.variant_config.get("mask_file", "wine_mask.png")
        masks_dir = Path(self.config.masks.get("input_dir", "masks"))
        mask_path = masks_dir / mask_file

        mask = self.mask_processor.load_mask_with_transform(str(mask_path))

        wordcloud = self._create_wordcloud(
            text=text,
            max_words=max_words,
            background_color=background_color,
            mask=mask,
            contour_width=contour_width,
            contour_color=contour_color,
        )

        return wordcloud
