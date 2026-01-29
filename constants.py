import pygame

# Window
WIDTH, HEIGHT = 800, 900

# Themes
LIGHT_THEME = {
    "bg": (245, 245, 245),
    "grid": (0, 0, 0),
    "text": (0, 0, 0),
    "menu_bg": (180, 210, 240),
    "button": (70, 130, 180),
    "button_hover": (100, 180, 255),
    "highlight": (200, 200, 200)
}
DARK_THEME = {
    "bg": (30, 30, 30),
    "grid": (220, 220, 220),
    "text": (230, 230, 230),
    "menu_bg": (20, 20, 40),
    "button": (90, 90, 140),
    "button_hover": (130, 130, 200),
    "highlight": (80, 80, 80)
}

# Palette (1-based keys)
PALETTE = {i: pygame.Color(*c) for i, c in enumerate([
    (255,0,0),(0,255,0),(0,0,255),(255,255,0),
    (255,0,255),(0,255,255),(255,165,0),(128,0,128),
    (0,128,128),(128,128,0),(255,192,203),(139,69,19),
    (0,100,0),(70,130,180),(210,105,30),(75,0,130)
], start=1)}

# Grid layout
GRID_SIZE, CELL = 10, 50
GRID_X, GRID_Y = 150, 120
