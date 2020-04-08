# This class takes in a postfix expression and creates the expression tree to solve the function for some input.
class ExpressionTree:
    def __init__(self, postfix):
        self.operators = ['^', '*', '/', '+', '-']
        self.root = self.convert(postfix)

    # Converts the postfix expression to an expression tree
    def convert(self, postfix):
        stack = []
        for token in postfix:
            if token == 'x':
                node = self.Node(token)
                stack.append(node)
            elif token not in self.operators:
                node = self.Node(float(token))
                stack.append(node)
            else:
                node = self.Node(token)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)

        head = stack.pop()
        # If the stack is not empty at this point there was a problem with the user's expression
        if len(stack) > 0:
            raise IndexError
        return head

    # This is the function called outside the class to evaluate the function for a given x value
    def evaluate(self, val):
        result = self.calc(self.root, val)
        return result

    # Recursive function that evaluates an expression tree for a given x value
    def calc(self, node, val):
        if node.val == 'x':
            return val
        elif node.val not in self.operators:
            return node.val
        elif node.val == '^':
            return self.calc(node.left, val) ** self.calc(node.right, val)
        elif node.val == '*':
            return self.calc(node.left, val) * self.calc(node.right, val)
        elif node.val == '/':
            return self.calc(node.left, val) / self.calc(node.right, val)
        elif node.val == '+':
            return self.calc(node.left, val) + self.calc(node.right, val)
        else:
            return self.calc(node.left, val) - self.calc(node.right, val)

    # Nested class that represents the nodes of the tree
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right