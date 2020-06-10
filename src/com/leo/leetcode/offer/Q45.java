package com.leo.leetcode.offer;

import com.leo.utils.LCUtil;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Q45 {

    public static void main(String[] args) {
        new Q45().TestOJ();
    }

    public void TestOJ() {
        System.out.println(minNumber(LCUtil.stringToIntegerArray("[824,8247]"))); // "8247824"
        System.out.println(minNumber(LCUtil.stringToIntegerArray("[824,938,1399,5607,6973,5703,9609,4398,8247]"))); // "1399439856075703697382478249389609"
        System.out.println(minNumber(LCUtil.stringToIntegerArray("[3,30,34,5,9]"))); // 3033459
    }

    public String minNumber(int[] nums) {
        List<Integer> n = Arrays.stream(nums).boxed().sorted((o1, o2) -> {
            String str1 = o1.toString() + o2.toString();
            String str2 = o2.toString() + o1.toString();
            return str1.compareTo(str2);
        }).collect(Collectors.toList());
        StringBuilder out = new StringBuilder();
        for (Integer integer : n) {
            out.append(integer);
        }
        return out.toString();
    }
}
