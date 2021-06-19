package com.leo.leetcode.algorithm.q1200;

import java.util.List;

import static com.leo.utils.LCUtil.stringToStringList;

/**
 * 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
 * 请返回所有可行解 s 中最长长度。
 * 提示：
 * 1、1 <= arr.length <= 16
 * 2、1 <= arr[i].length <= 26
 * 3、arr[i] 中只含有小写英文字母
 * <p>
 * 链接：https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
 */
public class Q1239 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q1239().maxLength(stringToStringList("[\"yy\",\"bkhwmpbiisbldzknpm\"]")));
        // 2
        System.out.println(new Q1239().maxLength(stringToStringList("[\"un\",\"ii\",\"ue\"]")));
        // 4
        System.out.println(new Q1239().maxLength(stringToStringList("[\"un\",\"iq\",\"ue\"]")));
        // 6
        System.out.println(new Q1239().maxLength(stringToStringList("[\"cha\",\"r\",\"act\",\"ers\"]")));
        // 26
        System.out.println(new Q1239().maxLength(stringToStringList("[\"abcdefghijklmnopqrstuvwxyz\"]")));
    }

    public int maxLength(List<String> arr) {
        int[] marks = new int[arr.size()];
        for (int i = 0; i < marks.length; i++) {
            String str = arr.get(i);
            int v = 0;
            for (char c : str.toCharArray()) {
                int f = (1 << (c - 'a'));
                if ((v & f) != 0) {
                    v = 0;
                    break;
                }
                v += f;
            }
            marks[i] = v;
        }

        return func(arr, marks, 0, 0, 0);
    }

    private int func(List<String> arr, int[] marks, int mark, int idx, int len) {
        if (idx == marks.length) return len;
        if (marks[idx] != 0 && (mark & marks[idx]) == 0) {
            return Math.max(func(arr, marks, mark + marks[idx], idx + 1, len + arr.get(idx).length()),
                    func(arr, marks, mark, idx + 1, len));
        } else {
            return func(arr, marks, mark, idx + 1, len);
        }
    }
}
