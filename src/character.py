import os
from kivy.config import ConfigParser
from kivy.atlas import Atlas
from icarus import Icarus


class CharacterError(Exception):
    pass


class CharacterLoadingError(CharacterError):

    def __init__(self, file):
        self.file = file


class CharacterDirParser:

    def __init__(self, directory):
        self.dir = directory

    def find_settings(self):
        settings = self.find_file("settings.ini")
        return settings

    def find_sprite_atlas(self):
        return self.find_file("sprites.atlas")

    def find_icon_atlas(self):
        return self.find_file("icons.atlas")

    def find_file(self, target):
        for file in os.listdir(self.dir):
            if file == target:
                return os.path.join(self.dir, file)
        return None


class Character:

    def __init__(self, directory):
        self.dir_parser = None
        self.sprites = None
        self.icon_keys = []
        self.icons = None
        self.name = self.extract_name(directory)
        self.config_parser = ConfigParser(self.name)
        self.load(directory)

    def load(self, directory):
        self.dir_parser = CharacterDirParser(directory)
        self.load_settings()
        self.load_sprites()
        self.load_icons()

    def load_icons(self):
        icon_atlas_path = self.dir_parser.find_icon_atlas()
        if icon_atlas_path is None:
            raise CharacterLoadingError("icons.atlas")
        self.icons = Atlas(icon_atlas_path)
        self.icon_keys = sorted(list(self.icons.textures.keys()))

    def load_sprites(self):
        sprite_atlas_path = self.dir_parser.find_sprite_atlas()
        if sprite_atlas_path is None:
            raise CharacterLoadingError("sprites.atlas")
        self.sprites = Icarus(sprite_atlas_path)

    def load_settings(self):
        settings = self.dir_parser.find_settings()
        if settings is None:
            raise CharacterLoadingError("settings.ini")
        self.config_parser.read(settings)

    def extract_name(self, directory):
        dirs = directory.split(os.sep)
        name = dirs[-1]
        return name

    def get_sprite(self, key):
        return self.sprites[key]

    def get_sprite_number(self):
        return len(self.icon_keys)
