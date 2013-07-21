#!/usr/bin/env python

import threading
import pygame

stop_event = threading.Event()


def init_screen():
    (width, height) = pygame.display.list_modes(0, pygame.FULLSCREEN)[0]
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("Keyboard Fun!")
    return screen, width, height


def main():
    pygame.init()
    clock = pygame.time.Clock()

    fps = 160
    y = 0
    dir = 1
    running = 1
    linecolor = 255, 0, 0
    bgcolor = 250,250,250
    dirty_rects = []

    # Set full-screen display
    screen, width, height = init_screen()

    # Drawing canvas
    canvas = pygame.Surface(screen.get_size())
    canvas = canvas.convert()

    # Text object
    font = pygame.font.Font(None, 36)
    text = font.render("Hello world!", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = canvas.get_rect().centerx

    # Event loop
    while not stop_event.isSet():
        tick = clock.tick(fps)
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop_event.set()
                    print "pygame.QUIT" + stop_event.isSet()
                elif event.type == pygame.KEYDOWN:
                    parse_key(event.key)

            # do calculations
            y += dir
            if y == 0 or y == height-1: dir *= -1

            # draw entities
            canvas.fill(bgcolor)
            pygame.draw.line(canvas, linecolor, (0, y), (width-1, y))
            canvas.blit(text, (textpos[0],textpos[1]+y))

            # flip to display
            screen.blit(canvas, (0,0))
            pygame.display.flip()
            #pygame.display.update(dirty_rects)

        except KeyboardInterrupt:
            stop_event.set()
    pygame.quit()


def parse_key(key):
    pressed = pygame.key.get_pressed()

    if (pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL]) and \
            pressed[pygame.K_c]:
        stop_event.set()


if __name__=='__main__':
    main()

