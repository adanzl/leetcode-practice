package com.leo.leetcode.algorithm.q2000;

import com.leo.utils.TestCase;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0  开始的字符串  s  ，它只包含字符  '*' 和  '|'  ，
 * 其中  '*'  表示一个 盘子  ，'|'  表示一支  蜡烛  。
 * 同时给你一个下标从 0  开始的二维整数数组  queries  ，其中  queries[i] = [left_i, right_i]  表示 子字符串  s[left_i...right_i]  （包含左右端点的字符）。
 * 对于每个查询，你需要找到 子字符串中  在 两支蜡烛之间  的盘子的 数目  。
 * 如果一个盘子在 子字符串中  左边和右边 都  至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间  。
 * 比方说，s = "||**||**|*"  ，查询  [3, 8]  ，表示的是子字符串  "*||**|"  。
 * 子字符串中在两支蜡烛之间的盘子数目为  2  ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
 * 请你返回一个整数数组  answer  ，其中  answer[i]  是第  i  个查询的答案。
 * 提示：
 * 1、3 <= s.length <= 10^5
 * 2、s  只包含字符  '*' 和  '|'  。
 * 3、1 <= queries.length <= 10^5
 * 4、queries[i].length == 2
 * 5、0 <= left_i <= right_i < s.length
 * 链接：https://leetcode-cn.com/problems/plates-between-candles
 */
public class Q2055 {

    public static void main(String[] args) {
        // [0]
        System.out.println(Arrays.toString(new Q2055().platesBetweenCandles("***|", stringToInt2dArray("[[2,2]]"))));
        // [0]
        System.out.println(Arrays.toString(new Q2055().platesBetweenCandles("***", stringToInt2dArray("[[2,2]]"))));
        //
        TestCase tc = new TestCase("resources/Q2055/Case002.txt");
        System.out.println(Arrays.toString(new Q2055().platesBetweenCandles(tc.getData(0), stringToInt2dArray(tc.getData(1)))));
        // [0,0,0,9,0]
        System.out.println(Arrays.toString(new Q2055().platesBetweenCandles("***|**|*****|**||**|*", stringToInt2dArray("[[4,5],[14,17],[5,11],[1,17],[15,16]]"))));
        // [2,0]
        System.out.println(Arrays.toString(new Q2055().platesBetweenCandles("|**|**||***|", stringToInt2dArray("[[0,5],[5,9]]"))));
        // [2,3]
        System.out.println(Arrays.toString(new Q2055().platesBetweenCandles("**|**|***|", stringToInt2dArray("[[2,5],[5,9]]"))));
    }

    public int[] platesBetweenCandles(String s, int[][] queries) {
        int[] ret = new int[queries.length];
        int[] sum = new int[s.length()], ids = new int[s.length()];
        boolean bLeft = false;
        int len = 0, iSum = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '*') {
                if (bLeft) len++;
            } else {
                bLeft = true;
                sum[iSum++] = len;
            }
            ids[i] = iSum;
        }
        if (iSum == 0) return ret;
        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0], r = queries[i][1];
            int i0 = ids[l] - 1, i1 = ids[r] - 1;
            if (s.charAt(l) == '*') i0++;
            if (i1 < i0) ret[i] = 0;
            else ret[i] = Math.max(0, sum[i1] - sum[i0]);
        }
        return ret;
    }
}
