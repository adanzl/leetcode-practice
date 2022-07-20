package com.leo.leetcode.algorithm.q1200;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 m 行 n  列的二维网格  grid  和一个整数  k。你需要将  grid  迁移  k  次。
 * 每次「迁移」操作将会引发下述活动：
 * 1、位于 grid[i][j]  的元素将会移动到  grid[i][j + 1]。
 * 2、位于  grid[i][n  - 1] 的元素将会移动到  grid[i + 1][0]。
 * 3、位于 grid[m  - 1][n - 1]  的元素将会移动到  grid[0][0]。
 * 请你返回  k 次迁移操作后最终得到的 二维网格。
 * 提示：
 * 1、m ==  grid.length
 * 2、n ==  grid[i].length
 * 3、1 <= m <= 50
 * 4、1 <= n <= 50
 * 5、-1000 <= grid[i][j] <= 1000
 * 6、0 <= k <= 100
 * 链接：https://leetcode.cn/problems/shift-2d-grid
 */
public class Q1260 {

    public static void main(String[] args) {
        // [[9,1,2],[3,4,5],[6,7,8]]
        System.out.println(new Q1260().shiftGrid(stringToInt2dArray("[[1,2,3],[4,5,6],[7,8,9]]"), 1));
        // [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
        System.out.println(new Q1260().shiftGrid(stringToInt2dArray("[[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]"), 4));
        // [[1,2,3],[4,5,6],[7,8,9]]
        System.out.println(new Q1260().shiftGrid(stringToInt2dArray("[[1,2,3],[4,5,6],[7,8,9]]"), 9));
    }

    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        List<List<Integer>> ret = new ArrayList<>();
        for (int[] l : grid) {
            List<Integer> line = new ArrayList<>();
            for (int i = 0; i < l.length; i++) line.add(0);
            ret.add(line);
        }
        int m = grid.length, n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int next = i * n + j + k, x = (next / n) % m, y = next % n;
                ret.get(x).set(y, grid[i][j]);
            }
        }

        return ret;
    }
}
