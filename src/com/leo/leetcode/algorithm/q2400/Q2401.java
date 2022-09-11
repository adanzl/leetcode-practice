package com.leo.leetcode.algorithm.q2400;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个由 正 整数组成的数组 nums 。
 * 如果 nums 的子数组中位于 不同 位置的每对元素按位 与（AND）运算的结果等于 0 ，则称该子数组为 优雅 子数组。
 * 返回 最长 的优雅子数组的长度。
 * 子数组 是数组中的一个 连续 部分。
 * 注意：长度为 1 的子数组始终视作优雅子数组。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/longest-nice-subarray
 */
public class Q2401 {
    public static void main(String[] args) {
        // 1
        System.out.println(new Q2401().longestNiceSubarray(stringToIntegerArray("[3]")));
        // 1
        System.out.println(new Q2401().longestNiceSubarray(stringToIntegerArray("[3,1,5,11,13]")));
        // 3
        System.out.println(new Q2401().longestNiceSubarray(stringToIntegerArray("[1,3,8,48,10]")));
        // 8
        System.out.println(new Q2401().longestNiceSubarray(stringToIntegerArray("[84139415,693324769,614626365,497710833,615598711,264,65552,50331652,1,1048576,16384,544,270532608,151813349,221976871,678178917,845710321,751376227,331656525,739558112,267703680]")));
    }

    public int longestNiceSubarray(int[] nums) {
        long flag = nums[0];
        int ans = 1, l = 0, r = 1;
        for (; r < nums.length; r++) {
            while (l < r && (flag | nums[r]) != flag + nums[r]) {
                flag -= nums[l];
                l++;
            }
            flag |= nums[r];
            ans = Math.max(ans, r - l + 1);
        }
        return ans;
    }
}
