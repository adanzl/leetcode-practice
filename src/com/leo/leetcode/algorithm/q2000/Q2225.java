package com.leo.leetcode.algorithm.q2000;

import static com.leo.utils.LCUtil.stringToInt2dArray;

import java.util.*;
import java.util.stream.Collectors;

/**
 * 给你一个整数数组 matches 其中 matches[i] = [winner_i, loser_i] 表示在一场比赛中 winner_i 击败了 loser_i 。
 * 返回一个长度为 2 的列表 answer ：
 * 1、answer[0] 是所有 没有 输掉任何比赛的玩家列表。
 * 2、answer[1] 是所有恰好输掉 一场 比赛的玩家列表。
 * 两个列表中的值都应该按 递增 顺序返回。
 * 注意：
 * 1、只考虑那些参与 至少一场 比赛的玩家。
 * 2、生成的测试用例保证 不存在 两场比赛结果 相同 。
 * 提示：
 * 1、1 <= matches.length <= 10^5
 * 2、matches[i].length == 2
 * 3、1 <= winner_i, loser_i <= 10^5
 * 4、winner_i != loser_i
 * 5、所有 matches[i] 互不相同
 * 链接：https://leetcode-cn.com/problems/find-players-with-zero-or-one-losses
 */
public class Q2225 {
    public static void main(String[] args) {
        // [[1,2,3,7],[4,5,6,8,9,16]]
        System.out.println(new Q2225().findWinners(stringToInt2dArray("[[1,5],[1,10],[1,11],[2,11],[2,13],[2,14],[3,4],[3,8],[4,12],[4,15],[5,6],[5,10],[5,13],[5,19],[6,9],[6,10],[6,13],[6,14],[6,18],[7,10],[7,11],[7,12],[7,14],[8,10],[8,11],[8,14],[9,11],[9,12],[9,13],[9,16],[9,19],[10,17],[11,13],[11,17],[12,15],[16,17],[16,18]]")));
        // [[1,2,10],[4,5,7,8]]
        System.out.println(new Q2225().findWinners(stringToInt2dArray("[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]")));
        // [[1,2,5,6],[]]
        System.out.println(new Q2225().findWinners(stringToInt2dArray("[[2,3],[1,3],[5,4],[6,4]]")));
        // [[],[1,2]]
        System.out.println(new Q2225().findWinners(stringToInt2dArray("[[1,2],[2,1]]")));
    }

    public List<List<Integer>> findWinners(int[][] matches) {
        Set<Integer> loseZero = new HashSet<>(), loseOne = new HashSet<>(), ignore = new HashSet<>();
        for (int[] match : matches) {
            if (!ignore.contains(match[0]) && !loseOne.contains(match[0])) {
                loseZero.add(match[0]);
            }
            if (!ignore.contains(match[1])) {
                if (loseOne.contains(match[1])) {
                    loseOne.remove(match[1]);
                    ignore.add(match[1]);
                } else {
                    loseOne.add(match[1]);
                }
            }
            loseZero.remove(match[1]);
        }
        List<List<Integer>> ret = new ArrayList<>();
        ret.add(loseZero.stream().sorted().collect(Collectors.toList()));
        ret.add(loseOne.stream().sorted().collect(Collectors.toList()));
        return ret;
    }
}
