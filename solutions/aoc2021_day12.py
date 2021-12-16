from collections import defaultdict, namedtuple, deque
import copy

def build_graph(data):
    graph = {}
    for line in data.splitlines():
        a, b = line.split("-")
        for vertex in (a,b):
            if vertex not in graph:
                graph[vertex] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def bfs(graph, start, end):
    # return num paths from start to end - thanks reddit...
    NodeCls = namedtuple('NodeCls', 'val visited')
    ct = 0
    q = [NodeCls(val=start, visited=set([start]))]
    while q:
        node = q.pop(0)
        if node.val == end:
            ct += 1
            continue
        for neighbor in graph[node.val]:
            if neighbor not in node.visited:
                visited_neighbor = copy.deepcopy(node.visited)
                if neighbor.islower():
                    visited_neighbor.add(neighbor)
                q.append(NodeCls(val=neighbor, visited=visited_neighbor))
    return ct

def bfs_visit_twice(graph, start, end):
    # return num paths from start to end - thanks reddit...
    NodeCls = namedtuple('NodeCls', 'val visited vtwice')
    ct = 0
    q = [NodeCls(val=start, visited=set([start]), vtwice=False)]
    while q:
        node = q.pop(0)
        if node.val == end:
            ct += 1
            continue
        for neighbor in graph[node.val]:
            if neighbor not in node.visited:
                visited_neighbor = copy.deepcopy(node.visited)
                if neighbor.islower():
                    visited_neighbor.add(neighbor)
                q.append(NodeCls(val=neighbor, visited=visited_neighbor, vtwice=node.vtwice))
            elif not node.vtwice and neighbor not in ["start", "end"]:
                q.append(NodeCls(val=neighbor, visited=node.visited, vtwice=True))
    return ct

def part1(data):
    graph = build_graph(data)
    ans = bfs(graph, "start", "end")
    print("part1 ", ans)

def part2(data):
    graph = build_graph(data)
    ans = bfs_visit_twice(graph, "start", "end")
    print("part2 ", ans)

with open("aoc2021_day12.txt") as f:
    data = f.read()

print("day12")
part1(data)
part2(data)
        