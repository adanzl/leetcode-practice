package com.leo.leetcode.lcci;

import java.util.Arrays;

public class Q1719 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Q1719().missingTwo(new int[] { 1, 2, 3, 4, 6, 7, 9, 10 }))); // 5,8
        System.out.println(Arrays.toString(new Q1719().missingTwo(new int[] { 1 }))); // 2,3
        System.out.println(Arrays.toString(new Q1719().missingTwo(new int[] { 3 }))); // 1,2
        System.out.println(Arrays.toString(new Q1719().missingTwo(new int[] { 2, 3 }))); // 1,4
        System.out.println(Arrays.toString(new Q1719().missingTwo(new int[] {}))); // 1,2
    }

    public int[] missingTwo(int[] nums) {
        if (nums.length == 0)
            return new int[] { 1, 2 };
        int[] out = new int[2];
        int index = 0, offset = 1;
        int[] ext = new int[] { -1, -1 };
        for (int i = 0; i < nums.length;) {
            int v = nums[i];
            if (v == -1 || v == i + 1)
                i++;
            else {
                if (v > nums.length) {
                    nums[i] = ext[v - nums.length - 1];
                    ext[v - nums.length - 1] = v;
                } else {
                    nums[i] = nums[v - 1];
                    nums[v - 1] = v;
                }
            }
        }
        for (int i = index; i < 2; i++)
            out[i] = nums[nums.length - 1] + offset++;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == -1)
                out[index++] = i + 1;
            if (index == 2)
                break;
        }
        for (int i = 0; i < ext.length; i++) {
            if (ext[i] == -1)
                out[index++] = nums.length + i + 1;
        }
        return out;
    }
}
