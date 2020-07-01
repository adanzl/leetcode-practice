package com.leo.utils;

import com.eclipsesource.json.Json;
import com.eclipsesource.json.JsonArray;

import java.util.*;

public class LCUtil {

    public static String int2dArrayToString(int[][] array) {
        if (array == null) return "null";
        if (array.length == 0) return "[]";
        StringBuilder sb = new StringBuilder("[");
        for (int[] item : array) {
            sb.append(Arrays.toString(item));
            sb.append(",");
        }

        sb.setCharAt(sb.length() - 1, ']');
        return sb.toString();
    }

    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) return new int[0];
        String[] parts = input.split(",");
        int[] output = new int[parts.length];
        for (int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Integer.parseInt(part);
        }
        return output;
    }

    public static char[] stringToCharArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) return new char[0];
        String[] parts = input.split(",");
        char[] output = new char[parts.length];
        for (int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = part.charAt(1);
        }
        return output;
    }

    public static TreeNode stringToTreeNode(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) return null;

        String[] parts = input.split(",");
        String item = parts[0];
        TreeNode root = new TreeNode(Integer.parseInt(item));
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);

        int index = 1;
        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.remove();
            if (index == parts.length) break;
            item = parts[index++];
            item = item.trim();
            if (!item.equals("null")) {
                int leftNumber = Integer.parseInt(item);
                node.left = new TreeNode(leftNumber);
                nodeQueue.add(node.left);
            }
            if (index == parts.length) break;
            item = parts[index++];
            item = item.trim();
            if (!item.equals("null")) {
                int rightNumber = Integer.parseInt(item);
                node.right = new TreeNode(rightNumber);
                nodeQueue.add(node.right);
            }
        }
        return root;
    }

    public static ListNode stringToListNode(String input) {
        // Generate array from the input
        int[] nodeValues = stringToIntegerArray(input);
        // Now convert that list into linked list
        ListNode dummyRoot = new ListNode(0);
        ListNode ptr = dummyRoot;
        for (int item : nodeValues) {
            ptr.next = new ListNode(item);
            ptr = ptr.next;
        }
        return dummyRoot.next;
    }

    public static ListNode[] stringToListNodeArray(String input) {
        JsonArray jsonArray = Json.parse(input).asArray();
        if (jsonArray.size() == 0) return new ListNode[0];
        ListNode[] arr = new ListNode[jsonArray.size()];
        for (int i = 0; i < arr.length; i++) {
            JsonArray cols = jsonArray.get(i).asArray();
            arr[i] = stringToListNode(cols.toString());
        }
        return arr;
    }

    public static String treeNodeToString(TreeNode root) {
        if (root == null) return "[]";
        StringBuilder output = new StringBuilder();
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);
        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.remove();
            if (node == null) {
                output.append("null, ");
                continue;
            }
            output.append(node.val).append(", ");
            nodeQueue.add(node.left);
            nodeQueue.add(node.right);
        }
        return "[" + output.substring(0, output.length() - 2) + "]";
    }

    public static String listNodeToString(ListNode node) {
        if (null == node) return "[]";
        StringBuilder output = new StringBuilder();
        while (null != node) {
            output.append(node).append("->");
            node = node.next;
        }
        return "[" + output.substring(0, output.length() - 2) + "]";
    }

    public static String treeNodeArrayToString(List<TreeNode> treeNodeList) {
        if (null == treeNodeList) return "[]";
        StringBuilder output = new StringBuilder();
        Queue<TreeNode> q = new LinkedList<>();
        for (TreeNode treeNode : treeNodeList) {
            StringBuilder line = new StringBuilder();
            q.add(treeNode);
            while (!q.isEmpty()) {
                TreeNode p = q.poll();
                if (p == null) {
                    line.append("null").append(',');
                    continue;
                }
                line.append(p.val).append(',');
                q.add(p.left);
                q.add(p.right);
            }
            output.append("[").append(line.substring(0, line.length() - 2)).append("],");
        }
        return "[" + output.substring(0, output.length() - 2) + "]";
    }

    public static void buildListNode(ListNode head, int tailPos) {
        if (head == null) return;
        ListNode p = head, tail = null;
        int i = 0;
        while (p.next != null) {
            if (i++ == tailPos) tail = p;
            p = p.next;
        }
        if (i == tailPos) tail = p;
        p.next = tail;
    }

    public static List<String> stringToStringList(String input) {
        JsonArray jsonArray = Json.parse(input).asArray();
        List<String> ret = new ArrayList<>();
        for (int i = 0; i < jsonArray.size(); i++) {
            ret.add(jsonArray.get(i).asString());
        }
        return ret;
    }

//    public static String[] stringToStringArray(String input) {
//        JsonArray jsonArray = Json.parse(input).asArray();
//        String[] arr = new String[jsonArray.size()];
//        for (int i = 0; i < arr.length; i++) {
//            arr[i] = jsonArray.get(i).asString();
//        }
//        return arr;
//    }

    public static int[][] stringToInt2dArray(String input) {
        JsonArray jsonArray = Json.parse(input).asArray();
        if (jsonArray.size() == 0) return new int[0][0];
        int[][] arr = new int[jsonArray.size()][];
        for (int i = 0; i < arr.length; i++) {
            JsonArray cols = jsonArray.get(i).asArray();
            arr[i] = stringToIntegerArray(cols.toString());
        }
        return arr;
    }

    public static char[][] stringToChar2dArray(String input) {
        JsonArray jsonArray = Json.parse(input).asArray();
        if (jsonArray.size() == 0) return new char[0][0];
        char[][] arr = new char[jsonArray.size()][];
        for (int i = 0; i < arr.length; i++) {
            JsonArray cols = jsonArray.get(i).asArray();
            arr[i] = stringToCharArray(cols.toString());
        }
        return arr;
    }

    public static double[] stringToDoubleArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) return new double[0];
        String[] parts = input.split(",");
        double[] output = new double[parts.length];
        for (int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Double.parseDouble(part);
        }
        return output;
    }

    public static List<List<String>> stringToListListString(String input) {
        List<List<String>> out = new ArrayList<>();
        JsonArray jsonArray = Json.parse(input).asArray();
        for (int i = 0; i < jsonArray.size(); i++) {
            JsonArray cols = jsonArray.get(i).asArray();
            List<String> c = new ArrayList<>();
            out.add(c);
            for (int j = 0; j < cols.size(); j++) {
                c.add(cols.get(j).asString());
            }
        }
        return out;
    }

    public static void calcRun(Runnable r) {
        long start_time = System.currentTimeMillis();
        r.run();
        System.out.println("[Running time]: " + (System.currentTimeMillis() - start_time));
    }

}
