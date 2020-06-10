package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import org.junit.Test;

import java.util.Arrays;

public class Q137 {
    @Test
    public void TestOJ() {
        System.out.println(singleNumber(LCUtil.stringToIntegerArray("[-2,-2,1,1,-3,1,-3,-3,-4,-2]"))); // -4
        System.out.println(singleNumber(LCUtil.stringToIntegerArray("[2,2,3,2]"))); // 3
        System.out.println(singleNumber(LCUtil.stringToIntegerArray("[0,1,0,1,0,1,99]"))); // 99
    }

    /**
     * https://leetcode-cn.com/problems/single-number-ii/solution/single-number-ii-mo-ni-san-jin-zhi-fa-by-jin407891/
     */
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        int pre = nums[0], c = 0;
        for (int num : nums) {
            if (num != pre) {
                if (c != 3) {
                    return pre;
                }
                pre = num;
                c = 0;
            }
            c++;

        }
        return pre;
    }
}
