class BigNumCalculator:  
    """
    This is a class that implements big number calculations, including adding, subtracting and multiplying.
    """



    def add(num1, num2):
        # Pad the shorter number with zeros to make them equal in length
        if len(num1) < len(num2):
            num1 = num1.zfill(len(num2))
        elif len(num2) < len(num1):
            num2 = num2.zfill(len(num1))
        # Initialize carry flag and sum
        carry = 0
        result = ""
        # Iterate through the digits of the two numbers from right to left
        for i in range(len(num1)-1, -1, -1):
            digit_sum = int(num1[i]) + int(num2[i]) + carry
            if digit_sum > 9:
                digit_sum -= 10
                carry = 1
            else:
                carry = 0
            result = str(digit_sum) + result
        # If there is still carry left, add it to the result
        if carry > 0:
            result = str(carry) + result
        return result