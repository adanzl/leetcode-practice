package com.leo.leetcode.algorithm.q0200;

/**
 * 在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
 * 每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
 * 说明: 假设矩形面积不会超出 int 的范围。
 * 链接：https://leetcode-cn.com/problems/rectangle-area/
 */
public class Q223 {

    public static void main(String[] args) {
        // 45
        System.out.println(new Q223().computeArea(-3, 0, 3, 4, 0, -1, 9, 2));
    }

    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int w0 = C - A, h0 = D - B, w1 = G - E, h1 = H - F, area0 = w0 * h0, area1 = w1 * h1, area_in;
        if (E >= C || A >= G || B >= H || F > D) area_in = 0;
        else if (area0 > area1 && G <= C && E >= A && H <= D && F >= B) area_in = area1;
        else if (G >= C && E <= A && H >= D && F <= B) area_in = area0;
        else area_in = Math.abs(Math.min(D, H) - Math.max(B, F)) * Math.abs(Math.min(C, G) - Math.max(A, E));
        return area0 - area_in + area1;
    }
}
