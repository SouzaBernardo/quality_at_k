
class BigNumCalculator: 

    @staticmethod
    def add(num1, num2):
        """
        Adds two big numbers.
        :param num1: The first number to add,str.
        :param num2: The second number to add,str.
        :return: The sum of the two numbers,str.
        """
        # Convert the strings to integers
        num1 = int(num1)
        num2 = int(num2)
    
        # Add the numbers
        result = num1 + num2
    
        # Convert the result back to a string and return it
        return str(result)
    @staticmethod
    def subtract(num1, num2):
        """
        Subtracts two big numbers.
        :param num1: The first number to subtract,str.
        :param num2: The second number to subtract,str.
        :return: The difference of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.subtract("12345678901234567890", "98765432109876543210")
        '-86419753208641975320'
        """
        # Convert the strings to integers
        num1 = int(num1)
        num2 = int(num2)
    
        # Subtract the numbers
        result = num1 - num2
    
        # Convert the result back to a string and return it
        return str(result)
    @staticmethod
    def multiply(num1, num2):
        """
        Multiplies two big numbers.
        :param num1: The first number to multiply,str.
        :param num2: The second number to multiply,str.
        :return: The product of the two numbers,str.
        """
        # Convert the strings to integers
        num1 = int(num1)
        num2 = int(num2)
    
        # Multiply the numbers
        product = num1 * num2
    
        # Convert the product back to a string and return it
        return str(product)
