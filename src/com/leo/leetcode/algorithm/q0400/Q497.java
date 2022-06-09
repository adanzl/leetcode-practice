package com.leo.leetcode.algorithm.q0400;

import java.util.Arrays;
import java.util.Random;
import java.util.TreeMap;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给定一个由非重叠的轴对齐矩形的数组 rects ，其中 rects[i] = [ai, bi, xi, yi] 表示 (ai, bi) 是第 i 个矩形的左下角点，
 * (xi, yi) 是第 i 个矩形的右上角点。设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。
 * 所有满足要求的点必须等概率被返回。
 * 在给定的矩形覆盖的空间内的任何整数点都有可能被返回。
 * 请注意 ，整数点是具有整数坐标的点。
 * 实现 Solution 类:
 * 1、Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。
 * 2、int[] pick() 返回一个随机的整数点 [u, v] 在给定的矩形所覆盖的空间内。
 * 提示：
 * 1、1 <= rects.length <= 100
 * 2、rects[i].length == 4
 * 3、-10^9 <= ai < xi <= 10^9
 * 4、-10^9 <= bi < yi <= 10^9
 * 5、xi - ai <= 2000
 * 6、yi - bi <= 2000
 * 7、所有的矩形不重叠。
 * 8、pick 最多被调用 10^4 次。
 * 链接：https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles
 */
public class Q497 {

    public static void main(String[] args) {
        Solution solution = new Solution(stringToInt2dArray("[[-2,-2,1,1],[2,2,4,6]]"));
        System.out.println(Arrays.toString(solution.pick())); // 返回 [1, -2]
        System.out.println(Arrays.toString(solution.pick())); // 返回 [1, -1]
        System.out.println(Arrays.toString(solution.pick())); // 返回 [-1, -2]
        System.out.println(Arrays.toString(solution.pick())); // 返回 [-2, -2]
        System.out.println(Arrays.toString(solution.pick())); // 返回 [0, 0]
    }

    static class Solution {

        TreeMap<Integer, Integer> tMap;
        int total = 0;
        Random random = new Random();
        int[][] rects;

        public Solution(int[][] rects) {
            tMap = new TreeMap<>();
            for (int i = 0; i < rects.length; i++) {
                int a = rects[i][0], b = rects[i][1], x = rects[i][2], y = rects[i][3];
                int area = Math.abs(x - a + 1) * Math.abs(y - b + 1);
                total += area;
                tMap.put(total, i);
            }
            this.rects = rects;
        }

        public int[] pick() {
            int r = random.nextInt(total + 1);
            int[] rect = rects[tMap.ceilingEntry(r).getValue()];
            int a = rect[0], b = rect[1], x = rect[2], y = rect[3];
            return new int[]{a + random.nextInt(x - a + 1), b + random.nextInt(y - b + 1)};
        }
    }

}
