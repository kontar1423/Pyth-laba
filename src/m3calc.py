def calc(expr):
    # Calc expression
    stack = []
    tokens = expr.split()
    state = 0 # for () proccesing
    brackets_stack = [] # for empty brackets detecting
    for token in tokens:
        if token == ')':
            if state == 0:
                raise ValueError('Wrong input with ()')
            if len(brackets_stack) == 0:
                raise ValueError('Empty brackets')
            state -= 1
            if state == 0:
                brackets_stack = []
            continue
        if token == '(':
            state += 1
            continue
        try: # checking is_number
            float(token.lstrip('-+')) # lstrip прикольная штука, жаль раньше не узнал о ней
            operator = '+-'
            num = token.lstrip('-+')
            num_with_minuses = token.replace('+','--')
            final_num = float(operator[num_with_minuses.count('-')%2]+num) # proccesing unare minus
            stack.append(final_num)
        except ValueError:
            if len(stack) < 2:
                raise ValueError("Not enough numbers for operation")
            right = stack.pop()
            left= stack.pop()   # poping numbers in stack
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
        raise ValueError("More than 1 numbers in stack left")
    if state != 0:
        raise ValueError('Wrong input with ()')
    return stack[0]
