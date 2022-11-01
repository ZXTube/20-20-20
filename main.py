import win32gui
import win32con
import pygame
import time
import os

pygame.font.init()
pygame.mixer.init()

projectFolder = os.path.dirname(__file__)
resourcesFolder = os.path.join(projectFolder, 'Resources')

FINISHED_SFX = pygame.mixer.Sound(
    os.path.join(resourcesFolder, 'Finished.wav'))
SMALL_FONT = pygame.font.SysFont('comicsans', 100)
BIG_FONT = pygame.font.SysFont('comicsans', 250)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (30, 30, 30)


def draw(timer, timerPos):
    WIN.fill(DARK_GRAY)
    WIN.blit(timer, timerPos)
    pygame.display.update()


def main(timerValue, playSoundEffect, font):
    clock = pygame.time.Clock()

    timer = font.render(str(timerValue), True, LIGHT_GRAY)

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
            break

        draw(timer, timerPos)

    pygame.display.quit()

    if running:
        if playSoundEffect:
            FINISHED_SFX.play()
        return True

    return False


if __name__ == "__main__":
    while True:
        WIN = pygame.display.set_mode((150, 150), pygame.NOFRAME)
        HALF_WIDTH, HALF_HEIGHT = 75, 75
        if not main(3, False, SMALL_FONT):
            time.sleep(1200)
            continue

        WIN = pygame.display.set_mode((0, 0))
        WIDTH, HEIGHT = WIN.get_size()
        HALF_WIDTH, HALF_HEIGHT = WIDTH/2, HEIGHT/2

        win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        main(20, True, BIG_FONT)
        time.sleep(1200)
