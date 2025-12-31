import numpy as np
from PIL import Image
from pathlib import Path
from typing import Optional
from .config import get_config


class MaskProcessor:
    def __init__(self):
        self.config = get_config()

    def load_mask(self, mask_path: str) -> np.ndarray:
        mask_full_path = Path(mask_path)
        img = Image.open(mask_full_path)

        # Convert palette images with transparency to RGB
        # This ensures compatibility with ImageColorGenerator
        if img.mode == "P":
            # Convert to RGBA first to preserve transparency
            img = img.convert("RGBA")
            # Then convert to RGB for color mapping
            img = img.convert("RGB")

        return np.array(img)

    def transform_format(self, mask: np.ndarray) -> np.ndarray:
        if len(mask.shape) == 2:
            # Grayscale image - apply 0->255 transformation
            transformed = mask.copy()
            transformed[transformed == 0] = 255
            return transformed.astype(np.int32)
        else:
            # 3D array (RGB) - apply transformation to all channels
            # This preserves color for ImageColorGenerator
            transformed = mask.copy()
            # Find pixels where all channels are 0 (black)
            black_pixels = np.all(mask == 0, axis=-1)
            # Set those to white (255, 255, 255)
            transformed[black_pixels] = 255
            return transformed.astype(np.int32)

    def load_mask_with_transform(self, mask_path: str) -> Optional[np.ndarray]:
        if self.config.masks.get("format_transform", False):
            mask = self.load_mask(mask_path)
            return self.transform_format(mask)
        else:
            return self.load_mask(mask_path)
