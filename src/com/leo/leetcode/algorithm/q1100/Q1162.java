package com.leo.leetcode.algorithm.q1100;

import com.leo.utils.TestCase;

import java.util.ArrayDeque;
import java.util.Queue;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 你现在手里有一份大小为 n x n 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。
 * 其中 0 代表海洋，1 代表陆地，请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的。
 * 如果网格上只有陆地或者海洋，请返回 -1。
 * 我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。
 * 提示：
 * 1、n == grid.length
 * 2、n == grid[i].length
 * 3、1 <= n <= 100
 * 4、grid[i][j] 不是 0 就是 1
 * 链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible
 */
public class Q1162 {
    public static void main(String[] args) {
        // -1
        System.out.println(new Q1162().maxDistance(stringToInt2dArray("[[0,0,0],[0,0,0],[0,0,0]]")));
        // -1
        System.out.println(new Q1162().maxDistance(stringToInt2dArray("[[1,1,1],[1,1,1],[1,1,1]]")));
        TestCase tc = new TestCase("resources/algorithm/q1100/Q1162/Case001.txt");
        // 161
        System.out.println(new Q1162().maxDistance(stringToInt2dArray(tc.getData(0))));
        // 2
        System.out.println(new Q1162().maxDistance(stringToInt2dArray("[[1,0,1],[0,0,0],[1,0,1]]")));
        // 4
        System.out.println(new Q1162().maxDistance(stringToInt2dArray("[[1,0,0],[0,0,0],[0,0,0]]")));
    }

    public int maxDistance(int[][] grid) {
        int ret = 1, w = grid.length, h = grid[0].length, size = w * h;
        int[][] dis = new int[w][h];
        Queue<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                if (grid[i][j] == 1) {
                    q.add(new int[]{i, j});
                    size--;
                    dis[i][j] = -1;
                }
            }
        }
        if (size == 0 || q.isEmpty()) return -1;
        while (size > 0) {
            int len = q.size();
            while (len-- > 0 && !q.isEmpty()) {
                int[] p = q.poll();
                if (p[0] > 0 && dis[p[0] - 1][p[1]] == 0) {
                    dis[p[0] - 1][p[1]] = ret;
                    q.add(new int[]{p[0] - 1, p[1]});
                    size--;
                }
                if (p[0] < w - 1 && dis[p[0] + 1][p[1]] == 0) {
                    dis[p[0] + 1][p[1]] = ret;
                    q.add(new int[]{p[0] + 1, p[1]});
                    size--;
                }
                if (p[1] > 0 && dis[p[0]][p[1] - 1] == 0) {
                    dis[p[0]][p[1] - 1] = ret;
                    q.add(new int[]{p[0], p[1] - 1});
                    size--;
                }
                if (p[1] < h - 1 && dis[p[0]][p[1] + 1] == 0) {
                    dis[p[0]][p[1] + 1] = ret;
                    q.add(new int[]{p[0], p[1] + 1});
                    size--;
                }
            }
            ret++;
        }
        return ret - 1;
    }

}
