package com.leo.leetcode.thread;

import java.util.concurrent.CountDownLatch;


public class Q1114 {
    public static void main(String[] args) {
        Foo obj = new Foo();

        new Thread(() -> runTask(obj, 2)).start();
        new Thread(() -> runTask(obj, 1)).start();
        new Thread(() -> runTask(obj, 3)).start();
    }

    static void runTask(Foo foo, int taskId) {
        try {
            switch (taskId) {
                case 1:
                    foo.first(() -> System.out.println(1));
                    break;
                case 2:
                    foo.second(() -> System.out.println(2));
                    break;
                case 3:
                    foo.third(() -> System.out.println(3));
                    break;
                default:
                    System.out.println("Unknown id: " + taskId);
                    break;
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    static class Foo {

        CountDownLatch c1;
        CountDownLatch c2;

        public Foo() {
            c1 = new CountDownLatch(1);
            c2 = new CountDownLatch(1);
        }

        public void first(Runnable printFirst) throws InterruptedException {

            // printFirst.run() outputs "first". Do not change or remove this line.
            printFirst.run();
            c1.countDown();
        }

        public void second(Runnable printSecond) throws InterruptedException {
            c1.await();
            // printSecond.run() outputs "second". Do not change or remove this line.
            printSecond.run();
            c2.countDown();
        }

        public void third(Runnable printThird) throws InterruptedException {
            c2.await();
            // printThird.run() outputs "third". Do not change or remove this line.
            printThird.run();
        }
    }
}
