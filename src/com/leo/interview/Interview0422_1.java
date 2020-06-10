package com.leo.interview;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

/**
 * 试题1
 * 构造线程池 ExecutorService executorService = new ThreadPoolExecutor(10, 20, 100, TimeUnit.SECONDS, new LinkedBlockingQueue<Runnable>())，
 * 假设 CPU 资源充裕，线程执行的任务为纯计算型任务，每个任务执行耗时 100ms。
 * 一次性提交1000 个任务到线程池，问第 815 个任务，从提交到执行完毕理论上耗时多久。
 */
public class Interview0422_1 {

    static long startTime;

    public static void main(String[] args) {
        ExecutorService executorService = new ThreadPoolExecutor(10,
                20,
                1,
                TimeUnit.SECONDS, new LinkedBlockingQueue<>(1000));

        startTime = System.currentTimeMillis();
        for (int i = 0; i < 1003; i++) {
            executorService.execute(new Task(i));
        }
    }

    static class Task implements Runnable {
        private int num;

        public Task(int num) {
            this.num = num;
        }

        @Override
        public void run() {
            try {
                Thread.sleep(10);
                if (num == 815) System.out.println(System.currentTimeMillis() - startTime);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
