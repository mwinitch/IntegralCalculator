# These functions are all used to take in a input string from the user, such as 'x^2+10' and convert
# it into a list in postfix form. For 'x^2+10' the postfix list would be [x, 2, ^, +, 10]. This list
# will eventually be used to create an expression tree in the ExpressionTree class. These functions
# also format the user string into something that will be understood by the expression tree such as
# converting '2x' into '2 * x'

operator = ['(', ')', '^', '*', '/', '+', '-']
# Returns True is some input is a number and not 'x' or an operator
def is_num(val):
    if val != 'x' and val not in operator:
        return True
    return False

# Helps convert negative numbers into a structure that can be interpret by the expression tree
def add_negative(infix_list, index):
    infix_list.pop(index + 1)
    infix_list.insert(index + 1, '(')
    infix_list.insert(index + 2, '0')
    infix_list.insert(index + 3, '-')
    infix_list.insert(index + 4, '1')
    infix_list.insert(index + 5, ')')
    infix_list.insert(index + 6, '*')
    return infix_list

# Function takes an infix expression in list form and does formatting on it before it becomes converted
# into postfix form so it will be able to be converted easily into an expression tree format
def fix_cases(infix_list):
    i = 0
    while i < len(infix_list):
        # Deals with cases where the functions starts with a negative number
        if i == 0 and infix_list[i] == '-':
            infix_list = add_negative(infix_list, -1)
            i += 5
        # Deals with the case where there is a negative sign right after an opening parenthesis
        elif infix_list[i] == '(' and infix_list[i + 1] == '-':
            infix_list = add_negative(infix_list, i)
            i += 5
        # Converts an expression like (2)(x + 1) into (2) * (x + 1)
        elif i + 1 < len(infix_list) and infix_list[i] == ')' and infix_list[i + 1] == '(':
            infix_list.insert(i + 1, '*')
            i += 1
        # Converts 2(x+1) into 2 * (x + 1)
        elif i + 1 < len(infix_list) and i not in operator and infix_list[i + 1] == '(':
            infix_list.insert(i + 1, '*')
            i += 1
        elif infix_list[i] == 'x' and i != 0:
            # Converts an expression like '3^2x' to '3^(2 * x)'
            if is_num(infix_list[i - 1]) and infix_list[i - 2] == '^':
                infix_list.insert(i - 1, '(')
                i += 1
                infix_list.insert(i, '*')
                i += 1
                infix_list.insert(i + 1, ')')
                i += 1
            # Converts an expression like '(32)x' to '(32) * x'
            elif infix_list[i-1] == ')':
                infix_list.insert(i, '*')
                i += 1
            # Converts an expression like '10 + 3x' to '10 + 3 * x'
            elif is_num(infix_list[i - 1]):
                infix_list.insert(i, '*')
                i += 1
        i += 1
    return infix_list

# Takes a string of infix form and returns a list in infix form
def formatting(infix):
    infix_list = []
    infix = infix.replace(' ', '')
    i = 0
    while i < len(infix):
        # Checks if there is a number of two or more digits (such as 11 or 5.0) and appends the whole value
        # to the infix_list
        if infix[i].isdigit() or infix[i] == '.':
            num = ''
            num += infix[i]
            while i != (len(infix) - 1) and (infix[i + 1].isdigit() or infix[i + 1] == '.'):
                num += infix[i+1]
                i += 1
            infix_list.append(num)
            i += 1
        else:
            infix_list.append(infix[i])
            i += 1

    infix_list = fix_cases(infix_list)
    return infix_list

rank = {'(': 4, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
# Takes an infix expression as a list and returns a list in postfix expression form
def make_postfix(infix):
    stack = []
    postfix = []
    for token in infix:
        if token not in operator:
            postfix.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while len(stack) != 0 and (stack[-1] != '(') and (rank[token] <= rank[stack[-1]]):
                postfix.append(stack.pop())
            stack.append(token)
    while len(stack) > 0:
        postfix.append(stack.pop())
    return postfix

# Checks that an infix expression has a matching amount of opening and closing parentheses
def valid_parentheses(infix):
    stack = []
    for i in infix:
        if i == '(':
            stack.append(i)
        elif i == ')':
            try:
                stack.pop()
            except IndexError:
                return False
    if len(stack) > 0:
        return False
    return True

# Checks that the user's expression contains only valid symbols
def valid_symbols(infix):
    infix = infix.replace(' ', '')
    for i in infix:
        if i in operator:
            continue
        elif i == 'x' or i == '.':
            continue
        elif i.isdigit():
            continue
        else:
            return False
    return True