package com.leo.leetcode.algorithm.q2200;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * Alice 和 Bob 是一场射箭比赛中的对手。比赛规则如下：
 * 1、Alice 先射 numArrows 支箭，然后 Bob 也射 numArrows 支箭。
 * 2、分数按下述规则计算：
 * 1）、箭靶有若干整数计分区域，范围从 0 到 11 （含 0 和 11）。
 * 2）、箭靶上每个区域都对应一个得分 k（范围是 0 到 11），Alice 和 Bob 分别在得分 k 区域射中 ak 和 bk 支箭。如果 ak >= bk ，那么 Alice 得 k 分。如果 ak < bk ，则 Bob 得 k 分
 * 3）如果 ak == bk == 0 ，那么无人得到 k 分。
 * 3、例如，Alice 和 Bob 都向计分为 11 的区域射 2 支箭，那么 Alice 得 11 分。如果 Alice 向计分为 11 的区域射 0 支箭，但 Bob 向同一个区域射 2 支箭，那么 Bob 得 11 分。
 * 给你整数 numArrows 和一个长度为 12 的整数数组 aliceArrows ，该数组表示 Alice 射中 0 到 11 每个计分区域的箭数量。现在，Bob 想要尽可能 最大化 他所能获得的总分。
 * 返回数组 bobArrows ，该数组表示 Bob 射中 0 到 11 每个 计分区域的箭数量。且 bobArrows 的总和应当等于 numArrows 。
 * 如果存在多种方法都可以使 Bob 获得最大总分，返回其中 任意一种 即可。
 * 提示：
 * 1、1 <= numArrows <= 10^5
 * 2、aliceArrows.length == bobArrows.length == 12
 * 3、0 <= aliceArrows[i], bobArrows[i] <= numArrows
 * 4、sum(aliceArrows[i]) == numArrows
 * 链接：https://leetcode-cn.com/problems/maximum-points-in-an-archery-competition
 */
public class Q2212 {

    public static void main(String[] args) {
        // [21,3,0,2,8,2,17,8,4,14,4,6]
        System.out.println(Arrays.toString(new Q2212().maximumBobPoints(89, stringToIntegerArray("[3,2,28,1,7,1,16,7,3,13,3,5]"))));
        // [0,0,0,0,1,1,0,0,1,2,3,1]
        System.out.println(Arrays.toString(new Q2212().maximumBobPoints(9, stringToIntegerArray("[1,1,0,1,0,0,2,1,0,1,2,0]"))));
        // [0,0,0,0,0,0,0,0,1,1,1,0]
        System.out.println(Arrays.toString(new Q2212().maximumBobPoints(3, stringToIntegerArray("[0,0,1,0,0,0,0,0,0,0,0,2]"))));
    }

    int maxScore = 0;
    int[] best;

    public int[] maximumBobPoints(int numArrows, int[] aliceArrows) {
        int[] ans = new int[12];
        func(ans, numArrows, aliceArrows, 0, 0);
        return best;
    }

    void func(int[] ans, int numArrows, int[] aliceArrows, int idx, int score) {
        if (idx >= aliceArrows.length) {
            if (score > maxScore) {
                maxScore = score;
                best = Arrays.copyOf(ans, ans.length);
                best[0] += numArrows;
            }
            return;
        }
        func(ans, numArrows, aliceArrows, idx + 1, score);
        if (numArrows > aliceArrows[idx]) {
            ans[idx] = aliceArrows[idx] + 1;
            func(ans, numArrows - ans[idx], aliceArrows, idx + 1, score + idx);
            ans[idx] = 0;
        }
    }
}
