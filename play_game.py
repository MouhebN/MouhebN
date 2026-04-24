import os
import random

folder = "tictactoe"
# Ensure we have our templates
x_src = os.path.join(folder, "x.png")
o_src = os.path.join(folder, "o.png")
empty_src = os.path.join(folder, "empty.png")

# 1. Reset everything to empty first to start fresh
for i in range(9):
    os.system(f"cp {folder}/empty.png {folder}/cell_{i}.png")
    os.system(f"cp {empty_src} {folder}/cell_{i}.png")

# 2. Pick 6 unique random positions
positions = random.sample(range(9), 6)
x_positions = positions[:3] # First 3 get X
o_positions = positions[3:] # Next 3 get O

# 3. Deploy the marks
for pos in x_positions:
    os.system(f"cp {x_src} {folder}/cell_{pos}.png")

for pos in o_positions:
    os.system(f"cp {o_src} {folder}/cell_{pos}.png")

print(f"Board randomized: X at {x_positions}, O at {o_positions}")