import pygame
import random

pygame.init()

# Screen dimensions and settings
width, height = 400, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# Colors and game settings
WHITE = (0, 0, 0)
GREEN = (0, 255, 0)
BLACK = (255, 255, 255)
FPS = 35
GRAVITY = 0.7
JUMP = -7
PIPE_WIDTH = 70
PIPE_GAP = 200


# Bird image setup
bird_img = pygame.Surface((30, 30))
bird_img.fill((255, 255, 0))

# Bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = height // 2  # Fixed typo "HELGHT"
        self.vel = 0
        self.rect = pygame.Rect(self.x, self.y, 30, 30)

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.vel = JUMP

    def draw(self, win):
        win.blit(bird_img, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = width
        self.height = random.randint(50, height - PIPE_GAP - 50)  # Fixed "rendint" typo
        self.top = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, height - self.height - PIPE_GAP)

    def update(self):
        self.x -= 5
        self.top.topleft = (self.x, 0)
        self.bottom.topleft = (self.x, self.height + PIPE_GAP)

    def draw(self, win):
        pygame.draw.rect(win, GREEN, self.top)
        pygame.draw.rect(win, GREEN, self.bottom)  # Fixed typo

# Game over screen
def game_over(win, score):
    font_big = pygame.font.SysFont(None, 72)
    font_small = pygame.font.SysFont(None, 36)
    game_over_text = font_big.render("Game Over", True, BLACK)
    score_text = font_big.render(f"Score: {score}", True, BLACK)
    restart_text = font_small.render("Press any key to exit", True, BLACK)

    win.fill(WHITE)
    win.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 3))
    win.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2))
    win.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 + 100))
    print(score)
    pygame.display.update()
    wait_for_exit()

def wait_for_exit():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False


def harder(score, FPS):
    if score >0 and score % 3 ==10:
        FPS +=100 


def main():
    clock = pygame.time.Clock()   
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    font = pygame.font.SysFont(None, 36)
    harder(score,FPS)  
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        bird.update()

        if pipes[-1].x < width // 2:
            pipes.append(Pipe())
  
        for pipe in pipes[:]:
            pipe.update()
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
                score += 1

        for pipe in pipes:
            if bird.rect.colliderect(pipe.top) or bird.rect.colliderect(pipe.bottom):
                game_over(win, score)
                run = False

        if bird.y > height or bird.y < 0:
            game_over(win, score)
            run = False

        win.fill(WHITE)
        bird.draw(win)
        for pipe in pipes:
            pipe.draw(win)
        score_text = font.render(f"Score: {score}", True, BLACK)
        win.blit(score_text, (10, 10))

        pygame.display.update()


    pygame.quit()

if _name_ == "_main_":
    main()