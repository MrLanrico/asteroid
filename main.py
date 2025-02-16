import pygame
from constants import *
from player import Player


def main():
    pygame.init  # Call init method
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create Clock object
    clock = pygame.time.Clock()  # Create Clock
    dt = 0  # initialize Delta time variable

    # Create Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        
        # Use Clock object to calculate frame rate and dt
        dt = clock.tick(60) / 1000 # Save the return value


if __name__ == "__main__":
    main()

