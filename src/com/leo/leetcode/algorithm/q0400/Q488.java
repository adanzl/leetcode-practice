package com.leo.leetcode.algorithm.q0400;

import java.util.*;

/**
 * 你正在参与祖玛游戏的一个变种。
 * 在这个祖玛游戏变体中，桌面上有 一排 彩球，每个球的颜色可能是：红色 'R'、黄色 'Y'、蓝色 'B'、绿色 'G' 或白色 'W' 。你的手中也有一些彩球。
 * 你的目标是 清空 桌面上所有的球。每一回合：
 * 1、从你手上的彩球中选出 任意一颗 ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。
 * 2、接着，如果有出现 三个或者三个以上 且 颜色相同 的球相连的话，就把它们移除掉。
 * 3、如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。
 * 4、如果桌面上所有球都被移除，则认为你赢得本场游戏。
 * 5、重复这个过程，直到你赢了游戏或者手中没有更多的球。
 * 给你一个字符串 board ，表示桌面上最开始的那排球。另给你一个字符串 hand ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，计算并返回所需的 最少 球数。如果不能移除桌上所有的球，返回 -1 。
 * 提示：
 * 1、1 <= board.length <= 16
 * 2、1 <= hand.length <= 5
 * 3、board 和 hand 由字符 'R'、'Y'、'B'、'G' 和 'W' 组成
 * 4、桌面上一开始的球中，不会有三个及三个以上颜色相同且连着的球
 * 链接：https://leetcode.cn/problems/zuma-game
 */
public class Q488 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q488().findMinStep("WR", "WWRR"));
        // -1
        System.out.println(new Q488().findMinStep("RRGGBBYYWWRRGGBB", "RGBYW"));
        // -1
        System.out.println(new Q488().findMinStep("BRWGWYY", "YGBWY"));
        // -1
        System.out.println(new Q488().findMinStep("WRRBBW", "RB"));
        // 2
        System.out.println(new Q488().findMinStep("WWRRBBWW", "WRBRW"));
        // 2
        System.out.println(new Q488().findMinStep("G", "GGGGG"));
        // 3
        System.out.println(new Q488().findMinStep("RBYYBBRRB", "YRBGB"));
    }

    public int findMinStep(String board, String hand) {
        char[] hands = hand.toCharArray();
        int ret = 0;
        Arrays.sort(hands);
        Set<String> signs = new HashSet<>();
        Queue<char[][]> queue = new ArrayDeque<>();
        queue.offer(new char[][]{board.toCharArray(), hands});
        while (!queue.isEmpty()) {
            ret++;
            int size = queue.size();
            while (size-- > 0 && !queue.isEmpty()) {
                char[][] cur = queue.poll();
                char[] curHand = cur[1], curBoard = cur[0];
                for (int i = 0; i < curHand.length; i++) {
                    if (i > 0 && curHand[i] == curHand[i - 1]) continue; // 当前球的颜色和上一个球的颜色相同
                    char h = curHand[i];
                    char[] newHand = new char[curHand.length - 1];
                    System.arraycopy(curHand, 0, newHand, 0, i);
                    System.arraycopy(curHand, i + 1, newHand, i, curHand.length - i - 1);
                    for (int j = 0; j <= curBoard.length; j++) {
                        if (j > 0 && curBoard[j - 1] == h) continue; // 只在连续相同颜色的球的开头位置插入新球
                        boolean choose = j < curBoard.length && curBoard[j] == h; // 当前球颜色与后面的球的颜色相同
                        // 当前后颜色相同且与当前颜色不同时候放置球
                        if (j > 0 && j < curBoard.length && curBoard[j - 1] == curBoard[j] && curBoard[j - 1] != h)
                            choose = true;
                        if (!choose) continue;
                        char[] newBoard = new char[curBoard.length + 1];
                        newBoard[j] = h;
                        System.arraycopy(curBoard, 0, newBoard, 0, j);
                        System.arraycopy(curBoard, j, newBoard, j + 1, curBoard.length - j);
                        int p = j, len, rLimit = newBoard.length;
                        do {
                            int l = p, r = p;
                            while (l >= 0 && newBoard[p] == newBoard[l]) l--;
                            while (r < rLimit && newBoard[p] == newBoard[r]) r++;
                            len = r - l - 1;
                            if (len >= 3) {
                                System.arraycopy(newBoard, r, newBoard, l + 1, rLimit - r);
                                rLimit -= len;
                                if (rLimit == 0) return ret;
                                p = l + 1;
                            }
                        } while (len >= 3);
                        newBoard = Arrays.copyOf(newBoard, rLimit);
                        String sign = new String(newBoard) + "_" + new String(newHand);
                        if (!signs.contains(sign)) {
                            signs.add(sign);
                            queue.offer(new char[][]{newBoard, newHand});
                        }
                    }
                }
            }
        }
        return -1;
    }
}
