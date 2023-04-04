import pygame
from decoration import Sky


class Registration:
    def __init__(self, surface):
        """
        :param surface: display surface
        """

        # user
        self.user_text = 'user1'
        self.text_before = 'Enter your username:'

        # setup
        self.input_rect = pygame.Rect(200, 310, 300, 40)
        self.box_color = pygame.Color('#b86574')
        self.user_text_color = pygame.Color('#9c4857')
        self.text_before_color = pygame.Color('#394c5f')
        self.surface = surface
        self.base_font = pygame.font.Font('graphics/ui/ARCADEPI.TTF', 30)
        self.sky = Sky(8, 'overworld')

    def input_text(self):
        keys = pygame.key.get_pressed()

        for letter in range(pygame.K_a, pygame.K_z+1):
            if keys[pygame.K_BACKSPACE]:
                self.user_text = self.user_text[:-1]
            elif keys[letter] and len(self.user_text) < 10:
                self.user_text += pygame.key.name(letter)
                pygame.time.delay(150)

    def text_surf(self, text, txt_color, x, y):
        text_surface = self.base_font.render(text, True, txt_color)
        self.surface.blit(text_surface, (self.input_rect.x + x, self.input_rect.y + y))

    def run(self):
        self.sky.draw(self.surface)
        pygame.draw.rect(self.surface, self.box_color, self.input_rect, 2, border_radius=12)
        self.input_text()
        self.text_surf(self.text_before, self.text_before_color, 0, -37)
        self.text_surf(self.user_text, self.user_text_color, 5, 5)


class Button:
    def __init__(self, text, width, height, pos, elevation, surface, create_overworld):
        """
        :param text: text on button
        :param width: button width
        :param height: button height
        :param pos: button position
        :param elevation: high of button press
        :param surface: display surface
        :param create_overworld: create overworld form
        """

        gui_font = pygame.font.Font('graphics/ui/ARCADEPI.TTF', 30)
        self.surface = surface
        self.create_overworld = create_overworld

        # core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # top rect
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # bottom rect
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#354B5E'

        # text
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.surface, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(self.surface, self.top_color, self.top_rect, border_radius=12)
        self.surface.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#b86574'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    self.create_overworld(0, 1)
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'


