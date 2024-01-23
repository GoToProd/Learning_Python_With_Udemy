import threading
import time


def heavy(n, i, thread):
    for i in range(1, n):
        for y in range(1,n):
            i**y
    print(f'loops {i} and threads {thread}')
    
    
def sequential(cals, thread):
    print(f'Starting the {thread} threads')
    for i in range(cals):
        heavy(500, i, thread)
    print(f'{cals} loops ended complete and {thread} threads finished')
    
    
def th(threads, cals):
    threas = []
    for thread in range(threads):
        t = threading.Thread(target=sequential, args=(cals, thread))
        threas.append(t)
        t.start()
        for t in threas:
            t.join()
            
            
if __name__ == '__main__':
    start = time.time()
    th(4,20)
    end = time.time()
    print(f'{start-end} all done')