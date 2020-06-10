package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import org.junit.Test;

import java.util.Arrays;

public class Q16 {
    @Test
    public void TestOJ() {
        System.out.println(threeSumClosest(LCUtil.stringToIntegerArray("[0,2,1,-3]"), 1)); // t
        System.out.println(threeSumClosest(LCUtil.stringToIntegerArray("[1,1,1,1]"), 0)); // t
    }

    public int threeSumClosest(int[] nums, int target) {

        Arrays.sort(nums);
        int out = target, delta = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int l = i + 1, r = nums.length - 1;
            int v1 = nums[i];
            while (l < r) {
                int sum = v1 + nums[l] + nums[r];
                int d = Math.abs(sum - target);
                if (d == 0) {
                    return target;
                } else if (sum < target) {
                    l++;
                } else if (sum > target) {
                    r--;
                }

                if (delta > d) {
                    delta = d;
                    out = sum;
                }
            }
        }

        return out;
    }
}
