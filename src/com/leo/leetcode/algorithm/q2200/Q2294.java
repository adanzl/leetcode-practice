package com.leo.leetcode.algorithm.q2200;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 和一个整数 k 。你可以将 nums 划分成一个或多个 子序列 ，使 nums 中的每个元素都 恰好 出现在一个子序列中。
 * 在满足每个子序列中最大值和最小值之间的差值最多为 k 的前提下，返回需要划分的 最少 子序列数目。
 * 子序列 本质是一个序列，可以通过删除另一个序列中的某些元素（或者不删除）但不改变剩下元素的顺序得到。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^5
 * 3、0 <= k <= 10^5
 * 链接：https://leetcode.cn/problems/partition-array-such-that-maximum-difference-is-k
 */
public class Q2294 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q2294().partitionArray(stringToIntegerArray("[3,6,1,2,5]"), 2));
        // 2
        System.out.println(new Q2294().partitionArray(stringToIntegerArray("[1,2,3]"), 1));
        // 3
        System.out.println(new Q2294().partitionArray(stringToIntegerArray("[2,2,4,5]"), 0));
    }

    public int partitionArray(int[] nums, int k) {
        Arrays.sort(nums);
        int pre = nums[0], n = nums.length, ret = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] - pre > k) {
                ret++;
                pre = nums[i];
            }
        }
        return ret;
    }
}
