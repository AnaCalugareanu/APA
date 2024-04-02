from collections import defaultdict, deque


class ExploreDFS:
    #Depth-First Search

    def __init__(self):
        self.connections = defaultdict(list)

    def linkNodes(self, node1, node2):
        #Link two nodes in the graph
        self.connections[node1].append(node2)

    def exploreFromNode(self, node, seen):
        #Recursively explore connected nodes
        seen.add(node)
        for adjacent in self.connections[node]:
            if adjacent not in seen:
                self.exploreFromNode(adjacent, seen)

    def traverse(self, startNode):
        #Start DFS traversal from a given node
        visitedNodes = set()
        self.exploreFromNode(startNode, visitedNodes)


class ExploreBFS:
    # Breadth-First Search

    def __init__(self):
        self.nodeLinks = defaultdict(list)

    def connect(self, node1, node2):
        #Connect two nodes bidirectionally
        self.nodeLinks[node1].append(node2)
        self.nodeLinks[node2].append(node1)

    def printGraph(self):
        #Print the adjacency list of the graph
        for node, edges in self.nodeLinks.items():
            print(f'{node}: {edges}')

    def traverseFrom(self, rootNode):
        #Perform BFS starting from rootNode
        toVisit = deque()
        largestNode = max(self.nodeLinks.keys(), default=-1)
        visited = [False] * (largestNode + 1)

        visited[rootNode] = True
        toVisit.append(rootNode)

        while toVisit:
            current = toVisit.popleft()
            for neighbour in self.nodeLinks[current]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    toVisit.append(neighbour)
