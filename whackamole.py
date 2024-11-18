import pygame
import random



def checkmouse(moouseposition, moleposition):
    cords_x = moouseposition[0]
    y_cords = moouseposition[1]
    moletopleftcords_x = moleposition[0]
    moletopleftcords_y = moleposition[1]
    molebottomrightcords_x = moleposition[0] + 32
    moleborroomrightcords_y = moleposition[1] + 32
    if cords_x - molebottomrightcords_x <= 0 <= cords_x - moletopleftcords_x:
        if y_cords - moleborroomrightcords_y <= 0 <= y_cords - moletopleftcords_y:
            return True
    return False

def  base32bit (numbervariable):
    if numbervariable % 32 == 0:
        return numbervariable
    else:
        return base32bit(numbervariable + 1)






def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x = 0
        y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            for i in range(1, 21):
                pygame.draw.line(screen, (0, 0, 0), (i*32, 0), (i*32, 512))
            for i in range (1,17):
                pygame.draw.line(screen, (0, 0, 0), (0, i*32), (640 , i*32))
            if event.type == pygame.MOUSEBUTTONDOWN:
                gaylord = event.pos
                straightlord = (x,y)
                bilord = checkmouse(gaylord, straightlord)
                if bilord:
                    x = random.randrange (0,609)
                    y = random.randrange (0,481)
                    x = base32bit(x)
                    y = base32bit(y)
                    print (x,y)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()



if __name__ == "__main__":
    main()
