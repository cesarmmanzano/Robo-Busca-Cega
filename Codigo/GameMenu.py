import pygame
from pygame.locals import *

import GameWindow
import Commons

import easygui

def MainMenu():

    wasButtonClicked = False
    isMenuRunning = True
    gameWindow = pygame.display.set_mode((int(Commons.GAME_WIDTH / 2), int(Commons.GAME_WIDTH / 2)))
    pygame.display.set_caption(Commons.GAME_TITLE)

    button_1 = pygame.Rect(100, 150, 200, 50)
    button_2 = pygame.Rect(100, 230, 200, 50)
    button_3 = pygame.Rect(100, 310, 200, 50)

    while isMenuRunning:     
            
        gameWindow.fill(Commons.LIGHT_BLACK)

        # binding click events
        x, y = pygame.mouse.get_pos()
        if button_1.collidepoint((x, y)) and wasButtonClicked:
                Commons.FILE_NAME = easygui.fileopenbox()                
                wasButtonClicked = False
                
        if button_2.collidepoint((x, y)) and wasButtonClicked:
            if Commons.FILE_NAME != None:
                OnMenuButtonClick(gameWindow, Commons.A_ALGORITHM)
            else:
                wasButtonClicked = False
                
        if button_3.collidepoint((x, y)) and wasButtonClicked:
                if Commons.FILE_NAME != None:
                    OnMenuButtonClick(gameWindow, Commons.BLIND_SEARCH_ALGORITHM)
                else:
                    wasButtonClicked = False

        # Mouse hover colors
        if button_1.collidepoint((x, y)) and not wasButtonClicked:
            pygame.draw.rect(gameWindow, Commons.LIGHT_ORANGE, button_1)
        else:
            pygame.draw.rect(gameWindow, Commons.ORANGE, button_1)

        if button_2.collidepoint((x, y)) and not wasButtonClicked:
            pygame.draw.rect(gameWindow, Commons.LIGHT_ORANGE, button_2)
        else:
            pygame.draw.rect(gameWindow, Commons.ORANGE, button_2)

        if button_3.collidepoint((x, y)) and not wasButtonClicked:
            pygame.draw.rect(gameWindow, Commons.LIGHT_ORANGE, button_3)
        else:
            pygame.draw.rect(gameWindow, Commons.ORANGE, button_3)

        RenderTexts(gameWindow)

        # Possible events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isMenuRunning = False
                Commons.QuitGame()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    isMenuRunning = False
                    Commons.QuitGame()

            if event.type == MOUSEBUTTONUP:
                if event.button == 1 and (button_1.collidepoint((x, y)) or button_2.collidepoint((x, y)) or button_3.collidepoint((x, y))):
                    wasButtonClicked = True                                  

# ==================== #

def OnMenuButtonClick(window, algorithm):
    Commons.CurrentAlgorithm = algorithm
    pygame.quit()
    window = pygame.display.set_mode((Commons.GAME_WIDTH, Commons.GAME_WIDTH))
    window.fill(Commons.LIGHT_BLACK)
    pygame.display.set_caption(Commons.GAME_TITLE + " - " + Commons.CurrentAlgorithm)
    GameWindow.MainMapScreen(window)

# ==================== #

def RenderTexts(window):
    Commons.RenderText(window, Commons.CHOOSE_A_FILE, (110, 165), 30, Commons.BLACK)
    Commons.RenderText(window, Commons.A_ALGORITHM, (140, 245), 30, Commons.BLACK)
    Commons.RenderText(window, Commons.BUTTON_2_TEXT, (140, 325), 30, Commons.BLACK)
    Commons.RenderText(window, Commons.NAMES_TITLE, (5, 5))
    Commons.RenderText(window, Commons.INSTRUCTIONS_TITLE, (5, 35))
    Commons.RenderText(window, Commons.INSTRUCTIONS_TITLE0_MENU, (5, 55))
    Commons.RenderText(window, Commons.INSTRUCTIONS_TITLE1_MENU, (5, 75))
    Commons.RenderText(window, Commons.INSTRUCTIONS_TITLE2_MENU, (5, 95))
    Commons.RenderText(window, Commons.INSTRUCTIONS_TITLE3_MENU, (5, 115))
    pygame.display.update()

# ==================== #

MainMenu()