#                           Higher Order Function = a function that either:
#                           argument an as function a accepts1.
#                                    or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(quiet)
hello(loud)