class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf_node = False

class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        root = TrieNode()
        res = []
        folder.sort()

        for fld in folder:
            curr_folder = fld[1:].split('/')
            temp = root
            n = len(curr_folder)
            index = 0
            
            while index < n and temp.children and curr_folder[index] in temp.children:
                temp = temp.children[curr_folder[index]]
                index += 1
            
            if temp.is_leaf_node:
                continue
            
            while index < n:
                temp.children[curr_folder[index]] = TrieNode()
                temp = temp.children[curr_folder[index]]
                index += 1
            temp.is_leaf_node = True
            res.append(fld)

        return res