package com.leo.leetcode.algorithm.q2800;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

import static com.leo.utils.LCUtil.stringToListListInt;

/**
 * 给你一个下标从 0 开始、大小为 n x n 的二维矩阵 grid ，其中 (r, c) 表示：
 * 1、如果 grid[r][c] = 1 ，则表示一个存在小偷的单元格
 * 2、如果 grid[r][c] = 0 ，则表示一个空单元格
 * 你最开始位于单元格 (0, 0) 。在一步移动中，你可以移动到矩阵中的任一相邻单元格，包括存在小偷的单元格。
 * 矩阵中路径的 安全系数 定义为：从路径中任一单元格到矩阵中任一小偷所在单元格的 最小 曼哈顿距离。
 * 返回所有通向单元格 (n - 1, n - 1) 的路径中的 最大安全系数 。
 * 单元格 (r, c) 的某个 相邻 单元格，是指在矩阵中存在的 (r, c + 1)、(r, c - 1)、(r + 1, c) 和 (r - 1, c) 之一。
 * 两个单元格 (a, b) 和 (x, y) 之间的 曼哈顿距离 等于 | a - x | + | b - y | ，其中 |val| 表示 val 的绝对值。
 * 提示：
 * 1、1 <= grid.length == n <= 400
 * 2、grid[i].length == n
 * 3、grid[i][j] 为 0 或 1
 * 4、grid 至少存在一个小偷
 * 链接：https://leetcode.cn/problems/find-the-safest-path-in-a-grid/
 */
public class Q2812 {

    public static void main(String[] args) {

        // 0
        System.out.println(new Q2812().maximumSafenessFactor(stringToListListInt("[[1]]")));
        // 2
        System.out.println(new Q2812().maximumSafenessFactor(stringToListListInt("[[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]")));
        // 0
        System.out.println(new Q2812().maximumSafenessFactor(stringToListListInt("[[1, 0, 0], [0, 0, 0], [0, 0, 1]]")));
    }

    public int maximumSafenessFactor(List<List<Integer>> grid) {
        int n = grid.size();
        int[][] dis = new int[n][n];
        List<Integer> qx = new ArrayList<>(), qy = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dis[i][j] = -1;
                if (grid.get(i).get(j) == 1) {
                    qx.add(i);
                    qy.add(j);
                    dis[i][j] = 0;
                }
            }
        }
        int[][] dirs = new int[][]{{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        for (int d = 0; d < n * n; d++) {
            List<Integer> nqx = new ArrayList<>(), nqy = new ArrayList<>();
            for (int i = 0; i < qx.size(); i++) {
                for (int[] dir : dirs) {
                    int nx = qx.get(i) + dir[0], ny = qy.get(i) + dir[1];
                    if (nx < 0 || ny < 0 || nx >= n || ny >= n || dis[nx][ny] != -1) continue;
                    nqx.add(nx);
                    nqy.add(ny);
                    dis[nx][ny] = d + 1;
                }
            }
            qx = nqx;
            qy = nqy;
        }
        boolean[][] vis = new boolean[n][n];
        int[][] ans = new int[n][n];
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(o -> -o[0]));
        q.add(new int[]{dis[0][0], 0, 0});
        while (!q.isEmpty()) {
            int[] p = q.poll();
            if (vis[p[1]][p[2]]) continue;
            vis[p[1]][p[2]] = true;
            for (int[] dir : dirs) {
                int nx = p[1] + dir[0], ny = p[2] + dir[1];
                if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
                int nv = Math.min(p[0], dis[nx][ny]);
                if (nv > ans[nx][ny]) {
                    ans[nx][ny] = nv;
                    q.add(new int[]{nv, nx, ny});
                }
            }
        }
        return ans[n - 1][n - 1];
    }
}
