from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_largest_values(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        max_val = float("-inf")
        for _ in range(len(q)):
            node = q.popleft()
            max_val = max(max_val, node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(max_val)

    return result


def main():
    assert find_largest_values(
        TreeNode(
            1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9))
        )
    ) == [1, 3, 9]
    assert find_largest_values(TreeNode(1, TreeNode(2), TreeNode(3))) == [1, 3]

    print("All tests passed!")


if __name__ == "__main__":
    main()
