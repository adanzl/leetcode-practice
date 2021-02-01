package com.leo.leetcode.algorithm.q0100;

import java.math.BigDecimal;
import java.util.HashMap;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
 * <p>
 * 链接：https://leetcode-cn.com/problems/max-points-on-a-line/
 */
public class Q149 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q149().maxPoints(stringToInt2dArray("[[0,0],[94911151,94911150],[94911152,94911151]]")));
        // 3
        System.out.println(new Q149().maxPoints(stringToInt2dArray("[[4,0],[4,-1],[4,5]]")));
        // 3
        System.out.println(new Q149().maxPoints(stringToInt2dArray("[[2,3],[3,3],[-5,3]]")));
        // 2
        System.out.println(new Q149().maxPoints(stringToInt2dArray("[[0,0],[1,1],[1,-1]]")));
        // 3
        System.out.println(new Q149().maxPoints(stringToInt2dArray("[[0,0],[1,1],[0,0]]")));
        // 3
        System.out.println(new Q149().maxPoints(stringToInt2dArray("[[1,1],[2,2],[3,3]]")));
        // 4
        System.out.println(new Q149().maxPoints(stringToInt2dArray("[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]")));
    }

    public int maxPoints(int[][] points) {
        if (points.length == 0) return 0;
        int ret = 0;
        for (int i = 0; i < points.length; i++) {
            Map<BigDecimal, Integer> kMap = new HashMap<>();
            int m = 0, nSame = 0, nInfinity = 0;
            for (int j = i + 1; j < points.length; j++) {
                if (points[i][0] == points[j][0] && points[i][1] == points[j][1]) {
                    nSame++;
                    continue;
                }
                if (points[i][0] == points[j][0]) {
                    nInfinity++;
                    m = Math.max(nInfinity, m);
                } else {
                    BigDecimal v1 = new BigDecimal(points[i][1] - points[j][1]), v2 = new BigDecimal(points[i][0] - points[j][0]);
                    BigDecimal k = v1.divide(v2,16, BigDecimal.ROUND_HALF_UP);
                    int count = kMap.getOrDefault(k, 0);
                    kMap.put(k, count + 1);
                    m = Math.max(count + 1, m);
                }
            }
            ret = Math.max(m + nSame, ret);
        }
        return ret + 1;
    }
}
