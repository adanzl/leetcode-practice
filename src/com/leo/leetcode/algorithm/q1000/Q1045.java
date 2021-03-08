package com.leo.leetcode.algorithm.q1000;

/**
 * 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
 * 在 S 上反复执行重复项删除操作，直到无法继续删除。
 * 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
 * <p>
 * 提示：
 * 1、1 <= S.length <= 20000
 * 2、S 仅由小写英文字母组成。
 * <p>
 * 链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string
 */
public class Q1045 {

    public static void main(String[] args) {
        // "abaca"
        System.out.println(new Q1045().removeDuplicates("abbbaca"));
        // ""
        System.out.println(new Q1045().removeDuplicates("aaccaa"));
        // "c"
        System.out.println(new Q1045().removeDuplicates("aacaa"));
    }

    public String removeDuplicates(String S) {
        char[] str = S.toCharArray();
        int l = -1, r = 0;
        while (r < str.length) {
            if (l == -1) {
                str[++l] = str[r++];
                continue;
            }
            boolean bBack = false;
            if (str[l] == str[r]) {
                bBack = true;
                r++;
            }
            if (bBack) l--;
            else str[++l] = str[r++];
        }
        return new String(str, 0, l + 1);
    }
}
