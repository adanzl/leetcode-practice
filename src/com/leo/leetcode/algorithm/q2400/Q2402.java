package com.leo.leetcode.algorithm.q2400;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个整数 n ，共有编号从 0 到 n - 1 的 n 个会议室。
 * 给你一个二维整数数组 meetings ，其中 meetings[i] = [start_i, end_i] 表示一场会议将会在 半闭 时间区间 [start_i, end_i) 举办。所有 start_i 的值 互不相同 。
 * 会议将会按以下方式分配给会议室：
 * 1、每场会议都会在未占用且编号 最小 的会议室举办。
 * 2、如果没有可用的会议室，会议将会延期，直到存在空闲的会议室。延期会议的持续时间和原会议持续时间 相同 。
 * 3、当会议室处于未占用状态时，将会优先提供给原 开始 时间更早的会议。
 * 返回举办最多次会议的房间 编号 。如果存在多个房间满足此条件，则返回编号 最小 的房间。
 * 半闭区间 [a, b) 是 a 和 b 之间的区间，包括 a 但 不包括 b 。
 * 提示：
 * 1、1 <= n <= 100
 * 2、1 <= meetings.length <= 10^5
 * 3、meetings[i].length == 2
 * 4、0 <= start_i < end_i <= 5 * 10^5
 * 5、start_i 的所有值 互不相同
 * 链接：https://leetcode.cn/problems/meeting-rooms-iii
 */
public class Q2402 {
    public static void main(String[] args) {
        // 1
        System.out.println(new Q2402().mostBooked(3, stringToInt2dArray("[[1,20],[2,10],[3,5],[4,9],[6,8]]")));
        // 0
        System.out.println(new Q2402().mostBooked(4, stringToInt2dArray("[[48,49],[22,30],[13,31],[31,46],[37,46],[32,36],[25,36],[49,50],[24,34],[6,41]]")));
        // 0
        System.out.println(new Q2402().mostBooked(4, stringToInt2dArray("[[10,11],[13,15],[9,19],[0,12],[12,20]]")));
        // 0
        System.out.println(new Q2402().mostBooked(2, stringToInt2dArray("[[0,10],[1,2],[12,14],[13,15]]")));
        // 0
        System.out.println(new Q2402().mostBooked(2, stringToInt2dArray("[[0,10],[1,5],[2,7],[3,4]]")));
    }

    public int mostBooked(int n, int[][] meetings) {
        int[] count = new int[n];
        Arrays.sort(meetings, Comparator.comparingInt(x -> x[0]));
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> a[0] == b[0] ? Long.compare(a[1], b[1]) : Long.compare(a[0], b[0])); // end, idx
        for (int i = 0; i < n; i++) pq.offer(new long[]{0, i});
        for (int[] meeting : meetings) {
            List<long[]> tmp = new ArrayList<>(); // 所有需要重排的
            while (!pq.isEmpty()) {
                long[] cur = pq.peek();
                long end = cur[0], idx = cur[1];
                if (end > meeting[0]) {
                    if (tmp.isEmpty()) {
                        tmp.add(cur);
                        pq.poll();
                    }
                    break;
                }
                pq.poll();
                tmp.add(new long[]{meeting[0], idx});
            }
            tmp.sort(Comparator.comparingLong(a -> a[1]));
            for (int i = 1; i < tmp.size(); i++) pq.offer(tmp.get(i));
            long end = tmp.get(0)[0], idx = tmp.get(0)[1];
            pq.offer(new long[]{end + meeting[1] - meeting[0], idx});
            count[(int) idx]++;
        }
        int ans = 0, max = 0;
        for (int i = 0; i < n; i++) {
            if (count[i] > max) {
                max = count[i];
                ans = i;
            }
        }
        return ans;
    }
}
