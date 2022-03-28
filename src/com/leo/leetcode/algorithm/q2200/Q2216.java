package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的整数数组 nums ，如果满足下述条件，则认为数组 nums 是一个 美丽数组 ：
 * 1、nums.length 为偶数
 * 2、对所有满足 i % 2 == 0 的下标 i ，nums[i] != nums[i + 1] 均成立
 * 注意，空数组同样认为是美丽数组。
 * 你可以从 nums 中删除任意数量的元素。当你删除一个元素时，被删除元素右侧的所有元素将会向左移动一个单位以填补空缺，而左侧的元素将会保持 不变 。
 * 返回使 nums 变为美丽数组所需删除的 最少 元素数目。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^5
 * 链接：https://leetcode-cn.com/problems/minimum-deletions-to-make-array-beautiful
 */
public class Q2216 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q2216().minDeletion(stringToIntegerArray("[1,1,2,3,5]")));
        // 2
        System.out.println(new Q2216().minDeletion(stringToIntegerArray("[1,1,2,2,3,3]")));
        // 1
        System.out.println(new Q2216().minDeletion(stringToIntegerArray("[1,1,2,3,5]")));
    }

    public int minDeletion(int[] nums) {
        boolean even = true;
        int ret = 0, pre = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (even && nums[i] == pre) {
                ret++;
            } else {
                even = !even;
                pre = nums[i];
            }
        }
        if (((nums.length - ret) & 1) == 1) ret++;
        return ret;
    }

}
