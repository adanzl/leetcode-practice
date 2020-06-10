package com.leo.interview;

import org.junit.Test;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class QRandom {
    @Test
    public void TestFun() {
        int count = 1_000_000;
        Runtime rt = Runtime.getRuntime();
        rt.gc();
        Map<Integer, Integer> people = new HashMap<>(count);
        long start = rt.freeMemory();
        Random r = new Random();
        long ts = System.currentTimeMillis();
        for (int i = 0; i < count; i++) {
            people.put(i, r.nextInt(100));
        }
        if (people.containsKey(1)) people.get(1);
        rt.gc();
        long end = rt.freeMemory();
        System.out.println("Time: " + (System.currentTimeMillis() - ts) + " Memory: " + ((start - end) >> 20));

        System.out.println();
    }
}
