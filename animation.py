import tkinter as tk
import random
import time
from firework import Firework

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400


class Animation:
    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(
            self.window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack()
        self.fireworks = []

    def animate(self):
        self.canvas.create_rectangle(
            0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill='black')
        if random.random() < 0.004:
            self.fireworks.append(Firework(self.canvas))

        time.sleep(0.0005)

        for f in self.fireworks:
            f.update()
            if f.is_done():
                self.fireworks.remove(f)

        self.window.update()
