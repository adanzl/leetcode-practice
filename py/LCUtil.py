import json
from typing import Deque, List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return treeNodeToString(self)


class ListNode:
    __slots__ = ['val', 'next']

    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return listNodeToString(self)


def arrayToTreeNode(_input: list[str]) -> Optional[TreeNode]:
    if not _input: return None

    root: TreeNode = TreeNode(int(_input[0]))
    q = Deque()
    q.append(root)

    index: int = 1
    while q:
        node: TreeNode = q.popleft()
        if index == len(_input): break
        item: str = _input[index].strip()
        index += 1
        if "null" != item:
            left_num: int = int(item)
            node.left = TreeNode(left_num)
            q.append(node.left)
        if index == len(_input): break
        item: str = _input[index].strip()
        index += 1
        if "null" != item:
            right_num: int = int(item)
            node.right = TreeNode(right_num)
            q.append(node.right)

    return root


def stringToTreeNode(_input: str) -> Optional[TreeNode]:
    _input = _input[1:-1]
    if not _input: return None
    return arrayToTreeNode(_input.split(','))


def treeNodeToString(root: TreeNode) -> str:
    if root is None: return "[]"
    ret = []
    q = Deque()
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
        else:
            break
    return '[' + ','.join(ret) + ']'


def treeNodeListToString(treeNodeList: List[TreeNode]) -> str:
    return "[" + ",".join([treeNodeToString(node) for node in treeNodeList]) + "]"


def stringToListNode(_input: str) -> Optional[ListNode]:
    nodeValues = _input[1:-1].split(",")
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for item in nodeValues:
        ptr.next = ListNode(int(item))
        ptr = ptr.next
    return dummyRoot.next


def listNodeToString(node: Optional[ListNode]) -> str:
    if node is None:
        return "[]"
    ans = []
    while node is not None:
        ans.append(str(node.val))
        node = node.next

    return "[" + ",".join(ans) + "]"
