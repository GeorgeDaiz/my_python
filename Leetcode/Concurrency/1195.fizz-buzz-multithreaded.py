"""
1195.交替打印字符串
编写一个可以从 1 到 n 输出代表这个数字的字符串的程序，但是：

如果这个数字可以被 3 整除，输出 "fizz"。
如果这个数字可以被 5 整除，输出"buzz"。
如果这个数字可以同时被 3 和 5 整除，输出 "fizzbuzz"。
例如，当n = 15，输出：1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz。

假设有这么一个类：

class FizzBuzz {
 public FizzBuzz(int n) { ... }              // constructor
  public void fizz(printFizz) { ... }          // only output "fizz"
  public void buzz(printBuzz) { ... }          // only output "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
  public void number(printNumber) { ... }      // only output the numbers
}

请你实现一个有四个线程的多线程版FizzBuzz，同一个FizzBuzz实例会被如下四个线程使用：

线程A将调用fizz()来判断是否能被 3 整除，如果可以，则输出fizz。
线程B将调用buzz()来判断是否能被 5 整除，如果可以，则输出buzz。
线程C将调用fizzbuzz()来判断是否同时能被 3 和 5 整除，如果可以，则输出fizzbuzz。
线程D将调用number()来实现输出既不能被 3 整除也不能被 5 整除的数字。
"""
from typing import Callable
from threading import Lock


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.f_lock = Lock()
        self.b_lock = Lock()
        self.fb_lock = Lock()
        self.num_lock = Lock()
        self.f_lock.acquire()
        self.b_lock.acquire()
        self.fb_lock.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                self.f_lock.acquire()
                printFizz()
                self.num_lock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 == 0:
                self.b_lock.acquire()
                printBuzz()
                self.num_lock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                self.fb_lock.acquire()
                printFizzBuzz()
                self.num_lock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.num_lock.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fb_lock.release()
            elif i % 3 == 0:
                self.f_lock.release()
            elif i % 5 == 0:
                self.b_lock.release()
            else:
                printNumber(i)
                self.num_lock.release()
