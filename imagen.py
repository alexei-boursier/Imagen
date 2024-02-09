# -*- coding: utf-8 -*-
"""
Imagen : Outil de génération d'oeuvre d'art.

Cet outil utilise OpenSimplex2.

Attention : cet outil nécessite :
 - Python 3.12
 - Numpy
 - PIL (Pillow)

De plus cet outil utilise la librairie OpenSimplex2,
qui ne fonctionne que sous Linux malheuresement.
"""
import ctypes
import time
from typing import Callable

# from IPython.core.display_functions import display
import numpy as np
from PIL import Image
from pyopensimplex2.api import Context, free, noise2, open_simplex2f, shutdown

# %% Load image
source = Image.open("source.jpg")
data = source.load()
width, height = source.size

pixels = [[data[x, y] for x in range(width)] for y in range(height)]

# %% Constants
FACTOR = 0.005
# %% Noise

contexts = {}


def make_noise(seed: int, x: float, y: float) -> float:
    """
    Make noise.

    Arguments
    ---------
    seed : int
        Seed for random number generator.
    x : float
        X position.
    y : float
        Y position.

    Returns
    -------
    float
        Number between 0 and 1.

    """
    if seed not in contexts:
        contexts[seed] = ctypes.pointer(Context())
        open_simplex2f(seed, ctypes.pointer(contexts[seed]))

    ctx = contexts[seed]

    result = (float(noise2(ctx, x * FACTOR, y * FACTOR)) + 1) / 2

    return result


# %% Image processor
def make_image(
    pixels: list[list[tuple[int, int, int]]],
    seed: int,
    op: Callable[[int, float], int],
    to: tuple[bool, bool, bool],
) -> Image.Image:
    """
    Make an image.

    Parameters
    ----------
    pixels : list[list[tuple[int, int, int]]]
        Original image pixels.
    seed : int
        Seed to use.
    op: Callable[[int, float], int]
        Takes a pixel and a noise, returns a new pixel.
    to: tuple[bool, bool, bool]
        Colors to apply op to (R,G,B).

    Returns
    -------
    None.

    """
    new_image = [[None for _ in range(len(pixels[0]))] for _ in range(len(pixels))]

    ctx = ctypes.pointer(Context())
    open_simplex2f(seed, ctypes.pointer(ctx))

    for y, row in enumerate(pixels):
        if y % 100 == 0:
            print(f"{y}/{len(pixels)}")
        for x, pixel in enumerate(row):
            noise = make_noise(seed, x, y)

            new_pixel = (
                op(pixel[0], noise) if to[0] else pixel[0],
                op(pixel[1], noise) if to[1] else pixel[1],
                op(pixel[2], noise) if to[2] else pixel[2],
            )

            new_image[y][x] = new_pixel

    return Image.fromarray(np.asarray(new_image, dtype=np.uint8))


# %% Images
images = []

images.append(
    make_image(
        pixels,
        int(time.time()),
        lambda pixel, noise: pixel + noise * 100,
        (False, False, False),
    )
)
images.append(
    make_image(
        pixels,
        int(time.time() + 1),
        lambda pixel, noise: pixel + noise * 100,
        (True, False, False),
    )
)
images.append(
    make_image(
        pixels,
        int(time.time() + 2),
        lambda pixel, noise: pixel + noise * 100,
        (False, True, False),
    )
)
images.append(
    make_image(
        pixels,
        int(time.time() + 3),
        lambda pixel, noise: pixel + noise * 100,
        (False, False, True),
    )
)
images.append(
    make_image(
        pixels,
        int(time.time() + 4),
        lambda pixel, noise: pixel + noise * 100,
        (True, True, False),
    )
)
images.append(
    make_image(
        pixels,
        int(time.time() + 5),
        lambda pixel, noise: pixel + noise * 100,
        (False, True, True),
    )
)
images.append(
    make_image(
        pixels,
        int(time.time() + 6),
        lambda pixel, noise: pixel + noise * 100,
        (True, False, True),
    )
)
images.append(
    make_image(
        pixels,
        int(time.time() + 7),
        lambda pixel, noise: pixel + noise * 100,
        (True, True, True),
    )
)
images.append(
    make_image(
        pixels,
        int(time.time()),
        lambda pixel, noise: (255 - pixel) + noise * 100,
        (True, True, True),
    )
)

# %% Tile
final = Image.new("RGB", (width * 3, height * 3), (255, 0, 255))

for y in range(3):
    for x in range(3):
        final.paste(images[(x * 3) + y], (width * x, height * y))

display(final)

final.save("result.png", "PNG")

# %% Cleanup
for ctx in contexts.values():
    free(ctx)
contexts.clear()
shutdown()
