from kivy.app import App
from character_loader import CharacterLoader
from root_layout import RootLayout


class CharacterCreatorApp(App):
    use_kivy_settings = False

    def build(self):
        return RootLayout()


if __name__ == '__main__':
    CharacterCreatorApp().run()


__all__ = ['CharacterLoader']
