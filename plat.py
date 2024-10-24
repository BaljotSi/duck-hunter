import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Load images
bird_left = pygame.image.load("Bird_left.png")
bird_left = pygame.transform.scale(bird_left,[100,100])

sling = pygame.image.load("sling.png")
sling = pygame.transform.scale(sling,[100,100])

rock = pygame.image.load("rock.png")
rock = pygame.transform.scale(rock,[50,50])

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.3)

class Rock(pygame.sprite.Sprite) :
    def __init__(self,x,y) :
        super().__init__()
        self.rockimage = pygame.transform.scale(pygame.image.load("rock.png"),[50,50])
        self.image = pygame.Surface([50, 50])
        self.image.fill("yellow")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self) :
        self.rect.y -= 10

    def display(self) :
        screen.blit(self.rockimage,(self.rect.x,self.rect.y))


class Player :
    def __init__(self,stones,lives,limit=1) :
        self.stones = stones
        self.lives = lives
        self.x = 640
        self.y = 650
        self.rocks = []
        self.rock_limit = limit
        self.loaded = 15

    def move(self,direction) :
        if direction == "right":
            self.x +=10
        elif direction == "left":
            self.x -=10

    def throw(self) :
        new_rock = Rock(self.x - 25, self.y - 20)
        self.rocks.append(new_rock)
        self.loaded -= 1

    def display_rock(self) :
        self.start_time = pygame.time.get_ticks() 
        for currentRock in self.rocks :
            currentRock.move()
            currentRock.display()
            if currentRock.rect.y < 0 and len(self.rocks) > 0 and self.rock_limit > 0 :
                self.rocks.remove(currentRock)
        if len(self.rocks) == 0 and self.rock_limit > 0 :
            if pygame.time.get_ticks() - self.start_time > 10 :
                self.start_time = pygame.time.get_ticks()
                self.throw()
            
        for rock in player.rocks:
            if rock.rect.colliderect(bird_left.get_rect(topleft=[590,30])) :
                print("hit")
                player.rocks.remove(rock)
                self.hit == True
        
class Bird(pygame.sprite.Sprite) :
    def __init__(self,x,y) :
        super().__init__()
        self.x = x
        self.y = y
        self.hit = False
        self.moving = False


    def death(self) :
        
        if self.hit == True :
            print("dead")
    
            
player = Player(0,5)
while running:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                 if player.loaded < 2 :
                    player.throw()
                    player.loaded = 15


    screen.fill("lightblue")  

    # GUI
    pygame.draw.rect(screen,"chartreuse3",[0,520,1280,200])

    pygame.draw.rect(screen,"black",[885,625,400,100],0,10,10,10,-1,10)
    pygame.draw.rect(screen,"white",[895,635,380,80],0,10,10,10,-1,10)

    # Player

    if player.loaded > 2:
        sling = pygame.image.load("loaded_sling.png")
        sling = pygame.transform.scale(sling,[80,80])
        screen.blit(sling,[player_pos.x-40,player_pos.y-40])

    else :
        sling = pygame.image.load("sling.png")
        sling = pygame.transform.scale(sling,[80,80])
        screen.blit(sling,[player_pos.x-40,player_pos.y-40])

    # Top rope
    pygame.draw.rect(screen,"black",[0,108,1280,2])
    pygame.draw.rect(screen,"chocolate4",[0,110,1280,100])

    # bottom rope
    pygame.draw.rect(screen,"chocolate4",[0,200,1280,120])
    pygame.draw.rect(screen,"black",[0,320,1280,2])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if player_pos.x > 40:
            player_pos.x -= 10
    if keys[pygame.K_d]:
        if player_pos.x < 1240:
            player_pos.x += 10


    screen.blit(bird_left,[590,30])

    if player.loaded > 0 :
        player.loaded -= 1


    player.display_rock()

    pygame.display.flip()


    clock.tick(60)

pygame.quit()

