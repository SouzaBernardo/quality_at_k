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




    def move(self, direction):
        """
        Move the snake in the specified direction. If the new position of the snake's head is equal to the position of the food, then eat the food; If the position of the snake's head is equal to the position of its body, then start over, otherwise its own length plus one.
        :param direction: tuple, representing the direction of movement (x, y).
        :return: None
        """
        new_head_position = (self.positions[0][0] + direction[0] * self.BLOCK_SIZE,
                             self.positions[0][1] + direction[1] * self.BLOCK_SIZE)
        if new_head_position[0] < 0 or new_head_position[0] >= self.SCREEN_WIDTH or new_head_position[1] < 0 or new_head_position[1] >= self.SCREEN_HEIGHT:
            # If the new position of the snake's head is outside the screen, then start over.
            self.reset()
        elif new_head_position in self.positions[1:]:
            # If the new position of the snake's head is equal to the position of its body, then start over.
            self.reset()
        elif new_head_position == self.food_position:
            # If the new position of the snake's head is equal to the position of the food, then eat the food and increment the score.
            self.score += 10
            self.length += 1
            self.food_position = self.generate_food_position()
        else:
            # Otherwise, move the snake in the specified direction.
            self.positions.insert(0, new_head_position)
            if len(self.positions) > self.length:
                # If the snake's length is greater than its own length, then remove the last position of the snake.
                self.positions.pop()



    def reset(self):
        """
        Reset the snake to its initial state. Set the length to 1, the snake head position to ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)), the score to 0, and randomly generate new food position.
        :return: None
        """
        self.length = 1
        self.positions = [((self.SCREEN_WIDTH / 2), (self.SCREEN_HEIGHT / 2))]
        self.score = 0
        self.food_position = self.generate_food_position()

