from Code.linked_binary_tree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    def __init__(self,token,left=None,right=None):
        super().__init__()
        if isinstance(token,str):
            raise TypeError("Token must be an operand")
        self._add_root(token)
        if left is not None:
            if token not in '-=+*x/':
                raise ValueError("Token must be operand")
            self.attach(self.root(),left,right)
    def __str__(self):
        result = []
        self._parenthesise_recur(self.root(),result)
        return result
    def parenthesise_recur(self,p,result):
        if p.is_leaf():
            result.append(str(p.element()))
        else:
            result.append('(')
            self._parenthesise_recur(self.left(p),result)
            result.append(p.element())
            self._parenthesise_recur(self.right(p),result)
            result.append(')')
    
