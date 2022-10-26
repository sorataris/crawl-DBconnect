import time
import threading


def do_something():
    print('START taking')
    time.sleep(3)
    print('Done Sleeping...')



start = time.perf_counter() #실행시간 측정
threads = []

#한번만 뜨레드 실행
t = threading.Thread(target=do_something)
t.start()
threads.append(t)
for i in range(1,20):
    time.sleep(1)



for thread in threads:
    thread.join()
finish = time.perf_counter()

