package com.leo.leetcode.algorithm.q1700;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums ，其中 nums[i] 表示第 i 个袋子里球的数目。同时给你一个整数 maxOperations 。
 * 你可以进行如下操作至多 maxOperations 次：
 * 选择任意一个袋子，并将袋子里的球分到 2 个新的袋子中，每个袋子里都有 正整数 个球。
 * 比方说，一个袋子里有 5 个球，你可以把它们分到两个新袋子里，分别有 1 个和 4 个球，或者分别有 2 个和 3 个球。
 * 你的开销是单个袋子里球数目的 最大值 ，你想要 最小化 开销。
 * 请你返回进行上述操作后的最小开销。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= maxOperations, nums[i] <= 10^9
 * 链接：https://leetcode-cn.com/problems/minimum-limit-of-balls-in-a-bag
 */
public class Q1760 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q1760().minimumSize(stringToIntegerArray("[9]"), 2));
        // 2
        System.out.println(new Q1760().minimumSize(stringToIntegerArray("[2,4,8,2]"), 4));
        // 7
        System.out.println(new Q1760().minimumSize(stringToIntegerArray("[7,17]"), 2));
    }

    public int minimumSize(int[] nums, int maxOperations) {
        int l = 1, r = 1000_000_000;
        while (l <= r) {
            int mid = l + ((r - l) >> 1), sum = 0;
            for (int num : nums) {
                if (num > mid) {
                    if (num % mid == 0) sum += num / mid - 1;
                    else sum += num / mid;
                }
                if (sum > maxOperations) break;
            }
            if (sum <= maxOperations) r = mid - 1;
            else l = mid + 1;
        }
        return l;
    }
}
