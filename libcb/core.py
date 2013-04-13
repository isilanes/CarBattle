import pygame

#------------------------------------------------------------------------------#

def load_car_png(name):
    fn = 'img/cars/' + name
    image = pygame.image.load(fn)
    if image.get_alpha():
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image, image.get_rect()

#------------------------------------------------------------------------------#
