package com.leo.leetcode.algorithm.q0700;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数 n 和一个 无重复 黑名单整数数组 blacklist 。
 * 设计一种算法，从 [0, n - 1] 范围内的任意整数中选取一个 未加入 黑名单 blacklist 的整数。
 * 任何在上述范围内且不在黑名单 blacklist 中的整数都应该有 同等的可能性 被返回。
 * 优化你的算法，使它最小化调用语言 内置 随机函数的次数。
 * 实现 Solution 类:
 * 1、Solution(int n, int[] blacklist) 初始化整数 n 和被加入黑名单 blacklist 的整数
 * 2、int pick() 返回一个范围为 [0, n - 1] 且不在黑名单 blacklist 中的随机整数
 * 提示:
 * 1、1 <= n <= 10^9
 * 2、0 <= blacklist.length <= min(10^5, n - 1)
 * 3、0 <= blacklist[i] < n
 * 4、blacklist 中所有值都 不同
 * 5、pick 最多被调用 2 * 10^4 次
 * 链接：https://leetcode.cn/problems/random-pick-with-blacklist
 */
public class Q710 {

    public static void main(String[] args) {
        Solution solution = new Solution(7, stringToIntegerArray("[2,3,5]"));
        System.out.println(solution.pick()); // 返回0，任何[0,1,4,6]的整数都可以。注意，对于每一个pick的调用，
        // 0、1、4和6的返回概率必须相等(即概率为1/4)。
        System.out.println(solution.pick()); // 返回 4
        System.out.println(solution.pick()); // 返回 1
        System.out.println(solution.pick()); // 返回 6
        System.out.println(solution.pick()); // 返回 1
        System.out.println(solution.pick()); // 返回 0
        System.out.println(solution.pick()); // 返回 4
    }

    static class Solution {
        private final int n;

        private final Map<Integer, Integer> blackMap = new HashMap<>();

        public Solution(int n, int[] blacklist) {
            this.n = n - blacklist.length;
            Set<Integer> set = new HashSet<>();
            for (int black : blacklist) set.add(black);
            int idx = 0;
            for (int j : blacklist) {
                if (j < this.n) {
                    while (set.contains(n - 1 - idx)) idx++;
                    blackMap.put(j, n - 1 - idx++);
                }
            }
        }

        public int pick() {
            int target = new Random().nextInt(n);
            return blackMap.getOrDefault(target, target);
        }
    }
}
