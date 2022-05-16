package com.leo.leetcode.algorithm.q2200;

import java.util.Arrays;
import java.util.Comparator;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个二维整数数组 tiles ，其中 tiles[i] = [li, ri] ，表示所有在 li <= j <= ri 之间的每个瓷砖位置 j 都被涂成了白色。
 * 同时给你一个整数 carpetLen ，表示可以放在 任何位置 的一块毯子。
 * 请你返回使用这块毯子，最多 可以盖住多少块瓷砖。
 * 提示：
 * 1、1 <= tiles.length <= 5 * 10^4
 * 2、tiles[i].length == 2
 * 3、1 <= li <= ri <= 10^9
 * 4、1 <= carpetLen <= 10^9
 * 5、tiles 互相 不会重叠 。
 * 链接：https://leetcode.cn/problems/maximum-white-tiles-covered-by-a-carpet
 */
public class Q2271 {

    public static void main(String[] args) {
        // 9
        System.out.println(new Q2271().maximumWhiteTiles(stringToInt2dArray("[[1,5],[10,11],[12,18],[20,25],[30,32]]"), 10));
        // 2
        System.out.println(new Q2271().maximumWhiteTiles(stringToInt2dArray("[[10,11],[1,1]]"), 2));
        // 126
        System.out.println(new Q2271().maximumWhiteTiles(stringToInt2dArray("[[8051,8057],[8074,8089],[7994,7995],[7969,7987],[8013,8020],[8123,8139],[7930,7950],[8096,8104],[7917,7925],[8027,8035],[8003,8011]]"), 9854));
    }

    public int maximumWhiteTiles(int[][] tiles, int carpetLen) {
        long ret = 0;
        int n = tiles.length;
        Arrays.sort(tiles, Comparator.comparingInt(a -> a[0]));
        long[] preSum = new long[n + 1];
        for (int i = 1; i <= n; i++) preSum[i] = preSum[i - 1] + tiles[i - 1][1] - tiles[i - 1][0] + 1;
        for (int i = 0; i < n; i++) {
            int[] tile = tiles[i];
            int l = 0, r = n - 1, pos = tile[0] + carpetLen - 1;
            while (l <= r) {
                int mid = (l + r) / 2;
                int[] t = tiles[mid];
                if (t[0] <= pos && pos <= t[1]) {
                    l = mid;
                    break;
                }
                if (tiles[mid][0] > pos) r = mid - 1;
                else l = mid + 1;
            }
            long v = preSum[l] - preSum[i];
            if (l < n) v += Math.max(0, Math.min(tiles[l][1], tile[0] + carpetLen - 1) - tiles[l][0] + 1);
            ret = Math.max(ret, v);
        }
        return (int) ret;
    }
}
