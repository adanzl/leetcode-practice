package com.leo.leetcode.algorithm.q2200;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 queries 和一个 正 整数 intLength ，请你返回一个数组 answer ，其中 answer[i] 是长度为 intLength 的 正回文数 中第 queries[i] 小的数字，如果不存在这样的回文数，则为 -1 。
 * 回文数 指的是从前往后和从后往前读一模一样的数字。回文数不能有前导 0 。
 * 提示：
 * 1、1 <= queries.length <= 5 * 10^4
 * 2、1 <= queries[i] <= 10^9
 * 3、1 <= intLength <= 15
 * 链接：https://leetcode-cn.com/problems/find-palindrome-with-fixed-length
 */
public class Q2217 {

    public static void main(String[] args) {
        // [1111,1331,1551]
        System.out.println(Arrays.toString(new Q2217().kthPalindrome(stringToIntegerArray("[2,4,6]"), 4)));
        // [-1]
        System.out.println(Arrays.toString(new Q2217().kthPalindrome(stringToIntegerArray("[510134]"), 10)));
        // [-1,-1,-1,-1,10801,-1]
        System.out.println(Arrays.toString(new Q2217().kthPalindrome(stringToIntegerArray("[449229674,501930675,40059525,908875541,9,672504016]"), 5)));
        // [22,44,66]
        System.out.println(Arrays.toString(new Q2217().kthPalindrome(stringToIntegerArray("[2,4,6]"), 2)));
        // [2,-1,8,-1,-1,-1,-1,9,7,6]
        System.out.println(Arrays.toString(new Q2217().kthPalindrome(stringToIntegerArray("[2,201429812,8,520498110,492711727,339882032,462074369,9,7,6]"), 1)));
        // [101,111,121,131,141,999]
        System.out.println(Arrays.toString(new Q2217().kthPalindrome(stringToIntegerArray("[1,2,3,4,5,90]"), 3)));
    }

    public long[] kthPalindrome(int[] queries, int intLength) {
        int limit = (int) Math.pow(10, (intLength >> 1) + ((intLength & 1) == 1 ? 0 : -1)) * 9;
        long[] ret = new long[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int query = queries[i];
            if (query > limit) ret[i] = -1;
            else ret[i] = getPalindrome(query, intLength);
        }
        return ret;
    }

    long getPalindrome(int idx, int len) {
        int suf = (len >> 1) + ((len & 1) == 1 ? 0 : -1);
        long num = idx - 1 + (long) Math.pow(10, suf);
        char[] numStr = String.valueOf(num).toCharArray();
        char[] newStr = new char[len];
        System.arraycopy(numStr, 0, newStr, 0, numStr.length);
        for (int i = 0; i <= suf; i++) newStr[len - 1 - i] = numStr[i];
        return Long.parseLong(new String(newStr));
    }
}
