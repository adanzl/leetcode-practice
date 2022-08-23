package com.leo.leetcode.algorithm.q0700;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 一个 n x n 的二维网络 board 仅由 0 和 1 组成 。每次移动，你能任意交换两列或是两行的位置。
 * 返回 将这个矩阵变为 “棋盘” 所需的最小移动次数 。如果不存在可行的变换，输出 -1。
 * “棋盘” 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。
 * 提示：
 * 1、n == board.length
 * 2、n == board[i].length
 * 3、2 <= n <= 30
 * 4、board[i][j] 将只包含 0或 1
 * 链接：https://leetcode.cn/problems/transform-to-chessboard
 */
public class Q782 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q782().movesToChessboard(stringToInt2dArray("[[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]")));
        // 0
        System.out.println(new Q782().movesToChessboard(stringToInt2dArray("[[0, 1], [1, 0]]")));
        // -1
        System.out.println(new Q782().movesToChessboard(stringToInt2dArray("[[1, 0], [1, 0]]")));
    }

    int n = 0, INF = 0x3f3f3f3f;

    int getCnt(int a, int b) {
        int c1 = 0, c2 = 0;
        for (int i = 0; i < n; i++) {
            c1 += ((a >> i) & 1);
            c2 += ((b >> i) & 1);
        }
        return c1 != c2 ? INF : Integer.bitCount(a ^ b) / 2;
    }

    public int movesToChessboard(int[][] g) {
        n = g.length;
        Set<Integer> r = new HashSet<>(), c = new HashSet<>();
        for (int i = 0; i < n; i++) {
            int m1 = 0, m2 = 0;
            for (int j = 0; j < n; j++) {
                if (g[i][j] == 1) m1 |= (1 << j);
                if (g[j][i] == 1) m2 |= (1 << j);
            }
            r.add(m1);
            c.add(m2);
        }
        if (r.size() != 2 || c.size() != 2) return -1;
        List<Integer> l1 = new ArrayList<>(r), l2 = new ArrayList<>(c);
        int r1 = l1.get(0), r2 = l1.get(1), c1 = l2.get(0), c2 = l2.get(1), mask = (1 << n) - 1;
        if ((r1 ^ r2) != mask || (c1 ^ c2) != mask) return -1;
        int t = 0;
        for (int i = 0; i < n; i += 2) t += (1 << i); // 0101 101
        int ans = Math.min(getCnt(r1, t), getCnt(r2, t)) + Math.min(getCnt(c1, t), getCnt(c2, t));
        return ans >= INF ? -1 : ans;
    }

}
