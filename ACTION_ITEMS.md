# WordCloud From Data on Image - Action Items Breakdown

## Phase 1: Project Setup (8 action items)

- [x] 1. Create main project directory `wordcloud_from_data/`
- [x] 2. Create virtual environment `.venv/`
- [x] 3. Create directory structure:
  - [x] `src/`
  - [x] `src/config/`
  - [x] `src/generators/`
  - [x] `data/`
  - [x] `masks/`
  - [x] `output/`
- [x] 4. Copy wine reviews data:
  - [x] Source: `../wine-reviews/winemag-data-130k-v2.csv`
  - [x] Destination: `data/winemag-data-130k-v2.csv`
- [x] 5. Copy mask images:
  - [x] Source: `../input_images/us_flag.png` → `masks/us_flag.png`
  - [x] Source: `../input_images/wine_mask_xgk1tq.png` → `masks/wine_mask_xgk1tq.png`
- [x] 6. Create `requirements.txt` with dependencies
- [x] 7. Create `setup.py` for package configuration
- [x] 8. Activate virtual environment and install dependencies:
  - [x] `source .venv/bin/activate`
  - [x] `pip install -r requirements.txt`

## Phase 2: Configuration (2 action items)

- [x] 9. Create `src/config/settings.yaml` with full configuration
- [x] 10. Create `src/config/__init__.py` with YAML loader

## Phase 3: Core Modules (6 action items)

- [x] 11. Create `src/data_loader.py`:
  - [x] Class: `WineDataLoader`
  - [x] Method: `load_csv()` - loads wine reviews CSV
  - [x] Method: `filter_by_country(country: str)` - returns filtered DataFrame
  - [x] Method: `get_country_list()` - returns list of available countries
  - [x] Method: `get_statistics()` - returns dataset statistics

- [x] 12. Create `src/text_processor.py`:
  - [x] Class: `TextProcessor`
  - [x] Method: `join_descriptions(df: pd.DataFrame)` - joins all descriptions
  - [x] Method: `load_stopwords()` - loads stopwords from YAML
  - [x] Method: `add_stopwords(words: List[str])` - adds custom stopwords
  - [x] Method: `get_text_stats(text: str)` - returns word count

- [x] 13. Create `src/mask_processor.py`:
  - [x] Class: `MaskProcessor`
  - [x] Method: `load_mask(mask_path: str)` - loads image as numpy array
  - [x] Method: `transform_format(mask: np.ndarray)` - converts 0→255 for white backgrounds
  - [x] Method: `load_mask_with_transform(mask_path: str)` - combined load + transform

- [x] 14. Create `src/visualizer.py`:
  - [x] Class: `WordCloudVisualizer`
  - [x] Method: `display(wordcloud: WordCloud)` - displays using matplotlib
  - [x] Method: `save(wordcloud: WordCloud, filename: str)` - saves to output directory
  - [x] Method: `save_to_path(wordcloud: WordCloud, filepath: str)` - saves to custom path

- [x] 15. Create `src/generators/base.py`:
  - [x] Class: `BaseWordCloudGenerator` (abstract)
  - [x] Method: `generate()` (abstract) - must be implemented by subclasses
  - [x] Method: `_create_wordcloud(text: str, **kwargs)` - common WordCloud creation
  - [x] Method: `save_output(wordcloud: WordCloud, filename: str)` - save helper

- [x] 16. Create `src/__init__.py`:
  - [x] Export main classes and functions

## Phase 4: Generator Variants (8 action items)

- [x] 17. Create `src/generators/__init__.py`:
  - [x] Export all generator classes

- [x] 18. Create `src/generators/basic_single.py`:
  - [x] Class: `BasicSingleGenerator` (extends `BaseWordCloudGenerator`)
  - [x] Method: `generate()` - generates word cloud from first review
  - [x] Uses config from YAML: `variants.basic_single`

- [x] 19. Create `src/generators/basic_all.py`:
  - [x] Class: `BasicAllGenerator` (extends `BaseWordCloudGenerator`)
  - [x] Method: `generate()` - generates word cloud from ALL reviews
  - [x] Uses custom stopwords
  - [x] Uses config from YAML: `variants.basic_all`

- [x] 20. Create `src/generators/wine_masked.py`:
  - [x] Class: `WineMaskedGenerator` (extends `BaseWordCloudGenerator`)
  - [x] Method: `generate()` - generates word cloud with wine bottle mask
  - [x] Applies `transform_format` for proper masking
  - [x] Uses config from YAML: `variants.wine_masked`

- [x] 21. Create `src/generators/country_masked.py`:
  - [x] Class: `CountryMaskedGenerator` (extends `BaseWordCloudGenerator`)
  - [x] Method: `generate(country: str)` - generates word cloud for specific country
  - [x] Method: `generate_all()` - generates for all countries in config
  - [x] Loads country-specific flag masks
  - [x] Applies `ImageColorGenerator` for color mapping
  - [x] Uses config from YAML: `variants.country_masked`

## Phase 5: CLI Interface (10 action items)

- [x] 22. Create `src/cli.py`:
  - [x] Import argparse, generator classes, config
  - [x] Function: `main()` - entry point for CLI
  - [x] Argument: `--variant` (required) - select variant
  - [x] Argument: `--country` (optional) - country for country_masked variant
  - [x] Argument: `--max-words` (optional) - override max words
  - [x] Argument: `--output-dir` (optional) - custom output directory
  - [x] Argument: `--list-variants` (flag) - list available variants
  - [x] Argument: `--list-countries` (flag) - list available countries
  - [x] Function: `list_variants()` - prints variant descriptions
  - [x] Function: `list_countries()` - prints available countries

## Phase 6: Documentation (3 action items)

- [x] 23. Create `PROJECT_PLAN.md` - project plan document
- [x] 24. Create `ACTION_ITEMS.md` - this action items document
- [x] 25. Create `README.md`:
  - [x] Project overview
  - [x] Installation instructions
  - [x] Usage examples
  - [x] CLI reference
  - [x] Configuration options

## Phase 7: Testing (8 action items)

- [x] 26. Test basic_single variant
- [x] 27. Test basic_all variant
- [x] 28. Test wine_masked variant
- [x] 29. Test country_masked variant (single country)
- [x] 30. Test country_masked variant (multiple countries)
- [x] 31. Test --list-variants
- [x] 32. Test --list-countries
- [x] 33. Test custom output directory

## Phase 8: Validation (4 action items)

- [x] 34. Verify virtual environment is properly isolated
- [x] 35. Verify all type hints are present
- [x] 36. Verify error handling for missing files
- [x] 37. Verify error handling for invalid country names

## Total Action Items: 37 (completed: 37, pending: 0)

## Implementation Summary

All action items have been successfully completed. The project structure is fully functional with:

1. ✅ **Complete project structure** with all required directories and files
2. ✅ **Virtual environment** setup and dependencies installed
3. ✅ **YAML configuration** for all settings
4. ✅ **Core modules** (data_loader, text_processor, mask_processor, visualizer)
5. ✅ **Base generator class** with common functionality
6. ✅ **Four generator variants** (basic_single, basic_all, wine_masked, country_masked)
7. ✅ **CLI interface** with full argument parsing
8. ✅ **Documentation** (README.md, PROJECT_PLAN.md, ACTION_ITEMS.md)
9. ✅ **All tests passing** including error handling for missing files

## Generated Output Files

- `output/basic_single.png` - Word cloud from first review
- `output/basic_all.png` - Word cloud from all reviews
- `output/wine_masked.png` - Wine mask word cloud
- `output/us_wine_wordcloud.png` - US country word cloud
- `custom_output/basic_single.png` - Custom output directory test

## Notes

- Other country flags (France, Italy, Spain, Portugal) should follow the naming convention `{country}_flag_mask.png`. To use them, add the corresponding PNG files to the `masks/` directory.

