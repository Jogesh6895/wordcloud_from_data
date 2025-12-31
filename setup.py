from setuptools import setup, find_packages

setup(
    name="wordcloud_from_data",
    version="0.1.0",
    description="Modular package for generating word clouds from wine reviews",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "Pillow>=8.3.0",
        "wordcloud>=1.8.0",
        "matplotlib>=3.4.0",
        "PyYAML>=5.4.0",
    ],
    python_requires=">=3.7",
)
