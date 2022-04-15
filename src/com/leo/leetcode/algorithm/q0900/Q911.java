package com.leo.leetcode.algorithm.q0900;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你两个整数数组 persons 和 times 。在选举中，第 i 张票是在时刻为 times[i] 时投给候选人 persons[i] 的。
 * 对于发生在时刻 t 的每个查询，需要找出在 t 时刻在选举中领先的候选人的编号。
 * 在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。
 * 实现 TopVotedCandidate 类：
 * 1、TopVotedCandidate(int[] persons, int[] times) 使用 persons 和 times 数组初始化对象。
 * 2、int q(int t) 根据前面描述的规则，返回在时刻 t 在选举中领先的候选人的编号。
 * 提示：
 * 1、1 <= persons.length <= 5000
 * 2、times.length == persons.length
 * 3、0 <= persons[i] < persons.length
 * 4、0 <= times[i] <= 10^9
 * 5、times 是一个严格递增的有序数组
 * 6、times[0] <= t <= 10^9
 * 7、每个测试用例最多调用 10^4 次 q
 * 链接：https://leetcode-cn.com/problems/online-election
 */
public class Q911 {

    public static void main(String[] args) {
        TopVotedCandidate topVotedCandidate = new TopVotedCandidate(
                stringToIntegerArray("[0, 1, 1, 0, 0, 1, 0]"),
                stringToIntegerArray("[0, 5, 10, 15, 20, 25, 30]"));
        System.out.println(topVotedCandidate.q(3));  // 返回 0 ，在时刻 3 ，票数分布为 [0] ，编号为 0 的候选人领先。
        System.out.println(topVotedCandidate.q(12)); // 返回 1 ，在时刻 12 ，票数分布为 [0,1,1] ，编号为 1 的候选人领先。
        System.out.println(topVotedCandidate.q(25)); // 返回 1 ，在时刻 25 ，票数分布为 [0,1,1,0,0,1] ，编号为 1 的候选人领先。（在平局的情况下，1 是最近获得投票的候选人）。
        System.out.println(topVotedCandidate.q(15)); // 返回 0
        System.out.println(topVotedCandidate.q(24)); // 返回 0
        System.out.println(topVotedCandidate.q(8));  // 返回 1
    }

    static class TopVotedCandidate {

        List<TreeMap<Integer, Integer>> voteMap = new ArrayList<>();

        TreeMap<Integer, int[]> qMap = new TreeMap<>();

        public TopVotedCandidate(int[] persons, int[] times) {
            for (int i = 0; i < persons.length; i++) voteMap.add(new TreeMap<>());
            for (int i = 0; i < persons.length; i++) {
                TreeMap<Integer, Integer> pMap = voteMap.get(persons[i]);
                Map.Entry<Integer, Integer> pEntry = pMap.floorEntry(times[i]);
                int pVote = pEntry == null ? 0 : pEntry.getValue();
                pMap.put(times[i], pVote + 1);
                Map.Entry<Integer, int[]> maxEntry = qMap.floorEntry(times[i]);
                if (null == maxEntry || maxEntry.getValue()[1] <= pVote)
                    qMap.put(times[i], new int[]{persons[i], pVote});
            }
        }

        public int q(int t) {
            Map.Entry<Integer, int[]> entry = qMap.floorEntry(t);
            return entry == null ? -1 : entry.getValue()[0];
        }
    }
}
