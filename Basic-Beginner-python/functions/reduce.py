#reduce() = apply a function to an iterable and reduce it to as a single cummalative value.
#           performs a function on  first to elements and repeats process until 1 value remains 
#
#reduce(function,iterable)

import functools

letters = ["h","e","l","l","o"]
word = functools.reduce(lambda x ,y :x+y,letters)
#here first x = h and y = e then x +y = he, it stores it in the letters["he","l","l","o"]
#["hel","l","o"]
#["hell","o"]
#["hello"]
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x ,y : x *y,factorial )
print(result)