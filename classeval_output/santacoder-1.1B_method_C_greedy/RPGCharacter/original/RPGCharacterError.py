
class RPGCharacter: 
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
        if self.defense > other_character.defense:
            self.hp -= other_character.attack_power + other_character.defense
        else:
            self.hp -= other_character.attack_power + other_character.defense - self.defense
        other_character.hp -= self.attack_power + self.defense
        self.exp += 1
        other_character.exp += 1
        print(f'{self.name} attacks {other_character.name} for {self.attack_power} damage.')
        print(f'{other_character.name} attacks {self.name} for {other_character.attack_power} damage.')
        print(f'{self.name} now has {self.hp} health points.')
        print(f'{other_character.name} now has {other_character.hp} health points.')
        print(f'{self.name} now has {self.exp} experience points.')
        print(f'{other_character.name} now has {other_character.exp} experience points.')
        print(f'{self.name} now has {self.level} level.')
        print(f'{other_character.name} now has {other_character.level} level.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character.name} now has {other_character.attack_power} attack power.')
        print(f'{self.name} now has {self.defense} defense points.')
        print(f'{other_character.name} now has {other_character.defense} defense points.')
        print(f'{self.name} now has {self.attack_power} attack power.')
        print(f'{other_character

    def heal(self):
        """
        Heal the character with 10 hp and the max hp is 100.
        :return: int, the current health points after healing.
        >>> player_1 = RPGCharacter('player 1', 93, 10, 3)
        >>> player_1.heal()
        100
        """
        self.hp += 10
        if self.hp > 100:
            self.hp = 100


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
        if self.exp + amount > 100:
            self.level_up()
            self.exp = 0
        else:
            self.exp += amount


    def level_up(self):
         """
        Level up the character and return to zero experience points, increase hp by 20 points, attack power and defense points by 5 points.
        max level is 100
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.level_up()
        (2, 120, 15, 8)
        """
        if self.level < 100:
            self.level += 1
            self.hp += 20
            self.attack_power += 5
            self.defense += 5
            return self.level, self.hp, self.attack_power, self.defense
        else:
            return self.level, self.hp, self.attack_power, self.defense

        """

    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.is_alive()
        True
        """
        return self.hp > 0
