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
        damage = self.attack_power - other_character.defense
        self.exp += damage
        other_character.hp -= damage
        if other_character.hp <= 0:
            print("The character died.")

    def heal(self):
        current_hp = self.hp
        self.hp = 10
        if self.hp > 100:
            self.hp = 100
        return current_hp

    def gain_exp(self, amount):
        self.exp += amount
        if amount * 100 > self.exp:
            self.level += 1
            while self.exp >= (100 * self.level):
                self.exp -= (100 * self.level)
                self.level += 1

    def level_up(self):
         """
        Level up the character and return to zero experience points, increase hp by 20 points, attack power and defense points by 5 points.
        max level is 100
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.level_up()
        (2, 120, 15, 8)
        """
        level = self.level + 1
        exp = self.exp
        hp = self.hp + 20
        attack_power = self.attack_power + 5
        defense = self.defense + 5
        return level, hp, attack_power, defense