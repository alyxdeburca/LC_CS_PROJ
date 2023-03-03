import pygame
import string

screen = pygame.display.set_mode((1280, 720))

class spriteSheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            print('Unable to load spritesheet image:', filename)
            raise SystemExit(message)

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey=None):
        """Loads image from x,y,x+offset,y+offset"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey=None):
        """Loads multiple images, supply a list of coordinates"""
        return [self.image_at(rect, colorkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey=None):
        """Loads a strip of images and returns them as a list"""
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)


def drawText(prompt, sheet, xy, surface, scale):
    ss = spriteSheet(sheet)
    images = ss.load_strip(rect=(0, 0, 9, 9), image_count=16, colorkey=None)
    images.extend(ss.load_strip(rect=(0, 9, 9, 9), image_count=16, colorkey=None))
    images.extend(ss.load_strip(rect=(0, 18, 9, 9), image_count=16, colorkey=None))
    numsheet = images[32:]
    alphabet = images[:26]
    i = 0
    lastletter = ""
    for letter in prompt:
        if letter == " ":
            pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(xy[0], xy[1] + (i * 80), 80, 80))
        elif letter.isalpha():
            if lastletter == letter:
                image = alphabet[string.ascii_lowercase.index(lastletter.lower())]
                image = pygame.transform.scale(image, (80, 80))
                surface.blit(image, (xy[0] + (prompt.index(lastletter) + 1) * 80 + 1, xy[1]))
            else:
                image = alphabet[string.ascii_lowercase.index(letter.lower())]
                image = pygame.transform.scale(image, (80, 80))
                surface.blit(image, (xy[0] + (i * 80) + 1, xy[1]))
        else:
            if lastletter == letter:
                image = numsheet[int(lastletter)]
                image = pygame.transform.scale(image, (80, 80))
                surface.blit(image, (xy[0] + (prompt.index(lastletter) + 1) * 80 + 1, xy[1]))
            else:
                image = numsheet[int(letter)]
                image = pygame.transform.scale(image, (80, 80))
                surface.blit(image, (xy[0] + (i * 80) + 1, xy[1]))
        i = i + 1
        lastletter = letter

# while True:
#     drawText("Help", "assets/fonts/Font.png", (0, 0), screen, 1)
#     pygame.display.flip()
