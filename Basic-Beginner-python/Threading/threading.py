#thread = a flow of excecution. Like a separate order of instructions .
#         However each thread takes a turn running to acheive concurrency 
#         GIL = (global interpreter lock),
#         allows only one thread to hold the control of the Python interpreter at one time)


#cpu bound = program/task spends most of it's time waiting for internal events(CPU intensive use multiprocessing)

#io bound = program / task spends most of it's time waiting for external events (user input use multiprocessing)

import threading
import time

def drink_cofee():
    time.sleep(3)
    print("You drink cofee!")

def eat_breakfast():
    time.sleep(4)
    print("You eat breakfast!")

def study():
    time.sleep(5)
    print("You finish study!")


x = threading.Thread(target=drink_cofee, args=())
x.start()

y = threading.Thread(target=eat_breakfast, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

#drink_cofee()
#eat_breakfast()
#study()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())#will return how long it returns our calling thread as in our main thread to finish its set of instructions
