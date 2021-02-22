package com.leo.leetcode.algorithm.q1000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 今天，书店老板有一家店打算试营业 customers.length 分钟。
 * 每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
 * 在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。
 * 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
 * 书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
 * 请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
 * <p>
 * 提示：
 * 1、1 <= X <= customers.length == grumpy.length <= 20000
 * 2、0 <= customers[i] <= 1000
 * 3、0 <= grumpy[i] <= 1
 * <p>
 * 链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner
 */
public class Q1052 {

    public static void main(String[] args) {
        // 18
        System.out.println(new Q1052().maxSatisfied(stringToIntegerArray("[10,1,7]"), stringToIntegerArray("[0,0,0]"), 2));
        // 16
        System.out.println(new Q1052().maxSatisfied(stringToIntegerArray("[1,0,1,2,1,1,7,5]"), stringToIntegerArray("[0,1,0,1,0,1,0,1]"), 3));
    }

    public int maxSatisfied(int[] customers, int[] grumpy, int X) {
        int ret = 0, sum = 0, ext = 0;
        for (int i = 0; i < customers.length; i++) {
            if (i >= X && grumpy[i - X] == 1) sum -= customers[i - X];
            if (grumpy[i] == 0) ret += customers[i];
            else {
                sum += customers[i];
                ext = Math.max(sum, ext);
            }
        }
        return ret + ext;
    }
}
