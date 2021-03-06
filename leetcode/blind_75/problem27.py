'''Probelm 105: Construct Binary Tree from Preorder and Inorder Traversal

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    '''The root is found at the first index in preorder. 
    The values to the left of the root in inorder is the left subtree.
    The values to the right of the root in inorder is the right subtree.
    '''
    if inorder:
        idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[idx])
        root.left(self.build_tree(preorder, inorder[:idx]))
        root.right(self.build_tree(preorder, inorder[idx+1:]))
        return root
        