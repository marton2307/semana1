from stack import Stack

class ExpressionEvaluator:
    def __init__(self):
        self.stack = Stack()
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def infix_to_postfix(self, expression):
        output = []
        for char in expression:
            if char.isnumeric():
                output.append(char)
            elif char in '*/+-':
                while (not self.stack.is_empty() and 
                       self.precedence.get(self.stack.peek(), 0) >= self.precedence[char]):
                    output.append(self.stack.pop())
                self.stack.push(char)
            else:
                raise ValueError(f"Unknown character: {char}")

        while not self.stack.is_empty():
            output.append(self.stack.pop())

        return ''.join(output)

    def evaluate_postfix(self, expression):
        for char in expression:
            if char.isnumeric():
                self.stack.push(int(char))
            elif char in '*/+-':
                b = self.stack.pop()
                a = self.stack.pop()
                if char == '+':
                    result = a + b
                elif char == '-':
                    result = a - b
                elif char == '*':
                    result = a * b
                elif char == '/':
                    result = a / b
                self.stack.push(result)
            else:
                raise ValueError(f"Unknown character: {char}")

        return self.stack.pop()
