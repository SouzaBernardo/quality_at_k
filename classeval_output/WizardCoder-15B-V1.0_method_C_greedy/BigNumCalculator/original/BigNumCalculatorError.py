
class BigNumCalculator: 


    def add(num1, num2):
        """
        Adds two big numbers.
        :param num1: The first number to add,str.
        :param num2: The second number to add,str.
        :return: The sum of the two numbers,str.
        """
        carry = 0
        result = ""
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(max(len(num1), len(num2))):
            n1 = int(num1[i]) if i < len(num1) else 0
            n2 = int(num2[i]) if i < len(num2) else 0
            s = n1 + n2 + carry
            carry = s // 10
            result += str(s % 10)
        if carry:
            result += str(carry)
        return result[::-1]

    def subtract(num1, num2):
        """
        Subtracts two big numbers.
        :param num1: The first number to subtract,str.
        :param num2: The second number to subtract,str.
        :return: The difference of the two numbers,str.
        """
        # Convert the input numbers to lists of digits
        num1_digits = [int(digit) for digit in num1]
        num2_digits = [int(digit) for digit in num2]
        # Pad the shorter number with zeros to make them the same length
        num1_digits = num1_digits.zfill(len(num2_digits))
        num2_digits = num2_digits.zfill(len(num1_digits))
        # Subtract the digits from each other, taking into account the borrow from the previous digit
        result_digits = []
        borrow = 0
        for i in range(len(num1_digits)-1, -1, -1):
            digit_diff = num1_digits[i] - num2_digits[i] - borrow
            if digit_diff < 0:
                digit_diff += 10
                borrow = 1
            else:
                borrow = 0
            result_digits.append(digit_diff)
        # Remove leading zeros from the result
        while len(result_digits) > 1 and result_digits[-1] == 0:
            result_digits.pop()
        # Convert the result back to a string
        result = "".join(str(digit) for digit in result_digits)
        return result

    def multiply(num1, num2):
        """
        Multiplies two big numbers.
        :param num1: The first number to multiply,str.
        :param num2: The second number to multiply,str.
        :return: The product of the two numbers,str.
        """
        # Convert the input strings to lists of digits
        num1_digits = [int(digit) for digit in num1]
        num2_digits = [int(digit) for digit in num2]
        # Pad the shorter number with zeros to make them the same length
        num1_digits.extend([0] * (len(num2_digits) - len(num1_digits)))
        num2_digits.extend([0] * (len(num1_digits) - len(num2_digits)))
        # Initialize the result list with zeros
        result_digits = [0] * len(num1_digits)
        # Multiply the digits and add the results to the result list
        for i in range(len(num1_digits)):
            result_digits[i] = num1_digits[i] * num2_digits[i]
        # Remove any leading zeros from the result list
        while len(result_digits) > 1 and result_digits[-1] == 0:
            result_digits.pop()
        # Convert the result list back to a string and return it
        return ''.join(str(digit) for digit in result_digits)