package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.TreeNode;

import java.util.LinkedList;
import java.util.Queue;

/**
 * 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
 * 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
 * 说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
 * 链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
 */
public class Q297 {

    public static void main(String[] args) {
        new Q297().TestOJ();
    }

    public void TestOJ() {
        Codec obj = new Codec();
        TreeNode tn;
        tn = obj.deserialize("[1,2,null,3,null,4,null,5]");
        System.out.println(obj.serialize(tn));
        System.out.println(obj.deserialize(obj.serialize(tn)));
        tn = obj.deserialize("[5,4,7,3,null,2,null,-1,null,9]");
        System.out.println(obj.serialize(tn));
        System.out.println(obj.deserialize(obj.serialize(tn)));
        tn = obj.deserialize("[1,2,3,null,null,4,5]");
        System.out.println(obj.serialize(tn));
        System.out.println(obj.deserialize(obj.serialize(tn)));
    }

    public static class Codec {

        // Encodes a tree to a single string.
        public String serialize(TreeNode root) {
            StringBuilder sb = new StringBuilder();
            Queue<TreeNode> q = new LinkedList<>();
            q.add(root);
            while (!q.isEmpty()) {
                TreeNode tn = q.remove();
                if (tn == null) {
                    sb.append("null");
                } else {
                    sb.append(tn.val);
                    q.add(tn.left);
                    q.add(tn.right);
                }
                sb.append(",");
            }
            return "[" + sb.substring(0, sb.length() - 1) + "]";
        }

        // Decodes your encoded data to tree.
        public TreeNode deserialize(String data) {
            String[] arr = data.substring(1, data.length() - 1).split(",");
            if (arr.length == 0) return null;
            TreeNode root = createNode(arr[0]);
            Queue<TreeNode> q = new LinkedList<>();
            q.add(root);
            int offset = 1, iArr = 1;
            while (iArr < arr.length) {
                for (int i = 0; i < offset; i++) {
                    TreeNode tn = q.poll();
                    if (tn == null) continue;
                    tn.left = createNode(arr[iArr++]);
                    q.add(tn.left);
                    if (iArr == arr.length) break;
                    tn.right = createNode(arr[iArr++]);
                    q.add(tn.right);
                }
                offset *= 2;
            }

            return root;
        }

        private TreeNode createNode(String val) {
            val = val.trim();
            if ("null".equals(val)) {
                return null;
            }
            return new TreeNode(Integer.parseInt(val));
        }
    }
}
