import tkinter as tk
import time

def toggle_cell(event):
    x, y = event.x // size_cell, event.y // size_cell
    if 0 <= x < cols and 0 <= y < rows:
        grid[y][x] = not grid[y][x]
        color = "black" if grid[y][x] else "white"
        canvas.itemconfig(rects[y][x], fill=color)

def get_neighbors(x, y):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx]:
            count += 1
    return count

def next_generation():
    global grid
    new_grid = [[False] * cols for _ in range(rows)]
    for y in range(rows):
        for x in range(cols):
            live_neighbors = get_neighbors(x, y)
            if grid[y][x]:
                new_grid[y][x] = live_neighbors in [2, 3]
            else:
                new_grid[y][x] = live_neighbors == 3
    grid = new_grid
    update_canvas()

def update_canvas():
    for y in range(rows):
        for x in range(cols):
            color = "black" if grid[y][x] else "white"
            canvas.itemconfig(rects[y][x], fill=color)

def start_game():
    def game_loop():
        next_generation()
        update_canvas()
        root.after(100, game_loop)
    game_loop()

rows, cols = 30, 30
size_cell = 20

grid = [[False] * cols for _ in range(rows)]

root = tk.Tk()
root.title("Game of Life")

canvas = tk.Canvas(root, width=cols * size_cell, height=rows * size_cell)
canvas.pack()

rects = [[canvas.create_rectangle(j * size_cell, i * size_cell, (j + 1) * size_cell, (i + 1) * size_cell, fill="white", outline="black") for j in range(cols)] for i in range(rows)]

canvas.bind("<Button-1>", toggle_cell)

start_button = tk.Button(root, text="Start", command=start_game)
start_button.config(width=30, height=5)
start_button.pack()

root.mainloop()
