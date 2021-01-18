package com.leo.leetcode.algorithm.q1000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.ArrayList;
import java.util.List;

public class Q1018 {
    public static void main(String[] args) {
        // [false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,true,false,false,true,true,true,true,false]
        System.out.println(new Q1018().prefixesDivBy5(stringToIntegerArray("[1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1]")));
        // [true,false,false]
        System.out.println(new Q1018().prefixesDivBy5(stringToIntegerArray("[0,1,1]")));
        // [false,false,false]
        System.out.println(new Q1018().prefixesDivBy5(stringToIntegerArray("[1,1,1]")));
        // [true,false,false,false,true,false]
        System.out.println(new Q1018().prefixesDivBy5(stringToIntegerArray("[0,1,1,1,1,1]")));
        // [false,false,false,false,false]
        System.out.println(new Q1018().prefixesDivBy5(stringToIntegerArray("[1,1,1,0,1]")));
    }

    public List<Boolean> prefixesDivBy5(int[] A) {
        List<Boolean> ret = new ArrayList<>();
        int value = 0;
        for (int v : A) {
            value = (value << 1) + v;
            value %= 5;
            ret.add(value == 0);
        }
        return ret;
    }
}
