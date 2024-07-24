class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def print_tree(root, level=0):
    if root is not None:
        print_tree(root.right, level + 1)
        print("  " * level + str(root.data))
        print_tree(root.left, level + 1)

def main():
    root = None
    while True:
        print("\nChoose an option:")
        print("1. Insert a node")
        print("2. Display the tree")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            data = int(input("Enter the data to insert: "))
            root = insert(root, data)
        elif choice == '2':
            if root is None:
                print("Tree is empty.")
            else:
                print_tree(root)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


