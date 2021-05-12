# printing a directory tree for a given path

import os


def tree_printer(root):
    for root, dirs, files in os.walk(root):
        for d in dirs:
            print(os.path.join(root, d))
        for f in files:
            print(os.path.join(root, f))


tree_printer('.')

# this is using inbuilt library


from DirectoryTree import TreeGenerator

Tree = TreeGenerator()
Tree.generate('C:\\Users\\XYZ\\ZZZ\\XXX\\Begineer')
