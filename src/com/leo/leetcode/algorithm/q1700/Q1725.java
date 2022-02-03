package com.leo.leetcode.algorithm.q1700;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个数组 rectangles ，其中 rectangles[i] = [li, wi] 表示第 i 个矩形的长度为 li 、宽度为 wi 。
 * 如果存在 k 同时满足 k <= li 和 k <= wi ，就可以将第 i 个矩形切成边长为 k 的正方形。例如，矩形 [4,6] 可以切成边长最大为 4 的正方形。
 * 设 maxLen 为可以从矩形数组 rectangles 切分得到的 最大正方形 的边长。
 * 请你统计有多少个矩形能够切出边长为 maxLen 的正方形，并返回矩形 数目 。
 * 提示：
 * 1、1 <= rectangles.length <= 1000
 * 2、rectangles[i].length == 2
 * 3、1 <= li, wi <= 10^9
 * 4、li != wi
 * <p>
 * 链接：https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square
 */
public class Q1725 {
    public static void main(String[] args) {
        // 3
        System.out.println(new Q1725().countGoodRectangles(stringToInt2dArray("[[5,8],[3,9],[5,12],[16,5]]")));
        // 3
        System.out.println(new Q1725().countGoodRectangles(stringToInt2dArray("[[2,3],[3,7],[4,3],[3,7]]")));
    }

    public int countGoodRectangles(int[][] rectangles) {
        int ret = 0, len = 0;
        for (int[] rect : rectangles) {
            int l = Math.min(rect[0], rect[1]);
            if (l == len) {
                ret++;
            } else if (l > len) {
                ret = 1;
                len = l;
            }
        }
        return ret;
    }
}
