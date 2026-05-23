import random
class Snake: 
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
        Move the snake in the specified direction. If the new position of the snake's head is equal to the position of the food, then eat the food; If the position of the snake's head is equal to the position of its body, then start over, otherwise increase its own length by one.
        :param direction: tuple, representing the direction of movement (x, y).
        :return: None
        """
        # Get the current position of the snake's head
        current_head_position = self.positions[0]
    
        # Calculate the new position of the snake's head based on the direction
        new_head_position = (current_head_position[0] + direction[0] * self.BLOCK_SIZE, current_head_position[1] + direction[1] * self.BLOCK_SIZE)
    
        # Check if the new position of the snake's head is equal to the position of the food
        if new_head_position == self.food_position:
            self.eat_food()  # Call the eat_food method to handle eating the food
        # Check if the new position of the snake's head is equal to the position of its body
        elif new_head_position in self.positions[1:]:
            self.reset()  # Call the reset method to start over
        else:
            # Add the new position of the snake's head to the positions list
            self.positions.insert(0, new_head_position)
            # Check if the length of the snake is greater than 1
            if self.length > 1:
                # Remove the last position from the positions list
                self.positions.pop()
        
        # Update the score based on the length of the snake
        self.score = self.length * 10
    

    def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
        while True:
            x = random.randint(0, self.SCREEN_WIDTH - self.BLOCK_SIZE) // self.BLOCK_SIZE * self.BLOCK_SIZE
            y = random.randint(0, self.SCREEN_HEIGHT - self.BLOCK_SIZE) // self.BLOCK_SIZE * self.BLOCK_SIZE
            if (x, y) not in self.positions:
                self.food_position = (x, y)
                break
    

    def reset(self):
        """
        Reset the snake to its initial state. Set the length to 1, the snake head position to ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)), the score to 0, and randomly generate new food position.
        :return: None
        """
        self.length = 1
        self.positions = [((self.SCREEN_WIDTH / 2), (self.SCREEN_HEIGHT / 2))]
        self.score = 0
        self.random_food_position()
    

    def eat_food(self):
        """
        Increase the length of the snake by 1 and increase the score by 100. Randomly generate a new food position, but
        don't place it on the snake.
        :return: None
        >>> snake = Snake(100, 100, 1, (51, 51))
        >>> snake.move((1,1))
        >>> snake.eat_food()
        self.length = 2
        self.score = 10
        """
        self.length += 1
        self.score += 100
        self.random_food_position()