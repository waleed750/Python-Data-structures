from mutable_maps import MapBase
class SortedTableMap(MapBase):
    def __init__(self):
        self._table = []

    def _find_index(self, k, low, high):
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if self._table[mid]._key == k:
                return mid
            elif  k < self._table[mid]._key :
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)

    def __getitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            return self._table[j]._value
        else:
            None

    def __setitem__(self, k, v):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v
        else: 
            self._table.insert(j, self._item(k, v))

    def __delitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table.pop(j)
            return
        raise KeyError("key Error " + repr(k))

    def __iter__(self):
        """return itertable of keys"""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key

    def __contains__(self, key):
        return self.__getitem__(key) is not None

    def __len__(self):
        return len(self._table)

    def find_min(self):
        """return (Key,value) Pair with minimum key (or else None)"""
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """return (Key,value) Pair with maximum key (or else None)"""
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        """return (Key,value) Pair with least key greater than or Equal to K(or else None)"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_gt(self, k):
        """return (Key,value) Pair with least key strictly greater than K(or else None)"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            j += 1
            if j < len(self._table):
                return (self._table[j]._key, self._table[j]._value)
            else:
                return None
        else:
            return None

    def find_lt(self, k):
        """return (Key,value) Pair with greatest key strictly less than K(or else None)"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0 :
            return (self._table[j-1]._key, self._table[j-1]._value)
        else:
            return None
    def find_le(self, k):
        """return (Key,value) Pair with greatest key  less than or Equal K(or else None)"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0 :
            if self._table[j]._key != k:
                j-=1
            return (self._table[j]._key, self._table[j]._value)
        else: 
            return None
    def find_range(self,start,stop):
        if start is None:
            j = 0 
        else:
            j = self._find_index(start,0,len(self._table) - 1)
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1


def reverse_print_map(M:SortedTableMap):
    rKeys = M.__reversed__()      # get all keys in reverse order 
    for key in rKeys:
     print(key, ':', M.__getitem__(key), sep='', end=' ')
     print()
