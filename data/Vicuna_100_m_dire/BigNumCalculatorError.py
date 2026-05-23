class BigNumCalculator: 


    def add(num1, num2):
        """
        Adds two big numbers.
        :param num1: The first number to add，str.
        :param num2: The second number to add，str.
        :return: The sum of the two numbers，str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.add("12345678901234567890", "98765432109876543210")
        '111111111011111111100'
    
        """
        # code to implement the add method

    def subtract(num1, num2):
        """
        Subtracts two big numbers.
        :param num1: The first number to subtract，str.
        :param num2: The second number to subtract，str.
        :return: The difference of the two numbers，str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.subtract("12345678901234567890", "98765432109876543210")
        '-86419753208641975320'
    
        """
        result = ""
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        for i in range(len(num1)):
            if num1[i] > num2[i]:
                result = str(num1[i]) + result
            else:
                result = str(num2[i]) + result
        return result

    def multiply(num1, num2):
        """
        Multiplies two big numbers.
        :param num1: The first number to multiply，str.
        :param num2: The second number to multiply，str.
        :return: The product of the two numbers，str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.multiply("12345678901234567890", "98765432109876543210")
        '1219326311370217952237463801111263526900'
        """
    
        product = ""
        while num1 and num2:
            if num1.isdigit() and num2.isdigit():
                product = product + str(int(num1) * int(num2))
                num1 = num1[:-1]
                num2 = num2[:-1]
            else:
                product = product + str(int(num1) * int(num2))
                num1 = num1[:-1]
                num2 = num2[:-1]
        return product