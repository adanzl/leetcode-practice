package com.leo.leetcode.offer;

public class Q56 {
    public static void main(String[] args) {
        // 834788759
        System.out.println(new Q56().singleNumber(new int[]{834788759, 2129209440, 2129209440, 2129209440, Integer.MAX_VALUE, Integer.MAX_VALUE, Integer.MAX_VALUE}));
    }

    public int singleNumber(int[] nums) {
        int[] marks = new int[32];
        for (int v : nums) {
            fillMarks(marks, v);
        }
        int out = 0;
        for (int i = 0; i < marks.length; i++) {
            if ((marks[i] % 3) != 0) out |= (1 << i);
        }
        return out;
    }

    void fillMarks(int[] marks, int n) {
        int mark = 0x1;
        for (int i = 0; i < 31; i++) {
            marks[i] += (mark & n) == 0 ? 0 : 1;
            mark <<= 1;
        }
    }
}
