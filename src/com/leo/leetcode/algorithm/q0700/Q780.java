package com.leo.leetcode.algorithm.q0700;

/**
 * 给定四个整数 sx , sy ，tx 和 ty，如果通过一系列的转换可以从起点 (sx, sy) 到达终点 (tx, ty)，则返回 true，否则返回 false。
 * 从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。
 * 提示:  1 <= sx, sy, tx, ty <= 10^9
 * 链接：https://leetcode-cn.com/problems/reaching-points
 */
public class Q780 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q780().reachingPoints(1, 1, 1_000_000_000, 1));
        // true
        System.out.println(new Q780().reachingPoints(1, 1, 3, 5));
        // false
        System.out.println(new Q780().reachingPoints(1, 1, 2, 2));
        // true
        System.out.println(new Q780().reachingPoints(1, 1, 1, 1));
    }

    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        while (tx > sx && ty > sy && tx != ty) {
            if (tx > ty) tx %= ty;
            else ty %= tx;
        }
        if (tx == sx && ty == sy) return true;
        else if (tx == sx) return ty > sy && (ty - sy) % tx == 0;
        else if (ty == sy) return tx > sx && (tx - sx) % ty == 0;
        else return false;
    }
}
