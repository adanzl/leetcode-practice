package com.leo.leetcode.algorithm.q2200;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 一个 ATM 机器，存有 5 种面值的钞票：20 ，50 ，100 ，200 和 500 美元。初始时，ATM 机是空的。用户可以用它存或者取任意数目的钱。
 * 取款时，机器会优先取 较大 数额的钱。
 * 1、比方说，你想取 $300 ，并且机器里有 2 张 $50 的钞票，1 张 $100 的钞票和1 张 $200 的钞票，那么机器会取出 $100 和 $200 的钞票。
 * 2、但是，如果你想取 $600 ，机器里有 3 张 $200 的钞票和1 张 $500 的钞票，那么取款请求会被拒绝，因为机器会先取出 $500 的钞票，然后无法取出剩余的 $100 。注意，因为有 $500 钞票的存在，机器 不能 取 $200 的钞票。
 * 请你实现 ATM 类：
 * 1、ATM() 初始化 ATM 对象。
 * 2、void deposit(int[] banknotesCount) 分别存入 $20 ，$50，$100，$200 和 $500 钞票的数目。
 * 3、int[] withdraw(int amount) 返回一个长度为 5 的数组，分别表示 $20 ，$50，$100 ，$200 和 $500 钞票的数目，并且更新 ATM 机里取款后钞票的剩余数量。如果无法取出指定数额的钱，请返回 [-1] （这种情况下 不 取出任何钞票）。
 * 提示：
 * 1、banknotesCount.length == 5
 * 2、0 <= banknotesCount[i] <= 10^9
 * 3、1 <= amount <= 10^9
 * 4、总共 最多有 5000 次 withdraw 和 deposit 的调用。
 * 5、函数 withdraw 和 deposit 至少各有 一次 调用。
 * 链接：https://leetcode-cn.com/problems/design-an-atm-machine
 */
public class Q2241 {

    public static void main(String[] args) {
        ATM atm = new ATM();
        atm.deposit(stringToIntegerArray("[0,0,1,2,1]"));           // 存入 1 张 $100 ，2 张 $200 和 1 张 $500 的钞票。
        // [0,0,1,0,1]
        System.out.println(Arrays.toString(atm.withdraw(600)));   // 返回 [0,0,1,0,1] 。机器返回 1 张 $100 和 1 张 $500 的钞票。机器里剩余钞票的数量为 [0,0,0,2,0] 。
        atm.deposit(stringToIntegerArray("[0,1,0,1,1]"));
        // [-1]
        System.out.println(Arrays.toString(atm.withdraw(600)));   // 返回 [-1] 。机器会尝试取出 $500 的钞票，然后无法得到剩余的 $100 ，所以取款请求会被拒绝。
        // [0,1,0,0,1]
        System.out.println(Arrays.toString(atm.withdraw(550)));   // 返回 [0,1,0,0,1] ，机器会返回 1 张 $50 的钞票和 1 张 $500 的钞票。
    }

    static class ATM {

        long[] cashes;
        int[] VALUES = new int[]{20, 50, 100, 200, 500};

        public ATM() {
            cashes = new long[5];
        }

        public void deposit(int[] banknotesCount) {
            for (int i = 0; i < banknotesCount.length; i++) cashes[i] += (long) banknotesCount[i] * VALUES[i];
        }

        public int[] withdraw(int amount) {
            int[] ret = new int[5];
            for (int i = cashes.length - 1; i >= 0 && amount > 0; i--) {
                if (cashes[i] == 0 || amount < VALUES[i]) continue;
                ret[i] = (int) Math.min(amount / VALUES[i], cashes[i] / VALUES[i]);
                amount -= ret[i] * VALUES[i];
            }
            if (amount > 0) return new int[]{-1};
            for (int i = 0; i < 5; i++) cashes[i] -= (long) VALUES[i] * ret[i];
            return ret;
        }
    }

}
