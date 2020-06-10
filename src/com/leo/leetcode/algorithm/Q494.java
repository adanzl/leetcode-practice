package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import org.junit.Test;

public class Q494 {
    @Test
    public void TestOJ() {
        System.out.println(findTargetSumWays(LCUtil.stringToIntegerArray("[1, 1, 1, 1, 1]"), 3)); // 5
        System.out.println(findTargetSumWays(LCUtil.stringToIntegerArray("[0,0,0,0]"), 3)); // 0
    }

    private int count;

    public int findTargetSumWays(int[] nums, int S) {
        this.count = 0;
        process(nums, S, 0, 0);
        return this.count;
    }

    private void process(int[] nums, int S, int index, int s) {
        if (index == nums.length - 1) {
            if (s + nums[index] == S) this.count++;
            if (s - nums[index] == S) this.count++;
            return;
        }
        process(nums, S, index + 1, s + nums[index]);
        process(nums, S, index + 1, s - nums[index]);
    }
}
