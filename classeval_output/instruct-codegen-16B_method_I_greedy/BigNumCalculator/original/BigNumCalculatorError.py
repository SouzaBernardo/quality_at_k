
class BigNumCalculator:  
    """
    This is a class that implements big number calculations, including adding, subtracting and multiplying.
    """



    def add(self, num1, num2):
        """
        Adds two big numbers.
        :param num1: The first number to add,str.
        :param num2: The second number to add,str.
        :return: The sum of the two numbers,str.
        """
        num1_list = list(num1)
        num2_list = list(num2)
        result_list = []
        carry = 0
        for i in range(max(len(num1_list), len(num2_list))):
            n1 = int(num1_list[i]) if i < len(num1_list) else 0
            n2 = int(num2_list[i]) if i < len(num2_list) else 0
            value = n1 + n2 + carry
            if value >= 10:
                carry = 1
            else:
                carry = 0
            result_list.append(str(value % 10))
        if carry > 0:
            result_list.append(str(carry))
        return ''.join(result_list[::-1])

    def subtract(num1, num2):
        """
        Subtracts two big numbers.
        :param num1: The first number to subtract,str.
        :param num2: The second number to subtract,str.
        :return: The difference of the two numbers,str.
        """
        num1_list = list(num1)
        num2_list = list(num2)
        result_list = []
        carry = 0
        for i in range(max(len(num1_list), len(num2_list))):
            n1 = int(num1_list[i]) if i < len(num1_list) else 0
            n2 = int(num2_list[i]) if i < len(num2_list) else 0
            value = n1 - n2 - carry
            if value < 0:
                carry = -1
                value += 10
            else:
                carry = 0
            result_list.append(str(value % 10))
        if carry < 0:
            result_list.append(str(carry))
        return ''.join(result_list[::-1])

    def multiply(num1, num2):
        """
        Multiplies two big numbers.
        :param num1: The first number to multiply,str.
        :param num2: The second number to multiply,str.
        :return: The product of the two numbers,str.
        """
        num1_list = list(num1)
        num2_list = list(num2)
        result_list = []
        carry = 0
        for i in range(len(num1_list)):
            n1 = int(num1_list[i])
            n2 = int(num2_list[i])
            for j in range(len(num2_list)):
                value = n1 * n2 + carry
                if value >= 10:
                    carry = 1
                else:
                    carry = 0
                result_list.append(str(value % 10))
            if carry > 0:
                result_list.append(str(carry))
        return ''.join(result_list[::-1])