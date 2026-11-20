import random



grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# print(grid)



# grid[0][0] = random.choice([2, 4])
# grid[0][1] = random.choice([2, 4])

# def add_random_tile(grid):
#     row = random.randint(0, 3)
#     col = random.randint(0, 3)
#     grid[row][col] = random.choice([2, 4])
#     return grid

def display_grid(grid):
    for row in grid:
        print(' '.join(str(num) for num in row))



def add_random_tile(grid):
    while True:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if grid[row][col] == 0:
            grid[row][col] = random.choice([2, 4])
            break
    return grid

for _ in range(2):
    grid = add_random_tile(grid)

# display_grid(grid)
# move = input("Enter move (w/a/s/d) or q to quit:").lower()

# if move == 'q':
#     print("Thanks for playing!")

# if move not in ['w', 'a', 's', 'd']:
#     print("Invalid input!")

# print(f"You pressed: {move}")

while True:
    display_grid(grid)

    move = input("Enter move (w/a/s/d) or q to quit: ").lower()

    if move == 'q':
        print("Thanks for playing!")
        break

    if move not in ['w', 'a', 's', 'd']:
        print("Invalid input!")
        continue

    print(f"You pressed: {move}")
