package com.leo.utils;

import com.eclipsesource.json.Json;
import com.eclipsesource.json.JsonArray;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class LCUtil {

    public static String char2dToString(char[][] array) {
        if (array == null)
            return "null";
        if (array.length == 0)
            return "[]";
        StringBuilder sb = new StringBuilder("[");
        for (char[] item : array) {
            sb.append(Arrays.toString(item));
            sb.append(",");
        }
        sb.setCharAt(sb.length() - 1, ']');
        return sb.toString();
    }

    public static String int2dArrayToString(int[][] array) {
        if (array == null)
            return "null";
        if (array.length == 0)
            return "[]";
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
        if (input.length() == 0)
            return new int[0];
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
        if (input.length() == 0)
            return new char[0];
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
        if (input.length() == 0)
            return null;

        String[] parts = input.split(",");
        String item = parts[0];
        TreeNode root = new TreeNode(Integer.parseInt(item));
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);

        int index = 1;
        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.remove();
            if (index == parts.length)
                break;
            item = parts[index++];
            item = item.trim();
            if (!item.equals("null")) {
                int leftNumber = Integer.parseInt(item);
                node.left = new TreeNode(leftNumber);
                nodeQueue.add(node.left);
            }
            if (index == parts.length)
                break;
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
        if (jsonArray.size() == 0)
            return new ListNode[0];
        ListNode[] arr = new ListNode[jsonArray.size()];
        for (int i = 0; i < arr.length; i++) {
            JsonArray cols = jsonArray.get(i).asArray();
            arr[i] = stringToListNode(cols.toString());
        }
        return arr;
    }

    public static String treeNodeToString(TreeNode root) {
        if (root == null)
            return "[]";
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
        return ("[" + output.substring(0, output.length() - 2) + "]").replaceAll("((, null)+(?=]))", "");
    }

    public static String listNodeToString(ListNode node) {
        if (null == node)
            return "[]";
        StringBuilder output = new StringBuilder();
        while (null != node) {
            output.append(node).append("->");
            node = node.next;
        }
        return "[" + output.substring(0, output.length() - 2) + "]";
    }

    public static String treeNodeArrayToString(List<TreeNode> treeNodeList) {
        if (null == treeNodeList)
            return "[]";
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
        if (head == null)
            return;
        ListNode p = head, tail = null;
        int i = 0;
        while (p.next != null) {
            if (i++ == tailPos)
                tail = p;
            p = p.next;
        }
        if (i == tailPos)
            tail = p;
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

    public static String[] stringToStringArray(String input) {
        JsonArray jsonArray = Json.parse(input).asArray();
        String[] arr = new String[jsonArray.size()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = jsonArray.get(i).asString();
        }
        return arr;
    }

    public static int[][] stringToInt2dArray(String input) {
        JsonArray jsonArray = Json.parse(input).asArray();
        if (jsonArray.size() == 0)
            return new int[0][0];
        int[][] arr = new int[jsonArray.size()][];
        for (int i = 0; i < arr.length; i++) {
            JsonArray cols = jsonArray.get(i).asArray();
            arr[i] = stringToIntegerArray(cols.toString());
        }
        return arr;
    }

    public static List<List<Integer>> stringToListListInt(String input) {
        List<List<Integer>> out = new ArrayList<>();
        JsonArray jsonArray = Json.parse(input).asArray();
        for (int i = 0; i < jsonArray.size(); i++) {
            JsonArray cols = jsonArray.get(i).asArray();
            List<Integer> c = new ArrayList<>();
            out.add(c);
            for (int j = 0; j < cols.size(); j++) {
                c.add(cols.get(j).asInt());
            }
        }
        return out;
    }

    public static char[][] stringToChar2dArray(String input) {
        JsonArray jsonArray = Json.parse(input).asArray();
        if (jsonArray.size() == 0)
            return new char[0][0];
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
        if (input.length() == 0)
            return new double[0];
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

    public static void showBTree(TreeNode root) {
        if (root == null) System.out.println("EMPTY!");
        // 得到树的深度
        int treeDepth = getTreeDepth(root);

        // 最后一行的宽度为2的（n - 1）次方乘3，再加1
        // 作为整个二维数组的宽度
        int arrayHeight = treeDepth * 2 - 1;
        int arrayWidth = (2 << (treeDepth - 2)) * 3 + 1;
        // 用一个字符串数组来存储每个位置应显示的元素
        String[][] res = new String[arrayHeight][arrayWidth];
        // 对数组进行初始化，默认为一个空格
        for (int i = 0; i < arrayHeight; i++) {
            for (int j = 0; j < arrayWidth; j++) {
                res[i][j] = " ";
            }
        }

        // 从根节点开始，递归处理整个树
        // res[0][(arrayWidth + 1)/ 2] = (char)(root.val + '0');
        writeArray(root, 0, arrayWidth / 2, res, treeDepth);

        // 此时，已经将所有需要显示的元素储存到了二维数组中，将其拼接并打印即可
        for (String[] line : res) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < line.length; i++) {
                sb.append(line[i]);
                if (line[i].length() > 1 && i <= line.length - 1) {
                    i += line[i].length() > 4 ? 2 : line[i].length() - 1;
                }
            }
            System.out.println(sb);
        }
    }

    public static int getTreeDepth(TreeNode root) {
        return root == null ? 0 : (1 + Math.max(getTreeDepth(root.left), getTreeDepth(root.right)));
    }

    private static void writeArray(TreeNode currNode, int rowIndex, int columnIndex, String[][] res, int treeDepth) {
        // 保证输入的树不为空
        if (currNode == null) return;
        // 先将当前节点保存到二维数组中
        res[rowIndex][columnIndex] = String.valueOf(currNode.val);

        // 计算当前位于树的第几层
        int currLevel = ((rowIndex + 1) / 2);
        // 若到了最后一层，则返回
        if (currLevel == treeDepth) return;
        // 计算当前行到下一行，每个元素之间的间隔（下一行的列索引与当前元素的列索引之间的间隔）
        int gap = treeDepth - currLevel - 1;

        // 对左儿子进行判断，若有左儿子，则记录相应的"/"与左儿子的值
        if (currNode.left != null) {
            res[rowIndex + 1][columnIndex - gap] = "/";
            writeArray(currNode.left, rowIndex + 2, columnIndex - gap * 2, res, treeDepth);
        }

        // 对右儿子进行判断，若有右儿子，则记录相应的"\"与右儿子的值
        if (currNode.right != null) {
            res[rowIndex + 1][columnIndex + gap] = "\\";
            writeArray(currNode.right, rowIndex + 2, columnIndex + gap * 2, res, treeDepth);
        }
    }

    /**
     * 通过String构建树
     *
     * @param input 输入字符，用null分割
     * @return 树的根节点
     */
    public static Node stringToNodeTree(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) return null;

        String[] parts = input.split(",");
        String item = parts[0];
        Node root = new Node(Integer.parseInt(item));
        Queue<Node> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);

        int index = 2;
        while (!nodeQueue.isEmpty()) {
            Node node = nodeQueue.poll();
            if (index == parts.length)
                break;
            item = parts[index++].trim();
            while (!item.equals("null")) {
                int val = Integer.parseInt(item);
                if (node.children == null) node.children = new ArrayList<>();
                Node childNode = new Node(val);
                node.children.add(childNode);
                nodeQueue.add(childNode);
                if (index == parts.length)
                    break;
                item = parts[index++].trim();
            }
        }
        return root;
    }

    /**
     * 使用python画出2d数组图像
     * 需要python3安装在环境变量中，同时安装了numpy和matplotlib依赖
     *
     * @param array 2dArray
     */
    public static void drawInt2dArray(int[][] array) {
        StringBuilder code = new StringBuilder();
        if (array.length == 0) return;
        int width = 10, fontSize = 20;
        int row = array.length, col = array[0].length;
        // 画格子
        for (int i = 0; i < row + 1; i++) {
            String lineCode = "[[0, " + i * width + "],[" + col * width + "," + i * width + "]]";
            code.append("    area = ").append(lineCode).append("\n");
            code.append("    draw_points_list(area, marker='o-',  b_ring=False)\n");
            // 刻度
            code.append(String.format("    plt.text(%f, %f, s='%s', size=10)\n", -0.2 * width, (i + 0.5) * width, i));
        }
        for (int i = 0; i < col + 1; i++) {
            String lineCode = "[[" + i * width + ", 0],[" + i * width + "," + row * width + "]]";
            code.append("    area = ").append(lineCode).append("\n");
            code.append("    draw_points_list(area, marker='o-',  b_ring=False)\n");
            // 刻度
            code.append(String.format("    plt.text(%f, %f, s='%s', size=10)\n", (i + 0.5) * width, -0.1 * width, i));
        }
        // 描点
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                double x = (0.5 + i) * width, y = (0.5 + j) * width;
                code.append(String.format("    plt.text(%f, %f, s='%s', size=%d)\n", x, y, array[i][j], fontSize));
            }
        }

        Thread t = new Thread(() -> {
            try {
                String script = "import matplotlib.pyplot as plt" + "\n" +
                        "import numpy as np" + "\n" +
                        "from matplotlib.ticker import MultipleLocator, FormatStrFormatter\n" +
                        "def draw_points_list(points, marker='x',  b_ring=True):" + "\n" +
                        "    pt = points.copy()\n" +
                        "    if  b_ring:\n" +
                        "        pt.append(pt[0])" + "\n" +
                        "    pt = np.array(pt)" + "\n" +
                        "    plt.plot(pt[:, 0], pt[:, 1], marker)" + "\n" +
                        "\n" +
                        "if __name__ == '__main__':\n" +
                        "    plt.figure(figsize=(8,8))\n" +
                        "    plt.axis('equal')\n" +
                        "    plt.axis('off')\n" +
                        "    ax = plt.gca()\n" +
                        "    ax.xaxis.set_ticks_position('top') " + "\n" +
                        "    ax.invert_yaxis() " + "\n" +
                        code +
                        "    plt.show()" + "\n";
                String scriptName = "debug.py";
                OutputStream pyFile = new FileOutputStream(scriptName);
                pyFile.write(script.getBytes(StandardCharsets.UTF_8));
                pyFile.close();
                String[] cmd = new String[]{"python3", scriptName};
                Process process = Runtime.getRuntime().exec(cmd);
                InputStreamReader isr = new InputStreamReader(process.getInputStream());
                BufferedReader br = new BufferedReader(isr);
                String line;
                while ((line = br.readLine()) != null) {
                    System.out.println(line);
                }
                isr = new InputStreamReader(process.getErrorStream());
                br = new BufferedReader(isr);
                while ((line = br.readLine()) != null) {
                    System.out.println(line);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
        t.start();
    }
}
