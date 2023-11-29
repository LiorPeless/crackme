import pygame
import random
import time
from multiprocessing import Semaphore

class Ball:
    def __init__(self, screen, semaphore):
        self.screen = screen
        self.semaphore = semaphore
        self.radius = 25
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.x = 0
        self.y = 0

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def erase(self):
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), self.radius)

    def move(self):
        with self.semaphore:
            while True:
                self.x = random.randint(self.radius + 3, self.screen.get_width() - self.radius - 3)
                self.y = random.randint(self.radius + 3, self.screen.get_height() - self.radius - 3)
                if self._area_is_clear():
                    break
            self.draw()
        time.sleep(1)
        self.erase()

    def _is_black_color(self, x, y):
        color = self.screen.get_at((x, y))
        return color == (0, 0, 0, 255)

    def _area_is_clear(self):
        return self._is_black_color(self.x, self.y) and self._is_black_color(self.x - self.radius - 2, self.y) \
               and self._is_black_color(self.x + self.radius + 2, self.y) \
               and self._is_black_color(self.x, self.y - self.radius - 2) \
               and self._is_black_color(self.x, self.y + self.radius + 2) \
               and self._is_black_color(self.x + self.radius + 2, self.y + self.radius + 2) \
               and self._is_black_color(self.x - self.radius - 2, self.y - self.radius - 2) \
               and self._is_black_color(self.x + self.radius + 2, self.y - self.radius - 2) \
               and self._is_black_color(self.x - self.radius - 2, self.y + self.radius + 2)
