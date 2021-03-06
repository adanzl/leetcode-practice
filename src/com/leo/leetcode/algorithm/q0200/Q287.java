package com.leo.leetcode.algorithm.q0200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
 * 假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。
 * <p>
 * 提示：
 * 1、2 <= n <= 3 * 10^4
 * 2、nums.length == n + 1
 * 3、1 <= nums[i] <= n
 * 4、nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
 * <p>
 * 进阶：
 * 1、如何证明 nums 中至少存在一个重复的数字?
 * 2、你可以在不修改数组 nums 的情况下解决这个问题吗？
 * 3、你可以只用常量级 O(1) 的额外空间解决这个问题吗？
 * 4、你可以设计一个时间复杂度小于 O(n2) 的解决方案吗？
 * <p>
 * 链接：https://leetcode-cn.com/problems/find-the-duplicate-number
 */
public class Q287 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q287().findDuplicate(stringToIntegerArray("[1,3,4,2,2]")));
        // 3
        System.out.println(new Q287().findDuplicate(stringToIntegerArray("[3,1,3,4,2]")));
    }

    private int findDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = nums.length - 1; j >= 0; j--) {
                if (nums[i] == nums[j]) {
                    if (i != j) return nums[i];
                    break;
                }
            }
        }
        return 0;
    }

}
