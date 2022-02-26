package com.leo.leetcode.algorithm.q0300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。第一个差（如果存在的话）可能是正数或负数。
 * 仅有一个元素或者含两个不等元素的序列也视作摆动序列。
 * 1、例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。
 * 2、相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
 * 子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。
 * 给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、0 <= nums[i] <= 1000
 * 进阶：你能否用 O(n) 时间复杂度完成此题?
 * 链接：https://leetcode-cn.com/problems/wiggle-subsequence
 */
public class Q376 {

    public static void main(String[] args) {
        // 6
        System.out.println(new Q376().wiggleMaxLength(stringToIntegerArray("[1,7,4,9,2,5]")));
        // 7
        System.out.println(new Q376().wiggleMaxLength(stringToIntegerArray("[1,17,5,10,13,15,10,5,16,8]")));
        // 2
        System.out.println(new Q376().wiggleMaxLength(stringToIntegerArray("[1,2,3,4,5,6,7,8,9]")));
    }

    public int wiggleMaxLength(int[] nums) {
        int n = nums.length, idx0 = 0, idx1 = 0;
        int[] dp = new int[n];
        dp[0] = 1;
        for (int i = 1; i < n; i++) {
            int d = nums[i] - nums[i - 1];
            if (d > 0) {
                dp[i] = Math.max(dp[i-1], dp[idx1] + 1);
                idx0 = i;
            } else if (d < 0) {
                dp[i] = Math.max(dp[i-1], dp[idx0] + 1);
                idx1 = i;
            } else {
                dp[i] = dp[i-1];
            }
        }
        return dp[n - 1];
    }
}
