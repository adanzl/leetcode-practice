package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

import java.util.ArrayList;
import java.util.List;

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
