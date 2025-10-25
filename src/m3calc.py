class Calculator:
    def __init__(self):
        self.stack = []
        self.state = 0  # for () processing
        self.brackets_stack = []  # for empty brackets detecting

    def _process_number(self, token):
        # checking is_number
        try:
            float(token.lstrip('-+'))  # lstrip прикольная штука, жаль раньше не узнал о ней
            operator = '+-'
            num = token.lstrip('-+')
            # processing unary minus
            final_num = float(operator[token.count('-')%2]+num)
            self.stack.append(final_num)
            # Добавляем в brackets_stack только если мы внутри скобок
            if self.state > 0:
                self.brackets_stack.append(final_num)
            return True
        except ValueError:
            return False

    def _process_operator(self, token):
        if len(self.stack) < 2:
            raise ValueError("Not enough numbers for operation")
        right = self.stack.pop()
        left = self.stack.pop()   # poping numbers in stack
        
        if token == '+':
            result = left + right
        elif token == '-':
            result = left - right
        elif token == '*':
            result = left * right
        elif token == '/':
            if right == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = left / right
        else:
            raise ValueError(f"Unknown operand: {token}")
        
        self.stack.append(result)

    def _process_brackets(self, token):
        if token == ')':
            if self.state == 0:
                raise ValueError('Wrong input with ()')
            if len(self.brackets_stack) == 0:
                raise ValueError('Empty brackets')
            self.state -= 1
            if self.state == 0:
                self.brackets_stack = []
            return True
        if token == '(':
            self.state += 1
            return True
        return False

    def calc(self, expr):
        # Calc expression
        tokens = expr.split()
        
        for token in tokens:
            # Try processing brackets first
            if self._process_brackets(token):
                continue
                
            # Try processing number
            if self._process_number(token):
                continue
                
            # If not bracket and not number - process operator
            self._process_operator(token)

        if len(self.stack) != 1:
            raise ValueError("More than 1 numbers in stack left")
        if self.state != 0:
            raise ValueError('Wrong input with ()')
        return self.stack[0]