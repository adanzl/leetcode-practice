package com.leo.leetcode.algorithm.q0300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个表示数据的整数数组 data ，返回它是否为有效的 UTF-8 编码。
 * UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：
 * 对于 1 字节 的字符，字节的第一位设为 0 ，后面 7 位为这个符号的 unicode 码。
 * 对于 n 字节 的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为 0 ，后面字节的前两位一律设为 10 。剩下的没有提及的二进制位，全部为这个符号的 unicode 码。
 * 这是 UTF-8 编码的工作方式：
 * Char. number range  |        UTF-8 octet sequence
 * (hexadecimal)    |              (binary)
 * --------------------+---------------------------------------------
 * 0000 0000-0000 007F | 0xxxxxxx
 * 0000 0080-0000 07FF | 110xxxxx 10xxxxxx
 * 0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
 * 0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
 * 注意：输入是整数数组。只有每个整数的 最低 8 个有效位 用来存储数据。这意味着每个整数只表示 1 字节的数据。
 * 提示:
 * 1、1 <= data.length <= 2 * 10^4
 * 2、0 <= data[i] <= 255
 * 链接：https://leetcode-cn.com/problems/utf-8-validation
 */
public class Q393 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q393().validUtf8(stringToIntegerArray("[240,162,138,147]")));
        // true
        System.out.println(new Q393().validUtf8(stringToIntegerArray("[1]")));
        // true
        System.out.println(new Q393().validUtf8(stringToIntegerArray("[197,130,1]")));
        // false
        System.out.println(new Q393().validUtf8(stringToIntegerArray("[237]")));
        // false
        System.out.println(new Q393().validUtf8(stringToIntegerArray("[235,140,4]")));
    }

    public boolean validUtf8(int[] data) {
        int size = 0;
        for (int d : data) {
            int len = getLen(d);
            if (len == -1) return false;
            if (size == 0) {
                if (len == 1) return false;
                size = Math.max(len - 1, 0);
            } else {
                if (len != 1) return false;
                size--;
            }
        }
        return size == 0;
    }

    int getLen(int v) {
        int mask = 1 << 7;
        for (int i = 0; i < 5; i++) {
            if ((v & mask) == 0) return i;
            mask >>= 1;
        }
        return -1;
    }
}
