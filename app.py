import tkinter as tk
from firework import Firework

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

window = tk.Tk()

canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

first_firework = Firework(canvas)

while True:
    first_firework.update()
    window.update()

window.mainloop()
