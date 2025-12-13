from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def degree(self, v):
        return len(self.graph[v])
    def vertices(self):
        return list(self.graph.keys())
    
def is_eulerian(graph):
 odd_degree = 0
 for v in graph.vertices():
  if graph.degree(v) % 2 != 0:
   odd_degree += 1
  if odd_degree == 0:
   return "Sirkuit Euler"
  elif odd_degree == 2:
   return "Lintasan Euler"
  else:
   return "Bukan Euler"
def find_euler_path(graph):
 g = defaultdict(list)
 for u in graph.graph:
   g[u] = graph.graph[u][:]
   
 start = None
 for v in g:
     if len(g[v]) % 2 != 0:
         start = v
         break
     if start is None:
        start = next(iter(g))
        path = []
        stack = [start]
        while stack:
            u = stack[-1]
            if g[u]:
                v = g[u].pop()
                g[v].remove(u)
                stack.append(v)
            else:
                path.append(stack.pop())
        return path[::-1]

def is_safe(v, path, graph):
 if v not in graph.graph[path[-1]]:
  return False
 if v in path:
  return False
 return True

def hamilton_util(graph, path, n):
 if len(path) == n:
  return True

 for v in graph.vertices():
  if is_safe(v, path, graph):
    path.append(v)
    if hamilton_util(graph, path, n):
     return True
    path.pop()
 return False

def find_hamilton_path(graph):
 n = len(graph.vertices())
 for start in graph.vertices():
  path = [start]
 if hamilton_util(graph, path, n):
  return path
 return None
    
if __name__ == "__main__":
 g = Graph()
 edges = [
     (0, 1), (1, 2), (2, 0), (1, 3),
     (3, 4), (4, 1)
 ]
 for u, v in edges:
     g.add_edge(u, v)
 
 print("Jenis Graph:", is_eulerian(g))
 if is_eulerian(g) != "Bukan Euler":
     path = find_euler_path(g)
     print("Lintasan/Sirkuit Euler:", path)

h_path = find_hamilton_path(g)
if h_path:
        print("Lintasan Hamilton:", h_path)
else:
        print("Tidak ada Lintasan Hamilton")