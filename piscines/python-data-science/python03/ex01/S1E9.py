from abc import ABC, abstractmethod


class Character(ABC):
    """This is a Character :D"""
    def __init__(self, first_name, is_alive=True):
        """Character constructor!! Just need a name and
        if it alive (optional)"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """If you like this character, avoid calling this fn"""
        pass


class Stark(Character):
    """This is (most probably) a famous character"""
    def die(self):
        """If you don't like Stark, you would like to call this fn"""
        self.is_alive = False
