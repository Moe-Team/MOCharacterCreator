from character import Character
from kivy.uix.floatlayout import FloatLayout


class CharacterLoader(FloatLayout):

    def __init__(self, cancel, **kwargs):
        super(CharacterLoader, self).__init__(**kwargs)
        self.character = None
        self.cancel = cancel

    def load_character(self, folder):
        self.character = Character(folder)
