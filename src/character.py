import os
from kivy.config import ConfigParser


class CharacterDirParser:

    def __init__(self, directory):
        self.dir = directory

    def find_settings(self):
        for file in os.listdir(self.dir):
            if file == "settings.ini":
                return os.path.join(self.dir, file)


class Character:

    def __init__(self, directory):
        self.dir_parser = None
        self.name = self.extract_name(directory)
        self.config_parser = ConfigParser(self.name)
        self.load(directory)

    def load(self, directory):
        self.dir_parser = CharacterDirParser(directory)
        settings = self.dir_parser.find_settings()

    def extract_name(self, directory):
        dirs = directory.split(os.sep)
        name = dirs[-1]
        return name
