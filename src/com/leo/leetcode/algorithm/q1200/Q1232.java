package com.leo.leetcode.algorithm.q1200;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，
 * 其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
 * 请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
 * <p>
 * 提示：
 * 1、2 <= coordinates.length <= 1000
 * 2、coordinates[i].length == 2
 * 3、-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
 * 4、coordinates 中不含重复的点
 * <p>
 * 链接：https://leetcode-cn.com/problems/check-if-it-is-a-straight-line
 */
public class Q1232 {
    public static void main(String[] args) {
        // false
        System.out.println(new Q1232().checkStraightLine(stringToInt2dArray("[[1,1],[2,2],[2,0]]")));
        // true
        System.out.println(new Q1232().checkStraightLine(stringToInt2dArray("[[0,0],[0,1],[0,-1]]")));
        // true
        System.out.println(new Q1232().checkStraightLine(stringToInt2dArray("[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]")));
        // false
        System.out.println(new Q1232().checkStraightLine(stringToInt2dArray("[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]")));
    }

    public boolean checkStraightLine(int[][] coordinates) {
        boolean bVertical = coordinates[0][0] == coordinates[1][0];
        float f0 = 0, d = 0.0001f;
        if (!bVertical) {
            f0 = tan(coordinates[0], coordinates[1]);
        }
        for (int i = 2; i < coordinates.length; i++) {
            if (bVertical) {
                if (coordinates[0][0] != coordinates[i][0]) return false;
            } else {
                float f = tan(coordinates[0], coordinates[i]);
                if (f - f0 > d || f - f0 < -d) return false;
            }
        }
        return true;
    }

    float tan(int[] p1, int[] p2) {
        return (float) (p2[1] - p1[1]) / (p2[0] - p1[0]);
    }
}
