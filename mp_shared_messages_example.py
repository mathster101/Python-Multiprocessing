import multiprocessing as mp
import time as t
from random import randint as ri
import os

def listener(msg_queue):
    start_time = t.time()
    while t.time() - start_time < 60:#stay active for one minute!
        if not msg_queue.empty():
            rcvd = msg_queue.get() #reads only one elem, should prolly read till empty
            print(f"listener received {rcvd} !")
        else:
            pass
    return

def talker(msg_queue):
    for i in range(61):
        val = i + ri(0,10)
        msg_queue.put(val)
        print(f"{os.getpid()} sent {val} !")
        t.sleep(1)
    return


if __name__ == '__main__':
    queue = mp.SimpleQueue()# can also use mp.Queue() but simple is safer!
    listener_proc = mp.Process(target = listener, args = (queue,))
    talker_proc1 = mp.Process(target = talker, args = (queue,))
    talker_proc2 = mp.Process(target = talker, args = (queue,))
    
    listener_proc.start()
    talker_proc1.start()
    talker_proc2.start()

    listener_proc.join()# only the listener really needs to be join()ed here tbh
    # talker_proc1.join()
    # talker_proc2.join()