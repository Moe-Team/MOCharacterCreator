from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty


class CharacterDisplay(RelativeLayout):
    character = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CharacterDisplay, self).__init__(**kwargs)

    def on_character(self, inst, value):
        pass
