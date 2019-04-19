import unittest
from AVL import *
from random import randint

#####################################################################
#                                                                   #
#   There will be other test cases when your code is graded.        #
#   Feel free to add your own test cases here, this file will       #
#   not be submitted. These are just for reference.                 #
#                                                                   #
#####################################################################


# We are just defining some aliases here
# to make it easy to manually write test cases
def mkleaf(a):
    return Node(None, a, None)


# Just for making test cases clearer
def mknode(l, k, r):
    return Node(l, k, r)


class TestAVL(unittest.TestCase):

    # One tree is empty
    def test_OneEmpty(self):
        V = mknode(mkleaf(8), 13, mkleaf(151))
        self.assertTrue(AVL.disjoint(None, V))

    # Both trees are empty
    def test_BothEmpty(self):
        self.assertTrue(AVL.disjoint(None, None))

    # Both trees have some common elements
    def test_Common1(self):
        T = mknode(mknode(mkleaf(1), 2, mkleaf(3)), 8, mkleaf(13))
        V = mknode(mkleaf(8), 13, mkleaf(151))
        self.assertFalse(AVL.disjoint(T, V))

    # Both trees have one common elements
    def test_Common2(self):
        T = mknode(mknode(mkleaf(1), 2, mkleaf(3)), 8, mkleaf(13))
        V = mknode(mknode(mkleaf(13), 14, mkleaf(16)), 17, mkleaf(19))
        self.assertFalse(AVL.disjoint(T, V))

    # Trees have no common elements
    def test_Disjoint1(self):
        T = mknode(mknode(None,
                          7,
                          mkleaf(8)),
                   9,
                   mknode(
            mkleaf(10),
            12,
            mkleaf(21)))
        V = mknode(mkleaf(6),
                   13,
                   mkleaf(15))
        self.assertTrue(AVL.disjoint(T, V))

    # Trees have no elements in common
    def test_Disjoint2(self):
        T = mknode(mkleaf(2),
                   5,
                   mknode(mkleaf(7),
                          9,
                          mkleaf(11)))
        V = mknode(mknode(mkleaf(1),
                          3,
                          mkleaf(6)),
                   8,
                   mkleaf(10))
        self.assertTrue(AVL.disjoint(T, V))


if __name__ == "__main__":
    unittest.main()
