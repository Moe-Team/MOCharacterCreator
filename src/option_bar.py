from kivy.uix.boxlayout import BoxLayout
from character_loader import CharacterLoader
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.app import App


class OptionBar(BoxLayout):
    character_display = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(OptionBar, self).__init__(**kwargs)
        self.popup = None

    def open_character_loader(self):
        content = CharacterLoader(self.cancel, self.character_display, self)
        config = App.get_running_app().config
        path = config.get('path', 'root_path')
        self.popup = Popup(title=path, content=content, size_hint=(0.89, 0.89))
        self.popup.open()

    def cancel(self, path):
        config = App.get_running_app().config
        config.set('path', 'root_path', path)
        config.write()
        self.popup.dismiss()
