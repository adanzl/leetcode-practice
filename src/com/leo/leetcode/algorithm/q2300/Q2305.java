package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 cookies ，其中 cookies[i] 表示在第 i 个零食包中的饼干数量。
 * 另给你一个整数 k 表示等待分发零食包的孩子数量，所有 零食包都需要分发。在同一个零食包中的所有饼干都必须分发给同一个孩子，不能分开。
 * 分发的 不公平程度 定义为单个孩子在分发过程中能够获得饼干的最大总数。
 * 返回所有分发的最小不公平程度。
 * 提示：
 * 1、2 <= cookies.length <= 8
 * 2、1 <= cookies[i] <= 10^5
 * 3、2 <= k <= cookies.length
 * 链接：https://leetcode.cn/problems/fair-distribution-of-cookies
 */
public class Q2305 {

    public static void main(String[] args) {
        // 38
        System.out.println(new Q2305().distributeCookies(stringToIntegerArray("[15,18,19,5,6,13,15,20]"), 3));
        // 16
        System.out.println(new Q2305().distributeCookies(stringToIntegerArray("[1,8,16,5,6,14]"), 6));
        // 31
        System.out.println(new Q2305().distributeCookies(stringToIntegerArray("[8,15,10,20,8]"), 2));
        // 7
        System.out.println(new Q2305().distributeCookies(stringToIntegerArray("[6,1,3,2,2,4,1,2]"), 3));
    }

    public int distributeCookies(int[] cookies, int k) {
        int n = cookies.length, max = 0;
        long sum = 0, ret = 0;
        for (int cookie : cookies) {
            max = Math.max(max, cookie);
            sum += cookie;
        }
        long l = max, r = sum;
        while (l <= r) {
            long mid = l + (r - l) / 2;
            minSep = Integer.MAX_VALUE;
            dfs(cookies, 1, 0, mid, new boolean[n], 0);
            if (minSep <= k) {
                ret = mid;
                r = mid - 1;
            } else l = mid + 1;
        }
        return (int) ret;
    }

    int minSep;

    void dfs(int[] cookies, int cnt, int sum, long limit, boolean[] visited, int visitedCnt) {
        if (visitedCnt == cookies.length) {
            minSep = Math.min(minSep, cnt);
            return;
        }
        for (int i = 0; i < cookies.length; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            if (sum + cookies[i] > limit) {
                dfs(cookies, cnt + 1, cookies[i], limit, visited, visitedCnt + 1);
            } else {
                dfs(cookies, cnt, sum + cookies[i], limit, visited, visitedCnt + 1);
            }
            visited[i] = false;
        }
    }

}
