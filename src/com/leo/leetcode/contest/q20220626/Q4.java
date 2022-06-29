package com.leo.leetcode.contest.q20220626;

import static com.leo.utils.LCUtil.stringToDoubleArray;

/**
 * 链接：https://leetcode.cn/contest/sf-tech/problems/uWWzsv/
 */
public class Q4 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q4().isPointInPolygon(6, 3, stringToDoubleArray("[1,2,3,4,5,3,6,1,3,1,1,2]")));
        // true
        System.out.println(new Q4().isPointInPolygon(1, 3, stringToDoubleArray("[0,0,0,4,4,4,2,2,4,0,0,0]")));
    }

    // https://wrfranklin.org/Research/Short_Notes/pnpoly.html
    public boolean isPointInPolygon(double x, double y, double[] coords) {
        if (coords.length <= 6) return false;
        int i, j;
        boolean c = false;
        for (i = 0, j = coords.length / 2 - 1; i < coords.length / 2; j = i++) {
            if (((coords[i * 2 + 1] > y) != (coords[j * 2 + 1] > y)) &&
                    (x < (coords[j * 2] - coords[i * 2]) * (y - coords[i * 2 + 1]) / (coords[j * 2 + 1] - coords[i * 2 + 1]) + coords[i * 2]))
                c = !c;
        }
        return c;
    }

}
