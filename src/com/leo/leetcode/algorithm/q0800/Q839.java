package com.leo.leetcode.algorithm.q0800;

/**
 * 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。
 * 如果这两个字符串本身是相等的，那它们也是相似的。
 * 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。
 * 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。
 * 注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。
 * 形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
 * 给你一个字符串列表 strs。
 * 列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。
 * 请问 strs 中有多少个相似字符串组？
 * <p>
 * 提示：
 * 1、1 <= strs.length <= 100
 * 2、1 <= strs[i].length <= 1000
 * 3、sum(strs[i].length) <= 2 * 104
 * 4、strs[i] 只包含小写字母。
 * 5、strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。
 * <p>
 * 备注：字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。
 * <p>
 * 链接：https://leetcode-cn.com/problems/similar-string-groups
 */
public class Q839 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q839().numSimilarGroups(new String[]{"tars", "rats", "arts", "star"}));
        // 1
        System.out.println(new Q839().numSimilarGroups(new String[]{"omv", "ovm"}));
    }

    int[] parent;

    public int numSimilarGroups(String[] strs) {
        parent = new int[strs.length];
        int count = strs.length;
        for (int i = 0; i < parent.length; i++) parent[i] = i;
        for (int i = 0; i < strs.length; i++) {
            for (int j = i + 1; j < strs.length; j++) {
                if (isSim(strs[i], strs[j]))
                    if (merge(i, j))
                        count--;
            }
        }
        return count;
    }

    boolean isSim(String s1, String s2) {
        int count = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) count++;
            if (count > 2) return false;
        }
        return true;
    }

    int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }

    boolean merge(int i0, int i1) {
        int r0 = find(i0), r1 = find(i1);
        if (r0 == r1) return false;
        parent[r1] = r0;
        return true;
    }
}
