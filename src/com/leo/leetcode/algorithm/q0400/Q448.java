package com.leo.leetcode.algorithm.q0400;

import com.leo.utils.LCUtil;

import java.util.ArrayList;
import java.util.List;

public class Q448 {
    public void TestOJ() {
        System.out.println(findDisappearedNumbers(LCUtil.stringToIntegerArray("[4,3,2,7,8,2,3,1]"))); // [5,6]
        System.out.println(findDisappearedNumbers(LCUtil.stringToIntegerArray("[1]"))); // []
        System.out.println(findDisappearedNumbers(LCUtil.stringToIntegerArray("[2,2]"))); // [1]
    }

    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> ret = new ArrayList<>();
        go:
        for (int i = 0; i < nums.length; i++) {
            int v = nums[i] - 1;
            while (true) {
                if (v == nums[v] - 1) {
                    continue go;
                }
                int t = v;
                v = nums[v] - 1;
                nums[t] = t + 1;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i + 1) {
                ret.add(i + 1);
            }
        }
        return ret;
    }
}
