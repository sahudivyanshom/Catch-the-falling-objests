import random
import pygame

pygame.init()

# Window settings
WIDTH = 500
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)
big_font = pygame.font.Font(None, 56)

# Basket settings
basket = pygame.Rect(210, 560, 80, 20)
basket_speed = 10

# Falling object settings
object_size = 20
falling_object = pygame.Rect(
    random.randint(0, WIDTH - object_size),
    0,
    object_size,
    object_size
)
object_speed = 5

score = 0
lives = 3
game_over = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            basket.x -= basket_speed
        if keys[pygame.K_RIGHT]:
            basket.x += basket_speed

        # Keep the basket inside the window
        basket.x = max(0, min(basket.x, WIDTH - basket.width))

        # Move the object down
        falling_object.y += object_speed

        # Catch the object
        if basket.colliderect(falling_object):
            score += 1
            falling_object.x = random.randint(0, WIDTH - object_size)
            falling_object.y = 0

        # Miss the object
        elif falling_object.top > HEIGHT:
            lives -= 1
            falling_object.x = random.randint(0, WIDTH - object_size)
            falling_object.y = 0

            if lives == 0:
                game_over = True

    # Draw the screen
    screen.fill((25, 25, 45))
    pygame.draw.rect(screen, (60, 180, 90), basket)
    pygame.draw.rect(screen, (230, 80, 80), falling_object)

    status = font.render(f"Score: {score}   Lives: {lives}", True, (255, 255, 255))
    screen.blit(status, (10, 10))

    if game_over:
        message = big_font.render("Game Over", True, (255, 220, 70))
        final_score = font.render(f"Final Score: {score}", True, (255, 255, 255))
        screen.blit(message, message.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        screen.blit(final_score, final_score.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()