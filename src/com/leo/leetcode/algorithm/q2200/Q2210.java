package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的整数数组 nums 。如果两侧距 i 最近的不相等邻居的值均小于 nums[i] ，则下标 i 是 nums 中，
 * 某个峰的一部分。类似地，如果两侧距 i 最近的不相等邻居的值均大于 nums[i] ，则下标 i 是 nums 中某个谷的一部分。对于相邻下标 i 和 j ，如果 nums[i] == nums[j] ， 则认为这两下标属于 同一个 峰或谷。
 * 注意，要使某个下标所做峰或谷的一部分，那么它左右两侧必须 都 存在不相等邻居。
 * 返回 nums 中峰和谷的数量。
 * 提示：
 * 1、3 <= nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 链接：https://leetcode-cn.com/problems/count-hills-and-valleys-in-an-array
 */
public class Q2210 {

    public static void main(String[] args) {
        // 23
        System.out.println(new Q2210().countHillValley(stringToIntegerArray("[49,16,11,24,82,24,73,61,62,44,25,59,3,57,62,7,38,61,22,92,90,60,28,21,37,54,43,14,3,64,48,51,55,55,58,43,67,46,36,32,78]")));
        // 3
        System.out.println(new Q2210().countHillValley(stringToIntegerArray("[2,4,1,1,6,5]")));
        // 0
        System.out.println(new Q2210().countHillValley(stringToIntegerArray("[6,6,5,5,4,1]")));
    }

    public int countHillValley(int[] nums) {
        int preFlag = 0, count = 0, ret = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) { // /
                if (preFlag == -1) ret += count;
                preFlag = 1;
                count = 1;
            } else if (nums[i] < nums[i - 1]) { // \
                if (preFlag == 1) ret += count;
                preFlag = -1;
                count = 1;
            }
        }
        return ret;
    }
}
