from threading import Semaphore, Barrier
class H2O:
    def __init__(self):
        self.H_Semaphore = Semaphore(2)
        self.O_Semaphore = Semaphore(1)
        self.HHO_Barrier = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.H_Semaphore: #implicitly acquires and releases the semaphore on exit
            self.HHO_Barrier.wait()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.O_Semaphore:
            self.HHO_Barrier.wait()
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()