import time
import threading


start = time.perf_counter()

def do_something(seconds):
    print('Sleeping...')
    time.sleep(seconds)
    print('done')


t1 = threading.Thread(target= do_something, args=[1.5])
t2 = threading.Thread(target= do_something, args= [1.5])

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()


print(f"Finished in {round(finish-start,2)}")

# OR 


with concurrent.futures.ThreadPoolExecutor() as exe:
    try:
        f1 = exe.submit(obstacles.generate)
    except RuntimeError:
        pass
    obstacles_ = f1.result()
    main(obstacles_)