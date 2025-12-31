from abc import ABC, abstractmethod
from wordcloud import WordCloud, ImageColorGenerator
from ..config import get_config
from ..visualizer import WordCloudVisualizer


class BaseWordCloudGenerator(ABC):
    def __init__(self):
        self.config = get_config()
        self.visualizer = WordCloudVisualizer()

    @abstractmethod
    def generate(self) -> WordCloud:
        pass

    def _create_wordcloud(
        self,
        text: str,
        mask=None,
        stopwords=None,
        max_words: int = 200,
        max_font_size: int = 50,
        min_font_size: int = 4,
        background_color: str = "black",
        prefer_horizontal: float = 0.9,
        relative_scaling: float = 0.5,
        contour_width: int = 0,
        contour_color: str = "black",
        mode: str = "RGB",
        **kwargs,
    ) -> WordCloud:
        wc_params = {
            "max_words": max_words,
            "max_font_size": max_font_size,
            "min_font_size": min_font_size,
            "background_color": background_color,
            "prefer_horizontal": prefer_horizontal,
            "relative_scaling": relative_scaling,
            "contour_width": contour_width,
            "contour_color": contour_color,
            "mode": mode,
        }

        if stopwords is not None:
            wc_params["stopwords"] = stopwords

        if mask is not None:
            wc_params["mask"] = mask

        wc_params.update(kwargs)

        wordcloud = WordCloud(**wc_params).generate(text)
        return wordcloud

    def save_output(self, wordcloud: WordCloud, filename: str) -> str:
        return self.visualizer.save(wordcloud, filename)

    def recolor_from_mask(self, wordcloud: WordCloud, mask) -> WordCloud:
        image_colors = ImageColorGenerator(mask)
        return wordcloud.recolor(color_func=image_colors)
