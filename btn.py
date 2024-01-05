import pygame
# Инициализация
pygame.init()

# Ширина, Высота, ФПС-none
S_WIDTH = 700
S_HEIGHT = 500
# FPS = 60
# FramePerSecond = pygame.time.Clock(FPS)

# Создание окна и его тайтл
SURFACE = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('Тесты прямоугольников')

#Параметры прямоугольника
RED = (255, 0, 0)
Green = (0, 255, 0)

# pygame.draw.rect(surface, color, rect(x, y, width, height), width=0)

# Прямоугольник x=50 y=50 weight = 60 height=20
pygame.draw.rect(SURFACE, RED, (50, 50, 60, 20))

# Прямоугольник x=50 y=50 weight = 60 height=20


class Button:
    def __init__(self, Pos_x, Pos_y, width, height, text, color, hover_color, text_color):
        self.Pos_x = Pos_x
        self.Pos_y = Pos_y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False

    def draw(self, window):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.Pos_x  < mouse_x < self.Pos_x + self.width and self.Pos_y < mouse_y < self.Pos_y + self.height:
            self.is_hovered = True
        else:
            self.is_hovered = False

        if self.is_hovered:
            pygame.draw.rect(window, self.hover_color, (self.Pos_x, self.Pos_y, self.width, self.height))
        else:
            pygame.draw.rect(window, self.color, (self.Pos_x, self.Pos_y, self.width, self.height))

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.Pos_x + self.width / 2, self.Pos_y + self.height / 2))
        window.blit(text_surface, text_rect)











button_Play = Button(100, 100, 221, 2, 'Играть', RED, Green, (255,255,255))
# Обновление экрана

# Ожидание закрытия окна
Open = True
while Open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Open = False
    button_Play.draw(SURFACE)
    pygame.display.flip()

pygame.quit()

