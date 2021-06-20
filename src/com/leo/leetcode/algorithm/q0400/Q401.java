package com.leo.leetcode.algorithm.q0400;

import java.util.ArrayList;
import java.util.List;

/**
 * 二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。每个 LED 代表一个 0 或 1，最低位在右侧。
 * 例如，下面的二进制手表读取 "3:25" 。
 * 给你一个整数 turnedOn ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 按任意顺序 返回答案。
 * 小时不会以零开头：
 * 例如，"01:00" 是无效的时间，正确的写法应该是 "1:00" 。
 * 分钟必须由两位数组成，可能会以零开头：
 * 例如，"10:2" 是无效的时间，正确的写法应该是 "10:02" 。
 * 解释：
 * 0 <= turnedOn <= 10
 * <p>
 * 链接：https://leetcode-cn.com/problems/binary-watch
 */
public class Q401 {

    public static void main(String[] args) {
        //
        System.out.println(new Q401().readBinaryWatch(4));
        // [0:03, 0:05, 0:09, 0:17, 0:33, 0:06, 0:10, 0:18, 0:34, 0:12, 0:20, 0:36, 0:24, 0:40, 0:48, 1:01, 1:02, 1:04, 1:08, 1:16, 1:32, 2:01, 2:02, 2:04, 2:08, 2:16, 2:32, 4:01, 4:02, 4:04, 4:08, 4:16, 4:32, 8:01, 8:02, 8:04, 8:08, 8:16, 8:32, 3:00, 5:00, 9:00, 6:00, 10:00]
        System.out.println(new Q401().readBinaryWatch(2));
        // ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
        System.out.println(new Q401().readBinaryWatch(1));
        // []
        System.out.println(new Q401().readBinaryWatch(9));
    }

    public List<String> readBinaryWatch(int turnedOn) {
        List<String> ret = new ArrayList<>();
        for (int i = Math.max(0, turnedOn - 6); i <= 3 && i <= turnedOn; i++) {
            List<String> hours = buildWatch(i, 0);
            List<String> minutes = buildWatch(turnedOn - i, 1);
            for (String h : hours) {
                for (String m : minutes) {
                    ret.add(h + ":" + m);
                }
            }
        }
        return ret;
    }

    public List<String> buildWatch(int turnedOn, int type) {
        List<String> ret = new ArrayList<>();
        int n = type == 0 ? fn4[turnedOn] : fn6[turnedOn], limit = type == 0 ? 12 : 60;
        int[][] flag = type == 0 ? f4 : f6;
        String format = type == 0 ? "%d" : "%02d";
        for (int i = 0; i < n; i++) {
            int v = flag[turnedOn][i];
            if (v >= limit) continue;
            ret.add(String.format(format, v));
        }
        return ret;
    }

    int[] fn4 = new int[]{1, 4, 6, 4, 1};
    int[] fn6 = new int[]{1, 6, 15, 20, 15, 6, 1};

    int[][] f4 = new int[][]{
            {0},
            {1, 2, 4, 8,},
            {3, 5, 9, 6, 10, 12,},
            {7, 11, 13, 14,},
            {15,},
    };
    int[][] f6 = new int[][]{
            {0},
            {1, 2, 4, 8, 16, 32,},
            {3, 5, 9, 17, 33, 6, 10, 18, 34, 12, 20, 36, 24, 40, 48,},
            {7, 11, 19, 35, 13, 21, 37, 25, 41, 49, 14, 22, 38, 26, 42, 50, 28, 44, 52, 56,},
            {15, 23, 39, 27, 43, 51, 29, 45, 53, 57, 30, 46, 54, 58, 60,},
            {31, 47, 55, 59, 61, 62,},
            {63,}
    };

//    int[] flag = new int[]{1, 1 << 1, 1 << 2, 1 << 3, 1 << 4, 1 << 5, 1 << 6};
//    void gen(int total) {
//        System.out.println("Gen: " + total);
//        for (int nOne = 1; nOne <= total; nOne++) {
//            System.out.print("[" + nOne + "]");
//            func(total, 0, nOne, 0, 0);
//            System.out.println();
//        }
//        System.out.println();
//    }
//
//    void func(int total, int idx, int tOne, int nOne, int num) {
//        if (total - idx < tOne - nOne) return;
//        if (tOne == nOne) {
//            System.out.print(num + ",");
//            return;
//        }
//        func(total, idx + 1, tOne, nOne + 1, num + flag[idx]);
//        func(total, idx + 1, tOne, nOne, num);
//    }
}
