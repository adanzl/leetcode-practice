package com.leo.leetcode.algorithm.q1200;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 有 n 个人被分成数量未知的组。每个人都被标记为一个从 0 到 n - 1 的唯一ID 。
 * 给定一个整数数组 groupSizes ，其中 groupSizes[i] 是第 i 个人所在的组的大小。例如，如果 groupSizes[1] = 3 ，则第 1 个人必须位于大小为 3 的组中。
 * 返回一个组列表，使每个人 i 都在一个大小为 groupSizes[i] 的组中。
 * 每个人应该 恰好只 出现在 一个组 中，并且每个人必须在一个组中。如果有多个答案，返回其中 任何 一个。可以 保证 给定输入 至少有一个 有效的解。
 * 提示：
 * 1、groupSizes.length == n
 * 2、1 <= n <= 500
 * 3、1 <= groupSizes[i] <= n
 * 链接：https://leetcode.cn/problems/group-the-people-given-the-group-size-they-belong-to
 */
public class Q1282 {

    public static void main(String[] args) {
        // [[5],[0,1,2],[3,4,6]]
        System.out.println(new Q1282().groupThePeople(stringToIntegerArray("[3,3,3,3,3,1,3]")));
        // [[1],[0,5],[2,3,4]]
        System.out.println(new Q1282().groupThePeople(stringToIntegerArray("[2,1,3,3,3,2]")));
    }

    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        List<List<Integer>> ret = new ArrayList<>();
        Map<Integer, List<Integer>> lMap = new HashMap<>();
        for (int i = 0; i < groupSizes.length; i++) {
            int idx = groupSizes[i];
            lMap.putIfAbsent(idx, new ArrayList<>());
            List<Integer> target = lMap.get(idx);
            target.add(i);
            if (target.size() == idx) {
                ret.add(target);
                lMap.remove(idx);
            }
        }
        return ret;
    }
}
