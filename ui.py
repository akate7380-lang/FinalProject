import pygame
from constants import PALETTE, GRID_SIZE, CELL, GRID_X, GRID_Y, LIGHT_THEME

def draw_theme_button(screen, theme_button, theme, BIG_FONT):
    pygame.draw.rect(screen, theme["button"], theme_button, border_radius=8)
    icon = "🌙" if theme == LIGHT_THEME else "🌞"
    screen.blit(BIG_FONT.render(icon, True, theme["text"]),
                (theme_button.x+8, theme_button.y+5))

def draw_menu_button(screen, menu_button, theme, FONT):
    pygame.draw.rect(screen, theme["button"], menu_button, border_radius=8)
    screen.blit(FONT.render("← Меню", True, theme["text"]),
                (menu_button.x+15, menu_button.y+10))

def draw_menu(screen, theme, BIG_FONT, FONT, theme_button):
    screen.fill(theme["menu_bg"])
    screen.blit(BIG_FONT.render("Малюнок за номерами", True, theme["text"]), (220,120))
    play_btn = pygame.Rect(300,350,200,70)
    exit_btn = pygame.Rect(300,450,200,70)
    mouse = pygame.mouse.get_pos()

    for btn, txt in [(play_btn,"ГРАТИ"), (exit_btn,"ВИЙТИ")]:
        color = theme["button_hover"] if btn.collidepoint(mouse) else theme["button"]
        pygame.draw.rect(screen, color, btn, border_radius=10)
        screen.blit(
            BIG_FONT.render(txt, True, theme["text"]),
            (btn.x+(btn.width-BIG_FONT.size(txt)[0])//2,
             btn.y+(btn.height-BIG_FONT.size(txt)[1])//2)
        )

    draw_theme_button(screen, theme_button, theme, BIG_FONT)
    return play_btn, exit_btn

def draw_grid(screen, level, player, selected, theme, FONT):
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            rect = pygame.Rect(GRID_X+c*CELL, GRID_Y+r*CELL, CELL, CELL)

            if level[r][c] == selected and not player[r][c]:
                pygame.draw.rect(screen, theme["highlight"], rect)

            pygame.draw.rect(screen, theme["grid"], rect, 2)

            if player[r][c]:
                pygame.draw.rect(screen, PALETTE[player[r][c]], rect)
            else:
                screen.blit(
                    FONT.render(str(level[r][c]), True, theme["text"]),
                    (rect.x+16, rect.y+14)
                )

def get_palette_rects(FONT):
    rows, size, margin = 2, 50, 10
    cols = (len(PALETTE)+rows-1)//rows
    start_x = GRID_X + (GRID_SIZE*CELL - (cols*size + (cols-1)*margin))//2
    start_y = GRID_Y + GRID_SIZE*CELL + 20

    rects = []
    for i, num in enumerate(PALETTE):
        rect = pygame.Rect(
            start_x+(i%cols)*(size+margin),
            start_y+(i//cols)*(size+margin),
            size, size
        )
        rects.append((rect, num))
    return rects

def draw_palette(screen, selected, theme, FONT):
    rows, size, margin = 2, 50, 10
    cols = (len(PALETTE)+rows-1)//rows
    start_x = GRID_X + (GRID_SIZE*CELL - (cols*size + (cols-1)*margin))//2
    start_y = GRID_Y + GRID_SIZE*CELL + 20

    for i, num in enumerate(PALETTE):
        rect = pygame.Rect(
            start_x+(i%cols)*(size+margin),
            start_y+(i//cols)*(size+margin),
            size, size
        )
        pygame.draw.rect(screen, PALETTE[num], rect)

        if num == selected:
            pygame.draw.rect(screen, theme["grid"], rect, 4)

        screen.blit(FONT.render(str(num), True, (0,0,0)),
                    (rect.x+17, rect.y+15))
