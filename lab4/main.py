#!/usr/bin/python3

import pygame
import cairosvg
import io
from PIL import Image

FPS = 30

screen = None
image = None

def loadImage(fname: str) -> int:
    '''
    This function loads svg into image
    @param fname path to svg
    @return Exit code
    '''
    global image

    out = cairosvg.svg2png(url=fname)
    svgBuffer = io.BytesIO()
    svgBuffer.write(out)
    image = Image.open(svgBuffer)

    return 0


def drawSvg() -> int:
    '''
    This function draws svg in several steps.
    First it loads svg, then converts to bitmap
    and then push it to screen
    @return Exit code
    '''
    global WIDTH, HEIGHT, screen, image
    
    surface = pygame.Surface((WIDTH, HEIGHT))
    pixelArray = pygame.PixelArray(surface)

    for x in range(image.width):
        for y in range(image.height):
            pixelArray[x, y] = image.getpixel((x, y))
    newSurf = pixelArray.make_surface()

    screen.blit(newSurf, (0, 0))
    pygame.display.update()

    return 0


def init() -> int:
    '''
    Init function.
    @return Exit code
    '''
    global screen, WIDTH, HEIGHT

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    return 0


def mainloop() -> int:
    '''
    Mainloop function.
    @return Exit code
    '''
    
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    return 0


def clean() -> int:
    '''
    Clean up function.
    @return Exit code
    '''
    
    pygame.quit()


def main(fname: str) -> int:
    '''
    The main function.
    @param fname filename of svg
    @return Exit code
    '''
    global HEIGHT, WIDTH

    loadImage(fname)

    HEIGHT, WIDTH = image.height, image.width
    
    init()

    drawSvg()

    mainloop()

    clean()
    return 0


if (__name__ == "__main__"):
    print("Usage: main(`filename`).")
