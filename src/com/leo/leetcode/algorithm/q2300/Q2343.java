package com.leo.leetcode.algorithm.q2300;

import java.math.BigDecimal;
import java.util.*;

import static com.leo.utils.LCUtil.*;

/**
 * 给你一个下标从 0 开始的字符串数组 nums ，其中每个字符串 长度相等 且只包含数字。
 * 再给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [k_i, trim_i] 。对于每个 queries[i] ，你需要：
 * 1、将 nums 中每个数字 裁剪 到剩下 最右边 trim_i 个数位。
 * 2、在裁剪过后的数字中，找到 nums 中第 k_i 小数字对应的 下标 。如果两个裁剪后数字一样大，那么下标 更小 的数字视为更小的数字。
 * 3、将 nums 中每个数字恢复到原本字符串。
 * 请你返回一个长度与 queries 相等的数组 answer，其中 answer[i]是第 i 次查询的结果。
 * 提示：
 * 1、裁剪到剩下 x 个数位的意思是不断删除最左边的数位，直到剩下 x 个数位。
 * 2、nums 中的字符串可能会有前导 0 。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i].length <= 100
 * 3、nums[i] 只包含数字。
 * 4、所有 nums[i].length 的长度 相同 。
 * 5、1 <= queries.length <= 100
 * 6、queries[i].length == 2
 * 7、1 <= k_i <= nums.length
 * 8、1 <= trim_i <= nums[0].length
 * 链接：https://leetcode.cn/problems/query-kth-smallest-trimmed-number
 */
public class Q2343 {

    public static void main(String[] args) {
        // [2,2,1,0]
        System.out.println(Arrays.toString(new Q2343().smallestTrimmedNumbers(stringToStringArray("[\"64333639502\",\"65953866768\",\"17845691654\",\"87148775908\",\"58954177897\",\"70439926174\",\"48059986638\",\"47548857440\",\"18418180516\",\"06364956881\",\"01866627626\",\"36824890579\",\"14672385151\",\"71207752868\"]")
                , stringToInt2dArray("[[9,4],[6,1],[3,8],[12,9],[11,4],[4,9],[2,7],[10,3],[13,1],[13,1],[6,1],[5,10]]"))));
        // [2,2,1,0]
        System.out.println(Arrays.toString(new Q2343().smallestTrimmedNumbers(stringToStringArray("[\"102\",\"473\",\"251\",\"814\"]"), stringToInt2dArray("[[1,1],[2,3],[4,2],[1,2]]"))));
        // [3,0]
        System.out.println(Arrays.toString(new Q2343().smallestTrimmedNumbers(stringToStringArray("[\"24\",\"37\",\"96\",\"04\"]"), stringToInt2dArray("[[2,1],[2,2]]"))));
    }

    public int[] smallestTrimmedNumbers(String[] nums, int[][] queries) {
        int n = queries.length, nn = nums.length;
        int[] ret = new int[n];
        for (int j = 0; j < n; j++) {
            List<BigDecimal[]> l = new ArrayList<>();
            for (int i = 0; i < nn; i++) {
                int sSize = nums[i].length(), idx = sSize - queries[j][1];
                l.add(new BigDecimal[]{new BigDecimal(nums[i].substring(idx)), new BigDecimal(i)});
            }
            l.sort((a, b) -> a[0].equals(b[0]) ? a[1].compareTo(b[1]) : a[0].compareTo(b[0]));
            ret[j] = l.get(queries[j][0] - 1)[1].intValue();
        }
        return ret;
    }

}
