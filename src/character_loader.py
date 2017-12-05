from character import Character
from kivy.uix.relativelayout import RelativeLayout


class CharacterLoader(RelativeLayout):

    def __init__(self, cancel, **kwargs):
        super(CharacterLoader, self).__init__(**kwargs)
        self.character = None
        self.cancel = cancel

    def load_character(self, folder):
        self.character = Character(folder)
