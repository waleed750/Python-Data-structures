from unsorted_table_map import UnsortedTableMap , print_map
from sorted_table_map import SortedTableMap , reverse_print_map
class ToolStore:
    def __init__(self,filename) :
        self._toolList = SortedTableMap()
        print("File opened")
        with open(filename,'r') as file :
            for line in file:
                line = line.strip().replace(" ","")
                key_value = line.split(",")
                self._toolList.__setitem__(key_value[0],int(key_value[1]))
        # print_map(self._toolList)
    def add_tool(self,k,v):# tool name , quantity 
        self._toolList.__setitem__(k,v)
        print("Tool addition/update completed")
    def sell_tool(self,k):
        k = k.strip()
        if self._toolList.__contains__(k):
            value = self._toolList.__getitem__(k)
            if value > 0 :
                value -= 1 
                self._toolList.__setitem__(k,value)
                print("Tool sold")
            else:
                print("Tool not found")    
        else:
            print("Tool not found")
    def display(self):
        print_map(self._toolList)    

# read file from tools.dat
tools = ToolStore("tools.dat")

# Main program loop
while True:
    choice = input("Enter your choice (A for add, S for sell, D for display, X for exit): ").upper()

    if choice == 'A':
        tool_name = input("Enter the tool name: ")
        quantity = int(input("Enter the quantity: "))
        tools.add_tool(tool_name, quantity)

    elif choice == 'S':
        tool_name = input("Enter the tool name: ")
        tools.sell_tool(tool_name)

    elif choice == 'D':
        tools.display()

    elif choice == 'X':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")