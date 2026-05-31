import re
from collections import deque
from decimal import Decimal
class ExpressionCalculator:  
    """
    This is a class in Python that can perform calculations with basic arithmetic operations, including addition, subtraction, multiplication, division, and modulo.
    """

    def __init__(self):
        """
        Initialize the expression calculator
        """
        self.postfix_stack = deque()
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]


    def calculate(self, expression):
        """
        Calculate the result of the given postfix expression
        :param expression: string, the postfix expression to be calculated
        :return: float, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0

        """
        expression = expression.strip()
        expression_stack = deque()
        expression_stack.append(expression)
        expression_stack.append(0)
        while len(expression_stack) > 0:
            expression = expression_stack.pop()
            operator = expression[0]
            operand1 = expression[1]
            operand2 = expression[2]
            operand3 = expression[3]
            operand4 = expression[4]
            operand5 = expression[5]
            operand6 = expression[6]
            operand7 = expression[7]
            operand8 = expression[8]
            operand9 = expression[9]
            operand10 = expression[10]
            operand11 = expression[11]
            operand12 = expression[12]
            operand13 = expression[13]
            operand14 = expression[14]
            operand15 = expression[15]
            operand16 = expression[16]
            operand17 = expression[17]
            operand18 = expression[18]
            operand19 = expression[19]
            operand20 = expression[20]
            operand21 = expression[21]
            operand22 = expression[22]
            operand23 = expression[23]
            operand24 = expression[24]
            operand25 = expression[25]
            operand26 = expression[26]
            operand27 = expression[27]
            operand28 = expression[28]
            operand29 = expression[29]
            operand30 = expression[30]
            operand31 = expression[31]
            operand32 = expression[32]
            operand33 = expression[33]
            operand34 = expression[34]
            operand35 = expression[35]
            operand36 = expression[36]
            operand37 = expression[37]
            operand38 = expression[38]
            operand39 = expression[39]
            operand40 = expression[40]
            operand41 = expression[41]
            operand42 = expression[42]
            operand43 = expression[43]
            operand44 = expression[44]
            operand45 = expression[45]
            operand46 = expression[46]
            operand47 = expression[47]
            operand48 = expression[48]
            operand49 = expression[49]
            operand50 = expression[50]
            operand51 = expression[51]
            operand52 = expression[52]
            operand53 = expression[53]
            operand54 = expression[54]
            operand55 = expression[55]
            operand56 = expression[56]
            operand57 = expression[57]
            operand58 = expression[58]
            operand59 = expression[59]
            operand60 = expression[60]
            operand61 = expression[61]
            operand62 = expression[62]
            operand63 = expression[63]
            operand64 = expression[64]
            operand65 = expression[65]
            operand66 = expression[66]
            operand67 = expression[67]
            operand68 = expression[68]
            operand69 = expression[69]
            operand70 = expression[70]
            operand71 = expression[71]
            operand72 = expression[72]
            operand73 = expression[73]
            operand74 = expression[74]
            operand75 = expression[75]
            operand76 = expression[76]
            operand77 = expression[77]
            operand78 = expression[78]
            operand79 = expression[79]
            operand80 = expression[80]
            operand81 = expression[81]
            operand82 = expression[82]
            operand83 = expression[83]
            operand84 = expression[84]
            operand85 = expression[85]
            operand86 = expression[86]
            operand87 = expression[87]
            operand88 = expression[88]
            operand89 = expression[89]
            operand90 = expression[90]
            operand91 = expression[91]
            operand92 = expression[92]
            operand93 = expression[93]
            operand94 = expression[94]
            operand95 = expression[95]
            operand96 = expression[96]
            operand97 = expression[97]
            operand98 = expression[98]
            operand99 = expression[99]
            operand100 = expression[100]
            operand101 = expression[101]
            operand102 = expression[102]
            operand103 = expression[103]
            operand104 = expression[104]
            operand105 = expression[105]
            operand106 = expression[106]
            operand107 = expression[107]
            operand108 = expression[108]
            operand109 = expression[109]
            operand110 = expression[110]
            operand111 = expression[111]
            operand112 = expression[112]
            operand113 = expression[113]
            operand114 = expression[114]
            operand115 = expression[115]
            operand116 = expression[116]
            operand117 = expression[117]
            operand118 = expression[118]
            operand119 = expression[119]
            operand120 = expression[120]
            operand121 = expression[121]
            operand122 = expression[122]
            operand123 = expression[123]
            operand124 = expression[124]
            operand125 = expression[125]
            operand126 = expression[126]
            operand127 = expression[127]
            operand128 = expression[128]
            operand129 = expression[129]
            operand130 = expression[130]
            operand131 = expression[131]
            operand132 = expression[132]
            operand133 = expression[133]
            operand134 = expression[134]
            operand135 = expression[135]
            operand136 = expression[136]
            operand137 = expression[137]
            operand138 = expression[138]
            operand139 = expression[139]
            operand140 = expression[140]
            operand141 = expression[141]
            operand142 = expression[142]
            operand143 = expression[143]
            operand144 = expression[144]
            operand145 = expression[145]
            operand146 = expression[146]
            operand147 = expression[147]
            operand148 = expression[148]
            operand149 = expression[149]
            operand150 = expression[150]
            operand151 = expression[151]
            operand152 = expression[152]
            operand153 = expression[153]
            operand154 = expression[154]
            operand155 = expression[155]
            operand156 = expression[156]
            operand157 = expression[157]
            operand158 = expression[158]
            operand159 = expression[159]
            operand160 = expression[160]
            operand161 = expression[161]
            operand162 = expression[162]
            operand163 = expression[163]
            operand164 = expression[164]
            operand165 = expression[165]
            operand166 = expression[166]
            operand167 = expression[167]
            operand168 = expression[168]
            operand169 = expression[169]
            operand170 = expression[170]
            operand171 = expression[171]
            operand172 = expression[172]
            operand173 = expression[173]
            operand174 = expression[174]
            operand175 = expression[175]
            operand176 = expression[176]
            operand177 = expression[177]
            operand178 = expression[178]
            operand179 = expression[179]
            operand180 = expression[180]
            operand181 = expression[181]
            operand182 = expression[182]
            operand183 = expression[183]
            operand184 = expression[184]
            operand185 = expression[185]
            operand186 = expression[186]
            operand187 = expression[187]
            operand188 = expression[188]
            operand189 = expression[189]
            operand190 = expression[190]
            operand191 = expression[191]
            operand192 = expression[192]
            operand193 = expression[193]
            operand194 = expression[194]
            operand195 = expression[195]
            operand196 = expression[196]
            operand197 = expression[197]
            operand198 = expression[198]
            operand199 = expression[199]
            operand200 = expression[200]
            operand201 = expression[201]
            operand202 = expression[202]
            operand203 = expression[203]
            operand204 = expression[204]
            operand205 = expression[205]
            operand206 = expression[206]
            operand207 = expression[207]
            operand208 = expression[208]
            operand209 = expression[209]
            operand210 = expression[210]
            operand211 = expression[211]
            operand212 = expression[212]
            operand213 = expression

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """


    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.is_operator("+")
        True

        """
        


    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True

        """


    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator._calculate("2", "3", "+")
        5.0

        """


    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"

        """
        

