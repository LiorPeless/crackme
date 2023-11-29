import pygame
import random
import time


class Ball:
    def __init__(self, screen):
        '''

        :param screen: pregame screen
        '''
        self.screen = screen
        self.radius = 25
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color
        self.x = 0
        self.y = 0

    def draw(self):
        '''

        :return: Draws the ball by the x and y values
        '''
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        # pygame.display.flip()  # Update the display

    def erase(self):
        '''

        :return: Erase the ball by drawing it with a black color (background color)
        '''
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), self.radius)
        # pygame.display.flip()  # Update the display

    def move(self):
        '''

        :return: sets new values for x and y, draws the ball, wait 1 second, erase it
        '''
        # trying to find a place to print that is empty
        # checking if a place is empty by checking the color of center of new printing area
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
        return color == (0, 0, 0, 255)  # Check if the color is black (0,0,0)

    def _area_is_clear(self):
        return self._is_black_color(self.x, self.y) and self._is_black_color(self.x - self.radius - 2, self.y) and self._is_black_color(self.x + self.radius + 2, self.y) and self._is_black_color(self.x, self.y - self.radius - 2) and self._is_black_color(self.x, self.y + self.radius + 2) and self._is_black_color(self.x + self.radius + 2, self.y + self.radius + 2)and self._is_black_color(self.x - self.radius - 2, self.y - self.radius - 2)and self._is_black_color(self.x + self.radius + 2, self.y - self.radius - 2) and self._is_black_color(self.x - self.radius - 2, self.y + self.radius + 2)



