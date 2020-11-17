"""
1115.交替打印FooBar
我们提供一个类：

class FooBar {
  public void foo() {
  for (int i = 0; i < n; i++) {
   print("foo");
   }
  }

  public void bar() {
  for (int i = 0; i < n; i++) {
   print("bar");
  }
  }
}
两个不同的线程将会共用一个 FooBar实例。其中一个线程将会调用foo()方法，另一个线程将会调用bar()方法。

请设计修改程序，以确保 "foobar" 被输出 n 次。

示例 1:
输入: n = 1
输出: "foobar"
解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。

示例 2:
输入: n = 2
输出: "foobarfoobar"
解释: "foobar" 将被输出两次。
"""
from threading import Lock
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_done = Lock()
        self.bar_done = Lock()
        self.foo_done.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.bar_done.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.foo_done.release()



    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_done.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.bar_done.release()

