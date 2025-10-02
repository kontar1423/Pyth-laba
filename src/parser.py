class Parser():
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def peek(self):
        if self.pos < len(self.text):
            return self.text[self.pos]
        return None

    def consume(self):
        if self.pos < len(self.text):
            self.pos += 1
            return self.text[self.pos - 1]
        return None

    def factor(self):
        if self.peek() is None:
            raise ValueError("Пустая строчка")

        sign = 1
        while True:
            a = self.peek()
            if a is None:
                break
            if a == '+':
                self.consume()
            elif a == '-':
                self.consume()
                sign *= -1
            else:
                break

        num_str = ''
        while True:
            a = self.peek()
            if a is None or (not a.isdigit() and a != '.'):
                break
            num_str += self.consume()

        if not num_str:
            raise ValueError("Неправильный ввод или пустое число")

        if '.' in num_str:
            value = float(num_str)
        else:
            value = int(num_str)

        return sign * value
    def term(self):
        value = self.factor()
        while True:
            b = self.peek()
            if b in ('*', '/'):
                self.consume()
                next_factor = self.factor()
                if b == '*':
                    value *= next_factor
                elif b == '/':
                    if next_factor == 0:
                        raise ZeroDivisionError("Нельзя делить на ноль")
                    value /= next_factor
            else:
                break
        return value

    def expr(self):
        value = self.term()
        while True:
            b = self.peek()
            if b in ('+', '-'):
                self.consume()
                next_term = self.term()
                if b == '+':
                    value += next_term
                elif b == '-':
                    value -= next_term
            else:
                break
        return value


def main():
    p = Parser('-123--12.343*2+1')
    print(p.expr())
if __name__ == "__main__":
    main()
