import random
from constants import GRID_SIZE, PALETTE

def generate_level():
    grid = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE//2):
            color = random.choice(list(PALETTE.keys()))
            grid[r][c] = color
            grid[r][GRID_SIZE-1-c] = color
    return grid

def reset_game():
    return generate_level(), [[None]*GRID_SIZE for _ in range(GRID_SIZE)]

print("Testing generate_level")
level, player = reset_game()
print("Success")
