package com.leo.leetcode.algorithm;

public class Q84 {

    public static void main(String[] args) {
        new Q84().TestOJ();
    }

    // 以第i根柱子为最矮柱子所能延伸的最大面积
    public void TestOJ() {
//        int heights[] = new int[]{2, 1, 5, 6, 2, 3}; // 10
        int[] heights = {1}; // 1
//        int heights[] = new int[]{9, 0}; // 9
//        int heights[] = new int[]{2, 3}; // 4
        System.out.println(largestRectangleArea(heights)); // 10
    }

    public int largestRectangleArea(int[] heights) {
        if (heights.length == 0) return 0;
        int ret = 0;
        int flagL, flagR;
        for (int i = 0; i < heights.length; i++) {
            int p = i - 1;
            // p 一直减少，找到第一个比当前高度小的柱子就停止
            while (p >= 0 && heights[p] >= heights[i]) {
                p--;
            }
            flagL = p;
            p = i;
            while (p < heights.length && heights[p] >= heights[i]) {
                p++;
            }
            flagR = p;
            ret = Math.max((flagR - flagL - 1) * heights[i], ret);
        }

        return ret;
    }
}
