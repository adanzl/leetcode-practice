package com.leo.leetcode.algorithm.q0900;

/**
 * 给你由 n 个小写字母字符串组成的数组 strs，其中每个字符串长度相等。
 * 这些字符串可以每个一行，排成一个网格。例如，strs = ["abc", "bce", "cae"] 可以排列为：
 * abc
 * bce
 * cae
 * 你需要找出并删除 不是按字典序升序排列的 列。在上面的例子（下标从 0 开始）中，列 0（'a', 'b', 'c'）和列 2（'c', 'e', 'e'）都是按升序排列的，而列 1（'b', 'c', 'a'）不是，所以要删除列 1 。
 * 返回你需要删除的列数。
 * 提示：
 * 1、n == strs.length
 * 2、1 <= n <= 100
 * 3、1 <= strs[i].length <= 1000
 * 4、strs[i] 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/delete-columns-to-make-sorted
 */
public class Q944 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q944().minDeletionSize(new String[]{"cba", "daf", "ghi"}));
        // 0
        System.out.println(new Q944().minDeletionSize(new String[]{"a", "b"}));
        // 3
        System.out.println(new Q944().minDeletionSize(new String[]{"zyx", "wvu", "tsr"}));
    }

    public int minDeletionSize(String[] strs) {
        int n = strs.length, len = strs[0].length(), ret = 0;
        for (int i = 0; i < len; i++) {
            char c = strs[0].charAt(i);
            for (int j = 1; j < n; j++) {
                if (strs[j].charAt(i) < c) {
                    ret++;
                    break;
                }
                c = strs[j].charAt(i);
            }
        }
        return ret;
    }
}
