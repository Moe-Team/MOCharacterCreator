from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
import math


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
        self.max_pages = 0
        self.page = 0

    def on_size(self, *args):
        if self.character is not None:
            self.page = 0
            self.display_character()

    def previous_page(self):
        if self.page > 0:
            self.page -= 1
            self.display_sprites()

    def next_page(self):
        if self.page < self.max_pages - 1:
            self.page += 1
            self.display_sprites()

    def on_character(self, inst, character):
        self.page = 0
        self.display_character()

    def display_character(self):
        self.calculate_max_pages()
        self.display_sprites()

    def calculate_max_pages(self):
        sprites_per_page = self.calculate_sprites_per_page()
        sprite_number = self.character.get_sprite_number()
        self.max_pages = math.ceil(sprite_number / sprites_per_page)

    def display_sprites(self):
        self.clear_page()
        sprites_per_page = self.calculate_sprites_per_page()
        offset = self.page * sprites_per_page
        for i in range(offset, sprites_per_page + offset):
            if i == self.character.get_sprite_number():
                return
            self.add_sprite(i)

    def clear_page(self):
        self.sprite_layout.clear_widgets()

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
