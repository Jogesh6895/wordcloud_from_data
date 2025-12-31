from pathlib import Path
from typing import List, Dict
from ..data_loader import WineDataLoader
from ..text_processor import TextProcessor
from ..mask_processor import MaskProcessor
from ..generators.base import BaseWordCloudGenerator
from wordcloud import WordCloud
from ..config import get_config


class CountryMaskedGenerator(BaseWordCloudGenerator):
    def __init__(self, csv_path: str):
        super().__init__()
        self.data_loader = WineDataLoader(csv_path)
        self.text_processor = TextProcessor()
        self.mask_processor = MaskProcessor()
        self.variant_config = self.config.variants.get("country_masked", {})

    def generate(self, country: str) -> WordCloud:
        df = self.data_loader.filter_by_country(country)
        text = self.text_processor.join_descriptions(df)

        max_words = self.variant_config.get("max_words", 10000)
        max_font_size = self.variant_config.get("max_font_size", 12)
        background_color = self.config.wordcloud.get("background_color", "black")
        contour_width = self.variant_config.get("contour_width", 1)
        contour_color = self.variant_config.get("contour_color", "white")
        color_from_mask = self.variant_config.get("color_from_mask", True)

        masks_dir = Path(self.config.masks.get("input_dir", "masks"))
        country_lower = country.lower()
        mask_filename = f"{country_lower}_flag_mask.png"
        mask_path = masks_dir / mask_filename

        mask = self.mask_processor.load_mask_with_transform(str(mask_path))

        wordcloud = self._create_wordcloud(
            text=text,
            max_words=max_words,
            max_font_size=max_font_size,
            background_color=background_color,
            mask=mask,
            contour_width=contour_width,
            contour_color=contour_color,
        )

        if color_from_mask:
            wordcloud = self.recolor_from_mask(wordcloud, mask)

        return wordcloud

    def generate_all(self) -> Dict[str, WordCloud]:
        countries = self.variant_config.get("countries", [])
        results = {}

        for country in countries:
            try:
                wordcloud = self.generate(country)
                results[country] = wordcloud
            except Exception as e:
                print(f"Warning: Could not generate wordcloud for {country}: {e}")

        return results
