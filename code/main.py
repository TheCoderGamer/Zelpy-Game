import pygame as pg
import sys
from settings import *
from debug import Debug
from level import Level


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGTH))
        self.clock = pg.time.Clock()
        self.running = True
        pg.display.set_caption(TITLE)
        
        self.level = Level()
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                print("Quitting...")
                pg.quit()
                sys.exit()

    def update(self):
        self.level.update()

    def draw(self):
        self.screen.fill("black")
        self.level.draw()
        
    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            Debug("FPS: " + str(int(self.clock.get_fps())), x = WIDTH - 90)
            pg.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    g = Game()
    g.run()