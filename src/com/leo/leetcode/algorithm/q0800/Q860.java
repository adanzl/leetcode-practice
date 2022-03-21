package com.leo.leetcode.algorithm.q0800;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
 * 每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
 * 注意，一开始你手头没有任何零钱。
 * 给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
 * 提示：
 * 1、1 <= bills.length <= 10^5
 * 2、bills[i] 不是 5 就是 10 或是 20
 * 链接：https://leetcode-cn.com/problems/lemonade-change
 */
public class Q860 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q860().lemonadeChange(stringToIntegerArray("[5,5,5,10,20]")));
        // false
        System.out.println(new Q860().lemonadeChange(stringToIntegerArray("[5,5,10,10,20]")));
    }

    public boolean lemonadeChange(int[] bills) {
        int[] count = new int[5];
        for (int bill : bills) {
            count[bill / 5]++;
            int remain = bill - 5;
            for (int i = count.length - 1; i >= 0 && remain != 0; ) {
                if (count[i] > 0 && i * 5 <= remain) {
                    remain -= i * 5;
                    count[i]--;
                } else i--;
            }
            if (remain != 0) return false;
        }
        return true;
    }
}
