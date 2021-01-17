package com.leo.leetcode.algorithm.q0000;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个Q数的组合。
 * 链接：https://leetcode-cn.com/problems/combinations/
 */
public class Q77 {
    public static void main(String[] args) {
        System.out.println(new Q77().combine(4, 2)); // [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    }

    public List<List<Integer>> combine(int n, int k) {
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = i + 1;
        List<List<Integer>> out = new ArrayList<>();
        build(out, null, nums, 0, k);
        return out;
    }

    void build(List<List<Integer>> out, LinkedList<Integer> ans, int[] nums, int offset, int k) {
        if (ans == null) ans = new LinkedList<>();
        for (int i = offset; i < nums.length; i++) {
            ans.add(nums[i]);
            if (k == 1) {
                out.add(new ArrayList<>(ans));
            } else {
                build(out, ans, nums, ++offset, k - 1);
            }
            ans.removeLast();
        }
    }
}
