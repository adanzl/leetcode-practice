package com.leo.leetcode.algorithm.q2200;

/**
 * 给你两个字符串 current 和 correct ，表示两个 24 小时制时间 。
 * 24 小时制时间 按 "HH:MM" 进行格式化，其中 HH 在 00 和 23 之间，而 MM 在 00 和 59 之间。最早的 24 小时制时间为 00:00 ，最晚的是 23:59 。
 * 在一步操作中，你可以将 current 这个时间增加 1、5、15 或 60 分钟。你可以执行这一操作 任意 次数。
 * 返回将 current 转化为 correct 需要的 最少操作数 。
 * 提示：
 * 1、current 和 correct 都符合 "HH:MM" 格式
 * 2、current <= correct
 * 链接：https://leetcode-cn.com/problems/minimum-number-of-operations-to-convert-time
 */
public class Q2224 {

    public static void main(String[] args) {
        // 32
        System.out.println(new Q2224().convertTime("00:00", "23:59"));
        // 3
        System.out.println(new Q2224().convertTime("02:30", "04:35"));
        // 1
        System.out.println(new Q2224().convertTime("11:00", "11:01"));
        // 20
        System.out.println(new Q2224().convertTime("23:59", "11:01"));
        // 19
        System.out.println(new Q2224().convertTime("23:59", "12:01"));
        // 10
        System.out.println(new Q2224().convertTime("2:59", "11:01"));
    }

    public int convertTime(String current, String correct) {
        int ret = 0;
        String[] currentArr = current.split(":"), correctArr = correct.split(":");
        int currentH = Integer.parseInt(currentArr[0]), currentM = Integer.parseInt(currentArr[1]);
        int correctH = Integer.parseInt(correctArr[0]), correctM = Integer.parseInt(correctArr[1]);
        int dm = Math.abs((currentH - correctH) * 60 + currentM - correctM);
        ret += dm / 60;
        dm %= 60;
        ret += dm / 15;
        dm %= 15;
        ret += dm / 5;
        dm %= 5;
        ret += dm;
        return ret;
    }
}
