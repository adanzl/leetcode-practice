package com.leo.leetcode.algorithm.q1000;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
 * 注意：请不要在超过该数组长度的位置写入元素。
 * 要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
 * 提示：
 * 1、1 <= arr.length <= 10000
 * 2、0 <= arr[i] <= 9
 * 链接：https://leetcode.cn/problems/duplicate-zeros
 */
public class Q1089 {

    public static void main(String[] args) {
        int[] arr;
        arr = stringToIntegerArray("[8,4,5,0,0,0,0,7]");
        new Q1089().duplicateZeros(arr);
        // [8,4,5,0,0,0,0,0]
        System.out.println(Arrays.toString(arr));
        arr = stringToIntegerArray("[1,0,2,3,0,4,5,0]");
        new Q1089().duplicateZeros(arr);
        // [1,0,0,2,3,0,0,4]
        System.out.println(Arrays.toString(arr));
        arr = stringToIntegerArray("[1,2,3]");
        new Q1089().duplicateZeros(arr);
        // [1,2,3]
        System.out.println(Arrays.toString(arr));
        arr = stringToIntegerArray("[0,0,0,0,0,0,0]");
        new Q1089().duplicateZeros(arr);
        // [0,0,0,0,0,0,0]
        System.out.println(Arrays.toString(arr));
    }

    public void duplicateZeros(int[] arr) {
        int idx = 0, n = arr.length, cnt = 0;
        for (; idx < n && cnt < n; idx++) {
            cnt++;
            if (arr[idx] == 0) cnt++;
        }
        for (int i = cnt - 1; i >= 0; i--) {
            idx--;
            if (i < n) arr[i] = arr[idx];
            if (arr[idx] == 0 && i > 0) {
                i--;
                arr[i] = 0;
            }
        }
    }
}
