package com.leo.leetcode.algorithm.q0400;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。
 * 你要用 所有的火柴棍 拼成一个正方形。你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。
 * 如果你能使这个正方形，则返回 true ，否则返回 false 。
 * 提示:
 * 1、1 <= matchsticks.length <= 15
 * 2、1 <= matchsticks[i] <= 10^8
 * 链接：https://leetcode.cn/problems/matchsticks-to-square
 */
public class Q473 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q473().makeSquare(stringToIntegerArray("[3,9,2,2,2,9,10,8,3,9,10,10,1,9,9]")));
        // false
        System.out.println(new Q473().makeSquare(stringToIntegerArray("[6,6,6,6,4,2,2]")));
        // true
        System.out.println(new Q473().makeSquare(stringToIntegerArray("[1,1,2,2,2]")));
        // false
        System.out.println(new Q473().makeSquare(stringToIntegerArray("[3,3,3,3,4]")));
    }

    // 倒序遍历火柴、穷举法
    public boolean makeSquare(int[] matchsticks) {
        long total = 0;
        int n = matchsticks.length;
        for (int stick : matchsticks) total += stick;
        if (total % 4 != 0) return false;
        sideLen = total / 4;
        Arrays.sort(matchsticks);
        return dfs(matchsticks, n - 1, new int[4]);
    }

    long sideLen;

    boolean dfs(int[] matchsticks, int idx, int[] cur) {
        if (idx == -1) {
            for (int i : cur) {
                if (i != sideLen) return false;
            }
            return true;
        }
        for (int i = 0; i < 4; i++) {
            int u = matchsticks[idx];
            if (cur[i] + u > sideLen) continue;
            cur[i] += u;
            if (dfs(matchsticks, idx - 1, cur)) return true;
            cur[i] -= u;
        }
        return false;
    }
}
