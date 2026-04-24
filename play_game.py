import os
import random

# Simple logic to find an empty cell and place an 'X'
cells = [f"tictactoe/cell_{i}.png" for i in range(9)]
empty_cells = [i for i, cell in enumerate(cells) if "empty.png" in cell]

if empty_cells:
    move = random.choice(empty_cells)
    # In a real scenario, you'd use logic to check clicks,
    # but for a start, we automate the 'X' move.
    os.system(f"cp tictactoe/x.png tictactoe/cell_{move}.png")
    print(f"Made a move at {move}")
else:
    # Reset game if full
    for i in range(9):
        os.system(f"cp tictactoe/empty.png tictactoe/cell_{i}.png")
    print("Game Reset")