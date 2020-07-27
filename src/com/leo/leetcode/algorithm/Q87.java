package com.leo.leetcode.algorithm;

/**
 * 给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
 * 下图是字符串 s1 = "great" 的一种可能的表示形式。
 *     great
 *    /    \
 *   gr    eat
 *  / \    /  \
 * g   r  e   at
 *            / \
 *           a   t
 * 在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。
 * 例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。
 *     rgeat
 *    /    \
 *   rg    eat
 *  / \    /  \
 * r   g  e   at
 *            / \
 *           a   t
 * 我们将 "rgeat” 称作 "great" 的一个扰乱字符串。
 * 同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。
 *     rgtae
 *    /    \
 *   rg    tae
 *  / \    /  \
 * r   g  ta   e
 *        / \
 *       t   a
 * 我们将 "rgtae” 称作 "great" 的一个扰乱字符串。
 * 给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。
 * 链接：https://leetcode-cn.com/problems/scramble-string
 */
public class Q87 {

    public static void main(String[] args) {
        System.out.println(new Q87().isScramble("ccabcbabcbabbbbcbb", "bbbbabccccbbbabcba")); // false
        System.out.println(new Q87().isScramble("abc", "bca")); // true
        System.out.println(new Q87().isScramble("great", "rgeat")); // true
        System.out.println(new Q87().isScramble("great", "rgtae")); // true
        System.out.println(new Q87().isScramble("abcde", "caebd")); // false
        System.out.println(new Q87().isScramble("abb", "bab")); // true
    }

    public boolean isScramble(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        return isScramble(s1.toCharArray(), 0, s1.length(), s2.toCharArray(), 0, s2.length());
    }

    boolean isScramble(char[] str1, int l1, int r1, char[] str2, int l2, int r2) {
        if (r1 - l1 == 1) return str1[l1] == str2[l2];
        for (int i = 1; i < r1 - l1; i++) {
            if ((isScramble(str1, l1, l1 + i, str2, l2, l2 + i) && isScramble(str1, l1 + i, r1, str2, l2 + i, r2))
                    || isScramble(str1, l1, l1 + i, str2, r2 - i, r2) && isScramble(str1, l1 + i, r1, str2, l2, r2 - i))
                return true;
        }
        return false;
    }
}
