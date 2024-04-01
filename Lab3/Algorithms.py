from collections import defaultdict, deque


class NetworkMap:

    def __init__(self):
        self.connections = defaultdict(list)

    def linkNodes(self, node1, node2):
        self.connections[node1].append(node2)

    def _exploreDFS(self, node, seen):
        seen.add(node)
        print(node, end=' ')

        for adjacent in self.connections[node]:
            if adjacent not in seen:
                self._exploreDFS(adjacent, seen)

    def traverseDFS(self, startNode):
        seen = set()
        self._exploreDFS(startNode, seen)

    def traverseBFS(self, startNode):
        queue = deque()
        seen = [False] * (max(self.connections.keys()) + 1)

        seen[startNode] = True
        queue.append(startNode)

        while queue:
            currentNode = queue.popleft()
            print(currentNode, end=" ")

            for adjacent in self.connections[currentNode]:
                if not seen[adjacent]:
                    seen[adjacent] = True
                    queue.append(adjacent)
