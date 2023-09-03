import pygame


# Helper function to scale image
def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))


def get_mouse_released(mouse_button: int) -> bool:
    """
    Helper function to check if mouse button was released
    1 - Left Mouse Button
    2 - Middle Mouse Button
    3 - Right Mouse Button
    """
    event = pygame.event.get(pygame.MOUSEBUTTONUP)
    if event:
        if event[0].button == mouse_button:
            return True
