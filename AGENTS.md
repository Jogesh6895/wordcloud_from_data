# AGENTS.md

This file provides guidelines for agentic coding agents working on this repository.

## Project Overview

A modular Python package for generating word clouds from wine reviews. The project uses a configuration-driven approach with YAML settings, supports multiple word cloud generation variants, and includes a CLI interface.

## Build/Lint/Test Commands

### Installation
```bash
pip install -r requirements.txt
# or
pip install -e .
```

### Running the Application
```bash
# Basic usage
python -m src.cli --variant basic_single
python -m src.cli --variant basic_all
python -m src.cli --variant wine_masked
python -m src.cli --variant country_masked --country US
```

### Code Quality Tools
```bash
# Format code
black src/ tests/ --line-length 88

# Type checking
mypy src/ --ignore-missing-imports

# Linting
flake8 src/ tests/ --max-line-length=88 --extend-ignore=E203,W503

# Sort imports
isort src/ tests/ --profile black
```

### Testing (Recommended Setup)
This project currently has no test framework. When adding tests:
```bash
# Install pytest
pip install pytest pytest-cov

# Run all tests
pytest

# Run a single test
pytest tests/test_file.py::test_function_name

# Run with coverage
pytest --cov=src --cov-report=html
```

## Code Style Guidelines

### Imports
- Group imports in order: standard library, third-party, local imports
- Use absolute imports for local modules (e.g., `from .data_loader import WineDataLoader`)
- Avoid wildcard imports (e.g., `from module import *`)
- Keep import blocks separate with blank lines

Example:
```python
from pathlib import Path
from typing import List, Dict, Any

import pandas as pd
from wordcloud import STOPWORDS

from .data_loader import WineDataLoader
from .config import get_config
```

### Type Hints
- Use type hints for all function signatures and class attributes
- Import from `typing` module: `List`, `Dict`, `Optional`, `Any`, etc.
- Return types are required for all functions
- Use `Optional[T]` for nullable values

```python
def process_text(self, text: str) -> Dict[str, int]:
    return {"word_count": len(text)}

def load_mask(self, mask_path: str) -> Optional[np.ndarray]:
    pass
```

### Naming Conventions
- **Classes**: PascalCase (e.g., `WineDataLoader`, `TextProcessor`, `MaskProcessor`)
- **Functions/Methods**: snake_case (e.g., `load_csv`, `generate_wordcloud`, `get_statistics`)
- **Variables**: snake_case (e.g., `csv_path`, `max_words`, `background_color`)
- **Private members**: prefix with underscore (e.g., `_df`, `_config`, `_stopwords`)
- **Constants**: UPPER_SNAKE_CASE (use sparingly, prefer config)

### Formatting
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (Black default)
- Two blank lines between top-level definitions
- One blank line between methods in a class
- Trailing commas in multi-line lists/_dicts

```python
class WordCloudGenerator:
    def __init__(self):
        self.config = get_config()

    def generate(self) -> WordCloud:
        pass
```

### Classes and Methods
- Use abstract base classes (ABC) for base classes that shouldn't be instantiated
- Call `super().__init__()` in subclass constructors
- Use `@property` decorators for computed attributes
- Keep methods focused and single-purpose
- Prefer composition over inheritance

```python
from abc import ABC, abstractmethod

class BaseGenerator(ABC):
    def __init__(self):
        self.config = get_config()

    @abstractmethod
    def generate(self) -> WordCloud:
        pass
```

### Configuration Management
- All settings must be in `src/config/settings.yaml`
- Use the singleton `get_config()` function to access configuration
- Provide sensible defaults when accessing config values
- Use `.get()` method for safe access with defaults

```python
config = get_config()
max_words = config.variants.get("basic_single", {}).get("max_words", 100)
```

### File I/O and Paths
- Use `pathlib.Path` for all file system operations (not `os.path`)
- Use `Path.mkdir(parents=True, exist_ok=True)` for creating directories
- Specify absolute paths when loading configuration files
- Keep data files in `data/`, masks in `masks/`, output in `output/`

```python
from pathlib import Path

mask_path = Path("masks/wine_mask.png")
output_dir = Path(self.config.output.get("directory", "output"))
output_dir.mkdir(parents=True, exist_ok=True)
```

### Error Handling
- Use explicit error handling for I/O operations (file loading, CSV parsing)
- Raise descriptive exceptions with informative messages
- Use `try/except` blocks for operations that may fail
- Consider logging errors (if logging is added)

```python
def load_csv(self) -> pd.DataFrame:
    if not self.csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {self.csv_path}")
    try:
        return pd.read_csv(self.csv_path)
    except pd.errors.EmptyDataError:
        raise ValueError(f"CSV file is empty: {self.csv_path}")
```

### Documentation
- Minimal inline comments - code should be self-documenting
- Use docstrings for classes and non-obvious methods
- Comment complex logic or non-intuitive transformations
- Keep comments concise and focused on "why", not "what"

### CLI Integration
- Use `argparse` for CLI argument parsing
- Provide `--help` documentation for all arguments
- Support `--list-variants` and similar informational flags
- Use `sys.exit(1)` for error exits

### Data Processing
- Use pandas DataFrames for CSV data
- Use numpy arrays for image data
- Convert palette images (mode "P") to RGB for color mapping
- Apply mask transformations to convert 0->255 for proper masking

### Output and Visualization
- Save output to configured output directory (default: `output/`)
- Use consistent filename patterns: `{variant_name}.{format}`
- Support custom output directories via CLI
- Return file paths from save methods for chaining

## Architecture Principles

1. **Modularity**: Separate concerns into distinct modules (data_loader, text_processor, mask_processor, visualizer, generators)
2. **Configuration-driven**: No hardcoded values - all settings in YAML
3. **Extensibility**: Add new word cloud variants by extending BaseWordCloudGenerator
4. **Single responsibility**: Each class has one clear purpose
5. **Lazy loading**: Load data only when needed (e.g., `_df` cached in WineDataLoader)

## Adding New Variants

To add a new word cloud generation variant:
1. Create new generator class extending `BaseWordCloudGenerator` in `src/generators/`
2. Import and export in `src/generators/__init__.py` and `src/__init__.py`
3. Add configuration to `src/config/settings.yaml` under `variants:` section
4. Update CLI choices in `src/cli.py` argparse configuration

Example:
```python
class NewVariantGenerator(BaseWordCloudGenerator):
    def __init__(self, csv_path: str):
        super().__init__()
        self.data_loader = WineDataLoader(csv_path)
        self.variant_config = self.config.variants.get("new_variant", {})

    def generate(self) -> WordCloud:
        pass
```
