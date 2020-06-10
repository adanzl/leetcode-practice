package com.leo.interview;

import java.util.concurrent.CountDownLatch;

public class QReadWriteLock {

    public static void main(String[] args) throws InterruptedException {
        new QReadWriteLock().TestOJ();
    }

    public void TestOJ() throws InterruptedException {
        QReadWriteLock rwLock = new QReadWriteLock();
        CountDownLatch cd = new CountDownLatch(4);
        new Thread(() -> {
            for (int i = 0; i < 10; i++) {
                try {
                    rwLock.readLock();
                    Thread.sleep(100);
                    rwLock.readUnlock();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            cd.countDown();
        }).start();
        new Thread(() -> {
            for (int i = 0; i < 10; i++) {
                try {
                    rwLock.readLock();
                    Thread.sleep(150);
                    rwLock.readUnlock();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            cd.countDown();
        }).start();
        new Thread(() -> {
            for (int i = 0; i < 10; i++) {
                try {
                    rwLock.writeLock();
                    Thread.sleep(110);
                    rwLock.writeUnlock();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            cd.countDown();
        }).start();
        new Thread(() -> {
            for (int i = 0; i < 10; i++) {
                try {
                    rwLock.writeLock();
                    Thread.sleep(100);
                    rwLock.writeUnlock();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            cd.countDown();
        }).start();
        cd.await();
    }

    volatile int write = 0;
    volatile int read = 0;

    synchronized void readLock() throws InterruptedException {
        while (write > 0) {
            wait();
        }
        System.out.println(Thread.currentThread().getName() + " GetRead R:" + read + " W:" + write);
        read++;
        notifyAll();
    }

    synchronized void readUnlock() throws InterruptedException {
        while (read == 0) {
            wait();
        }
        read--;
        notifyAll();
    }

    synchronized void writeLock() throws InterruptedException {
        while (write > 0 || read > 0) {
            wait();
        }
        System.out.println(Thread.currentThread().getName() + " GetWrite R:" + read + " W:" + write);
        write++;
        notifyAll();

    }

    synchronized void writeUnlock() throws InterruptedException {
        while (write == 0) {
            wait();
        }
        write--;
        notifyAll();
    }
}
