package com.leo.leetcode.algorithm.q2100;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个 正 整数数组 beans ，其中每个整数表示一个袋子里装的魔法豆的数目。
 * 请你从每个袋子中 拿出 一些豆子（也可以 不拿出），使得剩下的 非空 袋子中（即 至少 还有 一颗 魔法豆的袋子）魔法豆的数目 相等 。
 * 一旦魔法豆从袋子中取出，你不能将它放到任何其他的袋子中。
 * 请你返回你需要拿出魔法豆的 最少数目。
 * 提示：
 * 1、1 <= beans.length <= 10^5
 * 2、1 <= beans[i] <= 10^5
 * 链接：https://leetcode.cn/problems/removing-minimum-number-of-magic-beans
 */
public class Q2171 {

    public static void main(String[] args) {
        // 7
        System.out.println(new Q2171().minimumRemoval(stringToIntegerArray("[2,10,3,2]")));
        // 4
        System.out.println(new Q2171().minimumRemoval(stringToIntegerArray("[4,1,6,5]")));
    }

    public long minimumRemoval(int[] beans) {
        Arrays.sort(beans);
        int n = beans.length;
        long[] preSum = new long[n + 1];
        for (int i = 0; i < n; i++) preSum[i + 1] = preSum[i] + beans[i];
        long ret = preSum[n] - (long) beans[0] * n;
        for (int i = 0; i < n - 1; i++) {
            ret = Math.min(ret, preSum[i + 1] + (preSum[n] - preSum[i + 1] - (long) beans[i + 1] * (n - i - 1)));
        }
        return ret;
    }
}
