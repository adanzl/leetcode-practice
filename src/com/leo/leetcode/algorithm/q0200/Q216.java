package com.leo.leetcode.algorithm.q0200;

import java.util.ArrayList;
import java.util.List;

/**
 * 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
 * 说明：
 * 1、所有数字都是正整数。
 * 2、解集不能包含重复的组合。
 * 链接：https://leetcode-cn.com/problems/combination-sum-iii
 */
public class Q216 {

    public static void main(String[] args) {
        // []
        System.out.println(new Q216().combinationSum3(3, 18));
        // []
        System.out.println(new Q216().combinationSum3(2, 18));
        // [[1,6],[2,5],[3,4]]
        System.out.println(new Q216().combinationSum3(2, 7));
        // [[1,2,6], [1,3,5], [2,3,4]]
        System.out.println(new Q216().combinationSum3(3, 9));
        // [[1,2,4]]
        System.out.println(new Q216().combinationSum3(3, 7));
    }

    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ret = new ArrayList<>();
        fun(0, n, k, new ArrayList<>(k), ret);
        return ret;
    }

    void fun(int pre, int n, int k, List<Integer> ans, List<List<Integer>> out) {
        if (ans.size() == k - 1) {
            if(n > 9) return;
            ans.add(n);
            out.add(new ArrayList<>(ans));
            ans.remove(ans.size() - 1);
            return;
        }
        for (int i = pre + 1; i < Math.min((n + 1) >> 1, 10); i++) {
            ans.add(i);
            fun(i, n - i, k, ans, out);
            ans.remove(ans.size() - 1);
        }
    }
}
