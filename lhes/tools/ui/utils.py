def draw_text(display_surface, text, font, color, position, anchor='topleft'):
    display_rect = display_surface.get_rect()
    text_surf = font.render(str(text), False, color)
    text_rect = text_surf.get_rect(topleft=(0, 0))
    if "top" in anchor:
        text_rect.y += position[1]
    if "bottom" in anchor:
        text_rect.y = display_rect.height - text_rect.height - position[1]
    if "left" in anchor:
        text_rect.x += position[0]
    if "right" in anchor:
        text_rect.x = display_rect.width - text_rect.width - position[0]
    if 'center' in anchor:
        text_rect.x = (display_rect.width - text_rect.width - position[0]) // 2
        text_rect.y = (display_rect.height - text_rect.height - position[1]) // 2
    display_surface.blit(text_surf, text_rect)
