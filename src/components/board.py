import pygame
from utils.colors import WHITE

class Draw:
    def __init__(self, screen):
        self.color = WHITE
        self.screen = screen

    def update(self, from_x, from_y, to_x, to_y):
        pygame.draw.circle(self.screen, self.color, (from_x, from_y), 5)
        pygame.draw.line(self.screen, self.color, (from_x, from_y), (to_x, to_y), 10)
        pygame.draw.circle(self.screen, self.color, (to_x, to_y), 5)


class Board:
    def __init__(self, screen):
        self.line = Draw(screen)
        self.drawing = False
        self.last_pos = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.last_pos = event.pos
            self.drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.drawing = False

    def handle_iteration(self):
        x, y = pygame.mouse.get_pos() 
        if self.drawing:
            last_x, last_y = self.last_pos
            self.line.update(last_x, last_y, x, y)
        self.last_pos = x, y

