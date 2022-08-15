package com.leo.leetcode.algorithm.q2300;

/**
 * 给你下标从 0 开始、长度为 n 的字符串 pattern ，它包含两种字符，'I' 表示 上升 ，'D' 表示 下降 。
 * 你需要构造一个下标从 0 开始长度为 n + 1 的字符串，且它要满足以下条件：
 * 1、num 包含数字 '1' 到 '9' ，其中每个数字 至多 使用一次。
 * 2、如果 pattern[i] == 'I' ，那么 num[i] < num[i + 1] 。
 * 3、如果 pattern[i] == 'D' ，那么 num[i] > num[i + 1] 。
 * 请你返回满足上述条件字典序 最小 的字符串 num。
 * 提示：
 * 1、1 <= pattern.length <= 8
 * 2、pattern 只包含字符 'I' 和 'D' 。
 * 链接：https://leetcode.cn/problems/construct-smallest-number-from-di-string
 */
public class Q2375 {

    public static void main(String[] args) {
        // 123549876
        //  IIIDIDDD
        System.out.println(new Q2375().smallestNumber("IIIDIDDD"));
        // 4321
        System.out.println(new Q2375().smallestNumber("DDD"));
    }

    public String smallestNumber(String pattern) {
        int n = pattern.length();
        char[] s = new char[n + 1];
        s[0] = '1';
        for (int i = 0; i < n; i++) {
            if (pattern.charAt(i) == 'I') s[i + 1] = (char) (i + 2 + '0');
            else {
                s[i + 1] = s[i];
                for (int j = i; j >= 0; j--) {
                    s[j]++;
                    if (j > 0 && pattern.charAt(j - 1) == 'I') break;
                }
            }
        }
        return new String(s);
    }
}
