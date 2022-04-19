package com.leo.leetcode.algorithm.q0300;

import java.util.Stack;

/**
 * 假设有一个同时存储文件和目录的文件系统。下图展示了文件系统的一个示例：
 * 这里将 dir 作为根目录中的唯一目录。dir 包含两个子目录 subdir1 和 subdir2 。subdir1 包含文件 file1.ext 和子目录 subsubdir1；subdir2 包含子目录 subsubdir2，该子目录下包含文件 file2.ext 。
 * 在文本格式中，如下所示(⟶表示制表符)：
 * dir
 * ⟶ subdir1
 * ⟶ ⟶ file1.ext
 * ⟶ ⟶ subsubdir1
 * ⟶ subdir2
 * ⟶ ⟶ subsubdir2
 * ⟶ ⟶ ⟶ file2.ext
 * 如果是代码表示，上面的文件系统可以写为 "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 。'\n' 和 '\t' 分别是换行符和制表符。
 * 文件系统中的每个文件和文件夹都有一个唯一的 绝对路径 ，即必须打开才能到达文件/目录所在位置的目录顺序，所有路径用 '/' 连接。上面例子中，指向 file2.ext 的 绝对路径 是 "dir/subdir2/subsubdir2/file2.ext" 。
 * 每个目录名由字母、数字和/或空格组成，每个文件名遵循 name.extension 的格式，其中 name 和 extension由字母、数字和/或空格组成。
 * 给定一个以上述格式表示文件系统的字符串 input ，返回文件系统中 指向 文件 的 最长绝对路径 的长度 。 如果系统中没有文件，返回 0。
 * 提示：
 * 1、1 <= input.length <= 10^4
 * 2、input 可能包含小写或大写的英文字母，一个换行符 '\n'，一个制表符 '\t'，一个点 '.'，一个空格 ' '，和数字。
 * 链接：https://leetcode-cn.com/problems/longest-absolute-file-path
 */
public class Q388 {

    public static void main(String[] args) {
        // 20
        System.out.println(new Q388().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"));
        // 32
        System.out.println(new Q388().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"));
        // 0
        System.out.println(new Q388().lengthLongestPath("a"));
        // 12
        System.out.println(new Q388().lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt"));
    }

    public int lengthLongestPath(String input) {
        String[] paths = input.split("\n");
        Stack<Integer> stack = new Stack<>();
        int ret = 0;
        for (String path : paths) {
            int ct = 0, iDot = -1;
            for (char c : path.toCharArray()) {
                if (c == '\t') ct++;
                if (c == '.') iDot = ct;
            }
            while (stack.size() > ct) stack.pop();
            if (iDot == -1) {
                stack.push(path.length() - ct);
            } else {
                int len = path.length() - ct, i = 0;
                while (i < ct) len += stack.get(i++) + 1;
                ret = Math.max(ret, len);
            }
        }
        return ret;
    }
}
