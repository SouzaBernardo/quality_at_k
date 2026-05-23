class Calculator: 
    def __init__(self):
        """
        Initialize the operations performed by the five operators'+','-','*','/','^'
        """
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }



    def calculate(self, expression):
        """
        Calculate the value of a given expression
        :param expression: string, given expression
        :return:If successful, returns the value of the expression; otherwise, returns None
        """
        # Split the expression into individual numbers and operators
        nums = []
        ops = []
        temp_num = ""
        temp_op = ""
        for char in expression:
            if char.isdigit():
                temp_num += char
            elif char in self.operators:
                if temp_op!= "":
                    nums.append(int(temp_num))
                    ops.append(temp_op)
                temp_num = ""
                temp_op = char
            else:
                raise ValueError("Invalid expression")
        if temp_op!= "":
            nums.append(int(temp_num))
            ops.append(temp_op)
        # Apply the operators to the numbers
        result = nums[0]
        for i in range(1, len(nums), 2):
            result = self.operators[ops[i]](result, nums[i + 1])
        return result

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment. The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        """
        if operator in self.operators:
            return self.operators[operator].__code__.co_argcount - 1
        else:
            return 0

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operator stack, and store the results at the top of the operator stack
        :param operand_stack:list
        :param operator_stack:list
        :return: the updated operand_stack and operator_stack
        """
        operator = operator_stack.pop()
        x = operand_stack.pop()
        y = operand_stack.pop()
        result = self.operators[operator](x, y)
        operand_stack.append(result)
        return operand_stack, operator_stack