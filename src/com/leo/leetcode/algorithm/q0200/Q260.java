package com.leo.leetcode.algorithm.q0200;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。
 * 找出只出现一次的那两个元素。
 * <p>
 * 注意：
 * 1、结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
 * 2、你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
 * <p>
 * 链接：https://leetcode-cn.com/problems/single-number-iii/
 */
public class Q260 {

    public static void main(String[] args) {
        // [3,5]
        System.out.println(Arrays.toString(new Q260().singleNumber(stringToIntegerArray("[1,2,1,3,2,5]"))));
    }

    public int[] singleNumber(int[] nums) {
        int[] ret = new int[2];
        int mark = 0, mask = 1;
        for (int n : nums) mark ^= n;
        while ((mark & mask) == 0) mask <<= 1;
        for (int n : nums) {
            if ((n & mask) == 0) ret[1] ^= n;
            else ret[0] ^= n;
        }
        return ret;
    }
}
