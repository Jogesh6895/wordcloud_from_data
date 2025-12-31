import argparse
import sys
from pathlib import Path
from typing import Optional
from .data_loader import WineDataLoader
from .text_processor import TextProcessor
from .generators import (
    BasicSingleGenerator,
    BasicAllGenerator,
    WineMaskedGenerator,
    CountryMaskedGenerator,
)
from .config import get_config


def list_variants() -> None:
    print("Available variants:")
    print("  basic_single     - Word cloud from first review only")
    print("  basic_all        - Word cloud from ALL reviews with stopwords")
    print("  wine_masked      - Word cloud with wine bottle mask")
    print("  country_masked   - Country-specific masked word clouds")


def list_countries() -> None:
    config = get_config()
    countries = config.variants.get("country_masked", {}).get("countries", [])
    print("Available countries:")
    for country in countries:
        print(f"  {country}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate word clouds from wine reviews"
    )
    parser.add_argument(
        "--variant",
        choices=["basic_single", "basic_all", "wine_masked", "country_masked"],
        help="Word cloud variant to generate",
    )
    parser.add_argument(
        "--country",
        help="Country for country_masked variant (can be comma-separated for multiple)",
    )
    parser.add_argument(
        "--max-words", type=int, help="Override maximum number of words"
    )
    parser.add_argument("--output-dir", help="Custom output directory")
    parser.add_argument(
        "--list-variants", action="store_true", help="List available variants"
    )
    parser.add_argument(
        "--list-countries", action="store_true", help="List available countries"
    )

    args = parser.parse_args()

    if args.list_variants:
        list_variants()
        return

    if args.list_countries:
        list_countries()
        return

    if not args.variant:
        parser.print_help()
        sys.exit(1)

    config = get_config()
    csv_path = config.data.get("csv_path", "data/winemag-data-130k-v2.csv")

    if args.variant == "basic_single":
        generator = BasicSingleGenerator(csv_path)
        wordcloud = generator.generate()
        filename = "basic_single"
    elif args.variant == "basic_all":
        generator = BasicAllGenerator(csv_path)
        wordcloud = generator.generate()
        filename = "basic_all"
    elif args.variant == "wine_masked":
        generator = WineMaskedGenerator(csv_path)
        wordcloud = generator.generate()
        filename = "wine_masked"
    elif args.variant == "country_masked":
        if not args.country:
            print("Error: --country is required for country_masked variant")
            sys.exit(1)

        generator = CountryMaskedGenerator(csv_path)
        countries = [c.strip() for c in args.country.split(",")]

        if len(countries) == 1:
            wordcloud = generator.generate(countries[0])
            filename = f"{countries[0].lower()}_wine_wordcloud"
        else:
            wordclouds = generator.generate_all()
            for country, wc in wordclouds.items():
                output_path = generator.save_output(
                    wc, f"{country.lower()}_wine_wordcloud"
                )
                print(f"Saved word cloud for {country} to: {output_path}")
            return

    if args.output_dir:
        output_format = config.output.get("format", "png")
        output_path = generator.visualizer.save_to_path(
            wordcloud, f"{args.output_dir}/{filename}.{output_format}"
        )
    else:
        output_path = generator.save_output(wordcloud, filename)

    print(f"Saved word cloud to: {output_path}")


if __name__ == "__main__":
    main()
