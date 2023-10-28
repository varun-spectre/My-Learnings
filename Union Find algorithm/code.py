class UnionFind:
    def __init__(self):
        # Write your code here
        self.parents = {}
        self.rank = {}
        
    # O(1) time | O(1) space  
    def createSet(self, value):
        # Write your code here
        self.parents[value] = value
        self.rank[value] = 0
        
    # O(alpha(n)) time | O(alpha(n)) space
    def find(self, value):
        # Write your code here
        if value not in self.parents:
            return None
        if value !=  self.parents[value]:
            self.parents[value] = self.find(self.parents[value])
        return self.parents[value]
        
    # O(alpha(n)) time | O(alpha(n)) space
    def union(self, valueOne, valueTwo):
        # Write your code here
        parent1 = self.find(valueOne)
        
        parent2 = self.find(valueTwo)
        
        if parent1 is None or parent2 is None:
            return
            
        rank1 = self.rank[parent1]
        rank2 = self.rank[parent2]

        if rank1 < rank2:
            self.parents[parent1] = parent2
        elif rank1 > rank2:
            self.parents[parent2] = parent1
        else:
            self.parents[parent1] = parent2
            self.rank[parent2] += 1