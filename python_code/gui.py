import pygame
import sys

pygame.init()

# ----------------- Configuration de base ------------------
WIDTH, HEIGHT = 1280, 720

# Scale factor for maintaining proportions from original dimensions
SCALE_X = WIDTH / 1920  # Assuming original was 1920 width
SCALE_Y = HEIGHT / 1080  # Assuming original was 1080 height
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galérapagos - Interface Interactive")

# ----------------- Couleurs et polices --------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (240, 240, 240)
BLUE = (0, 0, 255)
GREEN = (200, 255, 200)
YELLOW = (255, 255, 200)
HIGHLIGHT = (255, 255, 0)
SCROLL_BG = (250, 250, 250)
GAUGE_BG = (220, 220, 220)
GAUGE_FILL = (100, 180, 255)

FONT = pygame.font.SysFont(None, int(36 * min(SCALE_X, SCALE_Y)))
SMALL_FONT = pygame.font.SysFont(None, int(28 * min(SCALE_X, SCALE_Y)))

# ----------------- Variables de jeu ------------------------
X_MAX = 10
resources = {"eau": 3, "nourriture": 2, "bois": 4}
event_message = "Bienvenue sur l'île !"
action_log = []
selected_zone = ""
pending_zone = None

# ----------------- Données sur les zones ------------------
zone_descriptions = {
    "foret": "Une forêt dense, idéale pour trouver du bois.",
    "mer": "Une vaste mer pleine de poissons.",
    "riviere": "Une rivière claire, source d'eau potable.",
    "campement": "Le campement principal où tout le monde se repose.",
    "plage": "Une plage ensoleillée, point d'observation des environs."
}

zone_noms = {
    "foret": "la forêt",
    "mer": "la mer",
    "riviere": "la rivière",
    "campement": "le campement",
    "plage": "la plage"
}

zone_resources = {
    "foret": {"bois": 5, "eau": 1, "nourriture": 2},
    "mer": {"bois": 0, "eau": 3, "nourriture": 7},
    "riviere": {"bois": 0, "eau": 8, "nourriture": 1},
    "campement": {"bois": 2, "eau": 2, "nourriture": 2},
    "plage": {"bois": 1, "eau": 1, "nourriture": 3},
}

# ----------------- Images et UI ---------------------------
ILE_WIDTH = int(900 * SCALE_X)
ILE_HEIGHT = HEIGHT
ILE_X = WIDTH - ILE_WIDTH
ILE_Y = 0

background_image = pygame.image.load("assets/gui/fond.png").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
ile_image = pygame.image.load("assets/gui/ile.png").convert()
ile_image = pygame.transform.scale(ile_image, (ILE_WIDTH, ILE_HEIGHT))

icon_size = int(40 * min(SCALE_X, SCALE_Y))
icon_eau = pygame.transform.scale(pygame.image.load("assets/gui/eau.png").convert_alpha(), (icon_size, icon_size))
icon_poisson = pygame.transform.scale(pygame.image.load("assets/gui/poisson.png").convert_alpha(), (icon_size, icon_size))
icon_arbre = pygame.transform.scale(pygame.image.load("assets/gui/arbre.png").convert_alpha(), (icon_size, icon_size))
bois_fond = pygame.image.load("assets/gui/bois_fond.png").convert()

# ----------------- Emplacements des éléments ---------------
action_buttons = {
    "eau":   {"center": (int(560 * SCALE_X), int(200 * SCALE_Y)), "radius": int(50 * min(SCALE_X, SCALE_Y)), "icon": icon_eau},
    "peche": {"center": (int(700 * SCALE_X), int(200 * SCALE_Y)), "radius": int(50 * min(SCALE_X, SCALE_Y)), "icon": icon_poisson},
    "bois":  {"center": (int(840 * SCALE_X), int(200 * SCALE_Y)), "radius": int(50 * min(SCALE_X, SCALE_Y)), "icon": icon_arbre}
}

map_zones = {
    "foret":     {"center": (ILE_X + int(350 * SCALE_X), int(500 * SCALE_Y)), "radius": int(60 * min(SCALE_X, SCALE_Y))},
    "mer":       {"center": (ILE_X + int(200 * SCALE_X), int(125 * SCALE_Y)), "radius": int(60 * min(SCALE_X, SCALE_Y))},
    "riviere":   {"center": (ILE_X + int(575 * SCALE_X), int(560 * SCALE_Y)), "radius": int(60 * min(SCALE_X, SCALE_Y))},
    "campement": {"center": (ILE_X + int(450 * SCALE_X), int(200 * SCALE_Y)), "radius": int(60 * min(SCALE_X, SCALE_Y))},
    "plage":     {"center": (ILE_X + int(700 * SCALE_X), int(300 * SCALE_Y)), "radius": int(60 * min(SCALE_X, SCALE_Y))}
}

confirm_button = {"center": (int(800 * SCALE_X), int(900 * SCALE_Y)), "radius": int(40 * min(SCALE_X, SCALE_Y))}
pending_action = None

# ----------------- Fonctions Utilitaires ------------------

def draw_text_centered(text, center, color=BLACK, font=FONT):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=center)
    screen.blit(surface, rect)

def is_inside_circle(pos, center, radius):
    return (pos[0] - center[0]) ** 2 + (pos[1] - center[1]) ** 2 <= radius ** 2

def draw_gauge(x, y, value, max_value):
    gauge_width = int(200 * SCALE_X)
    gauge_height = int(20 * SCALE_Y)
    pygame.draw.rect(screen, GAUGE_BG, (x, y, gauge_width, gauge_height))
    fill_width = int(gauge_width * value / max_value)
    pygame.draw.rect(screen, GAUGE_FILL, (x, y, fill_width, gauge_height))
    pygame.draw.rect(screen, BLACK, (x, y, gauge_width, gauge_height), 2)

def draw_circular_image(image, pos, radius):
    size = (radius * 2, radius * 2)
    mask_surface = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.circle(mask_surface, (255, 255, 255), (radius, radius), radius)
    image = pygame.transform.smoothscale(image, size)
    masked_image = pygame.Surface(size, pygame.SRCALPHA)
    masked_image.blit(image, (0, 0))
    masked_image.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    screen.blit(masked_image, pos)

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines

# ----------------- Fonction Principale d'affichage ---------
def draw_interface():
    screen.blit(background_image, (0, 0))
    screen.blit(ile_image, (ILE_X, ILE_Y))
    draw_text_centered("Carte de l'île", (ILE_X + int(450 * SCALE_X), int(40 * SCALE_Y)))

    mouse_pos = pygame.mouse.get_pos()

    for key, data in map_zones.items():
        color = HIGHLIGHT if is_inside_circle(mouse_pos, data["center"], data["radius"]) else BLACK
        pygame.draw.circle(screen, WHITE, data["center"], data["radius"])
        pygame.draw.circle(screen, color, data["center"], data["radius"], 3)
        draw_text_centered(key.capitalize(), data["center"])

    pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, ILE_X - int(20 * SCALE_X), int(100 * SCALE_Y)))
    draw_text_centered(event_message, (ILE_X // 2, int(40 * SCALE_Y)))

    resources_rect = (int(40 * SCALE_X), int(120 * SCALE_Y), int(300 * SCALE_X), int(230 * SCALE_Y))
    pygame.draw.rect(screen, (240, 248, 255), resources_rect)
    draw_text_centered(f"Eau : {resources['eau']}", (int(190 * SCALE_X), int(140 * SCALE_Y)))
    draw_gauge(int(90 * SCALE_X), int(165 * SCALE_Y), resources["eau"], X_MAX)
    draw_text_centered(f"Nourriture : {resources['nourriture']}", (int(190 * SCALE_X), int(210 * SCALE_Y)))
    draw_gauge(int(90 * SCALE_X), int(235 * SCALE_Y), resources["nourriture"], X_MAX)
    draw_text_centered(f"Bois : {resources['bois']}", (int(190 * SCALE_X), int(280 * SCALE_Y)))
    draw_gauge(int(90 * SCALE_X), int(305 * SCALE_Y), resources["bois"], X_MAX)

    for key, data in action_buttons.items():
        pygame.draw.circle(screen, BLUE, data["center"], data["radius"])
        icon_rect = data["icon"].get_rect(center=data["center"])
        screen.blit(data["icon"], icon_rect)
        if is_inside_circle(mouse_pos, data["center"], data["radius"]):
            pygame.draw.circle(screen, HIGHLIGHT, data["center"], data["radius"] + 3, 3)

    cartes_x = int(460 * SCALE_X)
    cartes_y = int(280 * SCALE_Y)
    cartes_width = int(410 * SCALE_X)
    cartes_height = int(80 * SCALE_Y)
    pygame.draw.rect(screen, YELLOW, (cartes_x, cartes_y, cartes_width, cartes_height), border_radius=8)
    cartes_text = "[Parapluie]  [Caisse de riz]  [Sac à dos]  [Potion d'eau]"
    lines = wrap_text(cartes_text, SMALL_FONT, cartes_width - int(30 * SCALE_X))
    for i, line in enumerate(lines):
        text_surface = SMALL_FONT.render(line, True, BLACK)
        screen.blit(text_surface, (cartes_x + int(15 * SCALE_X), cartes_y + int(10 * SCALE_Y) + i * int(28 * SCALE_Y)))

    desc_x = cartes_x
    desc_y = cartes_y + cartes_height + int(20 * SCALE_Y)
    desc_width = cartes_width + int(50 * SCALE_X)
    desc_height = int(170 * SCALE_Y)
    pygame.draw.rect(screen, (230, 230, 230), (desc_x, desc_y, desc_width, desc_height), border_radius=8)

    description = zone_descriptions.get(selected_zone, "Cliquez sur une zone pour voir la description.")
    lines = wrap_text(description, SMALL_FONT, desc_width - int(30 * SCALE_X))

    if selected_zone:
        ressources = zone_resources[selected_zone]
        ressources_text = (
            f"Vous pouvez espérer trouver ici :\n"
            f"- {ressources['bois']} bois\n"
            f"- {ressources['eau']} eau\n"
            f"- {ressources['nourriture']} nourriture"
        )
        for l in ressources_text.split("\n"):
            lines += wrap_text(l, SMALL_FONT, desc_width - int(30 * SCALE_X))

    for i, line in enumerate(lines):
        text_surface = SMALL_FONT.render(line, True, BLACK)
        screen.blit(text_surface, (desc_x + int(15 * SCALE_X), desc_y + int(10 * SCALE_Y) + i * int(28 * SCALE_Y)))

    if selected_zone:
        try:
            image = pygame.image.load("assets/gui/" + selected_zone + ".png").convert_alpha()
            radius = int(70 * min(SCALE_X, SCALE_Y))
            image_x = desc_x + (desc_width - 2 * radius) // 2
            image_y = desc_y + desc_height + int(15 * SCALE_Y)
            draw_circular_image(image, (image_x, image_y), radius)
        except Exception:
            pass

    pygame.draw.circle(screen, GREEN, confirm_button["center"], confirm_button["radius"])
    draw_text_centered("OK", confirm_button["center"], font=SMALL_FONT)

    journal_img = pygame.image.load("assets/gui/journal_fond.png").convert_alpha()
    journal_width = int((1063 // 2) * SCALE_X)
    journal_height = int((1025 // 2) * SCALE_Y)
    journal_img = pygame.transform.scale(journal_img, (journal_width, journal_height))
    journal_img_rotated = pygame.transform.rotate(journal_img, -5)
    journal_rect = journal_img_rotated.get_rect(midbottom=(int(200 * SCALE_X), HEIGHT + int(50 * SCALE_Y)))
    screen.blit(journal_img_rotated, journal_rect)

    def draw_scroll_text():
        scroll_angle = -6
        lines_to_display = action_log[-10:]
        base_x = int(90 * SCALE_X)
        base_y = HEIGHT - int(370 * SCALE_Y)
        line_spacing = int(30 * SCALE_Y)
        for i, line in enumerate(lines_to_display):
            rendered_text = SMALL_FONT.render(line, True, BLACK)
            rotated_text = pygame.transform.rotate(rendered_text, scroll_angle)
            screen.blit(rotated_text, (base_x, base_y + i * line_spacing))

    draw_scroll_text()

# ----------------- Traitement des actions ------------------
def process_action(action):
    global event_message

    if not selected_zone:
        event_message = "Rendez-vous d'abord dans une zone."
        return

    res_type = {
        "eau": "eau",
        "peche": "nourriture",
        "bois": "bois"
    }.get(action)

    if res_type:
        found = zone_resources[selected_zone][res_type]
        current = resources[res_type]
        gained = min(found, X_MAX - current)
        resources[res_type] += gained

        if gained < found:
            event_message = f"Je suis chargé à bloc de {res_type}."
        else:
            event_message = f"Vous avez trouvé {gained} {res_type} !"

        action_log.append(event_message)

# ----------------- Boucle principale -----------------------
def main():
    global selected_zone, pending_action, pending_zone

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for key, data in map_zones.items():
                    if is_inside_circle(pos, data["center"], data["radius"]):
                        selected_zone = key
                        pending_zone = key
                        break

                for action, data in action_buttons.items():
                    if is_inside_circle(pos, data["center"], data["radius"]):
                        pending_action = action
                        break

                if is_inside_circle(pos, confirm_button["center"], confirm_button["radius"]):
                    if pending_action:
                        process_action(pending_action)
                        pending_action = None
                    if pending_zone:
                        log_msg = f"Je me rends à {zone_noms.get(pending_zone, pending_zone)}."
                        action_log.append(log_msg)
                        pending_zone = None

        draw_interface()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

# ----------------- Lancement du programme ------------------
if __name__ == "__main__":
    main()
