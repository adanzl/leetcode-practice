package com.leo.leetcode.algorithm.q0000;

public class Q69 {

    public static void main(String[] args) {
        System.out.println(new Q69().mySqrt(1)); // 1
        System.out.println(new Q69().mySqrt(0)); // 0
        System.out.println(new Q69().mySqrt(3)); // 1
        System.out.println(new Q69().mySqrt(125300)); // 353
        System.out.println(new Q69().mySqrt(4)); // 2
        System.out.println(new Q69().mySqrt(8)); // 2
    }

    public int mySqrt(int x) {
        if (x == 0) return 0;
        if (x == 1) return 1;
        int l = 0, r = x, out = x;
        while (true) {
            int v = l + ((r - l) >> 1);
            int sv = x / v;
            if (v == out || sv == v) return v;
            if (sv > v) l = v;
            else r = v;
            out = v;
        }
    }
}
