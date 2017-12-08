import kivy_settings
from kivy.app import App
from kivy.lang.builder import Builder
from root_layout import RootLayout
import os


Builder.load_file('character_loader.kv')
Builder.load_file('option_bar.kv')
Builder.load_file('character_display.kv')


class CharacterCreatorApp(App):
    use_kivy_settings = False

    def build(self):
        return RootLayout()

    def build_config(self, config):
        config.setdefaults('path', {
            'root_path': os.getcwd()
        })

    def build_settings(self, settings):
        settings.add_json_panel('Main', self.config, 'settings.json')


if __name__ == '__main__':
    CharacterCreatorApp().run()

__all__ = ['kivy_settings']
