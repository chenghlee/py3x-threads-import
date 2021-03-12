from time import sleep
from threading import current_thread

# For the buggy(?) behavior to manifest itself, this sleep should be
# significantly longer than the thread switching interval set using
# `sys.setswitchinterval()`.
sleep(0.25)

def fn():
    thread = current_thread()
    print(f"{thread.name}: running fn()")
