package com.leo.leetcode.algorithm.q1000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.ArrayList;
import java.util.List;

/**
 * 给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。
 * 返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。
 *
 * 链接：https://leetcode-cn.com/problems/binary-prefix-divisible-by-5
 */
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
