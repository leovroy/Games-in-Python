import pygame
import sys
import random


class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_width / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (206, 7, 224)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*grid_size)) % screen_width), (cur[1] + (y*grid_size)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (grid_size, grid_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (48, 2, 56), r, 1)
    
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)


class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = (12, 250, 20)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width - 1) * grid_size, random.randint(0, grid_height - 1) * grid_size)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, self.color, r)
        #pygame.draw.rect(surface, (93, 216, 228), r, 1)



def draw_grid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*grid_size, y*grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, (242, 201, 245), r)
            else:
                rr = pygame.Rect((x*grid_size, y*grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, (244, 233, 245), rr)


# --variables
screen_width = 480
screen_height = 480

grid_size = 20
grid_width = screen_width / grid_size
grid_height = screen_height / grid_size

# -- directions
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("The Snake Game")
    
    # -- create a surface with screen dimensions
    surface = pygame.Surface(screen.get_size()).convert()

    draw_grid(surface)

    snake = Snake()
    food = Food()

    my_font = pygame.font.SysFont("monospace", 20)

    score = 0

    while True:
        clock.tick(10)
        snake.handle_keys()

        draw_grid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))

        text = my_font.render(f"Score: {score}", 1, (0,0,0))
        screen.blit(text, (8, 15))
        
        pygame.display.update()

main()




















































