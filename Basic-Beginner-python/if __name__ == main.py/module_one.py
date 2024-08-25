# python interpreter sets "special variables", one of which is __name__
# python will assign the __name__ variable  a value of '__main__' if it's
# the initial module being run 




def hello():
    print("hello")


if __name__ == '__main__':
    hello()
else:
    print("This module will run indirectly")