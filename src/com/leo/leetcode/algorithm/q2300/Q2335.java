package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 现有一台饮水机，可以制备冷水、温水和热水。每秒钟，可以装满 2 杯 不同 类型的水或者 1 杯任意类型的水。
 * 给你一个下标从 0 开始、长度为 3 的整数数组 amount ，其中 amount[0]、amount[1] 和 amount[2] 分别表示需要装满冷水、温水和热水的杯子数量。
 * 返回装满所有杯子所需的 最少 秒数。
 * 提示：
 * 1、amount.length == 3
 * 2、0 <= amount[i] <= 100
 * 链接：https://leetcode.cn/problems/minimum-amount-of-time-to-fill-cups
 */
public class Q2335 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q2335().fillCups(stringToIntegerArray("[0,2,2]")));
        // 4
        System.out.println(new Q2335().fillCups(stringToIntegerArray("[1,4,2]")));
        // 7
        System.out.println(new Q2335().fillCups(stringToIntegerArray("[5,4,4]")));
        // 5
        System.out.println(new Q2335().fillCups(stringToIntegerArray("[5,0,0]")));
    }

    public int fillCups(int[] amount) {
        int z = 0, ret = 0;
        for (int num : amount) if (num == 0) z++;
        while (z < 3) {
            int max = 0, min = Integer.MAX_VALUE, iMax = -1, iMin = -1;
            z = 0;
            for (int i = 0; i < 3; i++) {
                if (amount[i] >= max) {
                    max = amount[i];
                    iMax = i;
                }
            }
            for (int i = 2; i >= 0; i--) {
                if (amount[i] == 0) z++;
                else {
                    if (amount[i] <= min) {
                        min = amount[i];
                        iMin = i;
                    }
                }
            }
            if (z <= 1) {
                amount[iMax]--;
                amount[iMin]--;
                ret++;
            } else if (z == 2) {
                ret += amount[iMax];
                amount[iMax] = 0;
            }
        }
        return ret;
    }

}
