package com.leo.leetcode.algorithm.q1600;

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。
 * 跳蚤跳跃的规则如下：
 * 它可以 往前 跳恰好 a 个位置（即往右跳）。
 * 它可以 往后 跳恰好 b 个位置（即往左跳）。
 * 它不能 连续 往后跳 2 次。
 * 它不能跳到任何 forbidden 数组中的位置。
 * 跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。
 * 给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x ，请你返回跳蚤到家的最少跳跃次数。
 * 如果没有恰好到达 x 的可行方案，请你返回 -1 。
 * 提示：
 * 1、1 <= forbidden.length <= 1000
 * 2、1 <= a, b, forbidden[i] <= 2000
 * 3、0 <= x <= 2000
 * 4、forbidden 中所有位置互不相同。
 * 5、位置 x 不在 forbidden 中。
 * <p>
 * 链接：https://leetcode-cn.com/problems/minimum-jumps-to-reach-home
 */
public class Q1654 {

    public static void main(String[] args) {
        // 1548
        System.out.println(new Q1654().minimumJumps(stringToIntegerArray("[549, 693, 456, 1814, 1609]"),
                748, 889, 545));
        // 121
        System.out.println(new Q1654().minimumJumps(stringToIntegerArray("[162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]"),
                29, 98, 80));
        // 3
        System.out.println(new Q1654().minimumJumps(stringToIntegerArray("[14,4,18,1,15]"), 3, 15, 9));
        // -1
        System.out.println(new Q1654().minimumJumps(stringToIntegerArray("[8,3,16,6,12,20]"), 15, 13, 11));
        // 2
        System.out.println(new Q1654().minimumJumps(stringToIntegerArray("[1,6,2,14,5,17,4]"), 16, 9, 7));
    }

    public int minimumJumps(int[] forbidden, int a, int b, int x) {
        // 由于我们可以超出家的位置，最短路算法可能超时，故我们需要减小搜索范围。
        // 可以证明，一定可以在 [0, max(f + a + b, x + b)] 的下标范围内找到最优解，其中 f 是最远的禁止点的坐标。
        // 因为 f,a,b,x <= 2000，故搜索范围不会超过 6000。
        final int LIMIT = 2000 + a + b;
        boolean[][] visited = new boolean[LIMIT + 1][2];
        int ret = 0;
        Set<Integer> fSet = new HashSet<>(forbidden.length); // 0: r, 1: l
        for (int f : forbidden) fSet.add(f);
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0});
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0 && !q.isEmpty()) {
                int[] p = q.poll();
                int point = p[0], back = p[1];
                if (point == x) return ret;
                int rNext = point + a, lNext = point - b;
                if (rNext <= LIMIT && !visited[rNext][0] && !fSet.contains(rNext)) {
                    q.add(new int[]{rNext, 0});
                    visited[rNext][0] = true;
                    visited[rNext][1] = true;
                }
                if (lNext >= 0 && back < 1 && !visited[lNext][1] && !fSet.contains(lNext)) {
                    q.add(new int[]{lNext, 1});
                    visited[lNext][1] = true;
                }
            }
            ret++;
        }
        return -1;
    }
}
