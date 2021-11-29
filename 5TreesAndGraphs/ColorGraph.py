class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]
color_set = set()
color_set.add(1)
color_set.add(2)
color_set.add(3)
color_set.add(4)

for node in graph:
    illegal_colors = set([
        neighbor.color
        for neighbor in node.neighbors
        if neighbor.color
    ])

    # Assign the first legal color
    for color in color_set:
        if color not in illegal_colors:
            node.color = color
            print(node.color)
            break