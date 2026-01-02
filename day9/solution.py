import io

input = open('input','r')
test_input = io.StringIO("""7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""")

points = [list(map(int, line.split(','))) for line in input]
n_points = len(points)

def rect_area(p1, p2):
    dx = abs(p1[0] - p2[0]) + 1
    dy = abs(p1[1] - p2[1]) + 1
    return dx * dy

max_area = 0
for i in range(n_points):
    for j in range(i):
        area = rect_area(points[i], points[j])
        max_area = max(area, max_area)

print("Q1", max_area)

def line_cuts_rect(r1, r2, pt1, pt2):
    if max(pt1[0], pt2[0]) <= min(r1[0], r2[0]) or max(r1[0], r2[0]) <= min(pt1[0], pt2[0]):
        outside_0 = True
    else:
        outside_0 = False
    if max(pt1[1], pt2[1]) <= min(r1[1], r2[1]) or max(r1[1], r2[1]) <= min(pt1[1], pt2[1]):
        outside_1 = True
    else: 
        outside_1 = False
    return not outside_0 and not outside_1

lines = [(points[i], points[(i+1)%len(points)]) for i in range(len(points))]

max_area = 0
for i in range(n_points):
    for j in range(i):
        coords_i = points[i]
        coords_j = points[j]
        area = rect_area(coords_i, coords_j)
        if area > max_area:
            if any(map(lambda p: line_cuts_rect(coords_i, coords_j, p[0], p[1]), lines)):
                pass
            else:
                max_area = max(area, max_area)

print("Q2", max_area)
