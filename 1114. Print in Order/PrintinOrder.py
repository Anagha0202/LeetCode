#Barrier
from threading import Barrier
class FooBarrier:
    def __init__(self):
        self.first_second_barrier = Barrier(2)
        self.second_third_barrier =  Barrier(2)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_second_barrier.wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_second_barrier.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_third_barrier.wait()

    def third(self, printThird: 'Callable[[], None]'0) -> None:
        self.second_third_barrier.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

#Lock
from threading import Lock
class FooLock:
    def __init__(self):
        self.locks = [Lock(), Lock()]
        self.locks[0].acquire()
        self.locks[1].acquire()
    
    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.locks[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # needs to acquire locks[0] and then run the print and the release the lock
        # its done implicility when suing "with"
        with self.locks[0]:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.locks[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.locks[1]:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()    

#Event
from threading import Event
class FooEvent:
    def __init__(self):
        self.completed = (Event(), Event())

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.completed[0].set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.completed[0].wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.completed[1].set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.completed[1].wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

#Semaphore
from threading import Semaphore
class FooSemaphore:
    def __init__(self):
        self.semaphore = (Semaphore(0), Semaphore(0))

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.semaphore[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.semaphore[0]:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.semaphore[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.semaphore[1]:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
            self.semaphore[1].release()