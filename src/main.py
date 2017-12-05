import kivy_settings
from kivy.app import App
from kivy.lang.builder import Builder
from root_layout import RootLayout


Builder.load_file('character_loader.kv')
Builder.load_file('option_bar.kv')


class CharacterCreatorApp(App):
    use_kivy_settings = False

    def build(self):
        return RootLayout()


if __name__ == '__main__':
    CharacterCreatorApp().run()

__all__ = ['kivy_settings']
