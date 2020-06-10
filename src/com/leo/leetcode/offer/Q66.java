package com.leo.leetcode.offer;

import com.leo.utils.LCUtil;

import java.util.Arrays;

public class Q66 {

    public static void main(String[] args) {
        new Q66().TestOJ();
    }
    public void TestOJ() {
        System.out.println(Arrays.toString(constructArr(LCUtil.stringToIntegerArray("[1, 2, 3, 4, 5]")))); // [120,60,40,30,24]
    }

    public int[] constructArr(int[] a) {
        if (a.length == 0) return new int[0];
        int[] markLeft = new int[a.length];
        int[] markRight = new int[a.length];
        markLeft[0] = 1;
        markRight[markRight.length - 1] = 1;
        for (int i = 1; i < a.length; i++) {
            markLeft[i] = markLeft[i - 1] * a[i - 1];
        }
        for (int i = markRight.length - 2; i >= 0; i--) {
            markRight[i] = markRight[i + 1] * a[i + 1];
        }
        int[] out = new int[a.length];
        for (int i = 0; i < out.length; i++) {
            out[i] = markLeft[i] * markRight[i];
        }
        return out;
    }
}
