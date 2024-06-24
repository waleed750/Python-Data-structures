from collections.abc import MutableMapping

class MapBase(MutableMapping):
    class _item:
        __slots__ = '_key' , '_value'
        def __init__(self,k,v):
            self._key = k
            self._value = v
        def __eq__(self, other):
            return self._key == other._key
        def __ne__(self, other) :
            return not (self._key == other._key)
        def __lt__(self,other):
            return self._key < other._key
class UnSortedTableMap(MapBase):
    def __init__(self):
        self._table = []
    def __len__(self):
        return len(self._table)
    def is_empty(self):
        return len(self._table) == 0 
    def __setitem__(self,k,v):
        for item in self._table:
            if item._key == k :
                item._value = v
                return
        self._table.append(self._item(k,v))
    def __getitem__(self, k) :
        for item in self._table:
            if item._key == k :
                return item._value 
        raise KeyError("Key Error : "+repr(k))
    
    def __delitem__(self, k) :
        for index in range(len(self._table)):
            if self._table[index]._key == k :
                self._table.pop(index)
                return 
        raise KeyError("Key Error : "+repr(k))
    def __contains__(self, k):
        try:
            self.__getitem__(k)
            return True
        except KeyError:
            return False
    def __iter__(self):
        for item in self._table:
            yield item._key
     