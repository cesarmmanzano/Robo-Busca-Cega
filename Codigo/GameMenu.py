import pygame
from pygame.locals import *

import Busca
import Commons


def MainMenu():

    click = False
    isMenuRunning = True
    gameWindow = pygame.display.set_mode((int(Commons.GAME_WIDTH / 2), int(Commons.GAME_WIDTH / 2)))
    pygame.display.set_caption(Commons.GAME_TITLE)
    
    button_1 = pygame.Rect(100, 150, 200, 50)
    button_2 = pygame.Rect(100, 250, 200, 50)
    
    while isMenuRunning:

        gameWindow.fill(Commons.LIGHT_BLACK)        

        # binding click events
        x, y = pygame.mouse.get_pos()
        if button_1.collidepoint((x, y)):
            if click:
                OnMenuButtonClick(gameWindow, Commons.A_ALGORITHM)
        if button_2.collidepoint((x, y)):
            if click:
                OnMenuButtonClick(gameWindow, Commons.BLIND_SEARCH_ALGORITHM)               

        # Mouse hover colors
        if button_1.collidepoint((x, y)) and not click:
            pygame.draw.rect(gameWindow, Commons.LIGHT_ORANGE, button_1)
        else:
            pygame.draw.rect(gameWindow, Commons.ORANGE, button_1)

        if button_2.collidepoint((x, y)) and not click:
            pygame.draw.rect(gameWindow, Commons.LIGHT_ORANGE, button_2)
        else:
            pygame.draw.rect(gameWindow, Commons.ORANGE, button_2)
          
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
                if event.button == 1 and button_1.collidepoint((x, y)) or button_2.collidepoint((x, y)):
                    click = True

# ==================== #


def OnMenuButtonClick(window, algorithm):
    Commons.currentAlgorithm = algorithm
    pygame.quit()
    window = pygame.display.set_mode((Commons.GAME_WIDTH, Commons.GAME_WIDTH))
    pygame.display.set_caption(Commons.GAME_TITLE + " - " + Commons.currentAlgorithm)
    Busca.MainMapScreen(window)

# ==================== #

def RenderTexts(window):
    pygame.font.init() 
    myfont = pygame.font.SysFont(Commons.HELVETICA_NEUE_FONT, 30)
    nameFont = pygame.font.SysFont(Commons.HELVETICA_NEUE_FONT, 15)
    aStarText = myfont.render(Commons.A_ALGORITHM, True, (0, 0, 0))
    bSearchText = myfont.render('Blind Search', True, (0, 0, 0))
    window.blit(aStarText, (140, 165))
    window.blit(bSearchText, (140, 265))
    names = nameFont.render(Commons.NAMES_TITLE, True, (250, 250, 250))
    window.blit(names, (5, 5))
    instructions = nameFont.render(Commons.INSTRUCTIONS_TITLE, True, (250, 250, 250))
    window.blit(instructions, (5, 35))
    instructions1 = nameFont.render(Commons.INSTRUCTIONS_TITLE1_MENU, True, (250, 250, 250))
    window.blit(instructions1, (5, 55))
    instructions2 = nameFont.render(Commons.INSTRUCTIONS_TITLE2_MENU, True, (250, 250, 250))
    window.blit(instructions2, (5, 75))
    instructions3 = nameFont.render(Commons.INSTRUCTIONS_TITLE3_MENU, True, (250, 250, 250))
    window.blit(instructions3, (5, 95))
    pygame.display.update()
    
# ==================== #


MainMenu()
