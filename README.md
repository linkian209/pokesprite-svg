# Pokesprite-svg
This utility is designed to convert the sprites from the [PokéSprite](https://github.com/msikma/pokesprite) repository into SVGs.

## Installation
Requires Python 3.10+

`pip install -r requirements.txt`

Also requires checking out [PokéSprite](https://github.com/msikma/pokesprite) into some known directory.

## Usage
```bash
usage: main.py [-h] [-c] [-i INPUT_DIR] [-o OUTPUT_DIR] [-s] directories [directories ...]

This script converts the sprites from the PokeSprite repo into SVG files for better scaling. At least one of "icons", "items-outline", "items", "misc", "pokemon-gen7x", or "pokemon-gen8"
must be passed in.

positional arguments:
  directories           Directories to convert

options:
  -h, --help            show this help message and exit
  -c, --crop            Crop Sprites
  -i INPUT_DIR, --input-dir INPUT_DIR
                        Path to the PokeSprite repo. Default: pokesprite/
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Output directory. Default: build/
  -s, --single-thread   Don't multithread work.
```