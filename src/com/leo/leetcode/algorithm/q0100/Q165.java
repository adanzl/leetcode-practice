package com.leo.leetcode.algorithm.q0100;

/**
 * 比较两个版本号 version1 和 version2。
 * 如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。
 * 你可以假设版本字符串非空，并且只包含数字和 . 字符。
 *  . 字符不代表小数点，而是用于分隔数字序列。
 * 例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。
 * 你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。
 * 链接：https://leetcode-cn.com/problems/compare-version-numbers
 */
public class Q165 {

    public static void main(String[] args) {
        System.out.println(new Q165().compareVersion("0.1", "1.1")); // -1
        System.out.println(new Q165().compareVersion("1.0.1", "1")); // 1
        System.out.println(new Q165().compareVersion("7.5.2.4", "7.5.3")); // -1
        System.out.println(new Q165().compareVersion("1.01", "1.0010")); // -1
        System.out.println(new Q165().compareVersion("1.0", "1.0.0.0")); // 0
        System.out.println(new Q165().compareVersion("1.0", "1.0.0.1")); // -1
    }

    public int compareVersion(String version1, String version2) {
        String[] str1 = version1.split("\\."), str2 = version2.split("\\.");
        int i = 0;
        while (i < str1.length && i < str2.length) {
            int v1 = Integer.parseInt(str1[i]), v2 = Integer.parseInt(str2[i]);
            if (v1 < v2) return -1;
            if (v1 > v2) return 1;
            i++;
        }
        while (i < str1.length) {
            if (Integer.parseInt(str1[i]) != 0) return 1;
            i++;
        }
        while (i < str2.length) {
            if (Integer.parseInt(str2[i]) != 0) return -1;
            i++;
        }
        return 0;
    }
}
