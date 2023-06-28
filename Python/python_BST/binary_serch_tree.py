class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return BST(key)

    if root.value == key:
        return root
    elif root.value < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
   
    return root

def search(root, key):
    if root is None or root.value == key:
        return root
    if root.value < key:
        return search(root.right, key)
    if root.value > key:
        return search(root.left, key)


def delete(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = delete(root.left, key)
    
    elif key > root.value:
        root.right = delete(root.right, key)
    
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


if __name__ == "__main__":
    bst = BST(10)
    r = insert(bst, 5)
    r = insert(bst, 1)
    r = insert(bst, 11)
    r = insert(bst, 4)
    
    inorder(r)

    print("\nDelete 1")
    root = delete(bst, 1)
    inorder(root)

    print("\nfinding 5")
    root = search(bst, 5)
    inorder(root)

    