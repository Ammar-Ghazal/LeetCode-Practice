# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = ""
        queue = deque()
        queue.append(root)

        while queue:
            cur = queue.popleft()
            if cur == None:
                output += "null,"
            else:
                output += (str(cur.val) + ",")
                queue.append(cur.left)
                queue.append(cur.right)
            
        print(output.split(",")[:-1])
        return output

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        queue = deque()
        data = deque(data.split(",")[:-1])
        firstval = data.popleft()

        if firstval == "null": return None

        root = TreeNode(firstval)
        queue.append(root)

        while data:
            cur = queue.popleft()
            leftTree = data.popleft()
            rightTree = data.popleft()

            if leftTree != "null":
                cur.left = TreeNode(leftTree)
                queue.append(cur.left)
            if rightTree != "null":
                cur.right = TreeNode(rightTree)
                queue.append(cur.right)
        
        return root
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
