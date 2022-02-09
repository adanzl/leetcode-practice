package com.leo.leetcode.algorithm.q1400;

import com.leo.utils.LCUtil;

import java.util.ArrayList;
import java.util.List;

/**
 * 给你一个数组candies和一个整数extraCandies，其中candies[i]代表第 i 个孩子拥有的糖果数目。
 * 对每一个孩子，检查是否存在一种方案，将额外的extraCandies个糖果分配给孩子们之后，此孩子有 最多的糖果。注意，允许有多个孩子同时拥有 最多的糖果数目。
 * 提示：
 * 1、2 <= candies.length <= 100
 * 2、1 <= candies[i] <= 100
 * 3、1 <= extraCandies <= 50
 * 链接：https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies
 */
public class Q1431 {
    public static void main(String[] args) {
        System.out.println(new Q1431().kidsWithCandies(LCUtil.stringToIntegerArray("[2,3,5,1,3]"), 3)); // [true,true,true,false,true]
        System.out.println(new Q1431().kidsWithCandies(LCUtil.stringToIntegerArray("[4,2,1,1,2]"), 1)); // [true,false,false,false,false]
        System.out.println(new Q1431().kidsWithCandies(LCUtil.stringToIntegerArray("[12,1,12]"), 10)); // [true,false,true]
    }

    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> out = new ArrayList<>();
        int max = 0;
        for (int v : candies) max = Math.max(max, v);
        for (int v : candies) {
            out.add(v + extraCandies >= max);
        }
        return out;
    }
}
