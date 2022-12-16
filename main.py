from multiprocessing import Pool
from typing import List
from util.funcs import get_files_in_dir, convert_sprite
import argparse
import os
import tqdm


def main(directories: List[str], input_dir: str, output_dir: str, crop=False, single_thread=False) -> None:
    for dir in directories:
        jobs = [(sprite, crop, output_dir) for sprite in get_files_in_dir(directory=os.path.join(input_dir,dir), file_extension=".png")]
        if not single_thread:
            with Pool(os.cpu_count()) as pool:
                for _ in tqdm.tqdm(pool.imap(convert_sprite, jobs), total=len(jobs)):
                    pass
        else:
            for job in tqdm.tqdm(jobs):
                convert_sprite(job)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='''
                        This script converts the sprites from the PokeSprite repo into SVG files for better scaling.
                        At least one of "icons", "items-outline", "items", "misc", "pokemon-gen7x", or "pokemon-gen8" must be passed in.
                    '''
    )
    parser.add_argument("-c", "--crop", action="store_true", help="Crop Sprites")
    parser.add_argument('-i', "--input-dir", type=str, default="pokesprite", help="Path to the PokeSprite repo. Default: pokesprite/")
    parser.add_argument('-o', "--output-dir", type=str, default="build", help="Output directory. Default: build/")
    parser.add_argument('-s', '--single-thread', action="store_true", help="Don't multithread work.")
    parser.add_argument("directories", type=str, nargs="+", help="Directories to convert")
    args = parser.parse_args()
    main(**vars(args))