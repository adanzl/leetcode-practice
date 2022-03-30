package com.leo.leetcode.algorithm.q1500;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。
 * Rick 有 n 个空的篮子，第 i 个篮子的位置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。
 * 已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。
 * 给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。
 * 提示：
 * 1、n == position.length
 * 2、2 <= n <= 10^5
 * 3、1 <= position[i] <= 10^9
 * 4、所有 position 中的整数 互不相同 。
 * 5、2 <= m <= position.length
 * 链接：https://leetcode-cn.com/problems/magnetic-force-between-two-balls
 */
public class Q1552 {

    public static void main(String[] args) {
        // 12 1_000_000_000
        System.out.println(new Q1552().maxDistance(stringToIntegerArray("[94,95,37,30,67,7,5,44,26,55,42,28,97,19,100,74,13,88,18]"), 7));
        // 3
        System.out.println(new Q1552().maxDistance(stringToIntegerArray("[1,2,3,4,7]"), 3));
        // 999999999
        System.out.println(new Q1552().maxDistance(stringToIntegerArray("[5,4,3,2,1,1000000000]"), 2));
        // 4
        System.out.println(new Q1552().maxDistance(stringToIntegerArray("[5,4,3,2,1,1000000000]"), 3));
    }

    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);
        int l = 1, r = 1_000_000_000, n = position.length, ret = 0;
        while (l <= r) {
            int mid = l + ((r - l) >> 1), count = 1;
            for (int p1 = 0, p2 = 1; p2 < n; p2++) {
                if (position[p2] - position[p1] >= mid) {
                    p1 = p2;
                    count++;
                }
            }
            if (count < m) {
                ret = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return ret - 1;
    }
}
