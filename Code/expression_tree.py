from linked_binary_tree import LinkedBinaryTree
import re

class ExpressionTree(LinkedBinaryTree):
    def __init__(self,token,left=None,right=None):
        super().__init__()
        if not isinstance(token,str):
            raise TypeError("Token must be a string")
        self._add_root(token)
        if left is not None:
            if token not in '-=+*x/':
                raise ValueError("Token must be operand")
            self.attach(self.root(),left,right)
    def __str__(self) -> str:
        pieces = []
        self._parenthese_recur(self.root(),pieces)
        return " ".join(pieces)
    def _parenthese_recur(self,p,result): #((3+4)*5)
        if self.is_leaf(p):
            return str(p.element())
        result.append('(')# left parenthiese
        result.append(self._parenthese_recur(self.left(p),result))
        result.append(p.element())# operand
        result.append(self._parenthese_recur(self.right(p),result))
        result.append(')')
        return ''.join(result)
    def evaluate(self):
        return self._evalute_recur(self.root())
    def _evalute_recur(self,p):
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            x = self._evalute_recur(self.left(p))
            y  = self._evalute_recur(self.right(p))
            if op == '+':
                return x + y
            elif op == '-':
                return x - y
            elif op == '/':
                return x / y 
            else: #! treat x or '*' as multiplication
                return x*y

        
    def tokenize(self,raw):
        S = []
        currentNum = ""
        for r in raw:
            if r in "()+-*/":
                if len(currentNum) > 0 : 
                    S.append(currentNum)
                    currentNum = ""
                S.append(r)
            elif r in "0123456789":
                currentNum += r
        return S



    def build_expression_tree(self,token):
        tokens = self.tokenize(token)
        S = []
        
        for t in tokens:
            if t in "+-*/":
                S.append(t)
            elif t not in "()":
                S.append(ExpressionTree(t))
            elif t == ')': # end of expression
                right = S.pop()
                op = S.pop()
                left = S.pop()
                # print(f"Right : {right} , Left : {left}")
                S.append(ExpressionTree(op,left,right))
        return S.pop()
T1 = ExpressionTree("10")
T2 = ExpressionTree("20")
ET = ExpressionTree("*",T1,T2)
print(ET)
print(ET.evaluate())
print(ET.tokenize("((3+1)*10 - 10)"))
rt = ET.build_expression_tree("((3+1)*10)")
print(rt ," = ",rt.evaluate())


expressions = [
        "((3+1)/10)",
        "3+5*2-(4/2)",
        "(12+24)*(18-6)/3",
        "100/25+34*2-7",
        "(((((3+5)))))",
        "42",
        "7*8/4-2+6",
        "(10+2)*(6/3)",
        "8+(6*3)-(4/2)",
        "((3+1)/(4-2))"
    ]

for expr in expressions:
    tokens = ET.tokenize(expr)
    print(f"Expression: {expr}\nTokens: {tokens}\n")