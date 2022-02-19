package com.leo.leetcode.algorithm.q0900;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。
 * 给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、1 <= words[i].length <= 20
 * 3、order.length == 26
 * 4、在 words[i] 和 order 中的所有字符都是英文小写字母。
 * <p>
 * 链接：https://leetcode-cn.com/problems/verifying-an-alien-dictionary
 */
public class Q953 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q953().isAlienSorted(stringToStringArray("[\"my\",\"f\"]"), "gelyriwxzdupkjctbfnqmsavho"));
        // false
        System.out.println(new Q953().isAlienSorted(stringToStringArray("[\"word\",\"world\",\"row\"]"), "worldabcefghijkmnpqstuvxyz"));
        // true
        System.out.println(new Q953().isAlienSorted(stringToStringArray("[\"hello\",\"leetcode\"]"), "hlabcdefgijkmnopqrstuvwxyz"));
        // false
        System.out.println(new Q953().isAlienSorted(stringToStringArray("[\"apple\",\"app\"]"), "abcdefghijklmnopqrstuvwxyz"));
    }

    public boolean isAlienSorted(String[] words, String order) {
        int[] priority = new int[26];
        for (int i = 0; i < order.length(); i++) priority[order.charAt(i) - 'a'] = i;
        for (int i = 1; i < words.length; i++) {
            if (compare(words[i - 1], words[i], priority) > 0) return false;
        }
        return true;
    }

    // 1: s1 > s2 -1: s1 < s2 0: s1 == s2
    int compare(String s1, String s2, int[] priority) {
        int len1 = s1.length(), len2 = s2.length();
        int i = 0, j = 0;
        while (i < len1 && j < len2 && s1.charAt(i) == s2.charAt(j)) {
            i++;
            j++;
        }
        if (i == len1 && j == len2) return 0;
        if (i == len1) return -1;
        if (j == len2) return 1;
        return priority[s1.charAt(i) - 'a'] - priority[s2.charAt(j) - 'a'];
    }
}
