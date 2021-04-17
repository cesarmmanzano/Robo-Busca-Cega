import pygame
import sys
import math
from queue import PriorityQueue
from pygame.locals import *

import Busca
import Commons


def MainMenu():

    click = False
    isMenuRunning = True
    gameWindow = pygame.display.set_mode(
        (int(Commons.GAME_WIDTH / 2), int(Commons.GAME_WIDTH / 2)))
    pygame.display.set_caption(Commons.GAME_TITLE)

    while isMenuRunning:

        # fill menu window and create buttons
        gameWindow.fill(Commons.LIGHT_BLACK)
        button_1 = pygame.Rect(100, 100, 200, 50)
        button_2 = pygame.Rect(100, 200, 200, 50)

        # binding click events
        x, y = pygame.mouse.get_pos()
        if button_1.collidepoint((x, y)):
            if click:
                OnMenuButtonClick(
                    gameWindow, Commons.A_ALGORITHM, isMenuRunning)
        if button_2.collidepoint((x, y)):
            if click:
                OnMenuButtonClick(
                    gameWindow, Commons.BLIND_SEARCH_ALGORITHM, isMenuRunning)

        pygame.font.init()
        myfont = pygame.font.SysFont(Commons.HELVETICA_NEUE_FONT, 30)
        nameFont = pygame.font.SysFont(Commons.HELVETICA_NEUE_FONT, 15)

        # Mouse hover colors
        if button_1.collidepoint((x, y)) and not click:
            pygame.draw.rect(gameWindow, Commons.LIGHT_ORANGE, button_1)
        else:
            pygame.draw.rect(gameWindow, Commons.ORANGE, button_1)

        if button_2.collidepoint((x, y)) and not click:
            pygame.draw.rect(gameWindow, Commons.LIGHT_ORANGE, button_2)
        else:
            pygame.draw.rect(gameWindow, Commons.ORANGE, button_2)

        # render button text
        aStarText = myfont.render(Commons.A_ALGORITHM, True, (0, 0, 0))
        bSearchText = myfont.render('Blind Search', True, (0, 0, 0))
        gameWindow.blit(aStarText, (140, 115))
        gameWindow.blit(bSearchText, (140, 215))
        names = nameFont.render(Commons.NAMES_TITLE, True, (250, 250, 250))
        gameWindow.blit(names, (5, 5))
        pygame.display.update()

        # Possible events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isMenuRunning = False
                Commons.QuitGame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    isMenuRunning = False
                    Commons.QuitGame()

            if event.type == MOUSEBUTTONUP:
                if event.button == 1 and button_1.collidepoint((x, y)) or button_2.collidepoint((x, y)):
                    click = True

# ==================== #


def OnMenuButtonClick(window, algorithm, isMenuRunning):
    currentAlgorithm = algorithm
    isMenuRunning = False
    pygame.quit()
    window = pygame.display.set_mode((Commons.GAME_WIDTH, Commons.GAME_WIDTH))
    pygame.display.set_caption(Commons.GAME_TITLE + " - " + algorithm)
    Busca.MainMapScreen(window)

# ==================== #


MainMenu()
