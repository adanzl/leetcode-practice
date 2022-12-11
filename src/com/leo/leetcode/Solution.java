package com.leo.leetcode;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

class Solution {
    public int[] maxPoints(int[][] grid, int[] queries) {
        int m = grid.length, n = grid[0].length;
        int nn = queries.length;
        boolean[][] g = new boolean[m][n];
        int[][] ans_ = new int[nn][];
        for (int i = 0; i < nn; i++)
            ans_[i] = new int[]{0, -1};
        int[] ans = new int[nn];
        int[][] qq = new int[nn][];
        for (int i = 0; i < nn; i++)
            qq[i] = new int[]{queries[i], i};
        List<int[]> Q = new ArrayList<>();
        Q.add(new int[]{0, 0});
        int[][] dirs = new int[][]{{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        for (int i = 0; i < nn; i++) {
            int idx = qq[i][1], val = qq[i][0];
            if (i > 0) ans_[i][0] = ans_[i - 1][0];
            ans_[i][1] = idx;
            List<int[]> q = Q;
            Q = new ArrayList<>();
            while (!q.isEmpty()) {
                List<int[]> t = q;
                q = new ArrayList<>();
                for (int[] ne : t) {
                    int nx = ne[0], ny = ne[1];
                    if (nx < 0 || ny < 0 || nx > m - 1 || ny > n - 1) continue;
                    if (!g[nx][ny]) continue;
                    if (grid[nx][ny] >= val) {
                        Q.add(new int[]{nx, ny});
                        continue;
                    }
                    g[nx][ny] = true;
                    ans_[i][0] += 1;
                    for (int[] d : dirs) {
                        q.add(new int[]{nx + d[0], ny + d[1]});
                    }
                }
            }
        }
        for (int[] a : ans_) {
            ans[a[1]] = a[0];
        }
        return ans;
    }

    public static void main(String[] args) {
        //
        System.out.println(new Q().func());
    }
}
