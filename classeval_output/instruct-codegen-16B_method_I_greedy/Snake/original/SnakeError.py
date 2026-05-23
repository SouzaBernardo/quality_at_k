import random
class Snake:  
    """
    The class is a snake game, with allows snake to move and eat food, and also enables to reset, and generat a random food position.
    """

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, food_position):
        """
        Initialize the length of the snake, screen width, screen height, block size, snake head position, score, and food position.
        :param SCREEN_WIDTH: int
        :param SCREEN_HEIGHT: int
        :param BLOCK_SIZE: int, Size of moving units
        :param food_position: tuple, representing the position(x, y) of food.
        """
        self.length = 1
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.score = 0
        self.food_position = food_position




    def move(self):
        """
        Move the snake in the specified direction. If the new position of the snake's head is equal to the position of the food, then eat the food; If the position of the snake's head is equal to the position of its body, then start over, otherwise its own length plus one.
        :return: None
        """
        if self.new_position == self.food_position:
            self.eaten = True
            self.score += 1
        if self.new_position in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, self.new_position)
            if self.eaten:
                self.eaten = False
            else:
                self.positions.pop()
        self.new_position = (self.positions[0][0] + self.direction[0], self.positions[0][1] + self.direction[1])

    def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
        self.new_food_position = (random.randint(0, self.SCREEN_WIDTH - self.BLOCK_SIZE)//self.BLOCK_SIZE * self.BLOCK_SIZE,
        random.randint(0, self.SCREEN_HEIGHT - self.BLOCK_SIZE)//self.BLOCK_SIZE * self.BLOCK_SIZE)
        while self.new_food_position in self.positions:
            self.new_food_position = (random.randint(0, self.SCREEN_WIDTH - self.BLOCK_SIZE)//self.BLOCK_SIZE * self.BLOCK_SIZE,
        random.randint(0, self.SCREEN_HEIGHT - self.BLOCK_SIZE)//self.BLOCK_SIZE * self.BLOCK_SIZE)

    def reset(self):
        """
        Reset the snake to its initial state. Set the length to 1, the snake head position to ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)), the score to 0, and randomly generate new food position.
        :return: None
        """
        self.length = 1
        self.positions = [(50, 50)]
        self.score = 0
        self.random_food_position()

