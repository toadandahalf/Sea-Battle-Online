import sys
import pygame
from Classes.Board import Board
from Classes.Button import Button


def init(screen: pygame.Surface):
    image = pygame.image.load("Images/MainScreen3.jpg")
    image = pygame.transform.scale(image, screen.get_size())
    screen.blit(image, (0, 0))
    font = pygame.font.SysFont("Arial", 50)
    text = font.render("Морской бой", True, (50, 50, 175))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    screen.blit(text, text_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Морской бой онлайн")
    init(screen)
    r = Button(screen, 'START', 'white', 200, 200, 100, 120, 'pypypy')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            r.render()
        pygame.display.flip()


if __name__ == "__main__":
    main()
