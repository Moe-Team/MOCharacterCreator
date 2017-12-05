from kivy.uix.anchorlayout import AnchorLayout
from character_loader import CharacterLoader
from kivy.uix.popup import Popup


class RootLayout(AnchorLayout):

    def __init__(self, **kwargs):
        super(RootLayout, self).__init__(**kwargs)
        self._popup = None

    def open_character_loader(self):
        content = CharacterLoader(self.cancel)
        self._popup = Popup(title="Load a character", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def cancel(self):
        self._popup.dismiss()
