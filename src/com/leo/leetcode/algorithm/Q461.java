package com.leo.leetcode.algorithm;

import org.junit.Test;

public class Q461 {
    @Test
    public void TestOJ() {
        System.out.println(hammingDistance(93, 73)); // 2
        System.out.println(hammingDistance(1, 4)); // 2
    }

    public int hammingDistance(int x, int y) {
        int v = x ^ y, out = 0;
        while (v != 0) {
            if ((v & 1) == 1) out++;
            v >>= 1;
        }
        return out;
    }
}
