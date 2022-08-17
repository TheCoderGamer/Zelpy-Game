import	pygame
from settings import *
from tile import Tile
from player import Player
from debug import Debug

class Level:
    def __init__ (self):
        self.display_surface = pygame.display.get_surface()
        
        # Sprites groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        self.create_map()
        
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, tile in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                
                if tile == "x":
                    Tile((x,y), [self.visible_sprites, self.obstacles_sprites])
                elif tile == "p":
                    self.player = Player((x,y), self.visible_sprites, self.obstacles_sprites)
    def update(self):
        self.visible_sprites.update()
    
    def draw(self):
        self.visible_sprites.draw(self.display_surface)
        Debug(self.player.direction, line = 0)
        