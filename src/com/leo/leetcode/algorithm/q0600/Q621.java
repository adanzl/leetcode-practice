package com.leo.leetcode.algorithm.q0600;

import java.util.Arrays;

public class Q621 {
    public void TestOJ() {
        System.out.println(leastInterval(new char[]{'A', 'A', 'A', 'B', 'B', 'B'}, 2)); // 8
        System.out.println(leastInterval(new char[]{'A'}, 2)); // 1
    }

    private int leastInterval(char[] tasks, int n) {
        int[] flag = new int[26];
        for (char c : tasks) {
            flag[c - 'A']++;
        }
        Arrays.sort(flag);
        int count = (flag[25] - 1) * n;
        for (int i = 24; i >= 0; i--) {
            if (flag[i] == flag[25]) {
                count -= flag[25] - 1;
            } else {
                count -= flag[i];
            }
            if (count < 0) {
                return tasks.length;
            }
        }
        return count + tasks.length;
    }
}
