from character import Character, CharacterLoadingError
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.app import App


class CharacterLoader(RelativeLayout):
    filechooser = ObjectProperty(None)

    def __init__(self, cancel_func, character_display, **kwargs):
        super(CharacterLoader, self).__init__(**kwargs)
        self.character = None
        self.cancel = cancel_func
        self.character_display = character_display
        self.ready()

    def ready(self):
        config = App.get_running_app().config
        self.filechooser.path = config.get('path', 'root_path')

    def load_character(self, directories):
        try:
            self.character = Character(directories[0])
        except CharacterLoadingError as e:
            print("File not found: {0}".format(e.file))
            return
        self.character_display.character = self.character
