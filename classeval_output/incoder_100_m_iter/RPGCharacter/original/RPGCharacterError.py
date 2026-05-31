
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
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_2 = RPGCharacter('player 2', 100, 7, 2)
        >>> player_1.attack(player_2)
        >>> player_2.hp
        92
        """
        damage = self.attack_power - other_character.defense
        other_character.hp -= damage
        if other_character.hp <= 0:
            other_character.hp = 0
            other_character.level -= 1
            other_character.exp += damage
            print('{} has killed {}!'.format(self.name, other_character.name))
        else:
            print('{} has {} damage from {}!'.format(self.name, damage, other_character.name))


    def heal(self):
        """
        Heal the character with 10 hp and the max hp is 100.
        :return: int, the current health points after healing.
        >>> player_1 = RPGCharacter('player 1', 93, 10, 3)
        >>> player_1.heal()
        100
        """
        heal_hp = self.hp + 10
        if heal_hp > 100:
            heal_hp = 100
        self.hp = heal_hp
        print('{} has healed {} hp!'.format(self.name, self.hp))
        return self.hp


    def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level
        The experience that overflows should be used to calculate the next leve up untill exhausts
        :param amount: int, the amount of experience points to gain.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.gain_exp(1100)
        >>> player_1.exp
        100
        >>> player_1.level
        5
        """
        gain_exp = self.exp + amount
        if gain_exp > 100:
            gain_exp = 100
        self.exp = gain_exp
        print('{} has gained {} experience points from {}!'.format(self.name, self.exp, player_1.name))
        return self.exp


    def level_up(self):
         """
        Level up the character and return to zero experience points, increase hp by 20 points, attack power and defense points by 5 points.
        max level is 100
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.level_up()
        (2, 120, 15, 8)
        """
        level_up = self.level + 1
        if level_up > 100:
            level_up = 100
        self.level = level_up
        print('{} has leveled up to {}!'.format(self.name, self.level))
        return self.level, self.hp, self.attack_power, self.defense

    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.is_alive()
        True
        """
        alive = self.hp > 0
        return alive
