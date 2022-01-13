package com.leo.interview;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

public class TestBTree {

    public static void main(String[] args) {

        TreeNode root = LCUtil.stringToTreeNode("[1,2,3,4,5,6,7]");
        LCUtil.showBTree(root);
        rOrderVisit(root);
        lOrderVisit(root);
        mOrderVisit(root);
    }

    static void rOrderVisit(TreeNode root) {
        System.out.print("rOrder: ");
        TreeNode[] nStack = new TreeNode[100];
        int[] fStack = new int[100];
        int top = -1;
        TreeNode p = root;
        while (top != -1 || p != null) {
            if (p != null) {
                nStack[++top] = p;
                fStack[top] = 0;
                p = p.left;
            } else {
                int flag = fStack[top];
                p = nStack[top--];
                if (flag == 0) {
                    nStack[++top] = p;
                    fStack[top] = 1;
                    p = p.right;
                } else {
                    System.out.print("[" + p.val + " " + (top + 2) + "]-");
                    p = null;
                }
            }
        }
        System.out.println(" ");
    }

    static void lOrderVisit(TreeNode root) {
        System.out.print("lOrder: ");
        TreeNode[] stack = new TreeNode[100];
        int top = -1;
        TreeNode p = root;
        while (p != null || top != -1) {
            if (p != null) {
                stack[++top] = p;
                System.out.print(p.val + "-");
                p = p.left;
            } else {
                p = stack[top--].right;
            }
        }
        System.out.println(" ");
    }

    static void mOrderVisit(TreeNode root) {
        System.out.print("mOrder: ");
        TreeNode[] stack = new TreeNode[100];
        int top = -1;
        TreeNode p = root;
        while (p != null || top != -1) {
            if (p != null) {
                stack[++top] = p;
                p = p.left;
            } else {
                p = stack[top--];
                System.out.print(p.val + "-");
                p = p.right;
            }
        }
        System.out.println(" ");
    }

}
