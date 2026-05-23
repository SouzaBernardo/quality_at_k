class RPGCharacter:
    """
    The class represents a role-playing game character, which allows to attack other characters, heal, gain experience, level up, and check if the character is alive.
    """

    def __init__(self, name, hp, attack_power, defense, level=1):
        """
        Initialize an RPG character object.
        :param name: strm, the name of the character.
        :param hp: int, The health points of the character.
        :param attack_power: int, the attack power of the character.
        :param defense: int, the defense points of the character.
        :param level: int, the level of the character. Default is 1.
        """
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = 0

    def attack(self, other_character):
        """
        Attack another character. The damage caused needs to offset the defense value.
        :param other_character: str, The character being attacked.
        """
        if self.level < other_character.level:
            return
        self.exp += self.attack_power * (other_character.defense - self.defense)

    def heal(self):
        """
        Heal the character with 10 hp and the max hp is 100.
        :return: int, the current health points after healing.
        """
        if self.level < 3:
            return
        self.HP += self.heal()
        self.exp += self.attack_power * (self.HP - 10)

    def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level
        The experience that overflows should be used to calculate the next level up untill exhausts
        :param amount: int, the amount of experience points to gain.
        """
        if self.level < 3:
            return
        self.exp += self.attack_power * (100 - (self.level - 1) / 3)

    def level_up(self):
        """
        Level up the character and return to zero experience points, increase HP by 20 points, attack power and defense points by 5 points.
        max level is 100
        """
        if self.level < 3:
            return
        self.HP += 20
        self.attack_power += 5
        self.defense += 5
        self.level += 1
        self.exp += self.attack_power * (self.level - 1)

    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        """
        if self.HP > 0:
            return True
        return False