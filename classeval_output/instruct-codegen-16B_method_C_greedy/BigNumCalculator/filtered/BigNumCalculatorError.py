class BigNumCalculator: 


    def add(num1, num2):
        """
        Adds two big numbers.
        :param num1: The first number to add,str.
        :param num2: The second number to add,str.
        :return: The sum of the two numbers,str.
        """
        num1_list = list(num1)
        num2_list = list(num2)
        carry = 0
        result = []
        
        i = len(num1_list) - 1
        j = len(num2_list) - 1
        while i >= 0 or j >= 0:
            n1 = int(num1_list[i])
            n2 = int(num2_list[j])
            temp = n1 + n2 + carry
            if temp >= 10:
                carry = 1
                temp %= 10
            else:
                carry = 0
            result.append(str(temp))
            i -= 1
            j -= 1
        if carry > 0:
            result.append(str(carry))
        
        return ''.join(result[::-1])

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
        num1 = int(num1)
        num2 = int(num2)
        return str(num1 - num2)

    def multiply(num1, num2):
        """
        Multiplies two big numbers.
        :param num1: The first number to multiply,str.
        :param num2: The second number to multiply,str.
        :return: The product of the two numbers,str.
        """
        # Convert the strings to lists of ints
        num1_list = [int(x) for x in num1]
        num2_list = [int(x) for x in num2]
        # Initialize the result list
        result_list = []
        carry = 0
        # Iterate through the lists and multiply
        for i in range(len(num1_list)):
            # Multiply and add to the result list
            for j in range(len(num2_list)):
                # Make sure to account for leading 0s
                if num1_list[i] == 0 or num2_list[j] == 0:
                    result_list.append(0)
                else:
                    result_list.append(num1_list[i] * num2_list[j] + carry)
                carry = result_list[-1] // 10
                result_list[-1] %= 10
        # Add any remaining carry
        if carry > 0:
            result_list.append(carry)
        # Convert the result list back to a string
        result_str = ''.join([str(x) for x in result_list])
        return result_str