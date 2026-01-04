# WordCloud From Data on Image

A modular Python package for generating word clouds from wine reviews dataset with configurable options and multiple generation variants.

## Features

- **Modular Design**: Separate modules for data loading, text processing, and word cloud generation
- **Configuration-driven**: All settings in YAML, no hardcoded values
- **Multiple Variants**: Support for different word cloud generation approaches
- **CLI Interface**: Easy command-line usage for all variants
- **Mask Support**: Generate word clouds with custom image masks

## Installation

1. Clone the repository and navigate to the project directory:
   ```bash
   cd wordcloud_from_data
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On Linux/Mac
   # or
   .venv\Scripts\activate  # On Windows
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface

Generate word clouds using the CLI:

```bash
# Basic word cloud from first review
python -m src.cli --variant basic_single

# Word cloud from all reviews with stopwords
python -m src.cli --variant basic_all

# Word cloud with wine bottle mask
python -m src.cli --variant wine_masked

# Country-specific word cloud
python -m src.cli --variant country_masked --country US

# Multiple countries
python -m src.cli --variant country_masked --country US,France,Italy

# Custom output directory
python -m src.cli --variant basic_single --output-dir custom_output/

# List available variants
python -m src.cli --list-variants

# List available countries
python -m src.cli --list-countries
```

### Available Variants

| Variant | Description |
|---------|-------------|
| `basic_single` | Word cloud from first review only |
| `basic_all` | Word cloud from ALL reviews with stopwords |
| `wine_masked` | Word cloud with wine bottle mask |
| `country_masked` | Country-specific masked word clouds |

## Configuration

All settings are configurable via `src/config/settings.yaml`:

```yaml
data:
  csv_path: "data/winemag-data-130k-v2.csv"
  encoding: "utf-8"

text:
  default_stopwords:
    - "drink"
    - "now"
    - "wine"
    - "flavor"
    - "flavors"
  
wordcloud:
  max_words: 200
  max_font_size: 50
  min_font_size: 4
  background_color: "black"
  prefer_horizontal: 0.9
  relative_scaling: 0.5

masks:
  input_dir: "masks"
  format_transform: true

output:
  directory: "output"
  dpi: 300
  format: "png"

variants:
  basic_single:
    max_words: 100
    max_font_size: 50
  
  basic_all:
    max_words: 200
    use_stopwords: true
  
  wine_masked:
    max_words: 1000
    mask_file: "wine_mask.png"
    contour_width: 1
    contour_color: "white"
  
  country_masked:
    max_words: 10000
    max_font_size: 12
    contour_width: 1
    contour_color: "white"
    color_from_mask: true
    countries:
      - "US"
      - "France"
      - "Italy"
      - "Spain"
      - "Portugal"
```

## Project Structure

```
wordcloud_from_data/
├── src/
│   ├── config/           # Configuration files
│   ├── generators/       # Word cloud generators
│   ├── data_loader.py    # Data loading utilities
│   ├── text_processor.py # Text processing utilities
│   ├── mask_processor.py # Mask image processing
│   ├── visualizer.py     # Display and save word clouds
│   └── cli.py           # Command-line interface
├── data/                # Wine reviews CSV
├── masks/               # Mask images
├── output/              # Generated word clouds
└── requirements.txt     # Python dependencies
```

## Python API

You can also use the package programmatically:

```python
from src import WineDataLoader, BasicAllGenerator

# Load data
loader = WineDataLoader("data/winemag-data-130k-v2.csv")
df = loader.load_csv()

# Generate word cloud
generator = BasicAllGenerator("data/winemag-data-130k-v2.csv")
wordcloud = generator.generate()

# Save output
generator.save_output(wordcloud, "my_wordcloud")
```

## 📄 License

This project is a open source project and is available under the [MIT License](LICENSE).


## 👨‍💻 Author

**Jogesh Ghadai**
- Email: jogesh6895@gmail.com
- GitHub: [@Jogesh6895](https://github.com/Jogesh6895)

---
