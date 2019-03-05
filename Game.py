import pygame

from Ball import Ball, TexturedBall

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
COLOR_WHITE = 255, 255, 255
COLOR_BLACK = 0, 0, 0
CAPTION = 'AGAR'
MAX_SPEED = 4

COLOR_DARK_BLUE = 0, 34, 56

BALL_COLOR = 255, 66, 82
BALL_RADIUS = 30


class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

        self.balls_list = []

        self.run = True
        self.append = False

    def mainloop(self):
        while self.run:
            self.handle_events()

            self.screen.fill(COLOR_DARK_BLUE)

            # self.test_ball.draw(self.screen)
            # self.test_ball.move(SPEED)
            if self.append:
                self.balls_list.append(
                    TexturedBall(pygame.image.load('./res/ball_40.png'), SCREEN_WIDTH, SCREEN_HEIGHT, MAX_SPEED))

            for ball in self.balls_list:
                ball.draw(self.screen)
                ball.move()

            pygame.display.flip()

            self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    self.append = True
            elif event.type == pygame.KEYUP:
                if event.key == 32:
                    self.append = False


if __name__ == '__main__':
    g = Game()
    g.mainloop()
