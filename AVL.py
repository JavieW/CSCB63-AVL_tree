from Node import *

#################################################################
#                                                               #
#    Define any helper functions you need in this file only.    #
#    Make sure you take a look at Node.py to get familiar       #
#    with how we are storing the AVL tree, and the functions    #
#    provided. A few test cases are provided in Test.py.        #
#    You can test your code by running                          #
#               python Test.py                                  #
#    in the directory where the files are located.              #
#                                                               #
#    Please use Python 2.7.x. Python 3-specific features        #
#    may not work when being autograded.                        #
#                                                               #
#################################################################


class AVL():

    @staticmethod
    def disjoint(T, V):
        """
        Return True if T and V are disjoint (have no
        elements in common), and False otherwise.
        """
        # for efficiency the first parameter in intersect have more nodes
        if Node.size(T) >= Node.size(V) :
            t = AVL.intersect(T, V)
        else:
            t = AVL.intersect(V, T)

        return True if t is None else False

    @staticmethod
    def delete_max(T):
        """
        Delete the max key in T, return (T, k)
        where output T is the munipulated tree from input T
        and k the is the max value stored in input T
        Node -> (Node, obj)
        """
        cur = T
        # if T is None, there is no max in T
        if cur is None:
            k = None
        else:
            # max key at the right conner
            while cur.right is not None:
                cur = cur.right
            k = cur.key
            # if T has no right child, then cur still be root
            if cur.parent is None:
                # delete cur node, set T to be its left child
                # not update height required
                T = cur.left
                # break the line T.parent if T is not None
                if T is not None:
                    T.parent = None
            # if T has a right child
            else:
                # delete cur node by linking par.right to cur.left
                par = cur.parent
                par.link_right(cur.left)
                # update height from par up to root
                while par.parent != None:
                    par = par.parent
                    par.update()
                    # rebalance the tree based on the changing of height
                    AVL.rebalance(par)
        return (T, k)

    @staticmethod
    def ccw_rotation(x):
        """
        rotate x in counter clock wise order
        Node -> Node
        """
        k = x.right
        x.link_right(k.left)
        k.link_left(x)
        return k
    
    @staticmethod
    def cw_rotation(x):
        """
        rotate x in clock wise order
        Node -> Node
        """        
        k = x.left
        x.link_left(k.right)
        k.link_right(x)
        return k
 
    @staticmethod
    def rebalance(x):
        """
        single or double rotate on node x
        Node -> Node
        """
        # get the balance factor for x
        hl = Node.height(x.left)
        hr = Node.height(x.right)
        bf_x = hl - hr
        # if balance factor for x is -2
        if bf_x == -2 :
            # get the balance factor for x's right child
            r_hl = Node.height(x.right.left)
            r_hr = Node.height(x.right.right)
            bf_r = r_hl - r_hr
            # if bf_r is 1 do a double rotation
            if bf_r == 1:
                x.link_right(AVL.cw_rotation(x.right))
            return AVL.ccw_rotation(x)
        # if balance factor for x is 2
        elif bf_x == 2:
            #get the balance factor for x's left child
            l_hl = Node.height(x.left.left)
            l_hr = Node.height(x.left.right)
            bf_l = l_hl - l_hr
            # if bf_l is -1 do a double rotation
            if bf_l == -1:
                x.link_left(AVL.ccw_rotation(x.left))
            return AVL.cw_rotation(x)
        # otherwise no rotation needed
        return x

    @staticmethod
    def merge(T, k, V):
        # param k is opt, if null assign max key in T
        # assume keys in T less than keys in V
        if k is None:
            (T, k) = AVL.delete_max(T)
            # if k still None return V
            if k is None:
                return V
        if Node.height(T) > Node.height(V) + 1:
            # T much taller, insert V as subtree in T
            n = T
            while Node.height(n.right) > Node.height(V) + 1 :
                n = n.right
            # insert a new node between n and n.right
            # with right subtree V, left subtree n's right child.
            p = Node(n.right, k, V)
            n.link_right(p)
            #rebalance at n up to the root
            while n.parent != None :
                n.parent.link_right(AVL.rebalance(n))
                n = n.parent
            T = AVL.rebalance(T)
            return T
        # opposite case the same - just inverted
        elif Node.height(V) > Node.height(T) + 1:
            # V much taller, insert T as subtree in V
            n = V
            while Node.height(n.left) > Node.height(T) + 1 :
                n = n.left
            # insert a new node between n and n.left
            # with left subtree T, right subtree n's left child.
            p = Node(T, k, n.left)
            n.link_left(p)
            #rebalance at n up to the root
            while n.parent != None :
                n.parent.link_left(AVL.rebalance(n))
                n = n.parent
            V = AVL.rebalance(V)
            return V            
        else: # heights are within 1
            # make k the root of a new tree W and add T as left and V as right
            return Node(T, k, V)

    @staticmethod
    def split(T, k):
        # if T is None, T<k and T>k are both none and no k in T
        if T == None:
            return (None, False, None)
        else:
            r = T.key
            if r == k :
                return (T.left, True, T.right)
            elif r < k:
                # go down the right path, add r and r's left child L to Tltk
                # b is bool if k in T, recurse on r's right child R
                (Tltk, b, Tgtk) = AVL.split(T.right, k)
                return (AVL.merge(T.left, r, Tltk), b, Tgtk)
            else: #r > k
                # go down the left path, add r and r's right child R to Tgtk
                (Tltk, b, Tgtk) = AVL.split(T.left, k)
                return (Tltk, b, AVL.merge(Tgtk, r, T.right))

    @staticmethod
    def intersect(T, V):
        # base case
        if T is None or V is None :
            return None
        else:
            k = V.key
            (Tltk,hask,Tgtk) = AVL.split(T, k)
            VL = V.left
            VR = V.right
            L = AVL.intersect(Tltk,VL)
            R = AVL.intersect(Tgtk,VR)
            if hask:
                return AVL.merge(L, k, R)
            else:
                return AVL.merge(L, None, R)