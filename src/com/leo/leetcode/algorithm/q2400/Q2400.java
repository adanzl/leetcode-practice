package com.leo.leetcode.algorithm.q2400;

import java.util.HashMap;
import java.util.Map;

/**
 * 给你两个 正 整数 startPos 和 endPos 。最初，你站在 无限 数轴上位置 startPos 处。在一步移动中，你可以向左或者向右移动一个位置。
 * 给你一个正整数 k ，返回从 startPos 出发、恰好 移动 k 步并到达 endPos 的 不同 方法数目。由于答案可能会很大，返回对 10^9 + 7 取余 的结果。
 * 如果所执行移动的顺序不完全相同，则认为两种方法不同。
 * 注意：数轴包含负整数。
 * 提示：1 <= startPos, endPos, k <= 1000
 * 链接：https://leetcode.cn/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps
 */
public class Q2400 {
    public static void main(String[] args) {
        // 3
        System.out.println(new Q2400().numberOfWays(1, 2, 3));
        // 0
        System.out.println(new Q2400().numberOfWays(2, 5, 10));
        // 159835829
        System.out.println(new Q2400().numberOfWays(1000, 1000, 1000));
    }

    int MOD = 1_000_000_007;
    Map<String, Integer> mem = new HashMap<>();

    public int numberOfWays(int startPos, int endPos, int k) {
        String key = startPos + "_" + k;
        if (mem.containsKey(key)) return mem.get(key);
        if (startPos == endPos && k == 0) return 1;
        if (k == 0) return 0;
        long ans = numberOfWays(startPos + 1, endPos, k - 1) % MOD;
        ans = (ans + numberOfWays(startPos - 1, endPos, k - 1)) % MOD;
        mem.put(key, (int) ans);
        return (int) ans;
    }

}
