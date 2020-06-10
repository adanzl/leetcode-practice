package com.leo.leetcode.thread;

import java.util.concurrent.CountDownLatch;
import java.util.function.IntConsumer;

public class Q1116 {

    public static void main(String[] args) throws InterruptedException {
        new Q1116().TestOJ();
    }
    public void TestOJ() throws InterruptedException {

        CountDownLatch cd = new CountDownLatch(3);
        ZeroEvenOdd obj = new ZeroEvenOdd(6);

        new Thread(() -> {
            try {
                obj.zero(System.out::print);
                cd.countDown();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        new Thread(() -> {
            try {
                obj.even(System.out::print);
                cd.countDown();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        new Thread(() -> {
            try {
                obj.odd(System.out::print);
                cd.countDown();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        cd.await(); // 0102030405
    }

    class ZeroEvenOdd {
        private volatile int flag = 0; // 0: even, 1: odd
        private volatile boolean zero = true;
        private int n;

        public ZeroEvenOdd(int n) {
            this.n = n;
        }

        // printNumber.accept(x) outputs "x", where x is an integer.
        synchronized public void zero(IntConsumer printNumber) throws InterruptedException {
            for (int i = 0; i < n; i++) {
                while (!zero) {
                    wait();
                }
                printNumber.accept(0);
                zero = false;
                notifyAll();
            }
        }

        synchronized public void even(IntConsumer printNumber) throws InterruptedException { // 2
            for (int i = 2; i <= n; i += 2) {
                while (flag == 0 || zero) {
                    wait();
                }
                printNumber.accept(i);
                zero = true;
                flag = 0;
                notifyAll();
            }
        }

        synchronized public void odd(IntConsumer printNumber) throws InterruptedException { // 1
            for (int i = 1; i <= n; i += 2) {
                while (flag == 1 || zero) {
                    wait();
                }
                printNumber.accept(i);
                zero = true;
                flag = 1;
                notifyAll();
            }
        }
    }
}
