package com.leo.leetcode.algorithm;

import java.util.HashSet;
import java.util.Set;

public class Q279 {

    public static void main(String[] args) {
        new Q279().TestOJ();
    }

    public void TestOJ() {
        System.out.println(numSquares(12)); // 3
        System.out.println(numSquares(13)); // 2
        System.out.println(numSquares(101)); // 2
    }

    public int numSquares(int n) {
        int[] arr = new int[(int) Math.sqrt(n)];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (i + 1) * (i + 1);
        }
        int deep = 0;
        Set<Integer> s = new HashSet<>(), current = new HashSet<>();
        current.add(n);
        while (true) {
            Set<Integer> next = new HashSet<>();
            for (int v : current) {
                for (int i : arr) {
                    int c = v - i;
                    if (c < 0 || s.contains(c)) {
                        continue;
                    }
                    if (c == 0) return deep + 1;
                    s.add(c);
                    next.add(c);
                }
            }
            current = next;
            deep++;
        }
    }
}
