from RBTree import *

root = RBNode(7)
L = RBNode(3)
R = RBNode(9)
root.left = L
root.right = R
L.parent = root
R.parent = root
L.left = t.nil
R.left = t.nil
L.right = t.nil
R.right = t.nil
t.root = root
