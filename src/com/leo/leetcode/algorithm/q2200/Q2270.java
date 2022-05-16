package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个二维整数数组 tiles ，其中 tiles[i] = [li, ri] ，表示所有在 li <= j <= ri 之间的每个瓷砖位置 j 都被涂成了白色。
 * 同时给你一个整数 carpetLen ，表示可以放在 任何位置 的一块毯子。
 * 请你返回使用这块毯子，最多 可以盖住多少块瓷砖。
 * 提示：
 * 1、1 <= tiles.length <= 5 * 10^4
 * 2、tiles[i].length == 2
 * 3、1 <= li <= ri <= 10^9
 * 4、1 <= carpetLen <= 10^9
 * 5、tiles 互相 不会重叠 。
 * 链接：https://leetcode.cn/problems/maximum-white-tiles-covered-by-a-carpet
 */
public class Q2270 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q2270().waysToSplitArray(stringToIntegerArray("[0,0]")));
        // 2
        System.out.println(new Q2270().waysToSplitArray(stringToIntegerArray("[10,4,-8,7]")));
        // 2
        System.out.println(new Q2270().waysToSplitArray(stringToIntegerArray("[2,3,1,0]")));
        // 0
        System.out.println(new Q2270().waysToSplitArray(stringToIntegerArray("[-100000,100000]")));
    }

    public int waysToSplitArray(int[] nums) {
        int n = nums.length, ret = 0;
        long[] preSum = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            preSum[i] = preSum[i - 1] + nums[i - 1];
        }
        for (int i = 0; i < n - 1; i++) {
            if (preSum[n] - preSum[i + 1] <= preSum[i + 1])
                ret++;
        }
        return ret;
    }
}
