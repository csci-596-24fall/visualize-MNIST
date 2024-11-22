import numpy as np
import pygame
import cv2
from utils.colors import WHITE
from utils.constant import NN_SIZE, SCREEN_COLOR, SCREEN_DIVIDER

class Draw:
    # TODO: adjust stroke width to be thicker
    STROKE_WIDTH = 4
    def __init__(self, screen):
        self._color = WHITE
        self._screen = screen

    def update(self, from_x, from_y, to_x, to_y):
        pygame.draw.circle(self._screen, self._color, (from_x, from_y), self.STROKE_WIDTH)
        pygame.draw.line(self._screen, self._color, (from_x, from_y), (to_x, to_y), self.STROKE_WIDTH * 2)
        pygame.draw.circle(self._screen, self._color, (to_x, to_y), self.STROKE_WIDTH)



class Board:
    def __init__(self, screen):
        self._screen = screen
        self._line = Draw(screen)
        self._drawing = False
        self._last_pos = None
        self._img_arr = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self._last_pos = event.pos
            self._drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            self._drawing = False

    def handle_iteration(self):
        x, y = pygame.mouse.get_pos() 
        if self._drawing:
            last_x, last_y = self._last_pos
            self._line.update(last_x, last_y, x, y)
            self._save_img_to_array()
        self._last_pos = x, y

    def get_img(self):
        return self._img_arr
 
    def is_updated(self):
        return self._drawing

    def reset(self):
        self._screen.fill(SCREEN_COLOR)

    def _save_img_to_array(self):
        # Get current rgb array
        surface = pygame.display.get_surface()
        rgb = pygame.surfarray.array3d(surface)

        cropper = lambda x: rgb[0:SCREEN_DIVIDER,]
        grayscaler = lambda x: np.dot(x[..., :3], [0.299, 0.587, 0.114])
        resizer = lambda x: cv2.resize(x.astype('float32'), dsize=NN_SIZE.INPUT, interpolation=cv2.INTER_CUBIC)
        clipper = lambda x: np.clip(x, 0, 255)
        normalizer = lambda x: x / 255.0

        res = rgb
        for op in [cropper, resizer, clipper, grayscaler, clipper, normalizer]:
            res = op(res)

        self._img_arr = res.T
