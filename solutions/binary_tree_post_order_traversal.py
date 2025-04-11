from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def post_order_traversal(root: TreeNode | None) -> list[int]:
    if not root:
        return []

    stack = [root]
    path_stack = []
    result = []

    while stack:
        node = stack[-1]

        if path_stack and path_stack[-1] == node:
            result.append(node.val)
            path_stack.pop()
            stack.pop()
        else:
            path_stack.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return result


def post_order_traversal_2_stack_hack(root: TreeNode | None) -> list[int]:
    if not root:
        return []

    stack = [root]
    path_stack = []

    while stack:
        node = stack.pop()
        path_stack.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return path_stack[::-1]


def main():
    assert post_order_traversal(None) == []
    assert post_order_traversal_2_stack_hack(None) == []

    root = TreeNode(1)
    left_tree = TreeNode(2)
    right_tree = TreeNode(3)
    right_left_subtree = TreeNode(4)
    right_right_subtree = TreeNode(5)

    right_tree.left = right_left_subtree
    right_tree.right = right_right_subtree

    root.left = left_tree
    root.right = right_tree

    assert post_order_traversal(root) == [2, 4, 5, 3, 1]
    assert post_order_traversal_2_stack_hack(root) == [2, 4, 5, 3, 1]

    print("All test cases passed.")


if __name__ == "__main__":
    main()
