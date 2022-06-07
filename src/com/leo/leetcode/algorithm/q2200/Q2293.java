package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的整数数组 nums ，其长度是 2 的幂。
 * 对 nums 执行下述算法：
 * 1、设 n 等于 nums 的长度，如果 n == 1 ，终止 算法过程。否则，创建 一个新的整数数组 newNums ，新数组长度为 n / 2 ，下标从 0 开始。
 * 2、对于满足 0 <= i < n / 2 的每个 偶数 下标 i ，将 newNums[i] 赋值 为 min(nums[2 * i], nums[2 * i + 1]) 。
 * 3、对于满足 0 <= i < n / 2 的每个 奇数 下标 i ，将 newNums[i] 赋值 为 max(nums[2 * i], nums[2 * i + 1]) 。
 * 4、用 newNums 替换 nums 。
 * 5、从步骤 1 开始 重复 整个过程。
 * 执行算法后，返回 nums 中剩下的那个数字。
 * 提示：
 * 1、1 <= nums.length <= 1024
 * 2、1 <= nums[i] <= 10^9
 * 3、nums.length 是 2 的幂
 * 链接：https://leetcode.cn/problems/min-max-game
 */
public class Q2293 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q2293().minMaxGame(stringToIntegerArray("[1,3,5,2,4,8,2,2]")));
        // 3
        System.out.println(new Q2293().minMaxGame(stringToIntegerArray("[3]")));
    }

    public int minMaxGame(int[] nums) {
        int n = nums.length;
        while (n > 1) {
            int[] newNums = new int[n / 2];
            for (int i = 0; i < n / 2; i++) {
                if ((i & 1) == 0) newNums[i] = Math.min(nums[i * 2], nums[i * 2 + 1]);
                else newNums[i] = Math.max(nums[i * 2], nums[i * 2 + 1]);
            }
            n /= 2;
            nums = newNums;
        }
        return nums[0];
    }
}
