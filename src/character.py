import os
from kivy.config import ConfigParser
from kivy.atlas import Atlas
from icarus import Icarus
from kivy.uix.image import Image


class CharacterError(Exception):
    pass


class CharacterLoadingError(CharacterError):

    def __init__(self, file):
        self.file = file


class AtlasedCharacterDirParser:

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


class PNGCharacterDirParser:

    def __init__(self, directory):
        self.dir = directory

    def find_icons(self):
        if 'icons' in os.listdir(self.dir):
            return os.path.join(self.dir, 'icons')
        return None

    def find_sprites(self):
        for file in os.listdir(self.dir):
            if file.endswith('.png'):
                return self.dir
        return None


class Character:

    def load(self, directory):
        self.load_icons()
        self.load_sprites()
        self.load_settings()

    def extract_name(self, directory):
        dirs = directory.split(os.sep)
        name = dirs[-1]
        return name

    def load_icons(self):
        pass

    def load_sprites(self):
        pass

    def load_settings(self):
        pass


class AtlasedCharacter(Character):

    def __init__(self, directory):
        self.dir_parser = AtlasedCharacterDirParser(directory)
        self.sprites = None
        self.icon_keys = []
        self.icons = None
        self.name = self.extract_name(directory)
        self.config_parser = ConfigParser()
        self.load(directory)

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

    def get_sprite(self, key):
        return self.sprites[key]

    def get_sprite_number(self):
        return len(self.icon_keys)

    def get_sprite_name_by_index(self, index):
        return self.icon_keys[index]


class PNGSprite(Image):
    pass


class PNGCharacter(Character):

    def __init__(self, directory):
        self.dir_parser = PNGCharacterDirParser(directory)
        self.icons = {}
        self.icon_keys = []
        self.sprites = {}
        self.name = self.extract_name(directory)
        self.load(directory)

    def load_icons(self):
        icons_dir = self.dir_parser.find_icons()
        for icon_path in os.listdir(icons_dir):
            icon_name = self.extract_name(icon_path)
            self.icon_keys.append(icon_name)
            self.icons[icon_name] = None

    def load_sprites(self):
        sprites_dir = self.dir_parser.find_sprites()
        for sprite_path in os.listdir(sprites_dir):
            if sprite_path.endswith('.png'):
                sprite_name = self.extract_name(sprite_path)
                self.sprites[sprite_name] = None

    def load_settings(self):
        pass

    def get_sprite(self, key):
        if self.sprites[key] is None:
            sprite_path = os.path.join(self.dir_parser.find_sprites(), key)
            self.sprites[key] = PNGSprite(source=sprite_path)
        return self.sprites[key].texture

    def get_sprite_number(self):
        return len(self.sprites)

    def get_sprite_name_by_index(self, index):
        return self.icon_keys[index]
