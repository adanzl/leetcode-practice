package com.leo.leetcode.algorithm.q2200;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个二维整数数组 rectangles ，其中 rectangles[i] = [li, hi] 表示第 i 个矩形长为 li 高为 hi 。
 * 给你一个二维整数数组 points ，其中 points[j] = [xj, yj] 是坐标为 (xj, yj) 的一个点。
 * 第 i 个矩形的 左下角 在 (0, 0) 处，右上角 在 (li, hi) 。
 * 请你返回一个整数数组 count ，长度为 points.length，其中 count[j]是 包含 第 j 个点的矩形数目。
 * 如果 0 <= xj <= li 且 0 <= yj <= hi ，那么我们说第 i 个矩形包含第 j 个点。如果一个点刚好在矩形的 边上 ，这个点也被视为被矩形包含。
 * 提示：
 * 1、1 <= rectangles.length, points.length <= 5 * 10^4
 * 2、rectangles[i].length == points[j].length == 2
 * 3、1 <= li, xj <= 10^9
 * 4、1 <= hi, yj <= 100
 * 5、所有 rectangles 互不相同 。
 * 6、所有 points 互不相同 。
 * 链接：https://leetcode-cn.com/problems/count-number-of-rectangles-containing-each-point
 */
public class Q2250 {

    public static void main(String[] args) {
        // [2, 1]
        System.out.println(Arrays.toString(new Q2250().countRectangles(
                stringToInt2dArray("[[1,2],[2,3],[2,5]]"),
                stringToInt2dArray("[[2,1],[1,4]]"))));
        // [1, 3]
        System.out.println(Arrays.toString(new Q2250().countRectangles(
                stringToInt2dArray("[[1,1],[2,2],[3,3]]"),
                stringToInt2dArray("[[1,3],[1,1]]"))));
    }

    public int[] countRectangles(int[][] rectangles, int[][] points) {
        List<List<Integer>> yList = new ArrayList<>(100);
        int yMax = 0;
        for (int i = 0; i <= 100; i++) yList.add(new ArrayList<>());
        for (int[] rectangle : rectangles) {
            yList.get(rectangle[1]).add(rectangle[0]);
            yMax = Math.max(yMax, rectangle[1]);
        }
        for (int i = 0; i <= yMax; i++) yList.get(i).sort(Comparator.naturalOrder());
        int[] ret = new int[points.length];
        for (int i = 0; i < points.length; i++) {
            int[] point = points[i];
            for (int j = point[1]; j <= yMax; j++) {
                List<Integer> xList = yList.get(j);
                int l = 0, r = xList.size() - 1;
                while (l <= r) {
                    int mid = l + (r - l) / 2;
                    if (xList.get(mid) < point[0]) l = mid + 1;
                    else r = mid - 1;
                }
                ret[i] += xList.size() - l;
            }
        }
        return ret;
    }

}
