import multiprocessing as mp
import time as t
import os
def dummy(shared_var):
    for i in range(5):
        with shared_var.get_lock():
            shared_var.value += 1
            print(f'{os.getpid()}-->{shared_var.value}')
        t.sleep(1)



if __name__ == '__main__':
    shared_var = mp.Value('f',0)# float and start with va zero
    # or shared_var = mp.Array('i',[1,2,3,4]) for shared array
    procs = []
    for n in range(10):
        procs.append( mp.Process(target = dummy, args = (shared_var,)) )
        procs[-1].start()
    for p in procs:
        p.join()