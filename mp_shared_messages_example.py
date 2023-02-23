import multiprocessing as mp
import time as t

def listener(msg_queue):
    start_time = t.time()
    while t.time() - start_time < 60:#stay active for one minute!
        if not msg_queue.empty():
            rcvd = msg_queue.get()
            print(f"listener received {rcvd} !")
        else:
            pass
    return

def talker(msg_queue):
    for i in range(61):
        msg_queue.put(i)
        print(f"sender sent {i} !")
        t.sleep(1)
    return


if __name__ == '__main__':
    queue = mp.SimpleQueue()# can also use mp.Queue() but simple is safer!
    listener_proc = mp.Process(target = listener, args = (queue,))
    talker_proc = mp.Process(target = talker, args = (queue,))
    
    listener_proc.start()
    talker_proc.start()

    listener_proc.join()
    talker_proc.join()