import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catan Game Visual")

# Colors
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

# Resource-specific colors
RESOURCE_COLORS = {
    "wood": (34, 139, 34),     # Green
    "brick": (178, 34, 34),    # Red
    "wheat": (255, 215, 0),    # Gold
    "ore": (128, 128, 128),    # Gray
    "sheep": (173, 255, 47),   # Light Green
    "desert": (210, 180, 140)  # Sandy color
}

# Constants for hexagon layout
HEX_RADIUS = 40  # Radius for hexagons
HEX_WIDTH = math.sqrt(3) * HEX_RADIUS  # Horizontal distance between hex centers
HEX_HEIGHT = 2 * HEX_RADIUS  # Vertical distance between hex centers

# Font for text
font = pygame.font.SysFont(None, 24)

# Sample resource types and numbers (to be shuffled and assigned to tiles)
resources = ["wood", "brick", "wheat", "ore", "sheep", "desert"]
numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

# Shuffle resources and numbers for random assignment
random_resources = random.choices(resources, k=19)
random_numbers = random.choices(numbers, k=19)

# Helper function to draw a single hexagon with resource and number
def draw_hexagon(surface, position, resource, number):
    color = RESOURCE_COLORS.get(resource, (200, 200, 200))  # Default to gray if resource not found
    x, y = position
    points = [
        (x + HEX_RADIUS * math.cos(math.radians(angle)), y + HEX_RADIUS * math.sin(math.radians(angle)))
        for angle in range(0, 360, 60)
    ]
    pygame.draw.polygon(surface, color, points)

    # Draw resource text
    resource_text = font.render(resource, True, TEXT_COLOR)
    surface.blit(resource_text, (x - resource_text.get_width() // 2, y - 15))

    # Draw number text (skip desert since it has no number)
    if number != 0:
        number_text = font.render(str(number), True, TEXT_COLOR)
        surface.blit(number_text, (x - number_text.get_width() // 2, y + 10))

# Function to draw the hexagonal board pattern with resources and numbers
def draw_board():
    # Center starting position
    start_x = WIDTH // 2
    start_y = HEIGHT // 2

    # Number of hexes in each row to create the hexagonal shape
    hex_rows = [3, 4, 5, 4, 3]

    resource_idx = 0  # Index to track resources and numbers for each hex

    # Loop through each row
    for row_idx, hex_count in enumerate(hex_rows):
        y_offset = start_y + (row_idx - len(hex_rows) // 2) * HEX_HEIGHT * 0.87  # Adjusted vertical spacing
        x_offset_start = start_x - (hex_count - 1) * HEX_WIDTH * 0.5

        for hex_idx in range(hex_count):
            x_offset = x_offset_start + hex_idx * HEX_WIDTH * 1.02  # Adjusted horizontal spacing
            resource = random_resources[resource_idx]
            number = random_numbers[resource_idx] if resource != "desert" else 0  # Desert has no number
            draw_hexagon(window, (x_offset, y_offset), resource, number)
            resource_idx += 1

# Main game loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill background
        window.fill(BACKGROUND_COLOR)

        # Draw board
        draw_board()

        # Update display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
