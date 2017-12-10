from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.uix.image import Image


SPRITE_BUTTON_WIDTH = 250
SPRITE_BUTTON_HEIGHT = 250


class SpriteButton(Image):

    def __init__(self, **kwargs):
        super(SpriteButton, self).__init__(**kwargs)


class CharacterDisplay(RelativeLayout):
    character = ObjectProperty(None)
    sprite_layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CharacterDisplay, self).__init__(**kwargs)

    def on_character(self, inst, character):
        self.display_character()

    def display_character(self):
        self.display_sprites()

    def display_sprites(self):
        sprites_per_page = self.calculate_sprites_per_page()
        for i in range(sprites_per_page):
            self.add_sprite(i)

    def add_sprite(self, index):
        sprite_button = SpriteButton()
        key = self.character.icon_keys[index]
        sprite_button.texture = self.character.get_sprite(key)
        self.sprite_layout.add_widget(sprite_button)

    def calculate_sprites_per_page(self):
        width = self.width
        height = self.height - 30
        rows = int(self.width / SPRITE_BUTTON_WIDTH)
        cols = int(self.height / SPRITE_BUTTON_HEIGHT)
        sprite_number = rows * cols
        return sprite_number
