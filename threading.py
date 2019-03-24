"prints 200 each time, because shared resource access synchronized"

import threading, time
count = 0

def adder(addlock):                 # 传入共享锁
    global count
    with addlock: 
        count = count + 1           # 自动获得、释放锁 
    time.sleep(0.5)
    with addlock:
        count = count + 1           # 同一时间只有一个线程进行修改

addlock = threading.Lock()#设置共享锁
threads = []
for i in range(100):
    thread = threading.Thread(target=adder, args=(addlock,))
    thread.start()
    threads.append(thread)

for thread in threads: 
    thread.join()#等待所有线程退出
print(count)