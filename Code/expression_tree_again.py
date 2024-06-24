from linked_binary_tree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    def __init__(self, token, left=None, right=None):
        super().__init__()  # initiate root
        if not isinstance(token, str):
            raise TypeError("Token must be type string ")
        self._add_root(token)
        if left is not None:
            if token not in "+-*/x":
                raise ValueError("Must be operator")
            self.attach(self.root(), left, right)

    def __str__(self):
        pices = []
        self.parnthesize_recur(self.root(), pices)
        return "".join(pices)

    def parnthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append("(")
            self.parnthesize_recur(self.left(p),result)
            result.append(p.element())
            self.parnthesize_recur(self.right(p),result)
            result.append(")")

    def evaluate(self, token):
        return self.evaluate_recur(self.root(), token)

    def evaluate_recur(self, p, token):
        if self.is_leaf(p):
            return float(p.element())
        else:
            left = self.evaluate_recur(self.left(p), token)
            op = p.element()
            right = self.evaluate_recur(self.right(p), token)
            if op == "+":
                return left + right
            elif op == "-":
                return left - right
            elif op == "/":
                return left / right
            else: # * or  x 
                return left * right
    def build_expression_tree(self,token):
        s = []
        for t in token:
            if t in '+-*/x':
                s.append(t)
            elif t not in '()':
                s.append(ExpressionTree(t))
            elif t == ')':
                right = s.pop()
                op = s.pop()
                left = s.pop()
                s.append(ExpressionTree(op,left,right))
        return s.pop()
ET = ExpressionTree('+')
TE = ET.build_expression_tree("(((3+1)x4)/((9-5)+2))")
print(f"The value of this Expression {TE} : {TE.evaluate(TE)}")