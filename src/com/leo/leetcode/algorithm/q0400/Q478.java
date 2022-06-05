package com.leo.leetcode.algorithm.q0400;

import java.util.Arrays;
import java.util.Random;

/**
 * 给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。
 * 实现 Solution 类:
 * 1、Solution(double radius, double x_center, double y_center) 用圆的半径 radius 和圆心的位置 (x_center, y_center) 初始化对象
 * 2、randPoint() 返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 [x, y] 。
 * 提示：
 * 1、0 < radius <= 10^8
 * 2、-10^7 <= x_center, y_center <= 10^7
 * 3、randPoint 最多被调用 3 * 10^4 次
 * 链接：https://leetcode.cn/problems/generate-random-point-in-a-circle
 */
public class Q478 {

    public static void main(String[] args) {
        Q478 solution = new Q478(1.0, 0.0, 0.0);
        System.out.println(Arrays.toString(solution.randPoint()));//返回[-0.02493，-0.38077]
        System.out.println(Arrays.toString(solution.randPoint()));//返回[0.82314,0.38945]
        System.out.println(Arrays.toString(solution.randPoint()));//返回[0.36572,0.17248]
    }

    Random random;
    double xc, yc, r;

    public Q478(double radius, double x_center, double y_center) {
        random = new Random();
        xc = x_center;
        yc = y_center;
        r = radius;
    }

    // 拒绝采样法
    public double[] randPoint() {
        while (true) {
            double x = random.nextDouble() * (2 * r) - r;
            double y = random.nextDouble() * (2 * r) - r;
            if (x * x + y * y <= r * r) {
                return new double[]{xc + x, yc + y};
            }
        }
    }
}
