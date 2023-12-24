import pygame


class Board:
    def __init__(self, screen, color='white', left=10, top=10, width=5, height=5, cell_size=30):
        self.color = color
        self.screen = screen
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.cell_size = cell_size

        self.board = [[0] * width for _ in range(height)]

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                pygame.draw.rect(self.screen, self.color,
                                 (self.left + x * self.cell_size,
                                  self.top + y * self.cell_size,
                                  self.cell_size, self.cell_size), 1)
