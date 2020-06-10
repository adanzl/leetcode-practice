package com.leo.leetcode.thread;

import java.util.concurrent.CountDownLatch;

public class Q1115 {

    public static void main(String[] args) throws InterruptedException {
        new Q1115().TestOJ();
    }

    public void TestOJ() throws InterruptedException {

        FooBar obj = new FooBar(5);

        new Thread(() -> {
            try {
                obj.foo(() -> System.out.print("foo"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        new Thread(() -> {
            try {
                obj.bar(() -> System.out.println("bar"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        new CountDownLatch(1).await();
    }


    static class FooBar {
        private final int n;
        private CountDownLatch cFoo;
        private CountDownLatch cBar;

        public FooBar(int n) {
            this.n = n;
            this.cFoo = new CountDownLatch(1);
            this.cBar = new CountDownLatch(0);
        }

        public void foo(Runnable printFoo) throws InterruptedException {

            for (int i = 0; i < n; i++) {
                this.cBar.await();
                // printFoo.run() outputs "foo". Do not change or remove this line.
                printFoo.run();
                this.cBar = new CountDownLatch(1);
                this.cFoo.countDown();
            }
        }

        public void bar(Runnable printBar) throws InterruptedException {

            for (int i = 0; i < n; i++) {
                this.cFoo.await();
                // printBar.run() outputs "bar". Do not change or remove this line.
                printBar.run();
                this.cFoo = new CountDownLatch(1);
                this.cBar.countDown();
            }
        }
    }

}
