#################################################################
#                                                               #
#    You will ONLY be submitting AVL.py with your solution,     #
#    and so you should not be changing any of the logic here    #
#    as part of it. If you feel like you need to add any        #
#    temporary variables to debug, thats OK, but make           #
#    sure your solution only depends on this file as it was     #
#    in the starter code.                                       #
#                                                               #
#################################################################


class Node:
    """ 
    Represents a Node in an AVL Tree.
    Each Node stores the following information:
    - parent
    - left / right (children)
    - key
    - hgt (height of subtree rooted at the Node)
    - num (size of subtree rooted at the Node) 

    Note: You can use 
            Node.size(t) and Node.height(t)
        to avoid having to manually check if 't' is None.
    """

    def __init__(self, l, k, r):
        self.parent = None
        self.left = l
        self.right = r
        self.key = k
        if (self.left is not None):
            self.left.parent = self
        if (self.right is not None):
            self.right.parent = self
        self.update()

    def link_left(self, new_child):
        """
        Set new left child (can be null) and updating fields (num, hgt)
        assumes children's fields are correct
        """
        self.left = new_child
        if (new_child is not None):
            self.left.parent = self
        self.update()

    def link_right(self, new_child):
        """
        Set new right child (can be null) and updating fields (num, hgt)
        assumes children's fields are correct
        """
        self.right = new_child
        if (new_child is not None):
            self.right.parent = self
        self.update()

    def update(self):
        """
        Updates the internal data of the node 
        based off the definitions given in class.
        """
        self.num = Node.size(self.left) + Node.size(self.right) + 1
        self.hgt = 1 + max(Node.height(self.left), Node.height(self.right))

    @staticmethod
    def size(node):
        """
        Returns the size of the subtree rooted
        at the node. Use like this:
            Node.size(t)
        """
        return 0 if node is None else node.num

    @staticmethod
    def height(node):
        """
        Returns the height of the subtree rooted
        at the node. Use like this:
            Node.height(t)
        """
        return 0 if node is None else node.hgt

    def __str__(self):
        """
        Prints out the tree rooted at this node as a string

        Eg:

            a
           / \
          b   c
         / \
        d   e

        This tree is represented as
        ((d) b (e)) a (c)

        Use this to help you debug!
        """

        lt = "" if self.left is None else "(" + str(self.left) + ") "
        rt = "" if self.right is None else " (" + str(self.right) + ")"
        return lt + str(self.key) + rt
