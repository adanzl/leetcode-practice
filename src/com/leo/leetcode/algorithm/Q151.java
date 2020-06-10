package com.leo.leetcode.algorithm;

import org.junit.Test;

/**
 * 给定一个字符串，逐个翻转字符串中的每个单词。
 * 说明：
 * <p>
 * 无空格字符构成一个单词。
 * 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
 * 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 * <p>
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
public class Q151 {
    @Test
    public void TestOJ() {
        System.out.println(reverseWords("  hello world!  ")); // "world! hello"
        System.out.println(reverseWords("the sky is blue")); // "blue is sky the"
        System.out.println(reverseWords("a good   example")); // "example good a"
        System.out.println(reverseWords("   ")); // ""
        System.out.println(reverseWords("")); // ""
    }


    public String reverseWords(String s) {
        int i = 0, j = 0, head = 0;
        char[] str = s.toCharArray();
        for (; i < str.length; i++) {
            if (str[i] == ' ' && (i == 0 || i == str.length - 1 || str[i - 1] == ' ')) continue;
            str[j] = str[i];
            if (str[j] == ' ') {
                swap(str, head, j);
                head = j + 1;
            }
            j++;
        }
        swap(str, head, j);
        swap(str, 0, j);
        return new String(str, 0, j).trim();
    }

    void swap(char[] arr, int start, int end) {
        if (end > arr.length) return;
        int mid = (end - start) >> 1;
        for (int i = 0; i < mid; i++) {
            char t = arr[start + i];
            arr[start + i] = arr[end - i - 1];
            arr[end - i - 1] = t;
        }
    }
}
