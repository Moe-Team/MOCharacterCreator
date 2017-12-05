from kivy.uix.boxlayout import BoxLayout
from character_loader import CharacterLoader
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty


class OptionBar(BoxLayout):
    character_display = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(OptionBar, self).__init__(**kwargs)
        self._popup = None

    def open_character_loader(self):
        content = CharacterLoader(self.cancel, self.character_display)
        self._popup = Popup(title="Load a character", content=content, size_hint=(0.89, 0.89))
        self._popup.open()

    def cancel(self):
        self._popup.dismiss()
