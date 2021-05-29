class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def search(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)

    return search(root.left, key)


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root, sorted_list=[]):
    if root:
        inorder(root.left)
        sorted_list.append(root.val)
        inorder(root.right)

    return sorted_list


def tree_sort(arr):  # 0(nlgn)
    r = Node(arr[0])
    for i in range(1, len(arr)):
        r = insert(r, arr[i])
    return inorder(r)
