import pygame
import sys

from galerapagos.gui.gui_settings import *
from galerapagos.game import Game
from galerapagos.gametimer import GameTimer

pygame.init()

"""
To-do :
    - préciser le coût de déplacement
    - préciser le fait qu'il faut confirmer le déplacement
    - mettre les conditions pour gagner
"""

# ----------------- Configuration de base ------------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galérapagos - Interface Interactive")

# ----------------- Couleurs et polices --------------------
FONT = pygame.font.SysFont(None, int(36 * min(SCALE_X, SCALE_Y)))
SMALL_FONT = pygame.font.SysFont(None, int(28 * min(SCALE_X, SCALE_Y)))

# ----------------- Variables de jeu ------------------------
game_instance = Game()  # Instance de notre jeu

# Mapping entre les zones de l'interface et les noeuds du jeu
zone_to_node = {
    "alpha": game_instance.alpha_node,
    "cimetiere": game_instance.cime_node,
    "terrier": game_instance.terr_node,
    "camps": game_instance.camp_node,
    "foret": game_instance.foret_node,
    "cascade": game_instance.casc_node
}

# Mapping inverse pour l'affichage
node_to_zone = {v: k for k, v in zone_to_node.items()}

# ----------------- Variables d'interface ------------------
event_message = "Bienvenue dans Galèrapagos !"
action_log = []
selected_zone = "alpha"  # Zone de départ
pending_zone = None
game_running = True
timer_started = False
has_won = False

# ----------------- Données sur les zones ------------------
zone_descriptions = {
    "alpha": "Point de crash de l'avion. Votre point de départ.",
    "cimetiere": "Un cimetière brumeux et mystérieux.",
    "terrier": "Le terrier des phacochères, attention aux habitants !",
    "camps": "Le camp des survivants, lieu de rassemblement.",
    "foret": "La forêt des tambours, riche en ressources.",
    "cascade": "Une cascade brumeuse et rafraîchissante."
}

zone_noms = {
    "alpha": "Crashpoint alpha",
    "cimetiere": "Cimetière brumeuse", 
    "terrier": "Terrier des phacochères",
    "camps": "Camps des survivants",
    "foret": "Forêt des tambours",
    "cascade": "Cascade brumeuse"
}

# ----------------- Images et UI ---------------------------
background_image = pygame.image.load("assets/gui/fond.png").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
ile_image = pygame.image.load("assets/gui/ile.png").convert()
ile_image = pygame.transform.scale(ile_image, (ILE_WIDTH, ILE_HEIGHT))

icon_size = int(40 * min(SCALE_X, SCALE_Y))
icon_eau = pygame.transform.scale(pygame.image.load("assets/gui/eau.png").convert_alpha(), (icon_size, icon_size))
icon_poisson = pygame.transform.scale(pygame.image.load("assets/gui/poisson.png").convert_alpha(), (icon_size, icon_size))
icon_arbre = pygame.transform.scale(pygame.image.load("assets/gui/arbre.png").convert_alpha(), (icon_size, icon_size))

# ----------------- Emplacements des éléments ---------------
action_buttons = {
    "water": {"center": (int(560 * SCALE_X), int(200 * SCALE_Y)), "radius": int(50 * min(SCALE_X, SCALE_Y)), "icon": icon_eau},
    "food": {"center": (int(700 * SCALE_X), int(200 * SCALE_Y)), "radius": int(50 * min(SCALE_X, SCALE_Y)), "icon": icon_poisson},
    "wood": {"center": (int(840 * SCALE_X), int(200 * SCALE_Y)), "radius": int(50 * min(SCALE_X, SCALE_Y)), "icon": icon_arbre}
}

map_zones = {
    "alpha": {"center": (ILE_X + int(350 * SCALE_X), int(300 * SCALE_Y)), "radius": int(60 * min(SCALE_X, SCALE_Y))},
    "cimetiere": {"center": (ILE_X + int(200 * SCALE_X), int(200 * SCALE_Y)), "radius": int(60 * min(SCALE_X, SCALE_Y))},
    "terrier": {"center": (ILE_X + int(150 * SCALE_X), int(400 * SCALE_Y)), "radius": int(60 * min(SCALE_X, SCALE_Y))},
    "camps": {"center": (ILE_X + int(350 * SCALE_X), int(450 * SCALE_Y)), "radius": int(60 * min(SCALE_X, SCALE_Y))},
    "foret": {"center": (ILE_X + int(550 * SCALE_X), int(350 * SCALE_Y)), "radius": int(60 * min(SCALE_X, SCALE_Y))},
    "cascade": {"center": (ILE_X + int(500 * SCALE_X), int(500 * SCALE_Y)), "radius": int(60 * min(SCALE_X, SCALE_Y))}
}

move_button = {"center": (int(600 * SCALE_X), int(750 * SCALE_Y)), "radius": int(80 * min(SCALE_X, SCALE_Y))}
action_confirm_button = {"center": (int(800 * SCALE_X), int(750 * SCALE_Y)), "radius": int(80 * min(SCALE_X, SCALE_Y))}

pending_action = None
pending_move = None

# ----------------- Timer personnalisé ------------------
game_timer = GameTimer(120)  # 2 minutes au lieu de 30 secondes pour plus de gameplay

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
    if max_value > 0:
        fill_width = int(gauge_width * value / max_value)
        pygame.draw.rect(screen, GAUGE_FILL, (x, y, fill_width, gauge_height))
        
    pygame.draw.rect(screen, BLACK, (x, y, gauge_width, gauge_height), 2)

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines

def get_current_node():
    """Retourne le noeud actuel du joueur"""
    return game_instance.player.position

def get_available_moves():
    """Retourne les mouvements possibles depuis la position actuelle"""
    current_node = get_current_node()
    return game_instance.map.node_neighbors(current_node)

def get_move_cost(destination_node):
    """Retourne le coût de déplacement vers un noeud"""
    current_node = get_current_node()
    return game_instance.map.get_weight(current_node, destination_node)

def can_afford_move(destination_node):
    """Vérifie si le joueur peut se permettre le déplacement"""
    cost = get_move_cost(destination_node)
    return game_instance.player.has_enough_resources(cost)

# ----------------- Fonction Principale d'affichage ---------
# ----------------- Fonction Principale d'affichage ---------
def draw_interface():
    global event_message
            
    screen.blit(background_image, (0, 0))
    screen.blit(ile_image, (ILE_X, ILE_Y))
    draw_text_centered("Carte de Galèrapagos", (ILE_X + int(400 * SCALE_X), int(40 * SCALE_Y)))

    mouse_pos = pygame.mouse.get_pos()
    current_node = get_current_node()
    current_zone = node_to_zone.get(current_node, "alpha")
    available_moves = get_available_moves()

    # Dessiner les zones
    for key, data in map_zones.items():
        node = zone_to_node[key]
        
        # Couleur selon l'état
        if key == current_zone:
            color = GREEN  # Position actuelle
        elif key == pending_move:
            color = BLUE  # Zone sélectionnée pour déplacement
        elif node in available_moves:
            if can_afford_move(node):
                color = BLUE if is_inside_circle(mouse_pos, data["center"], data["radius"]) else HIGHLIGHT
            else:
                color = RED  # Pas assez de ressources
        else:
            color = GRAY  # Non accessible
            
        pygame.draw.circle(screen, WHITE, data["center"], data["radius"])
        pygame.draw.circle(screen, color, data["center"], data["radius"], 3)
        
        # Nom de la zone (version courte)
        zone_short_name = key.capitalize()
        draw_text_centered(zone_short_name, data["center"], font=SMALL_FONT)

    # Message d'événement
    pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, ILE_X - int(20 * SCALE_X), int(100 * SCALE_Y)))
    draw_text_centered(event_message, (ILE_X // 2, int(40 * SCALE_Y)), font=SMALL_FONT)

    # Ressources du joueur
    player_resources = game_instance.player.dic_resources
    resources_rect = (int(40 * SCALE_X), int(120 * SCALE_Y), int(300 * SCALE_X), int(280 * SCALE_Y))
    pygame.draw.rect(screen, (240, 248, 255), resources_rect)
    
    draw_text_centered(f"Eau : {player_resources['water']}", (int(190 * SCALE_X), int(140 * SCALE_Y)), font=SMALL_FONT)
    draw_gauge(int(90 * SCALE_X), int(165 * SCALE_Y), player_resources["water"], 10)
    
    draw_text_centered(f"Nourriture : {player_resources['food']}", (int(190 * SCALE_X), int(200 * SCALE_Y)), font=SMALL_FONT)
    draw_gauge(int(90 * SCALE_X), int(225 * SCALE_Y), player_resources["food"], 10)
    
    draw_text_centered(f"Bois : {player_resources['wood']}", (int(190 * SCALE_X), int(260 * SCALE_Y)), font=SMALL_FONT)
    draw_gauge(int(90 * SCALE_X), int(285 * SCALE_Y), player_resources["wood"], 10)
    
    draw_text_centered(f"Santé : {game_instance.player.health}", (int(190 * SCALE_X), int(320 * SCALE_Y)), font=SMALL_FONT)
    draw_gauge(int(90 * SCALE_X), int(345 * SCALE_Y), game_instance.player.health, 50)

    # Boutons d'action
    current_resources = current_node.get_resources()
    for key, data in action_buttons.items():
        # Vérifier si la ressource est disponible
        available = current_resources.get(key, 0) > 0
        
        # Couleur selon l'état
        if key == pending_action:
            color = HIGHLIGHT  # Action sélectionnée
        elif available:
            color = BLUE
        else:
            color = GRAY
        
        pygame.draw.circle(screen, color, data["center"], data["radius"])
        icon_rect = data["icon"].get_rect(center=data["center"])
        screen.blit(data["icon"], icon_rect)
        
        if available and is_inside_circle(mouse_pos, data["center"], data["radius"]):
            pygame.draw.circle(screen, HIGHLIGHT, data["center"], data["radius"] + 3, 3)

    # Informations sur la zone actuelle
    desc_x = int(460 * SCALE_X)
    desc_y = int(280 * SCALE_Y)
    desc_width = int(410 * SCALE_X)
    desc_height = int(200 * SCALE_Y)
    pygame.draw.rect(screen, (230, 230, 230), (desc_x, desc_y, desc_width, desc_height), border_radius=8)

    current_zone_name = zone_noms.get(current_zone, "Zone inconnue")
    description = f"Position actuelle: {current_zone_name}\n\n"
    description += zone_descriptions.get(current_zone, "")
    description += f"\n\nRessources disponibles:\n"
    description += f"- Eau: {current_resources.get('water', 0)}\n"
    description += f"- Nourriture: {current_resources.get('food', 0)}\n"
    description += f"- Bois: {current_resources.get('wood', 0)}"

    lines = wrap_text(description, SMALL_FONT, desc_width - int(30 * SCALE_X))
    for i, line in enumerate(lines[:8]):  # Limiter le nombre de lignes
        text_surface = SMALL_FONT.render(line, True, BLACK)
        screen.blit(text_surface, (desc_x + int(15 * SCALE_X), desc_y + int(10 * SCALE_Y) + i * int(22 * SCALE_Y)))

    # Boutons de confirmation
    move_color = YELLOW if pending_move else GREEN
    pygame.draw.circle(screen, move_color, move_button["center"], move_button["radius"])
    draw_text_centered("Bouger", move_button["center"], font=SMALL_FONT)
    
    action_color = YELLOW if pending_action else GREEN
    pygame.draw.circle(screen, action_color, action_confirm_button["center"], action_confirm_button["radius"])
    draw_text_centered("Action", action_confirm_button["center"], font=SMALL_FONT)

    # Timer
    timer_text = f"Temps restant: {game_timer.remaining}s"
    draw_text_centered(timer_text, (int(700 * SCALE_X), int(80 * SCALE_Y)), RED, SMALL_FONT)

    # Journal d'actions (simplifié)
    journal_y = HEIGHT - int(200 * SCALE_Y)
    pygame.draw.rect(screen, (255, 255, 240), (int(20 * SCALE_X), journal_y, int(750 * SCALE_X), int(180 * SCALE_Y)), border_radius=5)
    draw_text_centered("Journal des actions", (int(195 * SCALE_X), journal_y + int(15 * SCALE_Y)), font=SMALL_FONT)
    
    # Afficher les dernières actions
    for i, log_entry in enumerate(action_log[-6:]):
        text_surface = SMALL_FONT.render(log_entry, True, BLACK)
        screen.blit(text_surface, (int(30 * SCALE_X), journal_y + int(35 * SCALE_Y) + i * int(20 * SCALE_Y)))

# ----------------- Traitement des actions ------------------
def process_action(action_type):
    global event_message
    
    current_node = get_current_node()
    current_resources = current_node.get_resources()
    
    if current_resources.get(action_type, 0) <= 0:
        event_message = f"Aucune {action_type} disponible ici."
        action_log.append(event_message)
        return
    
    # Utiliser la logique du jeu original
    amount = current_resources[action_type]
    
    if action_type == "water":
        game_instance.player.add_water(amount)
        current_node.remove_water()
        event_message = f"Vous avez récupéré {amount} d'eau."
    elif action_type == "food":
        game_instance.player.add_food(amount)
        current_node.remove_food()
        event_message = f"Vous avez récupéré {amount} de nourriture."
    elif action_type == "wood":
        game_instance.player.add_wood(amount)
        current_node.remove_wood()
        event_message = f"Vous avez récupéré {amount} de bois."
    
    action_log.append(event_message)

def process_move(destination_zone):
    global event_message
    
    if destination_zone not in zone_to_node:
        event_message = "Destination invalide."
        return
    
    destination_node = zone_to_node[destination_zone]
    current_node = get_current_node()
    
    if destination_node == current_node:
        event_message = "Vous êtes déjà ici."
        return
    
    if destination_node not in get_available_moves():
        event_message = "Cette zone n'est pas accessible."
        return
    
    move_cost = get_move_cost(destination_node)
    
    if not can_afford_move(destination_node):
        wat_cost, wood_cost, food_cost = move_cost
        event_message = f"Pas assez de ressources! Coût: {wat_cost} eau, {wood_cost} bois, {food_cost} nourriture"
        action_log.append(event_message)
        return
    
    # Effectuer le déplacement
    game_instance.player.rm_from_weight(move_cost)
    game_instance.player.set_position(destination_node)
    
    wat_cost, wood_cost, food_cost = move_cost
    destination_name = zone_noms.get(destination_zone, destination_zone)
    event_message = f"Déplacement vers {destination_name}. Coût: {wat_cost} eau, {wood_cost} bois, {food_cost} nourriture"
    action_log.append(event_message)

def check_game_over():
    global game_running, event_message
    
    if game_instance.player.get_health() <= 0:
        event_message = "Vous êtes mort par manque de santé!"
        game_running = False
        return True
    elif game_instance.player.get_food() <= 0:
        event_message = "Vous êtes mort de faim!"
        game_running = False
        return True
    elif game_instance.player.get_water() <= 0:
        event_message = "Vous êtes mort de soif!"
        game_running = False
        return True
    return False

def check_game_win():
    global has_won, game_running, event_message
    if game_instance.player.get_wood() >= 6 and game_instance.player.get_water() >= 6:
        event_message = "Vous avez réussi à vous échappez !"
        game_running = False
        has_won = True
        return True
    

# ----------------- Boucle principale -----------------------
def main():
    global selected_zone, pending_action, pending_move, game_running, timer_started, has_won

    clock = pygame.time.Clock()
    
    # Démarrer le timer
    if not timer_started:
        game_timer.start()
        timer_started = True
        action_log.append("Le jeu commence ! Vous avez 2 minutes pour survivre.")

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # Clic sur les zones de la carte
                for zone_key, data in map_zones.items():
                    if is_inside_circle(pos, data["center"], data["radius"]):
                        node = zone_to_node[zone_key]
                        if node in get_available_moves() and can_afford_move(node):
                            pending_move = zone_key
                            selected_zone = zone_key
                        break

                # Clic sur les boutons d'action
                for action, data in action_buttons.items():
                    if is_inside_circle(pos, data["center"], data["radius"]):
                        current_resources = get_current_node().get_resources()
                        if current_resources.get(action, 0) > 0:
                            pending_action = action
                        break

                # Bouton de déplacement
                if is_inside_circle(pos, move_button["center"], move_button["radius"]):
                    if pending_move:
                        process_move(pending_move)
                        pending_move = None

                # Bouton d'action
                if is_inside_circle(pos, action_confirm_button["center"], action_confirm_button["radius"]):
                    if pending_action:
                        process_action(pending_action)
                        pending_action = None

        # Vérifier les conditions de fin de jeu
        if check_game_over() or check_game_win():
            break

        draw_interface()
        pygame.display.flip()
        clock.tick(30)

    # Ecran de fin jeu si joueur à gagné ! 
    if has_won:
        screen.fill(BLACK)
        draw_text_centered("Vous avez gagné !", (WIDTH//2, HEIGHT//2), WHITE)
        draw_text_centered("Appuyez sur une touche pour quitter", (WIDTH//2, HEIGHT//2 + 50), WHITE, SMALL_FONT)
        pygame.display.flip()
    
    else :
        # Ecran de fin de jeu
        screen.fill(BLACK)
        draw_text_centered("GAME OVER !", (WIDTH//2, HEIGHT//2), WHITE)
        draw_text_centered("Appuyez sur une touche pour quitter", (WIDTH//2, HEIGHT//2 + 50), WHITE, SMALL_FONT)
        pygame.display.flip()
    
    # Attendre une touche pour quitter
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False

    pygame.quit()
    sys.exit()

# ----------------- Lancement du programme ------------------
if __name__ == "__main__":
    main()