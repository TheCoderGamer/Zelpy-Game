import pygame as pg

pg.init()
font = pg.font.SysFont("none", 30)

def Debug(text, x = 10, y = 10, line = None):
    ''' Draw text on the screen'''
    if line != None: y = line * 25 + 5
    
    display_surface = pg.display.get_surface()
    debug_surf = font.render(str(text), True, "White")
    debug_rect = debug_surf.get_rect(topleft = (x, y))
    pg.draw.rect(display_surface, "Black", debug_rect)
    display_surface.blit(debug_surf, debug_rect)