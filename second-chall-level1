from __future__ import print_function
def solution(h, q):
    
    class Node(object):
        def __init__(self, val):
            self.val = val
            self.right = None
            self.left = None
            self.level = 1

        def add_node(self, val, max_level):
            if self.level < max_level:
                if self.left is None:
                    self.left = Node(0)
                    self.left.level = self.level + 1
                    self.left.add_node(val, max_level)
                elif self.left.val == 0:
                    self.left.add_node(val, max_level)
                elif self.val == 0:
                    if self.right is None:
                        self.right = Node(0)
                        self.right.level = self.level + 1
                        self.right.add_node(val, max_level)
                    elif self.right.val == 0:
                        self.right.add_node(val, max_level)
                    else:
                        self.val = val
                else:
                    if self.right is None:
                        self.right = Node(0)
                        self.right.level = self.level + 1
                        self.right.add_node(val, max_level)
                    elif self.right.val == 0:
                        self.right.add_node(val, max_level)
                    else:
                        self.val = val
            else:
                self.val = val


        def giveback(self, val, topper):
            if val >= topper or val <= 0:
                return (-1)
            else:
                if val < self.left.val:
                    return self.left.giveback(val,topper)
                elif val == self.left.val:
                    return (self.val)
                elif val < self.right.val:
                    return self.right.giveback(val,topper)
                elif val == self.right.val:
                    return (self.val)
    
    
    
    top = (2**h)-1
    response = Node(top)
    for i in range(1,top):
        response.add_node(i,h)

    sol = []
    for num in q:
        i = response.giveback(num,top)
        sol.append(i)
    print(*sol,sep=",")
