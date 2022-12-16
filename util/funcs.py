from typing import List, Tuple
from PIL import Image
import errno
import os
import svg


def convert_sprite_to_svg(sprite: str, crop_sprite: bool) -> svg.SVG:
    with Image.open(sprite) as sprite:
        sprite = sprite.convert("RGBA")
        width, height = sprite.size
        left = -1
        right = -1
        top = -1
        bottom = -1
        pixels = [[None for h in range(height)] for w in range(width)]

        for w in range(width):
            for h in range(height):
                try:
                    r, g, b, a = sprite.getpixel((w, h))
                except:
                    print(sprite)
                    raise

                pixels[w][h] = f"rgba({r}, {g}, {b}, {a})"

                # Update bounding boxes
                if a == 0:
                    continue

                if left == -1:
                    left = w
                if top == -1:
                    top = h

                if w < left:
                    left = w
                if w > right:
                    right = w
                if h < top:
                    top = h
                if h > bottom:
                    bottom = h

        if not crop_sprite:
            left = 0
            top = 0
            right = width-1
            bottom = height-1

        elements = []
        for w in range(left, right+1):
            elements.append([])
            for h in range(top, bottom+1):
                elements[w-left].append(svg.Rect(
                    x=w-left, y=h-top, width=1, height=1, fill=pixels[w][h],
                    shape_rendering="crispEdges"
                ))
        
        return svg.SVG(viewBox=svg.ViewBoxSpec(0, 0, right-left+1, bottom-top+1),
            preserveAspectRatio=svg.PreserveAspectRatio('xMinYmin'), elements=elements
        )

def convert_sprite(args: Tuple[str, bool, str]) -> None:
    sprite, crop, out_dir = args
    svg = convert_sprite_to_svg(sprite, crop)
    dir, file = os.path.split(sprite)
    dir = os.path.join(out_dir, dir)
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    outfile = os.path.join(dir, os.path.splitext(file)[0] + '.svg')
    with open(outfile, "w") as f:
        f.write(svg.as_str())


def get_files_in_dir(directory: str, file_extension: str) -> List[str]:
    retval = []
    for item in os.listdir(directory):
        if os.path.splitext(item)[-1] == file_extension:
            retval.append(os.path.join(directory, item))
        elif os.path.isdir(os.path.join(directory, item)):
            retval += get_files_in_dir(os.path.join(directory, item), file_extension)
        else:
            continue
    return retval
