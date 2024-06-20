from collections.abc import MutableMapping
class MapBase(MutableMapping):
    class _item:
        def __init__(self, k, v) -> None:
            __slots__ = "_key", "_value"
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self._key == other._key)

        def __it__(self, other):
            return self._key < other._key


class UnsortedTableMap(MapBase):
    def __init__(self) -> None:
        self._table: list = []

    def __getitem__(self, k):
        for item in self._table:
            if item._key == k:
                return item._value
        # didn't find a matched key
        raise KeyError("Key Error : " + repr(k))

    def __setitem__(self, k, v):
        for item in self._table:
            if item._key == k:
                item._value = v
                return
        # didn't find a matched key
        self._table.append(self._item(k, v))

    def __delitem__(self, k):
        for index in range(len(self._table)):
            item = self._table[index]
            if item._key == k:
                self._table.pop(index)
                return
        # didn't find a matched key
        raise KeyError("Key Error : " + repr(k))

    def __len__(self):
        return len(self._table)

    def __contains__(self, key):
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

    def __iter__(self):
        for item in self._table:
            yield item._key


def print_map(M):
    keys = iter(M)
    for key in keys:
        value = M.__getitem__(key)
        print(f"{key} : {value}", end=" ")
    print()


def main():
    M = UnsortedTableMap()
    print("Initial map length:", len(M))
    M.__setitem__("K", 2)
    M.__setitem__("B", 4)
    M.__setitem__("U", 2)
    M.__setitem__("V", 8)
    print("Map length after adding 4 items:", len(M))
    print("Map contents:")
    print_map(M)
    M.__setitem__("K", 9)
    print("Map contents after resetting value of key K:")
    print_map(M)
    print("item with key K exists:", M.__contains__("K"))
    M.__delitem__("B")
    print("item with key B exists:", M.__contains__("B"))
    print("Map contents after deleting item with key B:")
    print_map(M)
    sentence = input("Enter sentence : ")
    freqMap = UnsortedTableMap()
    for s in sentence.split():
        if freqMap.__contains__(s):
            freq = freqMap.__getitem__(s) + 1
            freqMap.__setitem__(s, freq)
        else:
            freqMap.__setitem__(s, 1)
    print_map(freqMap)


# main()


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

def main2():
    M = SortedTableMap()
    M.__setitem__('K', 2) 
    M.__setitem__('B', 14)
    M.__setitem__('U', 2)
    M.__setitem__('V', 8)
    print('Map length after adding 4 items:', len(M))
    print('Map contents:', end=' ')
    print_map(M)
    M.__setitem__('K', 9)
    print('Map contents after resetting value of key K:')
    print_map(M)
    M.__setitem__('F', 10)
    print('Map contents after adding an item with key F:', end=' ')
    print_map(M)  
    print('Minimum  element:', M.find_min())
    print('Maximum  element:', M.find_max())
    print('Element >= F:', M.find_ge('F'))
    print('Element >= L:', M.find_ge('L'))
    print('Element > F:', M.find_gt('F'))
    print('Element < F:', M.find_lt('F'))
    print('Element <= F:', M.find_le('F'))
    print('Element <= E:', M.find_le('E'))    
    range = M.find_range('F', 'U')
    print('All pairs with F <= key < U:' , end=' ')
    for elem in range:
        print(elem, end=' ') 
    print()    
    print('Reversed map contents:', end=' ')
    reverse_print_map(M) 
main2()
