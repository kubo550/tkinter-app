import math
import time
import random


BIAS = 2


class Firework:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randrange(start=0, stop=self.canvas.winfo_width())
        self.y = 400
        self.speedY = random.random() + BIAS
        self.color = "red"
        self.radius = 5
        self.exploded = False
        self.particles = []

    def draw(self):
        if self.is_exploded():
            return
        self.canvas.create_oval(self.x - self.radius, self.y - self.radius,
                                self.x + self.radius, self.y + self.radius, fill=self.color)

    def update(self):
        self.x += 0
        self.y -= self.speedY
        self.speedY -= 0.01
        self.draw()
        if self.speedY < 0 and not self.is_exploded():
            self.explode()

    def explode(self):
        self.exploded = True
        print('boom')

    def is_exploded(self):
        return self.exploded

    def is_done(self):
        return self.exploded and len(self.particles) == 0
