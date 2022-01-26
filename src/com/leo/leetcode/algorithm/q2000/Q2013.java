package com.leo.leetcode.algorithm.q2000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法：
 * 1、添加 一个在数据流中的新点到某个数据结构中。可以添加 重复 的点，并会视作不同的点进行处理。
 * 2、给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 面积为正 的 轴对齐正方形 ，统计 满足该要求的方案数目。
 * 轴对齐正方形 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。
 * 实现 DetectSquares 类：
 * 1、DetectSquares() 使用空数据结构初始化对象
 * 2、void add(int[] point) 向数据结构添加一个新的点 point = [x, y]
 * 3、int count(int[] point) 统计按上述方式与点 point = [x, y] 共同构造 轴对齐正方形 的方案数。
 * <p>
 * 链接：https://leetcode-cn.com/problems/detect-squares
 */
public class Q2013 {

    public static void main(String[] args) {
        DetectSquares obj = new DetectSquares();
        obj.add(stringToIntegerArray("[3, 10]"));
        obj.add(stringToIntegerArray("[11, 2]"));
        obj.add(stringToIntegerArray("[3, 2]"));
        System.out.println(obj.count(stringToIntegerArray("[11, 10]"))); // 1
        System.out.println(obj.count(stringToIntegerArray("[14, 8]")));  // 0
        obj.add(stringToIntegerArray("[11, 2]"));    // 允许添加重复的点。
        System.out.println(obj.count(stringToIntegerArray("[11, 10]"))); // 2
    }

    static class DetectSquares {

        private final int SIZE = 1001;

        private final int[][] map = new int[SIZE][SIZE];

        public void add(int[] point) {
            ++map[point[0]][point[1]];
        }

        public int count(int[] point) {
            int x = point[0], y = point[1], ret = 0;
            for (int i = 0; i < SIZE; i++) {
                if (map[x][i] == 0 || i == y) continue;
                int len = i - y;
                if (exists(x + len, y) && exists(x + len, y + len)) {
                    ret += map[x][i] * map[x + len][y] * map[x + len][y + len];
                }
                if (exists(x - len, y) && exists(x - len, y + len)) {
                    ret += map[x][i] * map[x - len][y] * map[x - len][y + len];
                }
            }
            return ret;
        }

        private boolean exists(int x, int y) {
            if (x < 0 || y < 0 || x >= SIZE || y >= SIZE) return false;
            return this.map[x][y] > 0;
        }
    }
}
