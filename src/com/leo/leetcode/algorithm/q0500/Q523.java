package com.leo.leetcode.algorithm.q0500;

import java.util.HashSet;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
 * 1、子数组大小 至少为 2 ，
 * 2、且子数组元素总和为 k 的倍数。
 * 如果存在，返回 true ；否则，返回 false 。
 * 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。
 * <p>
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^9
 * 3、0 <= sum(nums[i]) <= 2^31 - 1
 * 4、1 <= k <= 2^31 - 1
 * <p>
 * 链接：https://leetcode-cn.com/problems/continuous-subarray-sum
 */
public class Q523 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q523().checkSubArraySum(stringToIntegerArray("[1,1]"), 1));
        // false
        System.out.println(new Q523().checkSubArraySum(stringToIntegerArray("[1,2,12]"), 6));
        // false
        System.out.println(new Q523().checkSubArraySum(stringToIntegerArray("[0,5,0]"), 3));
        // true
        System.out.println(new Q523().checkSubArraySum(stringToIntegerArray("[0,0,5,0]"), 3));
        // false
        System.out.println(new Q523().checkSubArraySum(stringToIntegerArray("[1,0]"), 2));
        // true
        System.out.println(new Q523().checkSubArraySum(stringToIntegerArray("[23,2,4,6,6]"), 7));
        // false
        System.out.println(new Q523().checkSubArraySum(stringToIntegerArray("[23,2,6,4,7]"), 13));
        // true
        System.out.println(new Q523().checkSubArraySum(stringToIntegerArray("[23,2,4,6,7]"), 6));
        // true
        System.out.println(new Q523().checkSubArraySum(stringToIntegerArray("[23,2,6,4,7]"), 6));
        // false
        System.out.println(new Q523().checkSubArraySum(stringToIntegerArray("[23,2,6,4,7]"), Integer.MAX_VALUE));
    }

    public boolean checkSubArraySum(int[] nums, int k) {
        Set<Integer> marks = new HashSet<>();
        int sum = nums[0] % k, z = nums[0] % k == 0 ? 1 : 0;
        marks.add(sum);
        for (int i = 1; i < nums.length; i++) {
            int v = nums[i] % k;
            if (v == 0) {
                z++;
                if (z == 2) return true;
                continue;
            }
            z = 0;
            sum = (v + sum) % k;
            if (sum == 0 || marks.contains(sum))
                return true;
            else marks.add(sum);
        }
        return false;
    }
}
