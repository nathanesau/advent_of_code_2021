---
title: Day 12
date: 2021-12-15
modified: 2021-12-15
category: aoc2021
tags: python
Authors: Nathan Esau
---

See problem [here](https://adventofcode.com/2021/day/12).

If this problem was hard for you, you are not alone.. I hope to clear things up in this post.

## Background

First, let's go over some general graph traversal algorithms.

```python
def bfs(graph, start, end):
    # return True if there exists path from start to end
    q = [start]
    visited = set([start])
    while q:
        node = q.pop(0)
        if node == end:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return False
```

We can generalize this to get the nmber of paths from start to end as follows:

```python
NodeCls = namedtuple('NodeCls', 'val visited')
def bfs(graph, start, end):
    # return num paths from start to end
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
                visited_neighbor.add(neighbor)
                q.append(NodeCls(val=neighbor, visited=visited_neighbor))
    return ct
```

The idea here is to store visited separately for each node. In this way, we avoid backtracking to parents of the current node.

For this example

```
start-A
start-b
A-c
A-b
b-d
A-end
b-end
```

The `bfs` function above will return 4 as number of paths. There paths are:

```
start -> A -> end
start -> b -> end
start -> A -> b -> end
start -> b -> A -> end
```

## Part 1

So, for part1 it will be similar except we only care about avoiding backtracking to parents of current node which are lower case. So we only add lower case nodes to visited.

```python
def bfs(graph, start, end):
    # return num paths from start to end
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
```

So altogether we have:

```python
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

def part1(data):
    graph = build_graph(data)
    ans = bfs(graph, "start", "end")
    print("part1 ", ans)
```

## Part 2

For part2, we also want to track the number of times that we have visited the current node.

Previously, we did the following:

```python
if neighbor not in node.visited:
    visited_neighbor = copy.deepcopy(node.visited)
    if neighbor.islower():
        visited_neighbor.add(neighbor)
    q.append(NodeCls(val=neighbor, visited=visited_neighbor))
```

But now we want to do:

```python
if neighbor not in node.visited:
    # we will go here for upper case nodes or first time for lower case nodes
    visited_neighbor = copy.deepcopy(node.visited)
    if neighbor.islower():
        visited_neighbor.add(neighbor)
    q.append(NodeCls(val=neighbor, visited=visited_neighbor, vtwice=node.vtwice))
elif not node.vtwice and neighbor not in ["start", "end"]:
    q.append(NodeCls(val=neighbor, visited=node.visited, vtwice=True))
```

For nodes we haven't visited, logic is same as before, but we now keep track of new piece of information `vtwice`.

* This will be `false` initially.
* It could become `true` for example for the case `start -> b -> A -> b` or `start -> b -> d -> b`. We want to prevent visiting the node a third time so we set the flag to `true`.

This is the only difference for part2. Here is the entire function:

```python
def bfs_visit_twice(graph, start, end):
    # return num paths from start to end
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
```

So altogether we have:

```python
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

def part2(data):
    graph = build_graph(data)
    ans = bfs_visit_twice(graph, "start", "end")
    print("part2 ", ans)
```

Hope this helps.