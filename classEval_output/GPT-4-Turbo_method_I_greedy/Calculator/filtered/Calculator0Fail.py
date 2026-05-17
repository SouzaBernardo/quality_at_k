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
        try:
            # Split the expression into numbers and operators
            elements = re.findall(r"[\d]+|[+*/^-]", expression)
            # Initialize the result with the first number
            result = float(elements[0])
            # Iterate over the rest of the elements
            for i in range(1, len(elements), 2):
                # Apply the operator to the result and the next number
                result = self.operators[elements[i]](result, float(elements[i+1]))
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment. The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        """
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        elif operator == '^':
            return 3
        else:
            return 0
    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operand stack, and store the results at the top of the operand stack
        :param operand_stack:list
        :param operator_stack:list
        :return: the updated operand_stack and operator_stack
        """
        try:
            # Pop the top two numbers from the operand stack
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            # Pop the top operator from the operator stack
            operator = operator_stack.pop()
            # Perform the operation and push the result back onto the operand stack
            operand_stack.append(self.operators[operator](operand1, operand2))
            return operand_stack, operator_stack
        except IndexError:
            print("Error: Operator stack or operand stack is empty.")
        except KeyError:
            print("Error: Invalid operator.")
        except Exception as e:
            print(f"An error occurred: {e}")