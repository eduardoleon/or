# Author: Eduardo León
# Date:   September 18th

class Path(object):
    def __init__(self, succ):
        self.__succ = succ
    
    def follow(self, node):
        path = []
        while node != None:
            path.append(node)
            prev, node = node, self.__succ[node]
            self.__succ[prev] = None
        return path

class Graph(object):
    def __init__(self, nodes, infty, symm):
        self.__nodes = nodes
        self.__infty = infty
        self.__symm = symm
        self.__weights = [infty for _ in range(nodes * nodes)]
    
    def __getitem__(self, key):
        i, j = key
        k = self.__nodes * i + j
        return self.__weights[k]
    
    def __setitem__(self, key, value):
        i, j = key
        k = self.__nodes * i + j
        self.__weights[k] = value
        if self.__symm:
            k = self.__nodes * j + i
            self.__weights[k] = value
    
    def shortest_path(self, source, target):
        prev = set(range(self.__nodes))
        succ = dict()
        cost = [self.__infty for _ in range(self.__nodes * self.__nodes)]
        
        # perform a backwards search
        prev.discard(target)
        succ[target] = None
        cost[target] = 0
        
        # while there are unsolved nodes
        while prev:
            best = self.__infty
            cand = []
            
            # update costs
            for i in prev:
                for j in succ:
                    bound = self[i, j] + cost[j]
                    cost[i] = min(cost[i], bound)
                    
                    # update candidates
                    if bound < best:
                        best = bound
                        cand = [(i, j)]
                    elif bound == best:
                        cand.append((i,j))
            
            # promote candidates
            for (i, j) in cand:
                prev.discard(i)
                succ[i] = j
        
        # reconstruct path
        path = Path(succ)
        return path.follow(source)
    
    def minimum_spanning_tree(self, target):
        leaf = set()
        prev = set(range(self.__nodes))
        succ = dict()
        
        # grow the tree backwards
        leaf.add(target)
        prev.discard(target)
        succ[target] = None
        
        # while there are unconnected nodes
        while prev:
            best = self.__infty
            cand = None
            
            # select candidate link
            for i in prev:
                for j in succ:
                    if self[i, j] < best:
                        best = self[i, j]
                        cand = i, j
            
            # promote the candidate
            if cand:
                i, j = cand
                leaf.add(i)
                leaf.discard(j)
                prev.discard(i)
                succ[i] = j
            else:
                break
        
        # compute paths towards the root
        path = Path(succ)
        return [path.follow(source) for source in leaf]
