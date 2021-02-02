package com.leo.leetcode.algorithm.q0200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
 * <p>
 * 进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
 * <p>
 * 提示：
 * 1、n == nums.length
 * 2、1 <= n <= 10^4
 * 3、0 <= nums[i] <= n
 * 4、nums 中的所有数字都 独一无二
 * <p>
 * 链接：https://leetcode-cn.com/problems/missing-number
 */
public class Q268 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q268().missingNumber(stringToIntegerArray("[45,35,38,13,12,23,48,15,44,21,43,26,6,37,1,19,22,3,11,32,4,16,28,49,29,36,33,8,9,39,46,17,41,7,2,5,27,20,40,34,30,25,47,0,31,42,24,10,14]")));
        // 2
        System.out.println(new Q268().missingNumber(stringToIntegerArray("[3,0,1]")));
        // 2
        System.out.println(new Q268().missingNumber(stringToIntegerArray("[0,1]")));
        // 8
        System.out.println(new Q268().missingNumber(stringToIntegerArray("[9,6,4,2,3,5,7,0,1]")));
        // 1
        System.out.println(new Q268().missingNumber(stringToIntegerArray("[0]")));
    }

    public int missingNumber(int[] nums) {
        int sum = (nums.length + 1) * nums.length / 2;
        for (int n : nums) sum -= n;
        return sum;
    }
}
