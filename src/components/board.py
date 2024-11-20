import pygame
import cv2
from utils.colors import WHITE
from utils.constant import NN_SIZE, SCREEN_DIVIDER, SCREEN_HEIGHT, SCREEN_WIDTH

class Draw:
    STROKE_WIDTH = 10
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


    def _save_img_to_array(self):
        # Get array from drawing
        string_image = pygame.image.tostring(self._screen, 'RGB')
        surface = pygame.image.fromstring(string_image, (SCREEN_WIDTH, SCREEN_HEIGHT), 'RGB')
        temp_arr = pygame.surfarray.array2d(surface)

        # Crop the board part only
        cropped = temp_arr[0:SCREEN_DIVIDER,]
        # Make it smaller
        resized = cv2.resize(cropped.astype('float32'), dsize=NN_SIZE.INPUT, interpolation=cv2.INTER_AREA)
        # grayscale
        grayed = (resized > 0).astype(int)

        self._img_arr = grayed.T
