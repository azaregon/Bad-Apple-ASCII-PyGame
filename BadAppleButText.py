import pygame
from textify import Module
import os

pygame.init()



SIZE = WIDTH, HEIGHT = (1024, 720)
FPS = 30
FILEDIR = os.path.dirname(os.path.abspath(__file__))
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()

pygame.display.set_caption('Bad Apple Text')


def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.



font = pygame.font.SysFont('Cascadia Mono', 14)


f = [i for i in range(0, 6569)]
'''for i, x in enumerate(f):
    f[i] = str(x) + '.png'
'''
folder = 'BA64'
i = 0

maxFrames = 6569

os.startfile(f'{FILEDIR}/Touhou - Bad Apple.mp4')

while True:

    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()




    fn = str(i) + '.png'

    g = Module().textify(f'{FILEDIR}/{folder}/{fn}').res



    screen.fill(pygame.Color('black'))
    print(i)
    blit_text(screen, g, (20, 20), font)
    if i < maxFrames:
        i += 1

    pygame.display.update()
