import pygame
import os
import random
import math

pygame.init()

x_okna = 800
y_okna = 800

okno = pygame.display.set_mode((x_okna,y_okna))

def napisz(tekst, x, y, rozmiar):
    cz = pygame.font.SysFont("Arial", rozmiar)
    napis = cz.render(tekst,1,(100,255,100))
    
    okno.blit(napis,(x,y))

copokazuje = "menu"

class Przeszkoda():
    def __init__(self, x, szerokosc):
        self.x = x
        self.szerokosc = szerokosc
        self.y_gora = 0
        self.wysokosc_gora = random.randint(180,360)
        self.odstep = 300
        self.y_dol = self.wysokosc_gora + self.odstep
        self.wysokosc_dol = y_okna - self.y_dol
        self.kolor = (100,100,100)
        self.ksztalt_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.wysokosc_gora)
        self.ksztalt_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.wysokosc_dol)
        self.y_gwiazdka = random.randint(self.wysokosc_gora + 30, self.wysokosc_gora + self.odstep - 30)
        self.wysokosc_gwiazdka = 20
        self.szerokosc_gwiazdka = 20
        self.ksztalt_gwiazdka = pygame.Rect(self.x, self.y_gwiazdka, self.szerokosc_gwiazdka, self.wysokosc_gwiazdka)
        self.grafika = pygame.image.load(os.path.join('gwiazdka.png'))
    def rysuj(self):
        pygame.draw.rect(okno, self.kolor, self.ksztalt_gora, 0)
        pygame.draw.rect(okno, self.kolor, self.ksztalt_dol, 0)
        okno.blit(self.grafika, (self.x, self.y_gwiazdka))
    def ruch(self,v):
        self.x = self.x - v
        self.ksztalt_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.wysokosc_gora)
        self.ksztalt_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.wysokosc_dol)
        self.ksztalt_gwiazdka = pygame.Rect(self.x, self.y_gwiazdka, self.szerokosc_gwiazdka, self.wysokosc_gwiazdka)
    def kolizja(self, player):
        if self.ksztalt_dol.colliderect(player) or self.ksztalt_gora.colliderect(player):
            return True
        else:
            return False
    def punkt(self, player):
        if self.ksztalt_gwiazdka.colliderect(player):
    #        self.ksztalt_gwiazdka.destroy()
            return True
        else:
            return False

class Helikopter():
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.wysokosc = 50
        self.szerokosc = 50
        self.ksztalt = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        self.grafika = pygame.image.load(os.path.join('helikopter.png'))
    def rysuj(self):
        okno.blit(self.grafika, (self.x,self.y))
    def ruch(self, v):
        self.y = self.y + v
        self.ksztalt = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)

przeszkody = []
for i in range(21):
    przeszkody.append(Przeszkoda(i*x_okna/20,x_okna/20))

gracz = Helikopter(375,400)

dy = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -1
            if event.key == pygame.K_DOWN:
                dy = +1
            if event.key == pygame.K_SPACE:
                if copokazuje != "rozgrywka":
                    gracz = Helikopter(375,400)
                    dy = 0
                    copokazuje = "rozgrywka"
                    punkty = 0
                    punkty_dwa = 0
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 0
                
    okno.fill((0,0,0))
    if copokazuje == "menu":
        grafika = pygame.image.load(os.path.join('logo.JPG'))
        x_logo = (x_okna - grafika.get_rect().width)/2
        y_logo = (y_okna - grafika.get_rect().height)/3
        okno.blit(grafika,(x_logo,y_logo))
        x_napis = (x_okna - grafika.get_rect().width)/3
        y_napis = y_logo*2
        napisz("Nacisnij spacje aby zaczac gre", x_napis, y_napis, 32)
    elif copokazuje == "rozgrywka":
        for p in przeszkody:
            p.ruch(1)
            p.rysuj()
            if p.kolizja(gracz.ksztalt):
                copokazuje = "koniec"
            if p.punkt(gracz.ksztalt):
                punkty_dwa = punkty_dwa + 1
               # punkt.remove(p)
        for p in przeszkody:
            if p.x <= -p.szerokosc:
                przeszkody.remove(p)
                przeszkody.append(Przeszkoda(x_okna,x_okna/20))
                punkty = punkty + math.fabs(dy)
        gracz.rysuj()
        gracz.ruch(dy)
        napisz("Punkty: " +str(int(punkty)), 20, 20, 40)
        napisz("Gwiazdki: " +str(int(punkty_dwa)), 20, 60, 40)
   #     napisz("P: " +str(int(punkty_trzy)), 20, 90, 40)
    elif copokazuje == "koniec":
        grafika = pygame.image.load(os.path.join('logo.JPG'))
        x_logo = (x_okna - grafika.get_rect().width)/2
        y_logo = (y_okna - grafika.get_rect().height)/3
        okno.blit(grafika,(x_logo,y_logo))
        x_napis = (x_okna - grafika.get_rect().width)/2
        y_napis = y_logo*2
        #napisz("Konieec Gry", "Glowa do gory", sep="\n")
        napisz("Koniec Gry", x_napis/2, y_napis, 32)
        napisz("Twój wynik to: " +str(int(punkty)), x_napis/2, y_napis + 40, 32)
        napisz("Twoj gwiazdkowy wynik: " +str(int(punkty_dwa)), x_napis/2, y_napis + 80, 32)
        napisz("Nacisnij spacje by zagrac ponownie", x_napis/2, y_napis + 120, 32)
        
    pygame.display.update()
