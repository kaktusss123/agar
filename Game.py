import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
CAPTION = 'Eat da balls'


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

        self.run = True

    def mainloop(self):
        while self.run:
            self.handle_events()

            self.screen.fill((255, 255, 255))
            pygame.display.flip()

            self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False


if __name__ == '__main__':
    g = Game()
    g.mainloop()
