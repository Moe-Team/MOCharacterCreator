from character import AtlasedCharacter, CharacterLoadingError, PNGCharacter
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class CharacterLoader(RelativeLayout):
    filechooser = ObjectProperty(None)

    def __init__(self, cancel_func, character_display, root, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        self.character = None
        self.cancel = cancel_func
        self.character_display = character_display
        self.root = root
        self.ready()

    def display_error_popup(self, e):
        label = Label(text="Missing file: {}".format(e.file))
        popup = Popup(title="Error loading character", content=label)
        popup.open()

    def update_popup_title(self, inst, val):
        popup = self.root.popup
        popup.title = val

    def ready(self):
        config = App.get_running_app().config
        self.filechooser.path = config.get('path', 'root_path')
        self.filechooser.bind(path=self.update_popup_title)


class AtlasedCharacterLoader(CharacterLoader):

    def load_character(self, directories):
        try:
            self.character = AtlasedCharacter(directories[0])
        except CharacterLoadingError as e:
            self.display_error_popup(e)
            return
        self.character_display.character = self.character
        self.cancel(self.filechooser.path)


class PNGCharacterLoader(CharacterLoader):

    def load_character(self, directories):
        try:
            self.character = PNGCharacter(directories[0])
        except CharacterLoadingError as e:
            self.display_error_popup(e)
            return
        self.character_display.character = self.character
        self.cancel(self.filechooser.path)
