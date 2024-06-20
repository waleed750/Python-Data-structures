from tree import BinaryTree
class ArrayBinaryTree(BinaryTree):
    class Position(BinaryTree):
        def __init__(self,element,index) -> None:
            self._element = element
            self._index = index
        def element(self):
            return self._element        
    def __init__(self) -> None:
        self._tree = [None] * 10
        self._root = 0
        self._size = 0  
    def len(self):
        return self._size
    def root(self):
        return self._tree[self._root]
    def left(self,p):
        if self.is_empty(): raise ValueError("no children here")
        index = 2 * p._index + 1
        if len(self._tree) < index:
            return None
        return self._tree[index] 
    def right(self,p):
        if self.is_empty(): raise ValueError("no children here")
        index = 2 * p._index + 2
        if len(self._tree) < index:
            return None
        return self._tree[index]
    def _add_root(self,e):
        if self._tree[self._root] is not None:
            raise ValueError("Already there is a root")
        self._tree[self._root] = self.Position(e,self._root)
        self._size = 1
        return self._tree[self._root] 
    def _add_left(self,p,e):
        index = 2 * p._index + 1
        new_pos = self.Position(e,index)
        if index > len(self._tree) :
            self._tree.append(new_pos)
        else:
            self._tree[index] = new_pos
        self._size += 1
        return new_pos
    def _add_right(self,p,e):
        index = 2 * p._index + 2 # right position
        new_pos = self.Position(e,index)
        if index > len(self._tree) :
            self._tree.append(new_pos)
        else:
            self._tree[index] = new_pos
        self._size += 1
        return new_pos
    
        
AT = ArrayBinaryTree()
root = AT._add_root(10)
r_root = AT._add_right(root,12)
print(f"Root of the tree : {root.element()}")
print(f"Roo Right child :{AT.right(root).element()}")