package com.leo.leetcode.algorithm.q2200;

/**
 * 给你一个由若干数字（0 - 9）组成的字符串 s ，和一个整数。
 * 如果 s 的长度大于 k ，则可以执行一轮操作。在一轮操作中，需要完成以下工作：
 * 将 s 拆分 成长度为 k 的若干 连续数字组 ，使得前 k 个字符都分在第一组，接下来的 k 个字符都分在第二组，依此类推。注意，最后一个数字组的长度可以小于 k 。
 * 用表示每个数字组中所有数字之和的字符串来 替换 对应的数字组。例如，"346" 会替换为 "13" ，因为 3 + 4 + 6 = 13 。
 * 合并 所有组以形成一个新字符串。如果新字符串的长度大于 k 则重复第一步。
 * 返回在完成所有轮操作后的 s 。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、2 <= k <= 100
 * 3、s 仅由数字（0 - 9）组成。
 * 链接：https://leetcode-cn.com/problems/calculate-digit-sum-of-a-string
 */
public class Q2243 {

    public static void main(String[] args) {
        // 135
        System.out.println(new Q2243().digitSum("11111222223", 3));
        // 000
        System.out.println(new Q2243().digitSum("00000000", 3));
        // 0
        System.out.println(new Q2243().digitSum("0", 3));
    }

    public String digitSum(String s, int k) {
        char[] str = s.toCharArray();
        while (str.length > k) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < str.length; ) {
                int sum = 0, j = 0;
                while (j + i < str.length && j < k) {
                    sum += str[j + i] - '0';
                    j++;
                }
                i += j;
                sb.append(sum);
            }
            str = sb.toString().toCharArray();
        }
        return new String(str);
    }
}
