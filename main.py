import pygame
import time
import os

pygame.font.init()
pygame.mixer.init()

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = WIN.get_size()
HALF_WIDTH, HALF_HEIGHT = WIDTH/2, HEIGHT/2

projectFolder = os.path.dirname(__file__)
resourcesFolder = os.path.join(projectFolder, 'Resources')

FINISHED_SFX = pygame.mixer.Sound(
    os.path.join(resourcesFolder, 'Finished.wav'))
FONT = pygame.font.SysFont('comicsans', 250)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (30, 30, 30)


def draw(timer, timerPos):
    WIN.fill(DARK_GRAY)
    WIN.blit(timer, timerPos)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    startingTime = time.time()

    timer = FONT.render('22', True, LIGHT_GRAY)
    timerValue = 22

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
        timer = FONT.render(str(timerValue), True, LIGHT_GRAY)
        timerPos[0] = HALF_WIDTH - timer.get_width() / 2

        if timerValue == 0:
            break

        draw(timer, timerPos)

    pygame.display.quit()

    if running:
        FINISHED_SFX.play()


if __name__ == "__main__":
    while True:
        main()
        time.sleep(1200)
