from collections import deque


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.val})"


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        path = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                path.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                path.append("null")

        return ",".join(path)

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(",")
        if not nodes:
            return None

        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()
            if i < len(nodes) and nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1

            if i < len(nodes) and nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1

        return root


def main():
    root = TreeNode(1)
    left_tree = TreeNode(2)
    right_tree = TreeNode(3)
    right_left_subtree = TreeNode(4)
    right_right_subtree = TreeNode(5)

    right_tree.left = right_left_subtree
    right_tree.right = right_right_subtree

    root.left = left_tree
    root.right = right_tree

    codec = Codec()
    assert codec.serialize(root) == "1,2,3,null,null,4,5,null,null,null,null"
    assert codec.deserialize(codec.serialize(root)).left.val == 2

    print("All tests passed!!")


if __name__ == "__main__":
    main()
