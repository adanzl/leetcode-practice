package com.leo.leetcode.algorithm.q0500;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，其中 S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }且遵守以下的规则。
 * 假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元素。
 * 提示：
 * 1、N是[1, 20,000]之间的整数。
 * 2、A中不含有重复的元素。
 * 3、A中的元素大小在[0, N-1]之间。
 * 链接：https://leetcode.cn/problems/array-nesting
 */
public class Q565 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q565().arrayNesting(stringToIntegerArray("[5,4,0,3,1,6,2]")));
    }

    int[] parents, lens;
    int max = 1;

    public int arrayNesting(int[] nums) {
        int n = nums.length;
        parents = new int[n];
        lens = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
            lens[i] = 1;
        }

        for (int i = 0; i < n; i++) {
            merge(i, nums[i]);
        }
        return max;
    }

    int find(int x) {
        return parents[x] == x ? x : find(parents[x]);
    }

    void merge(int x1, int x2) {
        int r1 = find(x1), r2 = find(x2);
        if (r1 != r2) {
            parents[r2] = r1;
            lens[r1] += lens[r2];
            max = Math.max(max, lens[r1]);
        }
    }
}
