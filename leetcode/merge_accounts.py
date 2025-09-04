from typing import List


class Node:

    def __init__(self, val, children):
        self.val = val
        self.children = children # can this be a set

class Solution:

    # Question: Mantain sorted order?

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        roots = {}
        res = []

        for acct in accounts:
            # create trees
            emails = sorted(acct[1:])
            root = roots.setdefault(acct[0], Node(acct[0], set()))
            self.insert(root, emails)
        	
	
        for acct, root in roots.items():
            # root is the acct rootnode. This can contain multiple account groups.
            # each child of the root is the start of a new acct group.
            for newGroupEmailRoot in root.children:
                newGroup = [] 
                self.addAccount(newGroupEmailRoot, newGroup)
	        print(newGroup)
                res.append([acct] + newGroup.sort()) # O(O(m log m) + O(m) * n)

        return res

    def insert(self, root: Node, emails: List[str]):
        # Create email tree based on the same account name
        for email in emails:
            children = root.children
            if email in children:
                # set the root to the already existing child
                root = children[email]
            else:
                print("Adding new child to root " + root.val + " of value " + email)
                newChild = Node(email, set())
                children.add(newChild)
                root = newChild
                
    def addAccount(self, root: Node, group: List[str]):
        print(group)
        # This is just a DFS that visits every node
        # and adds them to the group.
        if root:
            group.append(root.val)
            for child in root.children:
                self.addAccount(child, group)
        



            
        
