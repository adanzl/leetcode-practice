package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;

public class Q89 {

    public static void main(String[] args) {
        System.out.println(new Q89().grayCode(4)); // [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8]
        System.out.println(new Q89().grayCode(0)); // [0]
        System.out.println(new Q89().grayCode(2)); // [0,1,3,2]
    }

    public List<Integer> grayCode(int n) {
        List<Integer> out = new ArrayList<>();
        out.add(0);
        gen(0, n, out);
        return out;
    }

    void gen(int num, int n, List<Integer> out) {
        if (n <= 0) return;
        int v = (1 << n - 1) | num;
        if (v != num && v != 0) out.add(v);
        gen((1 << n - 1) | num, n - 1, out);

        v = ((1 << n) - 1) & num;
        if (v != num && v != 0) out.add(v);
        gen(((1 << n) - 1) & num, n - 1, out);
    }
}
