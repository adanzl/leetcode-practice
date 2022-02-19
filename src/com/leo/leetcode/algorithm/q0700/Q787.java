package com.leo.leetcode.algorithm.q0700;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [from_i, to_i, price_i] ，
 * 表示该航班都从城市 from_i 开始，以价格 price_i 抵达 to_i。
 * 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，
 * 你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。
 * 如果不存在这样的路线，则输出 -1。
 * 提示：
 * 1、1 <= n <= 100
 * 2、0 <= flights.length <= (n * (n - 1) / 2)
 * 3、flights[i].length == 3
 * 4、0 <= from_i, to_i < n
 * 5、from_i != to_i
 * 6、1 <= price_i <= 10^4
 * 7、航班没有重复，且不存在自环
 * 0 <= src, dst, k < n
 * src != dst
 * 链接：https://leetcode-cn.com/problems/cheapest-flights-within-k-stops
 */
public class Q787 {

    public static void main(String[] args) {
        // 200
        System.out.println(new Q787().findCheapestPrice(3, stringToInt2dArray("[[0,1,100],[1,2,100],[0,2,500]]"), 0, 2, 1));
        // 500
        System.out.println(new Q787().findCheapestPrice(3, stringToInt2dArray("[[0,1,100],[1,2,100],[0,2,500]]"), 0, 2, 0));
        // 1
        System.out.println(new Q787().findCheapestPrice(3, stringToInt2dArray("[[0,1,2],[1,2,1],[2,0,10]]"), 1, 2, 1));
        // -1
        System.out.println(new Q787().findCheapestPrice(5, stringToInt2dArray("[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]"), 2, 1, 1));
    }

    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[][] prices = new int[n][k + 1];
        List<List<Ticket>> nextCities = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            nextCities.add(new ArrayList<>());
            Arrays.fill(prices[i], Integer.MAX_VALUE);
        }
        for (int[] fight : flights) {
            nextCities.get(fight[0]).add(new Ticket(fight[1], fight[2]));
        }
        Queue<Integer> q = new ArrayDeque<>();
        q.add(src);
        int step = 0;
        while (step <= k && !q.isEmpty()) {
            int size = q.size();
            Set<Integer> nCities = new HashSet<>();
            while (size-- > 0 && !q.isEmpty()) {
                int v = q.poll();
                for (Ticket next : nextCities.get(v)) {
                    nCities.add(next.city);
                    if (step == 0) {
                        prices[next.city][step] = next.price;
                    } else {
                        prices[next.city][step] = Math.min(prices[next.city][step], next.price + prices[v][step - 1]);
                    }
                }
            }
            q.addAll(nCities);
            ++step;
        }
        int ret = Integer.MAX_VALUE;
        for (int i = 0; i <= k; i++) {
            ret = Math.min(ret, prices[dst][i]);
        }
        return ret == Integer.MAX_VALUE ? -1 : ret;
    }

    static class Ticket {
        int city;
        int price;

        Ticket(int city, int price) {
            this.city = city;
            this.price = price;
        }
    }
}
