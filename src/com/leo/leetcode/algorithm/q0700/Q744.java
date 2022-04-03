package com.leo.leetcode.algorithm.q0700;

import static com.leo.utils.LCUtil.stringToCharArray;

/**
 * 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
 * 在比较时，字母是依序循环出现的。举个例子：
 * 如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
 * 提示：
 * 1、2 <= letters.length <= 10^4
 * 2、letters[i] 是一个小写字母
 * 3、letters 按非递减顺序排序
 * 4、letters 最少包含两个不同的字母
 * 5、target 是一个小写字母
 * 链接：https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target
 */
public class Q744 {

    public static void main(String[] args) {
        // c
        System.out.println(new Q744().nextGreatestLetter(stringToCharArray("[\"c\", \"f\", \"j\"]"), 'a'));
        // f
        System.out.println(new Q744().nextGreatestLetter(stringToCharArray("[\"c\",\"f\",\"j\"]"), 'c'));
        // f
        System.out.println(new Q744().nextGreatestLetter(stringToCharArray("[\"c\",\"f\",\"j\"]"), 'd'));
    }

    public char nextGreatestLetter(char[] letters, char target) {
        int n = letters.length, l = 0, r = n - 1;
        while (l <= r) {
            int mid = (l + r) >> 1;
            if (letters[mid] <= target) l = mid + 1;
            else r = mid - 1;
        }
        return l == n ? letters[0] : letters[l];
    }
}
