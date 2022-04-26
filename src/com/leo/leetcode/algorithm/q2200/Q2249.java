package com.leo.leetcode.algorithm.q2200;

import java.util.HashSet;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个二维整数数组 circles ，其中 circles[i] = [xi, yi, ri] 表示网格上圆心为 (xi, yi) 且半径为 ri 的第 i 个圆，返回出现在 至少一个 圆内的 格点数目 。
 * 注意：
 * 1、格点 是指整数坐标对应的点。
 * 2、圆周上的点 也被视为出现在圆内的点。
 * 提示：
 * 1、1 <= circles.length <= 200
 * 2、circles[i].length == 3
 * 3、1 <= xi, yi <= 100
 * 4、1 <= ri <= min(xi, yi)
 * 链接：https://leetcode-cn.com/problems/count-lattice-points-inside-a-circle
 */
public class Q2249 {

    public static void main(String[] args) {
        // 141
        System.out.println(new Q2249().countLatticePoints(stringToInt2dArray("[[8,9,6],[9,8,4],[4,1,1],[8,5,1],[7,1,1],[6,7,5],[5,5,3]]")));
        // 5
        System.out.println(new Q2249().countLatticePoints(stringToInt2dArray("[[2,2,1]]")));
        // 16
        System.out.println(new Q2249().countLatticePoints(stringToInt2dArray("[[2,2,2],[3,4,1]]")));
    }

    public int countLatticePoints(int[][] circles) {
        HashSet<String> set = new HashSet<>();
        for (int[] circle : circles) {
            int d = pow2(circle[2]);
            for (int i = circle[0] - circle[2]; i <= circle[0] + circle[2]; i++) {
                for (int j = circle[1] - circle[2]; j <= circle[1] + circle[2]; j++) {
                    if (pow2(i - circle[0]) + pow2(j - circle[1]) <= d) set.add(i + "_" + j);
                }
            }
        }
        return set.size();
    }

    int pow2(int x) {
        return x * x;
    }

}
