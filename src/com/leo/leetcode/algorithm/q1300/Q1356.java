package com.leo.leetcode.algorithm.q1300;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
 * 如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
 * 请你返回排序后的数组。
 * 提示：
 * 1、1 <= arr.length <= 500
 * 2、0 <= arr[i] <= 10^4
 * 链接：https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits
 */
public class Q1356 {
    public static void main(String[] args) {
        // [0,1,2,4,8,3,5,6,7]
        System.out.println(Arrays.toString(new Q1356().sortByBits(stringToIntegerArray("[0,1,2,3,4,5,6,7,8]"))));
        // [1,2,4,8,16,32,64,128,256,512,1024]
        System.out.println(Arrays.toString(new Q1356().sortByBits(stringToIntegerArray("[1024,512,256,128,64,32,16,8,4,2,1]"))));
        // [10000,10000]
        System.out.println(Arrays.toString(new Q1356().sortByBits(stringToIntegerArray("[10000,10000]"))));
        // [2,3,5,17,7,11,13,19]
        System.out.println(Arrays.toString(new Q1356().sortByBits(stringToIntegerArray("[2,3,5,7,11,13,17,19]"))));
        // [10,100,10000,1000]
        System.out.println(Arrays.toString(new Q1356().sortByBits(stringToIntegerArray("[10,100,1000,10000]"))));
    }

    public int[] sortByBits(int[] arr) {
        List<int[]> l = new ArrayList<>();
        for (int n : arr) l.add(new int[]{n, bitCount(n)});
        l.sort((o1, o2) -> o1[1] == o2[1] ? o1[0] - o2[0] : o1[1] - o2[1]);
        return l.stream().mapToInt(o -> o[0]).toArray();
    }

    int bitCount(int x) {
        int ret = 0;
        while (x != 0) {
            x &= (x - 1);
            ret++;
        }
        return ret;
    }
}
