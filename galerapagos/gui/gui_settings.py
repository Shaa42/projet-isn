import pygame

WIDTH, HEIGHT = 1280, 720

# ----------------- Configuration de base ------------------
# Scale factor for maintaining proportions from original dimensions
SCALE_X = WIDTH / 1920  # Assuming original was 1920 width
SCALE_Y = HEIGHT / 1080  # Assuming original was 1080 height

# ----------------- Couleurs et polices --------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (250, 250, 250)
LIGHT_GRAY = (240, 240, 240)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (200, 255, 200)
YELLOW = (255, 255, 200)
HIGHLIGHT = (255, 255, 0)
SCROLL_BG = (250, 250, 250)
GAUGE_BG = (220, 220, 220)
GAUGE_FILL = (100, 180, 255)

# ----------------- Images et UI ---------------------------
ILE_WIDTH = int(900 * SCALE_X)
ILE_HEIGHT = HEIGHT
ILE_X = WIDTH - ILE_WIDTH
ILE_Y = 0