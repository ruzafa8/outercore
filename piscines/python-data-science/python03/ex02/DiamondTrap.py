from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Who is that Character?... Is... King!!!"""
    def __init__(self, first_name):
        """Who is that Character?... Is... King!!!"""
        Lannister.__init__(self, first_name=first_name)
        Baratheon.__init__(self, first_name=first_name)

    def get_eyes(self):
        """Eyes getter"""
        return self.eyes

    def set_eyes(self, eyes):
        """Eyes setter"""
        self.eyes = eyes

    def get_hairs(self):
        """Hairs getter"""
        return self.hairs

    def set_hairs(self, hairs):
        """Haris setter"""
        self.hairs = hairs
