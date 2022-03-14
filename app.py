import tkinter as tk
import random
import time
from firework import Firework

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

window = tk.Tk()

canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

fireworks = []

while True:
    # draw background
    canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill='black')
    if random.random() < 0.004:
        fireworks.append(Firework(canvas))

    time.sleep(0.0005)

    for f in fireworks:
        f.update()
        if f.is_done():
            fireworks.remove(f)

    window.update()
