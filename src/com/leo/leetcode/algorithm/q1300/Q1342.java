package com.leo.leetcode.algorithm.q1300;

/**
 * 给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。
 * 提示：
 * 0 <= num <= 10^6
 * <p>
 * 链接：https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero/
 */
public class Q1342 {
    public static void main(String[] args) {
        // 6
        System.out.println(new Q1342().numberOfSteps(14));
        // 4
        System.out.println(new Q1342().numberOfSteps(8));
        //12
        System.out.println(new Q1342().numberOfSteps(123));
    }

    public int numberOfSteps(int num) {
        if (num == 0) return 0;
        int ret = 0;
        while (num != 0) {
            if ((num & 1) == 1) ret += 2;
            else ret += 1;
            num >>= 1;
        }
        return ret - 1;
    }
}
