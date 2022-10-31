import pygame
import time

pygame.font.init()

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = WIN.get_size()
HALF_WIDTH, HALF_HEIGHT = WIDTH/2, HEIGHT/2

font = pygame.font.SysFont('comicsans', 250)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (30, 30, 30)


def draw(timer, timerPos):
    WIN.fill(DARK_GRAY)
    WIN.blit(timer, timerPos)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    startingTime = time.time()

    timer = font.render('20', True, LIGHT_GRAY)
    timerValue = 20

    halfTimerWidth, halfTimerHeight = timer.get_size()
    halfTimerHeight /= 2
    halfTimerWidth /= 2

    timerPos = [HALF_WIDTH - halfTimerWidth, HALF_HEIGHT - halfTimerHeight]

    draw(timer, timerPos)

    running = True
    while running:
        clock.tick(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        timerValue -= 1
        timer = font.render(str(timerValue), True, LIGHT_GRAY)
        timerPos[0] = HALF_WIDTH - timer.get_width() / 2

        if timerValue == 0:
            running = False

        draw(timer, timerPos)


if __name__ == "__main__":
    main()
