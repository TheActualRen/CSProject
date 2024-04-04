import pygame
from object import Object

class Melon(Object):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, "melon")  # Adjust width and height as needed
        self.melon_sheet = pygame.image.load("assets/Items/Fruits/Melon.png")
        self.melon_frames = self.split_frames(self.melon_sheet)
        self.frame_index = 0
        self.image = self.melon_frames[self.frame_index]
        self.mask = pygame.mask.from_surface(self.image)

    def split_frames(self, sheet):
        frame_width = 32
        frame_height = 32
        frames = []
        for i in range(sheet.get_width() // frame_width):
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sheet.subsurface(rect)
            frames.append(frame)
        return frames

    def loop(self):
        self.frame_index = (self.frame_index + 1) % len(self.melon_frames)
        self.image = self.melon_frames[self.frame_index]
        self.mask = pygame.mask.from_surface(self.image)