package com.leo.leetcode.contest.q20220313;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 为了不断提高用户使用的体验，开发团队正在对产品进行全方位的开发和优化。
 * 已知开发团队共有若干名成员，skills[i] 表示第 i 名开发人员掌握技能列表。如果两名成员各自拥有至少一门对方未拥有的技能，则这两名成员可以「合作开发」。
 * 请返回当前有多少对开发成员满足「合作开发」的条件。由于答案可能很大，请你返回答案对 10^9 + 7 取余的结果。
 * 注意： 对于任意 skills[i] 均升序排列。
 * 提示：
 * 1、2 <= skills.length <= 10^5
 * 2、1 <= skills[i].length <= 4
 * 3、1 <= skills[i][j] <= 1000
 * 4、skills[i] 中不包含重复元素
 * 链接：https://leetcode.cn/contest/cnunionpay-2022spring/problems/lCh58I/
 */
public class Q4 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q4().coopDevelop(stringToInt2dArray("[[3],[6]]")));
        // 2
        System.out.println(new Q4().coopDevelop(stringToInt2dArray("[[1,2,3],[3],[2,4]]")));
    }

    public int coopDevelop(int[][] skills) {
        Arrays.sort(skills, Comparator.comparingInt(o -> o.length));
        int MOD = 1_000_000_007, n = skills.length;
        long ret = 0;
        Map<Long, Integer> signMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int[] skill = skills[i];
            Arrays.sort(skill);
            long sign = 0, cnt = 0;
            for (int s : skill) sign = sign * 1000 + s;
            List<Long> sub = new ArrayList<>();
            sub.add(0L);
            for (int s : skill) {
                int size = sub.size();
                for (int j = 0; j < size; j++) {
                    sub.add(sub.get(j) * 1000 + s);
                }
            }
            for (long s : sub) {
                cnt += signMap.getOrDefault(s, 0);
            }
            ret = (ret + i - cnt) % MOD;
            signMap.put(sign, signMap.getOrDefault(sign, 0) + 1);
        }
        return (int) ret;
    }
}
