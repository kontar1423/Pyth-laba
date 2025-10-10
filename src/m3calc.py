def is_number(token):
    # is this number
    try:
        float(token)
        return True
    except ValueError:
        return False

def parse_unare_minus(token):
    # do --2 to 2
    operator = '+-'
    num = token.lstrip('-+')
    token = token.replace('+','--')
    return float(operator[token.count('-')%2]+num)


def calc(expr):
    # Calc expression
    stack = []
    tokens = expr.split()
    state = 0 # for () proccesing
    brackets_stack = [] # for empty brackets detecting
    for token in tokens:
        if token in ')':
            if state == 0:
                raise ValueError('Wrong input with ()')
            if len(brackets_stack) == 0:
                raise ValueError('Empty brackets')
            state -= 1
            if state == 0:
                brackets_stack = []
            continue
        if token in '(':
            state += 1
            continue
        if is_number(token.lstrip('-+')):
            stack.append(parse_unare_minus(token))
        else:
            if len(stack) < 2:
                raise ValueError("Not enough numbers for operation")
            right = stack.pop()
            left= stack.pop()
            if token == '+':
                stack.append(left + right)
                if state >= 0:
                    brackets_stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
                if state >= 0:
                    brackets_stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
                if state >= 0:
                    brackets_stack.append(left * right)
            elif token == '/':
                if right == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                stack.append(left / right)
                if state >= 0:
                    brackets_stack.append(left / right)
            else:
                raise ValueError(f"Unknown operand: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid expression: leftover elements in stack")
    if state != 0:
        raise ValueError('Wrong input with ()')
    return stack[0]
