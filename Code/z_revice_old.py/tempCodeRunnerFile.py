n = 120 
# i = 2
# f = []
# def prime_factors_linked_stack(n):
#     """Returns a list of all prime factors of the nonnegative integer n."""
#     i = 2 
#     temp_stack = LinkedStack()
#     while i * i <= n :
#         if n % i :
#             i += 1
#         else:
#             n //= i 
#             temp_stack.push(i)
#     if n > 1 :
#         temp_stack.push(n)
#     factors = LinkedStack()
#     while not temp_stack.is_empty():
#         factors.push(temp_stack.pop())
#     return factors
# factors = prime_factors_linked_stack(int(input("Enter a number : ")))
# factors.display()
