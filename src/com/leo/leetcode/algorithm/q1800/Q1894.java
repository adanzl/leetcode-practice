package com.leo.leetcode.algorithm.q1800;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 一个班级里有 n 个学生，编号为 0 到 n - 1 。
 * 每个学生会依次回答问题，编号为 0 的学生先回答，然后是编号为 1 的学生，以此类推，直到编号为 n - 1 的学生，然后老师会重复这个过程，重新从编号为 0 的学生开始回答问题。
 * 给你一个长度为 n 且下标从 0 开始的整数数组 chalk 和一个整数 k 。一开始粉笔盒里总共有 k 支粉笔。当编号为 i 的学生回答问题时，他会消耗 chalk[i] 支粉笔。
 * 如果剩余粉笔数量 严格小于 chalk[i] ，那么学生 i 需要 补充 粉笔。
 * 请你返回需要 补充 粉笔的学生 编号 。
 * 提示：
 * 1、chalk.length == n
 * 2、1 <= n <= 10^5
 * 3、1 <= chalk[i] <= 10^5
 * 4、1 <= k <= 10^9
 * 链接：https://leetcode-cn.com/problems/find-the-student-that-will-replace-the-chalk
 */
public class Q1894 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q1894().chalkReplacer(stringToIntegerArray("[5,1,5]"), 22));
        // 1
        System.out.println(new Q1894().chalkReplacer(stringToIntegerArray("[3,4,1,2]"), 25));
    }

    public int chalkReplacer(int[] chalk, int k) {
        int n = chalk.length, l = 0, r = n;
        long sum = 0;
        long[] preSum = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            sum += chalk[i - 1];
            preSum[i] = sum;
        }
        k %= sum;
        while (l <= r) {
            int mid = l + ((r - l) >> 1);
            if (k < preSum[mid]) r = mid - 1;
            else l = mid + 1;
        }
        return l - 1;
    }
}
