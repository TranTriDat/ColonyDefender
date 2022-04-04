import pygame
import random
from pygame.locals import *
from pygame import mixer
import math


class Game:
    def __init__(self):
        pygame.init()
        self.xScreen, self.yScreen = 1000, 600
        self.vBullet = 15
        self.vPlanes = 15
        self.vEnemy = 6
        self.scores = 0
        self.numberEnemy = 2
        self.numberBullet = 6
        linkBackground = "colony.jpg"
        self.linkEnemy = "enemy.png"
        self.linkPlanes = "planes.png"
        self.sizexPlanes, self.sizeyPlanes = 80, 80
        self.xPlanes, self.yPlanes = self.xScreen / 2, self.yScreen - 100
        self.screen = pygame.display.set_mode((self.xScreen, self.yScreen))
        pygame.display.set_caption("Space Squad")
        self.background = pygame.image.load(linkBackground)
        icon = pygame.image.load(self.linkPlanes)
        pygame.display.set_icon(icon)
        self.gamerunning = True
        self.listBullet = []
        self.listEnemy = []
        self.YGameOver = 0
        self.K_DOWN = self.K_UP = self.K_LEFT = self.K_RIGHT = False

        # self.music()
        # pygame.mixer.music.load("zeta.mp3")
        # pygame.mixer.music.play()

        # self.music("zeta.mp3")

        # S = random.choice(Kamille)
        # self.kamille_quote()
        # self.music(pygame.mixer.music.load('zeta.mp3'))

    def kamille_quote(self):
        Kamille = ['Kamille1.ogg', 'Kamille2.ogg']
        i = 0
        for i in range(len(Kamille)):
            pygame.mixer.init()
            S = random.choice(Kamille)
            pygame.mixer.music.set_volume(0.50)
            pygame.mixer.music.load(S)
            pygame.mixer.music.play()

    def music(self, url):
        # i=0
        # for i in range(0,i+3,+1):
        #     pygame.mixer.init()
        #     S = random.choice(Kamille)
        #     pygame.mixer.music.set_volume(0.50)
        #     pygame.mixer.music.load(S)
        #     pygame.mixer.music.play()
        pygame.mixer.init()
        pygame.mixer.music.load(url)
        pygame.mixer.music.play(-1, 0.0)

    def show_score(self, x, y, scores, size):
        font = pygame.font.SysFont("comicsansms", size)
        score = font.render(str(scores), True, (255, 255, 255))
        self.screen.blit(score, (x, y))

    def image_draw(self, url, xLocal, yLocal, xImg, yImg):
        PlanesImg = pygame.image.load(url)
        PlanesImg = pygame.transform.scale(PlanesImg, (xImg, yImg))
        self.screen.blit(PlanesImg, (xLocal, yLocal))

    def enemy(self):
        for count, i in enumerate(self.listEnemy):
            xEnemy = i["xEnemy"]
            yEnemy = i["yEnemy"]
            self.YGameOver

            if xEnemy < 0 or xEnemy > self.xScreen - self.sizexPlanes:
                self.listEnemy[count]["direction"] = not self.listEnemy[count]["direction"]

            self.image_draw(self.linkEnemy, xEnemy, yEnemy, self.sizexPlanes, self.sizeyPlanes)
            self.listEnemy[count]["xEnemy"] = xEnemy + (
                self.vEnemy if self.listEnemy[count]["direction"] == False else - self.vEnemy)
            self.listEnemy[count]["yEnemy"] = yEnemy + self.vEnemy / 2.5
            self.YGameOver = yEnemy if yEnemy > self.YGameOver else self.YGameOver

    def bullet(self):
        for count, i in enumerate(self.listBullet):
            xBullet = i["xBullet"]
            yBullet = i["yBullet"]
            self.image_draw('bullet.png', xBullet, yBullet, 50, 50)
            self.listBullet[count]["yBullet"] = yBullet - self.vBullet
            if yBullet <= 5:
                self.listBullet.remove(self.listBullet[count])

    def run(self):
        while self.gamerunning:

            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.gamerunning = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.K_DOWN = True

                    if event.key == pygame.K_LEFT:
                        self.K_LEFT = True

                    if event.key == pygame.K_UP:
                        self.K_UP = True

                    if event.key == pygame.K_RIGHT:
                        self.K_RIGHT = True

                    if event.key == pygame.K_x:
                        if len(self.listBullet) < self.numberBullet:
                            # self.music("laser.wav")
                            # pygame.mixer.music.load("Kamille1.mp3")
                            # pygame.mixer.music.play()
                            self.listBullet.append({
                                "xBullet": self.xPlanes + self.sizexPlanes / 2 - 25,
                                "yBullet": self.yPlanes - self.sizexPlanes / 2,
                            })

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.K_DOWN = False

                    if event.key == pygame.K_UP:
                        self.K_UP = False

                    if event.key == pygame.K_LEFT:
                        self.K_LEFT = False

                    if event.key == pygame.K_RIGHT:
                        self.K_RIGHT = False

            if self.K_DOWN:
                self.yPlanes = self.yPlanes + self.vPlanes / 2

            if self.K_UP:
                self.yPlanes = self.yPlanes - self.vPlanes / 2

            if self.K_LEFT:
                self.xPlanes = self.xPlanes - self.vPlanes

            if self.K_RIGHT:
                self.xPlanes = self.xPlanes + self.vPlanes

            self.xPlanes = 0 if self.xPlanes < 0 else self.xPlanes
            self.xPlanes = self.xScreen - self.sizexPlanes if self.xPlanes + self.sizexPlanes > self.xScreen else self.xPlanes

            self.yPlanes = 0 if self.yPlanes < 0 else self.yPlanes
            self.yPlanes = self.yScreen - self.sizeyPlanes if self.yPlanes + self.sizeyPlanes > self.yScreen else self.yPlanes

            if len(self.listEnemy) < self.numberEnemy:
                self.listEnemy.append({
                    "xEnemy": random.randint(0, self.xScreen - self.sizexPlanes),
                    "yEnemy": random.randint(-50, self.yScreen / 6),
                    "direction": random.choice((True, False))
                })

            listEnemy2 = self.listEnemy

            # self.music(random.choice(Kamille))
            for countEnemy, enemyIteam in enumerate(listEnemy2):
                xEnemy = enemyIteam["xEnemy"]
                yEnemy = enemyIteam["yEnemy"]
                xEnemy = enemyIteam["xEnemy"]
                yEnemy = enemyIteam["yEnemy"]

                for countBullet, bulletIteam in enumerate(self.listBullet):
                    xBullet = bulletIteam["xBullet"]
                    yBullet = bulletIteam["yBullet"]

                    isInX = xEnemy <= xBullet <= xEnemy + self.sizexPlanes

                    isInY = yEnemy <= yBullet <= yEnemy + self.sizexPlanes / 2

                    if (isInX and isInY):
                        self.listEnemy.remove(self.listEnemy[countEnemy])
                        self.listBullet.remove(self.listBullet[countBullet])
                        self.scores = self.scores + 1
                        break
                # S = random.choice(Kamille)
                # self.music(S)
                if self.numberEnemy < 7:
                    self.numberEnemy = (self.scores / 15) + 2

                if self.YGameOver > self.yScreen - 50:
                    newGame = False
                    # self.music("musicbackground.wav")
                    # pygame.mixer.music.load("musicbackground.wav")
                    # pygame.mixer.music.play()

                    while (True):
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                self.gamerunning = False
                                newGame = True
                                break

                            if event.type == pygame.KEYDOWN:
                                newGame = True
                                break
                        if newGame == True:
                            break

                        self.show_score(100, 100, "Scores:{}".format(self.scores), 40)
                        self.show_score(self.xScreen / 2 - 100, self.yScreen / 2 - 100, "GAME OVER", 50)

                        pygame.display.update()

                    self.scores = 0
                    self.listBullet = []
                    self.listEnemy = []
                    self.YGameOver = 0

            self.show_score(10, 10, "Scores:{}".format(self.scores), 35)

            self.image_draw("sd.png", self.xScreen - 180, 10, 150, 60)
            self.enemy()
            self.bullet()
            self.image_draw(self.linkPlanes, self.xPlanes, self.yPlanes, self.sizexPlanes, self.sizeyPlanes)
            pygame.display.update()


# if __name__ == "main":
game = Game()
pygame.mixer.init()
pygame.mixer.music.load("zeta.mp3")
pygame.mixer.music.play()
# for i in range(10):
#     game.kamille_quote()
game.run()
