def findClosestValueInBst(tree, target):
    return helper(tree, target, float('inf'))

def helper(tree, target, closest):
    if tree is None:
        return closest

    if abs(closest - target) > abs(tree.value - target):
        closest = tree.value

    if tree.value > target:
        return helper(tree.left, target, closest)
    elif tree.value < target:
        return helper(tree.right, target, closest)
    else: 
        return tree.value
    


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
