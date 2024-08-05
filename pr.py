import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
CAR_WIDTH, CAR_HEIGHT = 50, 50
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50
ROAD_WIDTH = 200
FPS = 60

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the car
car_x, car_y = WIDTH // 2, HEIGHT - CAR_HEIGHT - 20
car_speed = 5

# Set up the obstacles
obstacles = []
obstacle_speed = 5
obstacle_timer = 0

# Set up the score
score = 0
score_timer = 0

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the pressed keys
    keys = pygame.key.get_pressed()

    # Move the car
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Keep the car on the road
    if car_x < WIDTH // 2 - ROAD_WIDTH // 2:
        car_x = WIDTH // 2 - ROAD_WIDTH // 2
    if car_x > WIDTH // 2 + ROAD_WIDTH // 2 - CAR_WIDTH:
        car_x = WIDTH // 2 + ROAD_WIDTH // 2 - CAR_WIDTH

    # Move the obstacles
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

    # Check for collisions
    for obstacle in obstacles:
        if (obstacle[0] < car_x + CAR_WIDTH and
            obstacle[0] + OBSTACLE_WIDTH > car_x and
            obstacle[1] < car_y + CAR_HEIGHT and
            obstacle[1] + OBSTACLE_HEIGHT > car_y):
            # Game over screen
            screen.fill(BLACK)
            text = font.render("Game Over! Score: " + str(score), True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

    # Remove obstacles that are off the screen
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < HEIGHT]

    # Add new obstacles
    obstacle_timer += 1
    if obstacle_timer >= 60:  # Add obstacle every second
        obstacles.append([random.randint(WIDTH // 2 - ROAD_WIDTH // 2, WIDTH // 2 + ROAD_WIDTH // 2 - OBSTACLE_WIDTH), -OBSTACLE_HEIGHT])
        obstacle_timer = 0

    # Update the score
    score_timer += 1
    if score_timer >= 60:  # Increase score every second
        score += 1
        score_timer = 0

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (WIDTH // 2 - ROAD_WIDTH // 2, 0, ROAD_WIDTH, HEIGHT))
    pygame.draw.rect(screen, RED, (car_x, car_y, CAR_WIDTH, CAR_HEIGHT))
    for obstacle in obstacles:
        pygame.draw.rect(screen, WHITE, (obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))  # Display the score at the top left corner

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)