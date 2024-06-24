#! ArrayStack
class EmptyError(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise EmptyError("Stack is empty")
        return self._data[-1]

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            raise EmptyError("Stack is empty")
        return self._data.pop()


#! 5.A
def infix_to_postfix(expr):
    postfix_expr = []
    lefty = "("
    righty = ")"
    operators = "+-*/"
    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }

    # Stack to hold operators
    S = ArrayStack()

    for c in expr:
        if c.isnumeric():  # Operand
            postfix_expr.append(c)
        elif c == lefty:  # Left parenthesis
            S.push(c)
        elif c == righty:  # Right parenthesis
            while not S.is_empty() and S.top() != lefty:
                postfix_expr.append(S.pop())
            S.pop()  # Remove the left parenthesis
        elif c in operators:  # Operator
            while (
                (not S.is_empty())
                and (S.top() in operators)
                and (precedence[S.top()] >= precedence[c])
            ):
                postfix_expr.append(S.pop())
            S.push(c)  # Push the current operator onto the stack

    # Pop any remaining operators from the stack
    while not S.is_empty():
        postfix_expr.append(S.pop())

    return "".join(postfix_expr)


# print(infix_to_postfix('(6-(2+3))*(3+8/2)+2'))
print(infix_to_postfix("(8-((((3+2)*2)-4)/3))"))


#! 5.B
def evaluate_Postifix(expr):

    S = ArrayStack()
    for c in expr:

        if c.isnumeric():  # if operand
            S.push(c)
        else:
            op2 = int(S.pop())  # ? add 2nd operand
            op1 = int(S.pop())  # ? add 1st operand
            if c == "+":
                S.push(int(op1 + op2))
            elif c == "-":
                S.push(int(op1 - op2))
            elif c == "*":
                S.push(int(op1 * op2))
            elif c == "/":
                S.push(int(op1 / op2))
            elif c == "%":
                S.push(int(op1 % op2))
    return S.pop()


print(evaluate_Postifix("623+-382/+*2+"))


def main():
    # Ex: '(6-(2+3))*(3+8/2)+2'
    # Ex: "623+-382/+*2+"
    txt = input("Enter Arthimitic expression in infix form: ")
    postForm = infix_to_postfix(txt)
    value = evaluate_Postifix(postForm)

    print(f"""
Input : {txt}   
Posifix Expression {postForm} , 
Evaluation of Postifix : {value}
    """
    )
if __name__ == "__main__":
    main()