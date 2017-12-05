from character import Character
from kivy.uix.relativelayout import RelativeLayout


class CharacterLoader(RelativeLayout):

    def __init__(self, cancel_func, character_display, **kwargs):
        super(CharacterLoader, self).__init__(**kwargs)
        self.character = None
        self.cancel = cancel_func
        self.character_display = character_display

    def load_character(self, directories):
        self.character = Character(directories[0])
        self.character_display.character = self.character
