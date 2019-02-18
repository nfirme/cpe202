from stack_array import Stack


# You do not need to change this class
class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    operators = ['+', '-', '*', '/', '>>', '<<', '**']
    exp = input_str.split()
    s = Stack(30)

    if len(exp) == 0:
        return 0

    for j in exp:
        if j not in operators and not j.isdigit() and not isfloat(j):
            raise PostfixFormatException('Invalid token')

    for i in exp:
        if i.isdigit():
            s.push(int(i))
        elif isfloat(i):
            s.push(float(i))
        elif i in operators:
            if s.size() >= 2:
                op1 = s.pop()
                op2 = s.pop()
            else:
                raise PostfixFormatException('Insufficient operands')
            if i == '+':
                val = op1 + op2
            elif i == '-':
                val = op2 - op1
            elif i == '*':
                val = op1 * op2
            elif i == '/':
                if op1 == 0:
                    raise ValueError('Cannot divide by 0')
                val = op2 / op1
            elif i == '**':
                val = op2 ** op1
            elif i == '>>':
                if type(op1) != int or type(op2) != int:
                    raise PostfixFormatException('Illegal bit shift operand')
                val = op2 >> op1
            elif i == '<<':
                if type(op1) != int or type(op2) != int:
                    raise PostfixFormatException('Illegal bit shift operand')
                val = op2 << op1
            s.push(val)

    if s.size() > 1:
        raise PostfixFormatException('Too many operands')

    return s.pop()


def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    if input_str == '':
        return input_str

    p = {}
    p['>>'] = 5
    p['<<'] = 5
    p['**'] = 4
    p['*'] = 3
    p['/'] = 3
    p['-'] = 2
    p['+'] = 2
    p['('] = 1

    operators = ['+', '-', '*', '/', '>>', '<<', '**']
    s = Stack(30)
    result = []
    input_list = input_str.split()

    for i in input_list:
        if i.isdigit():  # when you encounter a value, append value
            result.append(i)
        elif isfloat(i):  # when you encounter a value, append value
            result.append(i)
        elif i == '(':    # when you encounter opening parenthesis, push onto stack
            s.push(i)
        elif i == ')':
            top = s.pop()
            while top != '(':
                result.append(top)
                top = s.pop()
        elif i in operators:
            while (not s.is_empty()) and (s.peek() != '**') and (p[s.peek()] >= p[i]):
                result.append(str(s.pop()))
            s.push(i)

    while not s.is_empty():
        result.append(s.pop())

    return ' '.join(result)


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""

    if input_str == '':
        return input_str

    operators = ['+', '-', '*', '/', '>>', '<<', '**']
    s = Stack(30)
    input_list = input_str.split()

    for i in reversed(input_list):
        if i.isdigit() or isfloat(i):
            s.push(i)
        elif i in operators:
            op1 = s.pop()
            op2 = s.pop()
            str = op1 + ' ' + op2 + ' ' + i
            s.push(str)

    return s.pop()


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
