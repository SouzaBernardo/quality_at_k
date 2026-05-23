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

    def heal(self):
        """
        Heal the character with 10 hp and the max hp is 100.
        :return: int, the current health points after healing.
        >>> player_1 = RPGCharacter('player 1', 93, 10, 3)
        >>> player_1.heal()
        100
        """

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

    def level_up(self):
         """
        Level up the character and return to zero experience points, increase hp by 20 points, attack power and defense points by 5 points.
        max level is 100
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.level_up()
        (2, 120, 15, 8)
        """

    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.is_alive()
        True
        """

    def __str__(self):
        """
        Return a string representation of the character.
        :return: str, the string representation of the character.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.__str__()
        'player 1'
        """


class RPGCharacterFactory:
    """
    The class represents a factory for creating RPGCharacter objects.
    """

    def __init__(self):
        """
        Initialize a RPGCharacterFactory object.
        """

    def create_character(self, name, hp, attack_power, defense, level=1):
        """
        Create a RPGCharacter object.
        :param name: str, the name of the character.
        :param hp: int, The health points of the character.
        :param attack_power: int, the attack power of the character.
        :param defense: int, the defense points of the character.
        :param level: int, the level of the character. Default is 1.
        :return: RPGCharacter, the RPGCharacter object.
        """

    def create_player(self, name, hp, attack_power, defense):
        """
        Create a RPGCharacter object.
        :param name: str, the name of the character.
        :param hp: int, The health points of the character.
        :param attack_power: int, the attack power of the character.
        :param defense: int, the defense points of the character.
        :return: RPGCharacter, the RPGCharacter object.
        """

    def create_enemy(self, name, hp, attack_power, defense):
        """
        Create a RPGCharacter object.
        :param name: str, the name of the character.
        :param hp: int, The health points of the character.
        :param attack_power: int, the attack power of the character.
        :param defense: int, the defense points of the character.
        :return: RPGCharacter, the RPGCharacter object.
        """

    def create_boss(self, name, hp, attack_power, defense):
        """
        Create a RPGCharacter object.
        :param name: str, the name of the character.
        :param hp: int, The health points of the character.
        :param attack_power: int, the attack power of the character.
        :param defense: int, the defense points of the character.
        :return: RPGCharacter, the RPGCharacter object.
        """


class RPGCharacterFactoryTest(unittest.TestCase):
    """
    The class represents a test case for the RPGCharacterFactory class.
    """

    def test_create_character(self):
        """
        Test the create_character method.
        """
        character_factory = RPGCharacterFactory()
        player = character_factory.create_player('player', 100, 10, 3)
        self.assertEqual(player.name, 'player')
        self.assertEqual(player.hp, 100)
        self.assertEqual(player.attack_power, 10)
        self.assertEqual(player.defense, 3)
        self.assertEqual(player.level, 1)
        self.assertEqual(player.exp, 0)
        self.assertEqual(player.is_alive(), True)

    def test_create_player(self):
        """
        Test the create_player method.
        """
        character_factory = RPGCharacterFactory()
        player = character_factory.create_player('player', 100, 10, 3)
        self.assertEqual(player.name, 'player')
        self.assertEqual(player.hp, 100)
        self.assertEqual(player.attack_power, 10)
        self.assertEqual(player.defense, 3)
        self.assertEqual(player.level, 1)
        self.assertEqual(player.exp, 0)
        self.assertEqual(player.is_alive(), True)

    def test_create_enemy(self):
        """
        Test the create_enemy method.
        """
        character_factory = RPGCharacterFactory()
        enemy = character_factory.create_enemy('enemy', 100, 10, 3)
        self.assertEqual(enemy.name, 'enemy')
        self.assertEqual(enemy.hp, 100)
        self.assertEqual(enemy.attack_power, 10)
        self.assertEqual(enemy.defense, 3)
        self.assertEqual(enemy.level, 1)
        self.assertEqual(enemy.exp, 0)
        self.assertEqual(enemy.is_alive(), True)

    def test_create_boss(self):
        """
        Test the create_boss method.
        """
        character_factory = RPGCharacterFactory()
        boss = character_factory.create_boss('boss', 100, 10, 3)
        self.assertEqual(boss.name, 'boss')
        self.assertEqual(boss.hp, 100)
        self.assertEqual(boss.attack_power, 10)
        self.assertEqual(boss.defense, 3)
        self.assertEqual(boss.level, 1)
        self.assertEqual(boss.exp, 0)
        self.assertEqual(boss.is_alive(), True)


if __name__ == '__main__':
    unittest.main()