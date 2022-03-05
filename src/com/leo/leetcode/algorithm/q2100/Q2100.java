package com.leo.leetcode.algorithm.q2100;

import java.util.ArrayList;
import java.util.List;


import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 你和一群强盗准备打劫银行。给你一个下标从 0 开始的整数数组 security ，其中 security[i] 是第 i 天执勤警卫的数量。
 * 日子从 0 开始编号。同时给你一个整数 time 。
 * 如果第 i 天满足以下所有条件，我们称它为一个适合打劫银行的日子：
 * 1、第 i 天前和后都分别至少有 time 天。
 * 2、第 i 天前连续 time 天警卫数目都是非递增的。
 * 3、第 i 天后连续 time 天警卫数目都是非递减的。
 * 更正式的，第 i 天是一个合适打劫银行的日子当且仅当：security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].
 * 请你返回一个数组，包含 所有 适合打劫银行的日子（下标从 0 开始）。返回的日子可以 任意 顺序排列。
 * 提示：
 * 1、1 <= security.length <= 10^5
 * 2、0 <= security[i], time <= 10^5
 * 链接：https://leetcode-cn.com/problems/find-good-days-to-rob-the-bank
 */
public class Q2100 {

    public static void main(String[] args) {
        // []
        System.out.println(new Q2100().goodDaysToRobBank(stringToIntegerArray("[1,2,3,4]"), 1));
        // [0,1,2,3,4]
        System.out.println(new Q2100().goodDaysToRobBank(stringToIntegerArray("[1,1,1,1,1]"), 0));
        // [2,3]
        System.out.println(new Q2100().goodDaysToRobBank(stringToIntegerArray("[5,3,3,3,5,6,2]"), 2));
        // []
        System.out.println(new Q2100().goodDaysToRobBank(stringToIntegerArray("[1,2,3,4,5,6]"), 2));
        // []
        System.out.println(new Q2100().goodDaysToRobBank(stringToIntegerArray("[1]"), 5));
    }

    public List<Integer> goodDaysToRobBank(int[] security, int time) {
        List<Integer> ret = new ArrayList<>();
        int len = security.length;
        int[] upArr = new int[len], downArr = new int[len];
        upArr[0] = 1;
        downArr[len - 1] = 1;
        for (int i = 1; i < len; i++) {
            if (security[i - 1] >= security[i]) upArr[i] = upArr[i - 1] + 1;
            else upArr[i] = 1;
        }
        if (downArr[len - 1] > time && upArr[len - 1] > time) ret.add(len - 1);
        for (int i = len - 2; i >= time; i--) {
            if (security[i + 1] >= security[i]) downArr[i] = downArr[i + 1] + 1;
            else downArr[i] = 1;
            if (downArr[i] > time && upArr[i] > time) ret.add(i);
        }
        return ret;
    }
}
