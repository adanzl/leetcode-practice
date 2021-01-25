package com.leo.leetcode.algorithm.q1000;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个由一些多米诺骨牌组成的列表 dominoes。
 * 如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
 * 形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。
 * 在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。
 * 提示：
 * 1、1 <= dominoes.length <= 40000
 * 2、1 <= dominoes[i][j] <= 9
 * <p>
 * 链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs
 */
public class Q1128 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q1128().numEquivDominoPairs(stringToInt2dArray("[[1,2],[1,2],[1,1],[1,2],[2,2]]")));
        // 1
        System.out.println(new Q1128().numEquivDominoPairs(stringToInt2dArray("[[1,2],[2,1],[3,4],[5,6]]")));
        // 10
        System.out.println(new Q1128().numEquivDominoPairs(stringToInt2dArray("[[1,2],[2,1],[2,1],[2,1],[2,1]]")));
    }

    public int numEquivDominoPairs(int[][] dominoes) {
        int ret = 0;
        int[] map = new int[81];
        for (int[] domino : dominoes) {
            int x = domino[0] - 1, y = domino[1] - 1;
            ret += map[x * 9 + y]++;
            if (x != y) ++map[y * 9 + x];
        }
        return ret;
    }
}
