package com.leo.interview;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

/**
 * 1. 您需要写一个多线程有关的程序，主要是 Producer 和 Consumer 类；
 * 2. 程序以打印 ‘ Start’ 开始，以打印’Finished’结束，其他的在 Start 和 Finished 之间。
 * 3. Producer 不断生成 Item 实例，Consumer 不断消费 Producer 生产的 Item 实例；
 * 4. Producer 和 Consumer 实例要使用不同的线程进行生产、消费；
 * 5. Producer 生产的同一个 Item 实例只能被一个 Consumer 实例消费，并且只能消费一次；
 * 6. 每个 Consumer 每消费一个 Item 实例后，就打印出相关信息（参考下面打印示例）;
 * 7. 每个 Consumer 消费指定个数的 Item 实例后即完成任务（不能多不能少），然后告知 Producer ;
 * 8. 所有 Consumer 完成任务后，Producer 自动关闭，整个程序能够自动退出。
 */
public class Interview0422_2 {

    public static CountDownLatch CD;

    public static void main(String[] args) throws InterruptedException {
        CD = new CountDownLatch(1);
        int consumerCount = 8, itemCount = 3;
        Producer producer = new Producer(consumerCount);
        new Thread(producer).start();
        for (int i = 0; i < consumerCount; i++) {
            new Thread(new Consumer(i, producer, itemCount)).start();
        }
        CD.await();
    }

    static class Producer implements Runnable {
        AtomicInteger consumerCount;

        Item item;
        AtomicInteger itemCount = new AtomicInteger(0);
        final ReentrantLock lock = new ReentrantLock(true);
        final Condition condition = lock.newCondition();

        Producer(int consumerCount) {
            this.consumerCount = new AtomicInteger(consumerCount);
        }

        @Override
        public void run() {
            System.out.println("Start");

            while (consumerCount.get() != 0) {
                lock.lock();
                try {
                    while (itemCount.get() > 0) {
                        try {
                            condition.await();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                    item = new Item();
                    itemCount.getAndIncrement();
                    condition.signal();
                } finally {
                    lock.unlock();
                }
            }
            System.out.println("Finished");
            CD.countDown();
        }
    }

    static class Consumer implements Runnable {
        private int count;
        private int id;
        private Producer producer;

        Consumer(int id, Producer producer, int itemCount) {
            this.id = id;
            this.count = itemCount;
            this.producer = producer;
        }

        @Override
        public void run() {
            while (count > 0) {
                producer.lock.lock();
                try {
                    while (producer.itemCount.get() == 0) {
                        try {
                            producer.condition.await();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                    System.out.println("Consumer: " + id + " consume [" + producer.item + "] remain: " + count--);
                    producer.itemCount.getAndDecrement();
                    producer.condition.signal();
                } finally {
                    producer.lock.unlock();
                }
            }
            producer.consumerCount.getAndDecrement();
        }
    }

    static class Item {
        private int index;
        static int INDEX = 0;

        Item() {
            this.index = INDEX++;
        }

        @Override
        public String toString() {
            return "Item {" + index + "}";
        }
    }
}
