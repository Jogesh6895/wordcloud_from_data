# WordCloud From Data on Image - Project Plan

## Project Overview
Modularize the existing `WordCloudGenerator.py` script into a structured Python package with configurable YAML settings, CLI interface, and support for multiple word cloud generation variants.

## Project Structure

```
wordcloud_from_data/
├── .venv/                           # Virtual environment
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.yaml
│   ├── data_loader.py
│   ├── text_processor.py
│   ├── mask_processor.py
│   ├── generators/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── basic_single.py
│   │   ├── basic_all.py
│   │   ├── wine_masked.py
│   │   └── country_masked.py
│   ├── visualizer.py
│   └── cli.py
├── data/
│   └── winemag-data-130k-v2.csv
 ├── masks/
│   ├── us_flag_mask.png
│   ├── wine_mask.png
│   ├── france_flag_mask.png
│   ├── italy_flag_mask.png
│   ├── spain_flag_mask.png
│   └── portugal_flag_mask.png
├── output/
├── requirements.txt
├── setup.py
└── README.md
```

## Module Responsibilities

| Module | Purpose |
|--------|---------|
| `data_loader.py` | Load CSV data, filter by country, provide statistics |
| `text_processor.py` | Join descriptions, manage stopwords, text stats |
| `mask_processor.py` | Load mask images, transform format (0→255) |
| `generators/base.py` | Abstract base class for all generators |
| `generators/basic_single.py` | Word cloud from first review only |
| `generators/basic_all.py` | Word cloud from ALL reviews with stopwords |
| `generators/wine_masked.py` | Word cloud with wine bottle mask |
| `generators/country_masked.py` | Country-specific masked word clouds |
| `visualizer.py` | Display and save word cloud images |
| `cli.py` | Command-line interface for variant selection |

## YAML Configuration Structure

Location: `src/config/settings.yaml`

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

## Virtual Environment Setup

```bash
cd wordcloud_from_data
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## CLI Interface Examples

```bash
# Basic usage
python -m src.cli --variant basic_single

# With options
python -m src.cli --variant basic_all --max-words 300

# Country-specific
python -m src.cli --variant country_masked --country US

# Multiple countries
python -m src.cli --variant country_masked --country US,France,Italy

# Custom output
python -m src.cli --variant wine_masked --output-dir custom_output/

# List variants
python -m src.cli --list-variants

# List countries
python -m src.cli --list-countries
```

## Key Features

1. **Modular Design**: Each variant is a separate, importable module
2. **Configuration-driven**: All settings in YAML, no hardcoded values
3. **CLI-first**: Easy command-line usage for all variants
4. **Virtual Environment**: Isolated Python environment
5. **Non-destructive**: Original files remain untouched
6. **Type hints**: All functions include type annotations
7. **Error handling**: Graceful handling of missing files, invalid country names
8. **Logging**: Optional logging for debugging
