from S1E9 import Character


class Baratheon(Character):
    """Who is that Character?... Is... Baratheon!!!"""
    def __init__(self, first_name):
        """Baratheon constructor!!!"""
        super().__init__(first_name)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """If you don't like this character,
        you would like to call this fn"""
        self.is_alive = False

    def __repr__(self):
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Who is that Character?... Is... Lannister!!!"""
    def __init__(self, first_name, is_alive=True):
        """Lannister constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """If you don't like this character,
        you would like to call this fn"""
        self.is_alive = False

    def __repr__(self):
        """Internal representation of a Lannister"""
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        """Visual representation of a Lannister"""
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """This method instanciates a new Lannister ;)"""
        return cls(first_name, is_alive)
