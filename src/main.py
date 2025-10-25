from src.m3calc import Calculator

def main() -> None:
    try:
        while True:
            expr = input("Enter expression. Example: ( --2 3 + ): ")
            if expr == 'exit':
                print("Calculator stoped.")
                break
            try:
                result = Calculator()
                print("Result:", result.calc(expr))
            except Exception as error:
                print("Error:", error)
    except KeyboardInterrupt:
        print("\nCalculator stoped.")
if __name__ == "__main__":
    main()