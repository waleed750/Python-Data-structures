

#! I)
#! 1- Define dequeu ADT AND lIST METHODS THAT IT SUPPORTS. 
"""
 we consider a queue-like data structure that supports 
 insertion and deletion at both the front and the back of the  queue.
 List 
 Methods
 add_first - add_last - delete_first - delete_last
 first() - last() - is_empty() - len()
"""
#__________________________________________________________
#! 2- show the output of the following code



from z_array_stack import ArrayStack


def gen(n):
    for i in range(n):
        yield (i+1)**2
for t in zip(gen(4) , [5,10 , 15, 20 , 25 , 30]):
    print(t , end=" ")
print()
for x in enumerate(gen(5),1):
    print(x , end=" ")
print()

#? Answer: ___
#* output : 
"""
 (1,5) (4 , 10) (9,15) (16,20)
 (1,1) (2,4) (3 , 9 ) (4,16) (5,25)

"""
#___________________________________________________________
#! 3- 
#! Using the class ArrayStack, write a program that receives an infix expression
#! containing integer numbers (0 - 9) and the operators +, -, *. and /, then
#! evaluates and returns its value.
#! For example, if the infix expression is the result should be 6.
# !  
# !             (8-((((3+2)*2)-4)/3))

def infix_to_postifix(expr):
    s = ArrayStack()
    postifix_expr = []
    operators = {
        '+' : 1 , 
        '-' : 1 , 
        '*' : 2 , 
        '/' : 2 
    }
    lefty = '('
    righty = ')'
    nums = '0123456789'
    
    for c in expr:
        if c in nums:
            postifix_expr.append(c)
        elif c == lefty:
            s.push(c)
        elif c in righty :
            while not s.is_empty() and s.top() != lefty:
                postifix_expr.append(s.pop())
            s.pop() # remove left paranthesize
        elif c in operators.keys():
            while (
                (not s.is_empty())
                and (s.top() in operators.keys())
                and (operators[s.top()] >= operators[c])
            ) :
                postifix_expr.append(s.pop())
            s.push(c) # push the current operator 
    while not(s.is_empty()):
        postifix_expr.append(s.pop())
    return "".join(postifix_expr)

expr =infix_to_postifix("(8-((((3+2)*2)-4)/3))") 
print("Expr : " , expr)

def evaluate_postifix(expr):
    s = ArrayStack()
    nums = '0123456789'
    for c in expr:
        if c in nums:
            s.push(c)
        else:
            op2 = int(s.pop())
            op1 = int(s.pop())
            if c == '+':
                s.push(op1 + op2)
            elif c == '-':
                s.push(op1 - op2)
            elif c == '*':
                s.push(op1 * op2)     
            else:
                s.push(op1 / op2)
    return s.pop()
print(evaluate_postifix(expr))

