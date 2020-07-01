package com.leo.leetcode.algorithm;

import java.util.Arrays;
import java.util.List;

/**
 * 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
 * 在杨辉三角中，每个数是它左上方和右上方的数的和。
 * 进阶：
 * 你可以优化你的算法到 O(k) 空间复杂度吗？
 * 链接： https://leetcode-cn.com/problems/pascals-triangle-ii/
 */
public class Q119 {

    public static void main(String[] args) {
        System.out.println(new Q119().getRow(3)); // [1,3,3,1]
        System.out.println(new Q119().getRow(4)); // [1,3,3,1]
        System.out.println(new Q119().getRow(0)); // [1]
        System.out.println(new Q119().getRow(33)); //
    }

    public List<Integer> getRow(int rowIndex) {
        Integer[] res = new Integer[rowIndex + 1];
        res[0] = 1;
        res[res.length - 1] = 1;
        for (int i = 1; i < (rowIndex >> 1) + 1; i++) {
            int v = Math.toIntExact((long)res[i - 1] * (rowIndex + 1 - i) / i);
            res[i] = v;
            res[res.length - 1 - i] = v;
        }
        return Arrays.asList(res);
    }
}
