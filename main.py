import pygame
import sys
from constants import WIDTH, HEIGHT, LIGHT_THEME, DARK_THEME, PALETTE, GRID_SIZE, CELL, GRID_X, GRID_Y
from game import reset_game
from ui import (
    draw_menu, draw_grid, draw_palette,
    draw_menu_button, draw_theme_button, get_palette_rects
)

pygame.init()

# Window + fonts
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Малюнок за номерами")
FONT = pygame.font.SysFont(None, 26)
BIG_FONT = pygame.font.SysFont(None, 48)

# Game state
theme = LIGHT_THEME
level, player = reset_game()
selected = 1
menu = True
running = True
clock = pygame.time.Clock()

# Buttons
theme_button = pygame.Rect(WIDTH-60,10,50,50)
menu_button = pygame.Rect(10,10,120,40)

while running:
    screen.fill(theme["bg"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if theme_button.collidepoint(event.pos):
                theme = DARK_THEME if theme == LIGHT_THEME else LIGHT_THEME

            if menu:
                play_btn, exit_btn = draw_menu(screen, theme, BIG_FONT, FONT, theme_button)
                if play_btn.collidepoint(event.pos):
                    menu = False
                    level, player = reset_game()
                elif exit_btn.collidepoint(event.pos):
                    running = False
            else:
                if menu_button.collidepoint(event.pos):
                    menu = True
                else:
                    mx, my = event.pos

                    # palette
                    for rect, num in get_palette_rects(FONT):
                        if rect.collidepoint(mx, my):
                            selected = num
                            break

                    # grid
                    for r in range(GRID_SIZE):
                        for c in range(GRID_SIZE):
                            rect = pygame.Rect(GRID_X+c*CELL, GRID_Y+r*CELL, CELL, CELL)
                            if rect.collidepoint(mx, my):
                                if level[r][c] == selected:
                                    player[r][c] = selected

    if menu:
        draw_menu(screen, theme, BIG_FONT, FONT, theme_button)
    else:
        draw_menu_button(screen, menu_button, theme, FONT)
        draw_theme_button(screen, theme_button, theme, BIG_FONT)
        draw_grid(screen, level, player, selected, theme, FONT)
        draw_palette(screen, selected, theme, FONT)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
