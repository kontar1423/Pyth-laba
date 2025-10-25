from src.m3calc import calc

def main() -> None:
    try:
        while True:
            expr = input("Enter expression. Example: ( --2 3 + ): ")
            if expr == 'exit':
                print("Calculator stoped.")
                break
            try:
                result = calc(expr)
                print("Result:", result)
            except Exception as error:
                print("Error:", error)
    except KeyboardInterrupt:
        print("\nCalculator stoped.")
if __name__ == "__main__":
    main()
