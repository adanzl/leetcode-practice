package com.leo.leetcode.algorithm.q2200;

/**
 * 请你设计一个带光标的文本编辑器，它可以实现以下功能：
 * 1、添加：在光标所在处添加文本。
 * 2、删除：在光标所在处删除文本（模拟键盘的删除键）。
 * 3、移动：将光标往左或者往右移动。
 * 当删除文本时，只有光标左边的字符会被删除。光标会留在文本内，也就是说任意时候 0 <= cursor.position <= currentText.length 都成立。
 * 请你实现 TextEditor 类：
 * 1、TextEditor() 用空文本初始化对象。
 * 2、void addText(string text) 将 text 添加到光标所在位置。添加完后光标在 text 的右边。
 * 3、int deleteText(int k) 删除光标左边 k 个字符。返回实际删除的字符数目。
 * 4、string cursorLeft(int k) 将光标向左移动 k 次。返回移动后光标左边 min(10, len) 个字符，其中 len 是光标左边的字符数目。
 * 5、string cursorRight(int k) 将光标向右移动 k 次。返回移动后光标左边 min(10, len) 个字符，其中 len 是光标左边的字符数目。
 * 提示：
 * 1、1 <= text.length, k <= 40
 * 2、text 只含有小写英文字母。
 * 3、调用 addText ，deleteText ，cursorLeft 和 cursorRight 的 总 次数不超过 2 * 104 次。
 * 链接：https://leetcode.cn/problems/design-a-text-editor
 */
public class Q2296 {

    public static void main(String[] args) {
        TextEditor textEditor = new TextEditor(); // 当前 text 为 "|" 。（'|' 字符表示光标）
        textEditor.addText("leetcode"); // 当前文本为 "leetcode|" 。
        System.out.println(textEditor.deleteText(4)); // 返回 4 当前文本为 "leet|" 。删除了 4 个字符。
        textEditor.addText("practice"); // 当前文本为 "leetpractice|" 。
        System.out.println(textEditor.cursorRight(3)); // 返回 "etpractice"
        System.out.println(textEditor.cursorLeft(8)); // 返回 "leet"
        System.out.println(textEditor.deleteText(10)); // 返回 4 当前文本为 "|practice" 。只有 4 个字符被删除了。
        System.out.println(textEditor.cursorLeft(2)); // 返回 "" 当前文本为 "|practice" 。光标无法移动到文本以外，所以无法移动。"" 是光标左边的 min(10, 0) = 0 个字符。
        System.out.println(textEditor.cursorRight(6)); // 返回 "practi" 当前文本为 "practi|ce" 。"practi" 是光标左边的 min(10, 6) = 6 个字符。
    }

    static class TextEditor {
        Node head, cur;
        int offset = 0;

        public TextEditor() {
            head = new Node("");
            cur = head;
        }

        // 将 text 添加到光标所在位置。添加完后光标在 text 的右边。
        public void addText(String text) {
            Node node = new Node(text);
            Node pre = cur.pre, next = cur.next;
            if (offset > 0) {
                int strLen = cur.str.length();
                Node p1 = new Node(cur.str.substring(0, strLen - offset));
                Node p2 = new Node(cur.str.substring(strLen - offset));
                pre.next = p1;
                p1.pre = pre;
                p1.next = node;
                node.pre = p1;
                node.next = p2;
                p2.pre = node;
                if (null != next) {
                    p2.next = next;
                    next.pre = p2;
                }
                offset = 0;
            } else {
                cur.next = node;
                node.pre = cur;
                if (null != next) {
                    node.next = next;
                    next.pre = node;
                }
            }
            cur = node;
        }

        // 删除光标左边 k 个字符。返回实际删除的字符数目。
        public int deleteText(int k) {
            int ret = 0;
            while (head != cur && k > 0) {
                Node next = cur.next, pre = cur.pre;
                if (offset > 0) {
                    Node newNext = new Node(cur.str.substring(cur.str.length() - offset));
                    cur.str = cur.str.substring(0, cur.str.length() - offset);
                    newNext.next = next;
                    newNext.pre = cur;
                    if (null != next) next.pre = newNext;
                    cur.next = newNext;
                    next = newNext;
                }
                offset = 0;
                int cLen = cur.str.length();
                if (k >= cLen) {
                    cur = pre;
                    pre.next = next;
                    if (null != next) next.pre = pre;
                    ret += cLen;
                } else {
                    cur.str = cur.str.substring(0, cur.str.length() - k);
                    ret += k;
                }
                k -= cLen;
            }

            return ret;
        }

        // 将光标向左移动 k 次。返回移动后光标左边 min(10, len) 个字符，其中 len 是光标左边的字符数目。
        public String cursorLeft(int k) {
            while (head != cur) {
                Node pre = cur.pre;
                if (cur.str.length() - offset >= k) {
                    offset += k;
                    break;
                } else {
                    k -= cur.str.length() - offset;
                    offset = 0;
                    cur = pre;
                }
            }
            return getStr();
        }

        // 将光标向右移动 k 次。返回移动后光标左边 min(10, len) 个字符，其中 len 是光标左边的字符数目。
        public String cursorRight(int k) {
            while (k > 0) {
                Node next = cur.next;
                if (offset >= k) {
                    offset -= k;
                    break;
                } else {
                    k -= offset;
                    if (next == null) {
                        offset = 0;
                        break;
                    }
                    cur = next;
                    offset = cur.str.length();
                }
            }
            return getStr();
        }

        String getStr() {
            StringBuilder ret = new StringBuilder();
            Node p = cur;
            int off = offset;
            while (head != p && ret.length() < 10) {
                ret.insert(0, p.str.substring(0, p.str.length() - off));
                off = 0;
                p = p.pre;
            }
            return ret.substring(ret.length() - Math.min(10, ret.length()));
        }

        static class Node {
            Node(String str) {
                this.str = str;
            }

            String str;
            Node pre, next;
        }
    }
}
