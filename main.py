import copy
import time

import pygame, sys, bird, game_manager, player, Neural_Net, population, generation
from PIL import Image

def getMaxVal(val_list):
    ans = 0
    for val in val_list:
        ans = max(ans, val)
    return ans

def getMaxIndex(val_list):
    return val_list.index(getMaxVal(val_list))

def getMax(val_list):
    return val_list[getMaxIndex(val_list)]

w = 780
h = 480

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("FLAPPY BIRD")
my_font = pygame.font.SysFont('Comic Sans MS', 30)


red = (255, 0, 0, 0)
blue = (0, 0, 255, 0)
green = (0, 255, 255, 0)
gravity = 0.015          # 0.015
pipe_velx = -0.85        # -0.85
pipe_dist_ll = 300       # 200
pipe_dist_ul = 300       # 300
dt = 1                   # 1
acc = - 1.4              # -1.4
lower_space_limit = 150  # 130
upper_space_limit = 150  # 150
breadth_ll = 50          # 50
breadth_ul = 50          # 70
anglejump = 1            # 1
anggrav = -0.01          # -0.01
popnum = 100
prevbird = None
prevplayer = None
prevshow = False

start = False

bird_list = []
players = []
def initiatebirdlist():
    bird_list.clear()
    for i in range(popnum + 1):
        bird_list.append(bird.Bird(0, h / 2, 30, 30, w, h, gravity, anggrav, blue, red))
        players.append(player.Player(bird_list[i], bird_list[i].getScore, Neural_Net.NN(4, 1, 0, 4),))

initiatebirdlist()
pop = population.Population(players)
gen = generation.Generation(pop)
game = game_manager.Game_manager(bird_list, pipe_velx, pipe_dist_ll, pipe_dist_ul, green, w, h, lower_space_limit, upper_space_limit, breadth_ll, breadth_ul)
def restartGame():
    bird_list.clear()
    players[-1].neuralNet = gen.prevpop
    for i in range(len(players)):
        new = bird.Bird(0, h / 2, 30, 30, w, h, gravity, anggrav, blue, red)
        players[i].entity = new
        players[i].returnfitness = new.getScore
        bird_list.append(new)

    return game_manager.Game_manager(bird_list, pipe_velx, pipe_dist_ll, pipe_dist_ul, green, w, h,
                                     lower_space_limit, upper_space_limit, breadth_ll, breadth_ul)

back = pygame.image.load(r"D:\background.png").convert()
back = pygame.transform.scale(back, (w, h))



while True:
    game.update(dt)
    for play, birds in zip(players, bird_list):
        play.updateInputs([birds.posy,
                           game.getnextpipe(birds).l1,
                           game.getnextpipe(birds).l2,
                           game.getnextpipe(birds).posx])
        play.perform()
        if play.getOutputs()[0] > 0:
             # for x in play.neuralNet.hiddenlayerlist[0].neuron_list:
             #     print(play.getOutputs())
             play.entity.jump(acc, anglejump)
    #time.sleep(0.00) #0.003
    if start:
        screen.fill((0, 0, 0, 0))
        screen.blit(back, (0, 0, w, h))
        game.show(screen, prevshow)
        text_surface = my_font.render(str(game.score), False, (255, 255, 255))
        screen.blit(text_surface, (w / 2 - 25, 50))
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            start = not start
        if event.type == pygame.MOUSEBUTTONDOWN:
            prevshow = not prevshow

            # game.birdjump(acc, anglejump)
    if all([not x.entity.alive for x in players]):
        # start = False
        gen.createNewGen(0.3, 0.0001) #0.3, 0
        players = gen.currentpop.playerList
        game = restartGame()
