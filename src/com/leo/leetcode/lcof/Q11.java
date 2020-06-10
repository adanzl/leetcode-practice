package com.leo.leetcode.lcof;

import com.leo.utils.LCUtil;

public class Q11 {

    public static void main(String[] args) {
        new Q11().TestOJ();
    }

    public void TestOJ() {
        System.out.println(minArray(LCUtil.stringToIntegerArray("[1,0,1,1,1]"))); // 0
        System.out.println(minArray(LCUtil.stringToIntegerArray("[1,1,1,0,1]"))); // 0
        System.out.println(minArray(LCUtil.stringToIntegerArray("[3,4,5,1,2]"))); // 1
        System.out.println(minArray(LCUtil.stringToIntegerArray("[2,2,2,0,1]"))); // 0
        System.out.println(minArray(LCUtil.stringToIntegerArray("[1]"))); // 1
        System.out.println(minArray(LCUtil.stringToIntegerArray("[1,3,5]"))); // 1
    }

    public int minArray(int[] numbers) {
        return minArr(numbers, 0, numbers.length - 1);
    }

    int minArr(int[] numbers, int l, int r) {
        if (l == r) return numbers[l];
        int m = (r + l) / 2;
        if (numbers[m] == numbers[r]) return minArr(numbers, l, r - 1);
        if (numbers[m] > numbers[r]) return minArr(numbers, m + 1, r);
        return minArr(numbers, l, m);
    }
}
