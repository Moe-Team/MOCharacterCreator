from character import AtlasedCharacter, CharacterLoadingError, PNGCharacter
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.app import App


class CharacterLoader(RelativeLayout):
    pass


class AtlasedCharacterLoader(CharacterLoader):
    filechooser = ObjectProperty(None)

    def __init__(self, cancel_func, character_display, root, **kwargs):
        super(AtlasedCharacterLoader, self).__init__(**kwargs)
        self.character = None
        self.cancel = cancel_func
        self.character_display = character_display
        self.root = root
        self.ready()

    def ready(self):
        config = App.get_running_app().config
        self.filechooser.path = config.get('path', 'root_path')
        self.filechooser.bind(path=self.update_popup_title)

    def update_popup_title(self, inst, val):
        popup = self.root.popup
        popup.title = val

    def load_character(self, directories):
        try:
            self.character = AtlasedCharacter(directories[0])
        except CharacterLoadingError as e:
            print("File not found: {0}".format(e.file))
            return
        self.character_display.character = self.character
        self.cancel(self.filechooser.path)


class PNGCharacterLoader(CharacterLoader):
    filechooser = ObjectProperty(None)

    def __init__(self, cancel_func, character_display, root, **kwargs):
        super(PNGCharacterLoader, self).__init__(**kwargs)
        self.character = None
        self.cancel = cancel_func
        self.character_display = character_display
        self.root = root
        self.ready()

    def ready(self):
        config = App.get_running_app().config
        self.filechooser.path = config.get('path', 'root_path')
        self.filechooser.bind(path=self.update_popup_title)

    def update_popup_title(self, inst, val):
        popup = self.root.popup
        popup.title = val

    def load_character(self, directories):
        try:
            self.character = PNGCharacter(directories[0])
        except CharacterLoadingError as e:
            print("File not found: {0}".format(e.file))
            return
        self.character_display.character = self.character
        self.cancel(self.filechooser.path)
