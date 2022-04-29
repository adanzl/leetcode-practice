package com.leo.leetcode.algorithm.q0800;

/**
 * 给定一个正整数 n，找到并返回 n 的二进制表示中两个 相邻 1 之间的 最长距离 。如果不存在两个相邻的 1，返回 0 。
 * 如果只有 0 将两个 1 分隔开（可能不存在 0 ），则认为这两个 1 彼此 相邻 。
 * 两个 1 之间的距离是它们的二进制表示中位置的绝对差。例如，"1001" 中的两个 1 的距离为 3 。
 * 提示：1 <= n <= 10^9
 * 链接：https://leetcode-cn.com/problems/binary-gap
 */
public class Q868 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q868().binaryGap(22));
        // 0
        System.out.println(new Q868().binaryGap(8));
        // 2
        System.out.println(new Q868().binaryGap(5));
        // 3
        System.out.println(new Q868().binaryGap(1000000000));
    }

    public int binaryGap(int n) {
        int ret = 0, p1 = -1, p2 = 0;
        while (n != 0) {
            if ((n & 1) != 0) {
                if (p1 >= 0) ret = Math.max(ret, p2 -  p1);
                p1 = p2;
            }
            p2++;
            n >>= 1;
        }
        return ret;
    }
}
