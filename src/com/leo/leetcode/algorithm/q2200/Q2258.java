package com.leo.leetcode.algorithm.q2200;

import java.util.ArrayDeque;
import java.util.Queue;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个下标从 0 开始大小为 m x n 的二维整数数组 grid ，它表示一个网格图。每个格子为下面 3 个值之一：
 * 1、0 表示草地。
 * 2、1 表示着火的格子。
 * 3、2 表示一座墙，你跟火都不能通过这个格子。
 * 一开始你在最左上角的格子 (0, 0) ，你想要到达最右下角的安全屋格子 (m - 1, n - 1) 。每一分钟，你可以移动到 相邻 的草地格子。
 * 每次你移动 之后 ，着火的格子会扩散到所有不是墙的 相邻 格子。
 * 请你返回你在初始位置可以停留的 最多 分钟数，且停留完这段时间后你还能安全到达安全屋。如果无法实现，请你返回 -1 。
 * 如果不管你在初始位置停留多久，你 总是 能到达安全屋，请你返回 10^9 。
 * 注意，如果你到达安全屋后，火马上到了安全屋，这视为你能够安全到达安全屋。
 * 如果两个格子有共同边，那么它们为 相邻 格子。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、2 <= m, n <= 300
 * 4、4 <= m * n <= 2 * 10^4
 * 5、grid[i][j] 是 0 ，1 或者 2 。
 * 6、grid[0][0] == grid[m - 1][n - 1] == 0
 * 链接：https://leetcode-cn.com/problems/escape-the-spreading-fire
 */
public class Q2258 {

    public static void main(String[] args) {
        // 13
        System.out.println(new Q2258().maximumMinutes(stringToInt2dArray("[[0,2,1,0,0,0,0],[0,2,2,2,2,2,0],[0,2,0,0,0,0,0],[0,2,0,2,2,2,2],[0,2,0,0,0,0,0],[0,2,2,2,2,2,0],[0,2,0,0,0,0,0],[0,2,0,2,2,2,2],[0,0,0,0,0,0,0]]")));
        // 0
        System.out.println(new Q2258().maximumMinutes(stringToInt2dArray("[[0,2,0,0,1],[0,2,0,2,2],[0,2,0,0,0],[0,0,2,2,0],[0,0,0,0,0]]")));
        // 1000000000
        System.out.println(new Q2258().maximumMinutes(stringToInt2dArray("[[0,0,0],[2,2,0],[1,2,0]]")));
        // 3
        System.out.println(new Q2258().maximumMinutes(stringToInt2dArray("[[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]")));
        // -1
        System.out.println(new Q2258().maximumMinutes(stringToInt2dArray("[[0,0,0,0],[0,1,2,0],[0,2,0,0]]")));
    }

    public int maximumMinutes(int[][] grid) {
        int m = grid.length, n = grid[0].length, ret = -1, INF = Integer.MAX_VALUE;
        int[][] fireMatrix = new int[m][n];
        int count = 0;
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) q.add(new int[]{i, j});
                else fireMatrix[i][j] = INF;
            }
        }
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0 && !q.isEmpty()) {
                int[] p = q.poll();
                if (p[0] < 0 || p[1] < 0 || p[0] >= m || p[1] >= n || grid[p[0]][p[1]] == 2 || visited[p[0]][p[1]])
                    continue;
                fireMatrix[p[0]][p[1]] = count;
                visited[p[0]][p[1]] = true;
                q.add(new int[]{p[0] - 1, p[1]});
                q.add(new int[]{p[0] + 1, p[1]});
                q.add(new int[]{p[0], p[1] - 1});
                q.add(new int[]{p[0], p[1] + 1});
            }
            count++;
        }
        int l = 0, r = 1_000_000_000;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (check(mid, fireMatrix, grid)) {
                ret = mid;
                l = mid + 1;
            } else r = mid - 1;
        }
        return ret;
    }

    boolean check(int base, int[][] fireMatrix, int[][] grid) {
        if (fireMatrix[0][0] <= base) return false;
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0});
        int m = grid.length, n = grid[0].length, step = 0;
        boolean[][] visited = new boolean[m][n];
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0 && !q.isEmpty()) {
                int[] p = q.poll();
                if (p[0] < 0 || p[1] < 0 || p[0] >= m || p[1] >= n || grid[p[0]][p[1]] == 2 || visited[p[0]][p[1]])
                    continue;
                if (step + base > fireMatrix[p[0]][p[1]]) continue;
                if ((p[0] != m - 1 || p[1] != n - 1) && step + base == fireMatrix[p[0]][p[1]]) continue;
                visited[p[0]][p[1]] = true;
                q.add(new int[]{p[0] - 1, p[1]});
                q.add(new int[]{p[0] + 1, p[1]});
                q.add(new int[]{p[0], p[1] - 1});
                q.add(new int[]{p[0], p[1] + 1});
            }
            step++;
        }
        return visited[m - 1][n - 1];
    }
}
