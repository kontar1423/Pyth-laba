from parser import Parser
def main():
    print('Введите выражение')
    p = Parser(input())
    print(p.expr())
if __name__ == "__main__":
    main()
