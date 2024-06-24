from collections.abc import MutableMapping #1 

class MapBase(MutableMapping):
    class _item:
        __slots__ = "_key", "_value"

        def __init__(self, k, v) -> None:
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self._key == other._key)

        def __lt__(self, other):
            return self._key < other._key


class UnsortedTableMap(MapBase):
    #! getitem - setitem - deleteitem - contains(try except) - iter
    #! raise key Error if key not found
    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if item._key == k:
                return item._value
        raise KeyError("Key Error " + repr(k))

    def __setitem__(self, k, v):
        for item in self._table:
            if item._key == k:
                item._value = v
                return
        self._table.append(self._item(k, v))

    def __delitem__(self, k) -> None:
        for index in range(len(self._table)):
            if self._table[index]._key == k:
                self._table.pop(index)
                return
        raise KeyError("Key Error " + repr(k))

    def __len__(self):
        return len(self._table)

    def __contains__(self, k):
        try:
            self.__getitem__(k)
            return True
        except:
            return False

    def __iter__(self):
        for item in self._table:
            yield item._key


def print_map(M):
    print("Map : { ", end="")
    for key in iter(M):
        value = M.__getitem__(key)
        print(f"{key}:{value}", end=" ")
    print("}")


# m = UnsortedTableMap()
# print(f"Initial Map length : {len(m)}")
# m.__setitem__('k',2)
# m.__setitem__('B',4)
# m.__setitem__('U',2)
# m.__setitem__('V',8)
# print_map(m)
# m.__delitem__('B')
# print(f"item with key K exists {m.__contains__('k')}")
# print(f"item with key B exists {m.__contains__('B')}")
# print(" Map contents after deleting item with key B:")
# print_map(m)


#! _find_index (works like binary tree high -low )
# k < mid [low to mid -1 ] if k> mid [mid to high]
# base case high < low
# mid = (high + low ) // 2


class SortedTableMap(MapBase):
    def __init__(self):
        self._table = []

    def _find_index(self, k, low, high):
        if high < low:
            return high + 1  # key not found
        mid = (high + low) // 2
        if k == self._table[mid]._key:
            return mid
        elif k < self._table[mid]._key:
            return self._find_index(k, low, mid - 1)
        else:
            return self._find_index(k, mid + 1, high)

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) and self._table[j]._key != k:
            raise KeyError("Key Error " + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v
        else:
            self._table.insert(j, self._item(k, v))

    def __delitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) and self._table[j] != k:
            raise KeyError("Key Error " + repr(k))
        self._table(j)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key

    def _find_min(self):
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)

    def _find_max(self):
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)

    def _find_ge(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def _find_gt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            j += 1
            if j < len(self._table):
                return (self._table[j]._key, self._table[j]._value)
            else:
                return None

    def _find_lt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            return (self._table[j - 1]._key, self._table[j - 1]._value)
        else:
            return None

    def _find_le(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            if self._table[j]._key != k:
                j -= 1
            return (self._table[j]._key, self._table[j]._value)  # Note use of j-1
        else:
            return None

    def _find_range(self, start, stop):
        if start is None:
            j = 0
        else:
            j = self._find_index(start,0, len(self._table) - 1)
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1


def reverse_print_map(M):
    rKeys = M.__reversed__()  # get all keys in reverse order
    for key in rKeys:
        print(key, ":", M.__getitem__(key), sep="", end=" ")
    print()


# M = SortedTableMap()
# M.__setitem__("K", 2)
# M.__setitem__("B", 14)
# M.__setitem__("U", 2)
# M.__setitem__("V", 8)
# print("Map length after adding 4 items:", len(M))
# print("Map contents:", end=" ")
# print_map(M)
# M.__setitem__("K", 9)
# print("Map contents after resetting value of key K:")
# print_map(M)
# M.__setitem__("F", 10)
# print("Map contents after adding an item with key F:", end=" ")
# print_map(M)
# print("Minimum  element:", M._find_min())
# print("Maximum  element:", M._find_max())
# print("Element >= F:", M._find_ge("F"))
# print("Element >= L:", M._find_ge("L"))
# print("Element > F:", M._find_gt("F"))
# print("Element < F:", M._find_lt("F"))
# print("Element <= F:", M._find_le("F"))
# print("Element <= E:", M._find_le("E"))
# range = M._find_range("F", "U")
# print("All pairs with F <= key < U:", end=" ")
# for elem in range:
#     print(elem, end=" ")
# print()
# print("Reversed map contents:", end=" ")
# reverse_print_map(M)

# class ToolStore:
#     def __init__(self) -> None:
#         # load data from the file tool.dat
#         self._toolList = SortedTableMap()
#         with open('tools.dat','r') as f:
#             for line in f:
#                 line = line.strip()
#                 tq = line.split(",")
#                 self._toolList.__setitem__(tq[0],int(tq[1]))
#     def AddTool(self,t,q):
#         self._toolList.__setitem__(t,q)
#         print("Tool addition/update completed")
#     def sellTool(self,t):


captials = {
    "Nepal": "Kathmandu",
    "USA": "Washington DC",
    "England": "London",
    "Australia": "Canberra"
}