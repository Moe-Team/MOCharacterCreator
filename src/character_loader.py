from character import Character, CharacterLoadingError
from kivy.uix.relativelayout import RelativeLayout


class CharacterLoader(RelativeLayout):

    def __init__(self, cancel_func, character_display, **kwargs):
        super(CharacterLoader, self).__init__(**kwargs)
        self.character = None
        self.cancel = cancel_func
        self.character_display = character_display

    def load_character(self, directories):
        try:
            self.character = Character(directories[0])
        except CharacterLoadingError as e:
            print("File not found: {0}".format(e.file))
            return
        self.character_display.character = self.character
