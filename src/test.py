import pygame
from dataclasses import dataclass, field
import random
from functools import partial

MAX_WIDTH = 300
MAX_HEIGHT = 300

pygame.init()
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


@dataclass
class Animal:
    name: str
    screen: pygame.Surface
    x: int = field(default_factory=partial(random.randint, 0, MAX_WIDTH))
    y: int = field(default_factory=partial(random.randint, 0, MAX_HEIGHT))
    size: int = 3
    color: str = "black"
    step: int = 1
    previous_x: int = 0
    previous_y: int = 0

    def __post_init__(self):
        self.previous_y = self.y
        self.previous_x = self.x

    def __str__(self):
        return f'Animal: {self.name} [x={self.x}, y={self.y}] (previous: [x={self.previous_x}, y={self.previous_y}])'

    def move_right(self):
        self.previous_x = self.x

        if self.x < MAX_WIDTH:
            self.x += self.step

    def move_left(self):
        self.previous_x = self.x
        if self.x > 0:
            self.x -= self.step

    def move_up(self):
        self.previous_y = self.y

        if self.y > 0:
            self.y -= self.step

    def move_down(self):
        self.previous_y = self.y

        if self.y < MAX_HEIGHT:
            self.y += self.step

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size)

    def follow(self, animal: "Animal"):
        if self.x > animal.x:
            self.move_left()
        elif self.x < animal.x:
            self.move_right()
        if self.y > animal.y:
            self.move_up()
        elif self.y < animal.y:
            self.move_down()

    def avoid(self, animal: "Animal"):
        if self.x > animal.x:
            self.move_right()
        elif self.x < animal.x:
            self.move_left()
        if self.y > animal.y:
            self.move_down()
        elif self.y < animal.y:
            self.move_up()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def x_diff(self, other):
        return abs(self.x - other.x)

    def y_diff(self, other):
        return abs(self.y - other.y)

    def diff(self, other):
        return self.x_diff(other) + self.y_diff(other)


lion = Animal("Lion", screen=screen, color="red", size=5)
buffalo = Animal("Buffalo", screen=screen, color='green', size=5)


me = Animal("Me", color="black", size=5, step=5, screen=screen)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    screen.fill("white")

    lion.avoid(me)

    if lion.diff(me) > 100:
        lion.follow(buffalo)
    lion.draw()

    buffalo.avoid(lion)
    buffalo.draw()

    me.draw()

    if lion == buffalo:
        pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        me.move_up()
    if keys[pygame.K_s]:
        me.move_down()
    if keys[pygame.K_a]:
        me.move_left()
    if keys[pygame.K_d]:
        me.move_right()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
