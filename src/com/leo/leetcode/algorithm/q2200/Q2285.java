package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToInt2dArray;

import java.util.*;

/**
 * 给你一个整数 n ，表示一个国家里的城市数目。城市编号为 0 到 n - 1 。
 * 给你一个二维整数数组 roads ，其中 roads[i] = [ai, bi] 表示城市 ai 和 bi 之间有一条 双向 道路。
 * 你需要给每个城市安排一个从 1 到 n 之间的整数值，且每个值只能被使用 一次 。道路的 重要性 定义为这条道路连接的两座城市数值 之和 。
 * 请你返回在最优安排下，所有道路重要性 之和 最大 为多少。
 * 提示：
 * 1、2 <= n <= 5 * 10^4
 * 2、1 <= roads.length <= 5 * 10^4
 * 3、roads[i].length == 2
 * 4、0 <= ai, bi <= n - 1
 * 5、ai != bi
 * 6、没有重复道路。
 * 链接：https://leetcode.cn/problems/maximum-total-importance-of-roads
 */
public class Q2285 {
    public static void main(String[] args) {
        // 43
        System.out.println(new Q2285().maximumImportance(5, stringToInt2dArray("[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]")));
        // 20
        System.out.println(new Q2285().maximumImportance(5, stringToInt2dArray("[[0,3],[2,4],[1,3]]")));
    }

    public long maximumImportance(int n, int[][] roads) {
        int[] d = new int[n];
        for (int[] road : roads) {
            d[road[0]]++;
            d[road[1]]++;
        }
        Arrays.sort(d);
        long ret = 0;
        for (int i = n; i >= 1; i--) ret += (long) d[i - 1] * i;
        return ret;
    }

}
