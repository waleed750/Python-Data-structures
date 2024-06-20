from mutable_maps import MapBase
class UnsortedTableMap(MapBase):
    def __init__(self) -> None:
        '''initialize table with Empty list'''
        self._table : list = [] 
    def __getitem__(self,k):
        for item in self._table:
            if item._key == k:
                return item._value
        raise KeyError("key Error "+repr(k))
    def __setitem__(self,k,v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        # didn;t find match for key    
        self._table.append(self._item(k,v))
    def __delitem__(self,k):
        for index in range(len(self._table)):
            item = self._table[index]
            if item._key == k:
                self._table.pop(index)
                return
        #didn't find match for key
        raise KeyError("Key Error"+repr(k))
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
         keys = iter(M)      # get all keys
         for key in keys:
            print(key, ':', M.__getitem__(key), sep='', end=' ')
         print()
def main():
    M = UnsortedTableMap()
    print('Initial map length:', len(M))
    M.__setitem__('K', 2) 
    M.__setitem__('B', 4)
    M.__setitem__('U', 2)
    M.__setitem__('V', 8)
    print('Map length after adding 4 items:', len(M))    
    print('Map contents:')
    print_map(M)
    M.__setitem__('K', 9)
    print('Map contents after resetting value of key K:')
    print_map(M)
    print('item with key K exists:', M.__contains__('K'))
    M.__delitem__('B')
    print('item with key B exists:', M.__contains__('B'))
    print('Map contents after deleting item with key B:')
    print_map(M)

    ''' Example:Find the frequencies of distinct 
    words in a given sentence '''
    txt= input("Enter Sentence : ")
    freq = UnsortedTableMap()
    for t in txt.split():
        if freq.__contains__(t):
            freq.__setitem__(t, freq.__getitem__(t) + 1)
        else:
            freq.__setitem__(t,1)
    print_map(freq)
main()