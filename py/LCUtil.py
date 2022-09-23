from typing import *
from collections import *


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def arrayToTreeNode(_input: list[str]) -> TreeNode:
    if not _input: return None

    root: TreeNode = TreeNode(int(_input[0]))
    q = deque()
    q.append(root)

    index: int = 1
    while q:
        node: TreeNode = q.popleft()
        if index == len(_input): break
        item: str = _input[index]
        index += 1
        if "null" != item:
            left_num: int = int(item)
            node.left = TreeNode(left_num)
            q.append(node.left)
        if index == len(_input): break
        item: str = _input[index]
        index += 1
        if "null" != item:
            right_num: int = int(item)
            node.right = TreeNode(right_num)
            q.append(node.right)

    return root


def stringToTreeNode(_input: str) -> TreeNode:
    _input = _input[1:-1]
    return arrayToTreeNode(_input.split(','))


def treeNodeToString(root: TreeNode) -> str:
    if root is None: return "[]"
    ret = []
    q = deque()
    q.append(root)
    while q:
        node: TreeNode = q.popleft()
        if node is None:
            ret.append("null")
            continue
        ret.append(str(node.val))
        q.append(node.left)
        q.append(node.right)
    for i in range(len(ret) - 1, -1, -1):
        if ret[i] == "null":
            del ret[i]
        else : break
    return str(ret)


def treeNodeListToString(treeNodeList: List[TreeNode]) -> str:
    return "[" + ",".join([treeNodeToString(node) for node in treeNodeList]) + "]"
