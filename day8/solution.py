import io

input = open('input','r')
test_input = io.StringIO("""162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""")

points = [list(map(int, line.split(','))) for line in input]
n_points = len(points)

def dist_sq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2

# compute distance matrix
point_distances = [[0 for _i in range(n_points)] for _j in range(n_points)]
for i in range(n_points):
    for j in range(i):
        point_distances[i][j] = dist_sq(points[i], points[j])
        point_distances[j][i] = point_distances[i][j]

# set the diagonal of distance matrix to maximum distance
max_dist = max(map(max, point_distances))
for i in range(n_points):
    point_distances[i][i] = max_dist + 1

point_distances_flat = []
for i in range(n_points):
    for j in range(i):
        point_distances_flat.append((point_distances[i][j], i, j))

# sort by distance
point_distances_flat.sort(key=lambda v: v[0])

# build graph
n_connections = 1000
connections = 0

graphs = [set([i]) for i in range(n_points)]
def index_graph(graphs, node):
    for i in range(len(graphs)):
        if node in graphs[i]:
            return i
    raise "node {} not found".format(node)
def merge_graphs(graphs_in, g1_id, g2_id):
    graphs = graphs_in.copy()
    if g1_id == g2_id:
        return graphs
    new_graph = graphs[g1_id].union(graphs[g2_id])
    graphs[g1_id] = new_graph
    del graphs[g2_id]
    return graphs

while len(graphs) > 1:
    next_candidate = point_distances_flat.pop(0)
    fr = next_candidate[1]
    to = next_candidate[2]
    graph_fr = index_graph(graphs, fr)
    graph_to = index_graph(graphs, to)
    connections += 1
    graphs = merge_graphs(graphs, graph_fr, graph_to)
    if connections == n_connections:
        graph_sizes = list(map(len, graphs))
        graph_sizes.sort()
        print("Q1", graph_sizes[-1] * graph_sizes[-2] * graph_sizes[-3])

print("Q2", points[fr][0] * points[to][0])