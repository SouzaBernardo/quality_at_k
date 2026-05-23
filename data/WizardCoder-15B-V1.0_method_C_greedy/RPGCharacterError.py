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
        """
        damage = self.attack_power - other_character.defense
        if damage > 0:
            other_character.hp -= damage
            print(f"{self.name} attacks {other_character.name} for {damage} damage.")
        else:
            print(f"{self.name} attacks {other_character.name} but does no damage.")
        if other_character.hp <= 0:
            other_character.hp = 0
            print(f"{other_character.name} has been defeated.")
            return False
        return True





    def level_up(self):
        """
        Level up the character and return to zero experience points, increase hp by 20 points, attack power and defense points by 5 points.
        max level is 100
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        """
        if self.level < 100:
            self.level += 1
            self.hp += 20
            self.attack_power += 5
            self.defense += 5
            self.exp = 0
            return (self.level, self.hp, self.attack_power, self.defense)
        else:
            return (self.level, self.hp, self.attack_power, self.defense)

    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        """
        return self.hp > 0