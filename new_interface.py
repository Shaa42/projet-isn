selected_location = None
choosing_resource = False

def choose_resource_interface():
    pygame.draw.rect(screen, LIGHT_GRAY, (150, 550, 900, 180))
    draw_text("Choisissez une ressource à récolter :", (180, 580))
    options = ["eau", "nourriture", "bois"]
    for i, option in enumerate(options):
        rect = pygame.Rect(200 + i*300, 620, 200, 60)
        pygame.draw.rect(screen, BLUE, rect)
        draw_text(option.capitalize(), (rect.x + 50, rect.y + 20), WHITE)
    return options

def handle_resource_choice(mouse_pos):
    global choosing_resource, selected_location, event_message
    options = ["eau", "nourriture", "bois"]
    for i, option in enumerate(options):
        rect = pygame.Rect(200 + i*300, 620, 200, 60)
        if rect.collidepoint(mouse_pos):
            resources[option] += 2
            event_message = f"Vous avez récolté {option} dans la zone {selected_location} !"
            choosing_resource = False
            selected_location = None
            return

def process_location(location):
    global event_message, choosing_resource, selected_location
    if resources["eau"] < 1 or resources["nourriture"] < 2:
        event_message = "Pas assez de ressources pour explorer ! (1 eau + 2 nourriture)"
        return

    resources["eau"] -= 1
    resources["nourriture"] -= 2
    selected_location = location
    choosing_resource = True
    event_message = f"Vous explorez {location}. Choisissez une ressource à récolter."

def main():
    global choosing_resource
    clock = pygame.time.Clock()
    running = True

    while running:
        draw_interface()

        if choosing_resource:
            choose_resource_interface()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if choosing_resource:
                    handle_resource_choice(mouse_pos)
                else:
                    for key, rect in action_buttons.items():
                        if rect.collidepoint(mouse_pos):
                            process_action(key)

                    for key, rect in map_zones.items():
                        if rect.collidepoint(mouse_pos):
                            process_location(key)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()
