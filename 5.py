import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    color_map = []
    node_list = list(tree.nodes())
    for node_id in node_list:
        color_map.append(colors.get(node_id, "skyblue"))
    
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=color_map)
    plt.show()


def build_heap_tree(heap, index=0):
  if index>= len(heap):
    return None
  root = Node(heap[index])

  left_index = 2 * index + 1
  right_index = 2 * index + 2

  root.left = build_heap_tree(heap, left_index)
  root.right = build_heap_tree(heap, right_index)
              

  return root

def generate_colors(num_colors):
    colors = list(mcolors.CSS4_COLORS.values())
    step = len(colors) // num_colors
    return [colors[i * step] for i in range(num_colors)]


def bfs(tree_root):
    visited_nodes = {}
    queue = [(tree_root, 0)]
    colors = generate_colors(100)
    color_index = 0

    while queue:
        node, depth = queue.pop(0)
        if node and node.id not in visited_nodes:
            color = colors[color_index]
            color_index += 1
            visited_nodes[node.id] = color
            draw_tree(tree_root, visited_nodes)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


def dfs(tree_root):
    visited_nodes = {}
    stack = [(tree_root, 0)]
    colors = generate_colors(100)
    color_index = 0

    while stack:
        node, depth = stack.pop()
        if node and node.id not in visited_nodes:
            color = colors[color_index]
            color_index += 1
            visited_nodes[node.id] = color
            draw_tree(tree_root, visited_nodes)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))


if __name__ == "__main__":

    heap_list = [1, 3, 5, 7, 9, 2]
    heapq.heapify(heap_list)
    print(heap_list)

    root = build_heap_tree(heap_list)


    print("DFS Traversal:")
    dfs(root)

    print("BFS Traversal:")
    bfs(root)