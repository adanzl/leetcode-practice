package com.leo.leetcode.algorithm.q2000;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个有 n 个服务器的计算机网络，服务器编号为 0 到 n - 1 。同时给你一个二维整数数组 edges ，其中 edges[i] = [ui, vi] 表示服务器 ui 和 vi 之间有一条信息线路，
 * 在 一秒 内它们之间可以传输 任意 数目的信息。再给你一个长度为 n 且下标从 0 开始的整数数组 patience 。
 * 题目保证所有服务器都是 相通 的，也就是说一个信息从任意服务器出发，都可以通过这些信息线路直接或间接地到达任何其他服务器。
 * 编号为 0 的服务器是 主 服务器，其他服务器为 数据 服务器。每个数据服务器都要向主服务器发送信息，并等待回复。
 * 信息在服务器之间按 最优 线路传输，也就是说每个信息都会以 最少时间 到达主服务器。主服务器会处理 所有 新到达的信息并 立即 按照每条信息来时的路线 反方向 发送回复信息。
 * 在 0 秒的开始，所有数据服务器都会发送各自需要处理的信息。从第 1 秒开始，每 一秒最 开始 时，每个数据服务器都会检查它是否收到了主服务器的回复信息（包括新发出信息的回复信息）：
 * 1、如果还没收到任何回复信息，那么该服务器会周期性 重发 信息。数据服务器 i 每 patience[i] 秒都会重发一条信息，也就是说，数据服务器 i 在上一次发送信息给主服务器后的 patience[i] 秒 后 会重发一条信息给主服务器。
 * 2、否则，该数据服务器 不会重发 信息。
 * 当没有任何信息在线路上传输或者到达某服务器时，该计算机网络变为 空闲 状态。
 * 请返回计算机网络变为 空闲 状态的 最早秒数 。
 * 提示：
 * 1、n == patience.length
 * 2、2 <= n <= 10^5
 * 3、patience[0] == 0
 * 4、对于 1 <= i < n ，满足 1 <= patience[i] <= 10^5
 * 5、1 <= edges.length <= min(10^5, n * (n - 1) / 2)
 * 6、edges[i].length == 2
 * 7、0 <= ui, vi < n
 * 8、ui != vi
 * 9、不会有重边。
 * 10、每个服务器都直接或间接与别的服务器相连。
 * 链接：https://leetcode-cn.com/problems/the-time-when-the-network-becomes-idle
 */
public class Q2039 {

    public static void main(String[] args) {
        // 8
        System.out.println(new Q2039().networkBecomesIdle(stringToInt2dArray("[[0,1],[1,2]]"), stringToIntegerArray("[0,2,1]")));
        // 3
        System.out.println(new Q2039().networkBecomesIdle(stringToInt2dArray("[[0,1],[0,2],[1,2]]"), stringToIntegerArray("[0,10,10]")));
    }

    public int networkBecomesIdle(int[][] edges, int[] patience) {
        int step = 0, ret = 0;
        int[] dist = new int[patience.length];
        boolean[] visited = new boolean[patience.length];
        List<List<Integer>> nextMap = new ArrayList<>(patience.length);
        for (int i = 0; i < patience.length; i++) nextMap.add(new ArrayList<>());
        for (int[] edge : edges) {
            nextMap.get(edge[0]).add(edge[1]);
            nextMap.get(edge[1]).add(edge[0]);
        }
        Queue<Integer> q = new ArrayDeque<>();
        q.add(0);
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0 && !q.isEmpty()) {
                int cur = q.poll();
                if (visited[cur]) continue;
                visited[cur] = true;
                dist[cur] = step;
                q.addAll(nextMap.get(cur));
            }
            step++;
        }
        for (int i = 1; i < dist.length; i++) {
            int pc = (dist[i] * 2 - 1) / patience[i];
            ret = Math.max(ret, pc * patience[i] + dist[i] * 2);
        }

        return ret + 1;
    }
}
