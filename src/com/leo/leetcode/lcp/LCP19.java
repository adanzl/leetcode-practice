package com.leo.leetcode.lcp;

/**
 * 小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves，
 * 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
 * 出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。
 * 每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。
 * 提示：
 * 1、3 <= leaves.length <= 10^5
 * 2、leaves 中只包含字符 'r' 和字符 'y'
 * 链接：https://leetcode.cn/problems/UlBDOe
 */
public class LCP19 {

    public static void main(String[] args) {
        // 41
        System.out.println(new LCP19().minimumOperations("ryyryyyrryyyyyryyyrrryyyryryyyyryyrrryryyyryrryrrrryyyrrrrryryyrrrrryyyryyryrryryyryyyyryyrryrryryy"));
        // 2
        System.out.println(new LCP19().minimumOperations("rrryyyrryyyrr"));
        // 0
        System.out.println(new LCP19().minimumOperations("ryr"));
    }

    // 动态规划 https://leetcode.cn/problems/UlBDOe/solution/qiu-xie-shou-cang-ji-by-leetcode-solution/
    public int minimumOperations(String leaves) {
        int n = leaves.length();
        int[][] dp = new int[n][3];
        dp[2][0] = (leaves.charAt(0) == 'r' ? 0 : 1) + (leaves.charAt(1) == 'r' ? 0 : 1) + (leaves.charAt(2) == 'r' ? 0 : 1);
        dp[2][1] = (leaves.charAt(0) == 'r' ? 0 : 1) + (leaves.charAt(2) == 'y' ? 0 : 1);
        dp[2][2] = (leaves.charAt(0) == 'r' ? 0 : 1) + (leaves.charAt(1) == 'y' ? 0 : 1) + (leaves.charAt(2) == 'r' ? 0 : 1);
        for (int i = 3; i < n; i++) {
            char c = leaves.charAt(i);
            dp[i][0] = dp[i - 1][0] + (c == 'r' ? 0 : 1);
            dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][1]) + (c == 'y' ? 0 : 1);
            dp[i][2] = Math.min(dp[i - 1][2], dp[i - 1][1]) + (c == 'r' ? 0 : 1);
        }
        return dp[n - 1][2];
    }
}
