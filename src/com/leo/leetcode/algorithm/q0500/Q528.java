package com.leo.leetcode.algorithm.q0500;

import java.util.Random;
import java.util.TreeMap;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个 下标从 0 开始 的正整数数组 w ，其中 w[i] 代表第 i 个下标的权重。
 * 请你实现一个函数 pickIndex ，它可以 随机地 从范围 [0, w.length - 1] 内（含 0 和 w.length - 1）选出并返回一个下标。
 * 选取下标 i 的 概率 为 w[i] / sum(w) 。
 * 例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3) = 0.75（即，75%）。
 * 提示：
 * 1、1 <= w.length <= 10^4
 * 2、1 <= w[i] <= 10^5
 * 3、pickIndex 将被调用不超过 10^4 次
 * 链接：https://leetcode-cn.com/problems/random-pick-with-weight
 */
public class Q528 {

    public static void main(String[] args) {
        Solution obj = new Solution(stringToIntegerArray("[1]"));
        System.out.println(obj.pickIndex()); // 0
        System.out.println("=======================");
        obj = new Solution(stringToIntegerArray("[1, 3]"));
        System.out.println(obj.pickIndex()); // 返回 1，返回下标 1，返回该下标概率为 3/4 。
        System.out.println(obj.pickIndex()); // 返回 1
        System.out.println(obj.pickIndex()); // 返回 1
        System.out.println(obj.pickIndex()); // 返回 1
        System.out.println(obj.pickIndex()); // 返回 0，返回下标 0，返回该下标概率为 1/4 。
        System.out.println("=======================");
    }


    static class Solution {

        TreeMap<Integer, Integer> treeMap;

        public Solution(int[] w) {
            treeMap = new TreeMap<>();
            treeMap.put(w[0], 0);
            for (int i = 1; i < w.length; i++) {
                w[i] += w[i - 1];
                treeMap.put(w[i], i);
            }
        }

        public int pickIndex() {
            int target = new Random().nextInt(treeMap.lastKey());
            return treeMap.higherEntry(target).getValue();
        }
    }
}
