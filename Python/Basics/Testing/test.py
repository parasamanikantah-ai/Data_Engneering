# import sys

# a = [1, 2, 3]  # Reference count of [1, 2, 3] is 1 (from 'a')
# print(f"Reference count of 'a': {sys.getrefcount(a) - 1}") # -1 because sys.getrefcount itself adds a temporary reference

# b = a          # Reference count of [1, 2, 3] is now 2 (from 'a' and 'b')
# print(f"Reference count of 'a' after 'b = a': {sys.getrefcount(a) - 1}")

# del a          # Reference count of [1, 2, 3] is now 1 (only from 'b')
# print(f"Reference count of 'a' after 'del a': {sys.getrefcount(b) - 1}")



# del b          # Reference count of [1, 2, 3] is now 0. Memory is reclaimed.
# # After 'del b', trying to access 'b' would result in a NameError.
# # The object [1, 2, 3] is now eligible for immediate deallocation.



# for i in range(99):
#     print(i)


def generate():
    for i in range(1,34):
        yield i 

gen = generate()



print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))