

#! IV) 
#! 1- getMin()

from z_tree import LinkedBinaryTree


def preorder(self):
    if not self.is_empty():
        for p in self.preorder_recur(self.root()):
            yield p 
def preorder_recur(self,p):
    yield p 
    for c in self.children(p):
        for other in self.preorder_recur(c):
            yield other
def getMin(self):
    minmum = self._head._element
    for p in self.preorder():
        if minmum > p.element():
            minmum = p.element()
    return minmum    

#! 3- insertBst()

def insertBst(self,k,T):
    if T is None:
        T = LinkedBinaryTree()
    self.insertBst_recur(T.root(),k,T)
    return T
def insertBst_recur(self,p,k,T):
    if p is None:
        return T._add_root(k)
    else:
        if k < p.element() : 
            if T.left(p) is None:
                return T._add_left(p,k)
            else:
                return T.insertBst_recur(T.left(p),k,T)
        else:
            if T.right(p) is None:
                return T._add_right(p,k)
            else:
                return T.insertBst_recur(T.right(p),k,T)
    

