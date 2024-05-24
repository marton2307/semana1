from evaluator import ExpressionEvaluator

def main():
    evaluator = ExpressionEvaluator()

    while True:
        try:
            expression = input("Enter an infix expression (or 'quit' to exit): ")
            if expression.lower() == 'quit':
                break

            postfix = evaluator.infix_to_postfix(expression)
            print(f"Postfix expression: {postfix}")

            result = evaluator.evaluate_postfix(postfix)
            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
