import pygame

class Menu:
    def __init__(self, screen):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800
        self.BUTTON_WIDTH = 200
        self.BUTTON_HEIGHT = 50
        self.BUTTON_SPACING = 10
        self.BUTTON_COLOR = (255, 255, 255)
        self.BUTTON_HOVER_COLOR = (150, 150, 150)
        self.TEXT_COLOR = (0, 0, 0)
        self.FONT_SIZE = 32
        self.FONT_NAME = 'Arial'
        self.background = pygame.image.load("assets/background.jpg")
        self.background = pygame.transform.scale(self.background, (800, 800))
        self.is_running = True
        self.screen = screen
        self.font = pygame.font.SysFont(self.FONT_NAME, self.FONT_SIZE)
    def get_menu(self):
        pygame.init()
        while self.is_running:
            pygame.display.update()
            self.screen.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
            start_button = self.create_button('Start',
                                              self.SCREEN_WIDTH / 2 - self.BUTTON_WIDTH / 2,
                                              self.SCREEN_HEIGHT / 2 - self.BUTTON_HEIGHT - self.BUTTON_SPACING,
                                              self.BUTTON_WIDTH,
                                              self.BUTTON_HEIGHT,
                                              self.BUTTON_COLOR,
                                              self.BUTTON_HOVER_COLOR)
            quit_button = self.create_button('Quit',
                                             self.SCREEN_WIDTH / 2 - self.BUTTON_WIDTH / 2,
                                             self.SCREEN_HEIGHT / 2 + self.BUTTON_SPACING,
                                             self.BUTTON_WIDTH,
                                             self.BUTTON_HEIGHT,
                                             self.BUTTON_COLOR,
                                             self.BUTTON_HOVER_COLOR)
            if start_button:
                running = False
                return True
            elif quit_button:
                running = False
                pygame.quit()

    def create_button(self, text, x, y, width, height, inactive_color, active_color):
        pygame.init()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen.screen, active_color, (x, y, width, height))
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(self.screen.screen, inactive_color, (x, y, width, height))

        text_surface = self.font.render(text, True, self.TEXT_COLOR)
        text_rect = text_surface.get_rect(
            center=(x + width / 2, y + height / 2))
        self.screen.screen.blit(text_surface, text_rect)

        return False

