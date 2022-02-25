package com.leo.leetcode.algorithm.q0900;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。
 * 如果小镇法官真的存在，那么：
 * 1、小镇法官不会信任任何人。
 * 2、每个人（除了小镇法官）都信任这位小镇法官。
 * 3、只有一个人同时满足属性 1 和属性 2 。
 * 给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。
 * 如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。
 * 提示：
 * 1、1 <= n <= 1000
 * 2、0 <= trust.length <= 10^4
 * 3、trust[i].length == 2
 * 4、trust 中的所有trust[i] = [ai, bi] 互不相同
 * 5、ai != bi
 * 6、1 <= ai, bi <= n
 * 链接：https://leetcode-cn.com/problems/find-the-town-judge
 */
public class Q997 {

    public static void main(String[] args) {
        // -1
        System.out.println(new Q997().findJudge(3, stringToInt2dArray("[[1,2],[2,3]]")));
        // 3
        System.out.println(new Q997().findJudge(3, stringToInt2dArray("[[1,3],[2,3]]")));
        // 2
        System.out.println(new Q997().findJudge(2, stringToInt2dArray("[[1,2]]")));
        // -1
        System.out.println(new Q997().findJudge(2, stringToInt2dArray("[[1,3],[2,3],[3,1]]")));
    }

    public int findJudge(int n, int[][] trust) {
        Map<Integer, Set<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) map.put(i + 1, new HashSet<>());
        for (int[] t : trust) {
            map.remove(t[0]);
            if (map.containsKey(t[1])) {
                map.get(t[1]).add(t[0]);
            }
        }
        if (map.isEmpty()) return -1;
        for (Map.Entry<Integer, Set<Integer>> entry : map.entrySet()) {
            if (entry.getValue().size() == n - 1) return entry.getKey();
        }
        return -1;
    }
}
