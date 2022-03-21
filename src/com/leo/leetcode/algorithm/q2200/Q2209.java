package com.leo.leetcode.algorithm.q2200;

/**
 * 给你一个下标从 0 开始的 二进制 字符串 floor ，它表示地板上砖块的颜色。
 * 1、floor[i] = '0' 表示地板上第 i 块砖块的颜色是 黑色 。
 * 2、floor[i] = '1' 表示地板上第 i 块砖块的颜色是 白色 。
 * 同时给你 numCarpets 和 carpetLen 。你有 numCarpets 条 黑色 的地毯，每一条 黑色 的地毯长度都为 carpetLen 块砖块。
 * 请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余 白色 砖块的数目 最小 。地毯相互之间可以覆盖。
 * 请你返回没被覆盖的白色砖块的 最少 数目。
 * 提示：
 * 1、1 <= carpetLen <= floor.length <= 1000
 * 2、floor[i] 要么是 '0' ，要么是 '1' 。
 * 3、1 <= numCarpets <= 1000
 * 链接：https://leetcode-cn.com/problems/minimum-white-tiles-after-covering-with-carpets
 */
public class Q2209 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q2209().minimumWhiteTiles("0110110111", 3, 2));
        // 3
        System.out.println(new Q2209().minimumWhiteTiles("00100000000010101101100111", 4, 2));
        // 0
        System.out.println(new Q2209().minimumWhiteTiles("10110101", 5, 1));
        // 3
        System.out.println(new Q2209().minimumWhiteTiles("01111111110111101111001111110111111111101101101111111110111011110111111101101110011110111011001", 72, 1));
        // 2
        System.out.println(new Q2209().minimumWhiteTiles("10110101", 2, 2));
        // 3
        System.out.println(new Q2209().minimumWhiteTiles("0111101", 1, 2));
        // 0
        System.out.println(new Q2209().minimumWhiteTiles("11111", 2, 3));
        // 2
        System.out.println(new Q2209().minimumWhiteTiles("10110101", 2, 2));
    }

    public int minimumWhiteTiles(String floor, int numCarpets, int carpetLen) {
        int count = 0, len = floor.length(), max = 0;
        int[] flag = new int[len + 1];
        int[][] dp = new int[len + 1][numCarpets + 1];
        for (int i = 0; i < floor.length(); i++) {
            if (floor.charAt(i) == '1') count++;
            flag[i + 1] = count;
        }
        for (int i = 1; i <= len; i++) {
            int last = Math.max(0, i - carpetLen);
            for (int j = 1; j <= numCarpets; j++) {
                dp[i][j] = Math.max(dp[last][j - 1] + flag[i] - flag[last], dp[i - 1][j]);
                max = Math.max(max, dp[i][j]);
            }
        }
        return count - max;
    }
}
