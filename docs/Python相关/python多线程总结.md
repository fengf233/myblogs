

### 概述

#### 进程与线程

进程：进程是资源（CPU、内存等）分配的最小单位，进程有独立的地址空间与系统资源，一个进程可以包含一个或多个线程

线程：线程是CPU调度的最小单位，是进程的一个执行流，线程依赖于进程而存在，线程共享所在进程的地址空间和系统资源，每个线程有自己的堆栈和局部变量

形象的解释：

系统是一个工厂，进程就是工厂里面的车间；

车间的空间大小以及里面的生产工具就是系统分配给进程的资源（CPU、内存等）；

车间要完成生产，就需要工人，工人就是线程；

工人可以使用车间的所有资源，就是线程共享进程资源；

工人使用车间内的一个工作间(全局变量，共享内存)工作的时候,为了防止其他工人打扰，会上一把锁，工作完成才会取下，这是线程锁；

有的工作间可以同时容纳多个工人工作，于是就有多把钥匙，每个工人就拿上一把，所有钥匙被取完后，其他工人就只能等着，这是信号量(Semaphore)；

有时候工人之间有合作，当一个工作间的工人工作到满足某个条件时，会发出通知并同时退出工作间，将钥匙交给另外符合条件正在等待的工人完成工作，这叫条件同步；

还有一种工作模式，当一个工人完成到某个指标时，会将工作传递给其它等待这个指标触发的工人工作，这叫事件同步

#### 并发与并行

并发：当系统只有一个CPU时，想执行多个线程，CPU就会轮流切换多个线程执行，当有一个线程被执行时，其他线程就会等待，但由于CPU调度很快，所以看起来像多个线程同时执行

并行：当系统有多个CPU时，执行多个线程，就可以分配到多个CPU上同时执行 

#### 同步与异步

同步：调用者调用一个功能时，必须要等到这个功能执行完返回结果后，才能再调用其他功能

异步：调用者调用一个功能时，不会立即得到结果，而是在调用发出后，被调用功能通过状态、通知来通告调用者，或通过回调函数处理这个调用

### 多线程模块

#### threading模块

threading模块常用函数

- threading.current_thread(): 返回当前的线程对象。
- threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
- threading.active_count(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

#### Thread类

通过threading.Thread()创建线程对象

主要参数：

**threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)**

- **group** 默认为 None，为了日后扩展 ThreadGroup 类实现而保留。
- **target** 是用于 run() 方法调用的可调用对象。默认是 None，表示不需要调用任何方法。
- **name** 是线程名称。默认情况下，由 "Thread-N" 格式构成一个唯一的名称，其中 N 是小的十进制数
- **args** 是用于调用目标函数的参数元组。默认是 ()
- **kwargs** 是用于调用目标函数的关键字参数字典。默认是 {}。
- **daemon**表示线程是不是守护线程。

**Thread类常用方法与属性**

- **run():** 用以表示线程活动的方法。
- **start():**启动线程活动。 
- **join(**timeout=None**):** 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
- **isAlive():** 返回线程是否活动的。
- **getName():** 返回线程名。
- **setName():** 设置线程名。
- **name**：线程对象名字
- **setDaemon()**：设置是否为守护线程

#### 创建多线程

1.通过函数方法创建

```
import threading
import time


def run(sec):
    print('%s 线程开始了！' % threading.current_thread().name)
    time.sleep(sec)
    print('%s 线程结束了！' % threading.current_thread().name)


if __name__ == '__main__':

    print('主线程开始执行：', threading.current_thread().name)

    s_time = time.time()
    # 创建thread对象，target传入线程执行的函数，args传参数
    t1 = threading.Thread(target=run, args=(1,))
    t2 = threading.Thread(target=run, args=(2,))
    t3 = threading.Thread(target=run, args=(3,))
    # 使用start()开始执行
    t1.start()
    t2.start()
    t3.start()
    # 使用join()来完成线程同步
    t1.join()
    t2.join()
    t3.join()

    print('主线程执行结束', threading.current_thread().name)
    print('一共用时：', time.time()-s_time)
```

2.通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法

```
import threading
import time


class MyThread(threading.Thread):

    def __init__(self, sec):
        super(MyThread, self).__init__()
        self.sec = sec
    #重写run()方法，使它包含线程需要做的工作
    def run(self):
        print('%s 线程开始了！' % threading.current_thread().name)
        time.sleep(self.sec)
        print('%s 线程结束了！' % threading.current_thread().name)


if __name__ == '__main__':

    print('主线程开始执行', threading.current_thread().name)
    s_time = time.time()

    # 实例化MyThread对象
    t1 = MyThread(1)
    t2 = MyThread(2)
    t3 = MyThread(3)
    # 实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法
    t1.start()
    t2.start()
    t3.start()
    # 使用join()来完成线程同步
    t1.join()
    t2.join()
    t3.join()

    print('一共用时：', time.time()-s_time)
    print('主线程结束执行', threading.current_thread().name)
```

### 线程锁

多个线程操作全局变量的时候，如果一个线程对全局变量操作分几个步骤，当还没有得到最后结果时，这个线程就被撤下CPU，使用其他线程继续上CPU操作，最后就会搞乱全局变量数据

```
import time, threading

balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000):
        change_it(n)

#这里重复实验100次
for i in range(100):
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
```

这里可以发现打印出数据会有非0情况

而线程锁就是防止这种情况。每当一个线程a要访问共享数据时，必须先获得锁定；如果已经有别的线程b获得锁定了，那么就让线程a暂停，也就是同步阻塞；等到线程b访问完毕，释放锁以后，再让线程a继续

锁有两种状态：被锁（locked）和没有被锁（unlocked）。拥有acquire()和release()两种方法，并且遵循一下的规则：

- 如果一个锁的状态是unlocked，调用acquire()方法改变它的状态为locked；
- 如果一个锁的状态是locked，acquire()方法将会阻塞，直到另一个线程调用release()方法释放了锁；
- 如果一个锁的状态是unlocked调用release()会抛出RuntimeError异常；
- 如果一个锁的状态是locked，调用release()方法改变它的状态为unlocked。

```
import time, threading

balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    #获取锁，用于线程同步
    lock.acquire()
    balance = balance + n
    balance = balance - n
    # 释放锁，开启下一个线程
    lock.release()

def run_thread(n):
    for i in range(1000):
        change_it(n)

#这里重复实验100次
for i in range(100):
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
```

锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。

### 条件同步

条件同步机制是指：一个线程等待特定条件，而另一个线程发出特定条件满足的信号。

解释条件同步机制的一个很好的例子就是生产者/消费者（producer/consumer）模型。生产者随机的往列表中生产一个随机整数，而消费者从列表中消费整数。

```
import threading
import random
import time

class Producer(threading.Thread):
    """
    向列表中生产随机整数
    """

    def __init__(self, integers, condition):
        """
        构造器

        @param integers 整数列表
        @param condition 条件同步对象
        """
        super(Producer, self).__init__()
        self.integers = integers
        self.condition = condition

    def run(self):
        """
        实现Thread的run方法。在随机时间向列表中添加一个随机整数
        """
        while True:
            integer = random.randint(0, 256)
            self.condition.acquire()  # 获取条件锁
            self.integers.append(integer)
            print ('%d appended to list by %s' % (integer, self.name))
            self.condition.notify()  # 唤醒消费者线程
            self.condition.release()  # 释放条件锁
            time.sleep(1)  # 暂停1秒钟


class Consumer(threading.Thread):
    """
    从列表中消费整数
    """

    def __init__(self, integers, condition):
        """
        构造器

        @param integers 整数列表
        @param condition 条件同步对象
        """
        super(Consumer, self).__init__()
        self.integers = integers
        self.condition = condition

    def run(self):
        """
        实现Thread的run()方法，从列表中消费整数
        """
        while True:
            self.condition.acquire()  # 获取条件锁
            while True:
                if self.integers:  # 判断是否有整数
                    integer = self.integers.pop()
                    print ('%d popped from list by %s' % (integer, self.name))
                    break
                self.condition.wait()  # 等待商品，并且释放资源
            self.condition.release()  # 最后释放条件锁


if __name__ == '__main__':
    integers = []
    condition = threading.Condition()
    t1 = Producer(integers, condition)
    t2 = Consumer(integers, condition)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```

类似于线程锁，通过给生产者和消费者传入同个条件对象后，他们都会通过acquire()获取条件锁；如上，消费者获取条件锁，如果没有锁，就会去判断integers中是否有整数，没有就会触发wait()方法，等待生产者线程notify()的唤醒；wait()方法会释放底层锁，并且阻塞，

直到在另外一个线程中调用同一个条件对象的notify() 或 notify_all() 唤醒它，或者超时发生。生产者则就是获取锁，向integers添加值，唤醒其他wait()的线程，释放锁的循环过程。

### 事件同步(Event)

基于事件的同步是指：一个线程发送/传递事件，另外的线程等待事件的触发。与条件同步类似，只是少了我们自己添加锁的步骤。

同样用消费者与生产者为例

```
import threading
import random
import time


class Producer(threading.Thread):
    """
    向列表中生产随机整数
    """

    def __init__(self, integers, event):
        """
        构造器

        @param integers 整数列表
        @param event 事件同步对象
        """
        super(Producer, self).__init__()
        self.integers = integers
        self.event = event

    def run(self):
        """
        实现Thread的run方法。在随机时间向列表中添加一个随机整数
        """
        while True:
            integer = random.randint(0, 256)
            self.integers.append(integer)
            print('%d appended to list by %s' % (integer, self.name))
            print('event set by %s' % self.name)
            self.event.set()  # 设置事件
            self.event.clear()  # 发送事件
            print('event cleared by %s' % self.name)
            time.sleep(1)


class Consumer(threading.Thread):
    """
     从列表中消费整数
    """

    def __init__(self, integers, event):
        """
        构造器

        @param integers 整数列表
        @param event 事件同步对象
        """
        super(Consumer, self).__init__()
        self.integers = integers
        self.event = event

    def run(self):
        """
        实现Thread的run()方法，从列表中消费整数
        """
        while True:
            self.event.wait()  # 等待事件被触发
            try:
                integer = self.integers.pop()
                print('%d popped from list by %s' % (integer, self.name))
            except IndexError:
                # catch pop on empty list
                time.sleep(1)


if __name__ == '__main__':
    integers = []
    event=threading.Event()
    t1 = Producer(integers, event)
    t2 = Consumer(integers, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```

事件对象的set()方法会将内部标志设置为true，并且唤醒其他阻塞的线程；clear()方法则是将内部标志设置为False；wait()方法当内部标准为false时就阻塞，true则不阻塞且wait()内部什么都不操作

### 队列(Queue)

队列可以看作事件同步与条件同步的简单版，线程A可以往队列里面存数据，线程B则可以从队列里面取，不用关心同步以及锁的问题，主要方法有:

- put(): 向队列中添加一个项
- get(): 从队列中删除并返回一个项
- task_done(): 当某一项任务完成时调用,表示前面排队的任务已经被完成
- join(): 阻塞直到所有的项目都被处理完

```
import threading
import queue
import random
import time

class Producer(threading.Thread):

    def __init__(self, queue):
        super(Producer,self).__init__()
        self.queue = queue

    def run(self):
        while True:
            integer = random.randint(0, 1000)
            self.queue.put(integer)
            print('%d put to queue by %s' % (integer, self.name))
            time.sleep(1)


class Consumer(threading.Thread):

    def __init__(self, queue):
        super(Consumer, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            integer = self.queue.get()
            print('%d popped from list by %s' % (integer, self.name))
            self.queue.task_done()


if __name__ == '__main__':

    queue = queue.Queue()
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```

参考:

[http://yoyzhou.github.io/blog/2013/02/28/python-threads-synchronization-locks/](http://yoyzhou.github.io/blog/2013/02/28/python-threads-synchronization-locks/)

[https://www.cnblogs.com/cnkai/p/7506476.html](https://www.cnblogs.com/cnkai/p/7506476.html)

[https://docs.python.org/zh-cn/3/library/threading.html](https://docs.python.org/zh-cn/3/library/threading.html)
