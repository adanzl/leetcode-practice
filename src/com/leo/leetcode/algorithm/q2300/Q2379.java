package com.leo.leetcode.algorithm.q2300;

/**
 * 给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。
 * 给你一个整数 k ，表示想要 连续 黑色块的数目。
 * 每一次操作中，你可以选择一个白色块将它 涂成 黑色块。
 * 请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。
 * 提示：
 * 1、n == blocks.length
 * 2、1 <= n <= 100
 * 3、blocks[i] 要么是 'W' ，要么是 'B' 。
 * 4、1 <= k <= n
 * 链接：https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks
 */
public class Q2379 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2379().minimumRecolors("WBBWWBBWBW", 7));
        // 0
        System.out.println(new Q2379().minimumRecolors("WBWBBBW", 2));
        // 4
        System.out.println(new Q2379().minimumRecolors("BWBBWWBBBWBWWWBWWBBWBWBBWBB", 11));
    }

    public int minimumRecolors(String blocks, int k) {
        int n = blocks.length(), ans = n;
        int[] preSum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            preSum[i + 1] = preSum[i] + (blocks.charAt(i) == 'W' ? 1 : 0);
            if (i >= k - 1) {
                ans = Math.min(ans, preSum[i + 1] - preSum[i + 1 - k]);
            }
        }
        return ans;
    }

}
