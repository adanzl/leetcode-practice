package com.leo.leetcode.thread;

import java.util.concurrent.CountDownLatch;

public class QTurnPrint {

    public static void main(String[] args) throws InterruptedException {
        new QTurnPrint().TestOJ();
    }

    volatile int flag = 0;

    public void TestOJ() throws InterruptedException {
        Object lock = new Object();
        CountDownLatch cd = new CountDownLatch(2);
        new Thread(() -> {
            char[] str = "1234".toCharArray();
            int i = 0;
            synchronized (lock) {
                while (i < str.length) {
                    while (flag != 0) {
                        try {
                            lock.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                    flag = 1;
                    System.out.println(str[i++]);
                    lock.notifyAll();
                }
                cd.countDown();
            }
        }).start();
        new Thread(() -> {
            char[] str = "abcd".toCharArray();
            int i = 0;
            synchronized (lock) {
                while (i < str.length) {
                    while (flag != 1) {
                        try {
                            lock.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                    flag = 0;
                    System.out.println(str[i++]);
                    lock.notifyAll();
                }
                cd.countDown();
            }

        }).start();
        cd.await();
    }
}
