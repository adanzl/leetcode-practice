package com.leo.leetcode.algorithm.q0400;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 有一个 m × n 的长方形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。
 * 这个岛被分割成一个个方格网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度 。
 * 岛上雨水较多，如果相邻小区的高度 小于或等于 当前小区的高度，雨水可以直接向北、南、东、西流向相邻小区。水可以从海洋附近的任何细胞流入海洋。
 * 返回 网格坐标 result 的 2D列表 ，其中 result[i] = [ri, ci] 表示雨水可以从单元格 (ri, ci) 流向 太平洋和大西洋 。
 * 提示：
 * 1、m == heights.length
 * 2、n == heights[r].length
 * 3、1 <= m, n <= 200
 * 4、0 <= heights[r][c] <= 10^5
 * 链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow
 */
public class Q417 {

    public static void main(String[] args) {
        // [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,2],[1,3],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5]]
        System.out.println(new Q417().pacificAtlantic(stringToInt2dArray("[[3,3,3,3,3,3],[3,0,3,3,0,3],[3,3,3,3,3,3]]")));
        // [[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
        System.out.println(new Q417().pacificAtlantic(stringToInt2dArray("[[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]")));
        // [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        System.out.println(new Q417().pacificAtlantic(stringToInt2dArray("[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]")));
        // [[0,0],[0,1],[1,0],[1,1]]
        System.out.println(new Q417().pacificAtlantic(stringToInt2dArray("[[2,1],[1,2]]")));
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> ret = new ArrayList<>();
        int[][] mark = new int[heights.length][heights[0].length];
        for (int i = 0; i < heights[0].length; i++) {
            expand(heights, 0, i, mark, heights[0][i], new boolean[heights.length][heights[0].length], 1);
            expand(heights, heights.length - 1, i, mark, heights[heights.length - 1][i], new boolean[heights.length][heights[0].length], 2);
        }
        for (int i = 0; i < heights.length; i++) {
            expand(heights, i, 0, mark, heights[i][0], new boolean[heights.length][heights[0].length], 1);
            expand(heights, i, heights[0].length - 1, mark, heights[i][heights[0].length - 1], new boolean[heights.length][heights[0].length], 2);
        }
        for (int i = 0; i < mark.length; i++) {
            for (int j = 0; j < mark[0].length; j++) {
                if (mark[i][j] == 3) ret.add(Arrays.asList(i, j));
            }
        }
        return ret;
    }

    void expand(int[][] heights, int x, int y, int[][] mark, int v, boolean[][] visited, int mask) {
        if (x < 0 || x > heights.length - 1 || y < 0 || y > heights[0].length - 1 || visited[x][y] || heights[x][y] < v)
            return;
        visited[x][y] = true;
        mark[x][y] |= mask;
        expand(heights, x - 1, y, mark, heights[x][y], visited, mask);
        expand(heights, x + 1, y, mark, heights[x][y], visited, mask);
        expand(heights, x, y - 1, mark, heights[x][y], visited, mask);
        expand(heights, x, y + 1, mark, heights[x][y], visited, mask);
    }
}
