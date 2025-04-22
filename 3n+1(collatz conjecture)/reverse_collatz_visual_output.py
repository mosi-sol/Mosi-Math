# pip install ete3
from ete3 import Tree, TreeStyle

def reverse_collatz_step(n):
    """
    Find all possible predecessors of 'n' in the Collatz sequence.
    Returns a list of tuples, each containing the predecessor and the operation applied.
    """
    predecessors = []
    predecessors.append((n * 2, 'even'))
    if (n - 1) % 3 == 0:
        pred = (n - 1) // 3
        if pred > 1 and pred % 2 == 1:
            predecessors.append((pred, 'odd'))
    return predecessors

def build_ete3_tree(n, depth, parent_node=None):
    """
    Recursively builds an ete3 Tree structure representing reverse Collatz paths.
    """
    current_node_name = f"{n}"
    if parent_node is None:
        root = Tree(name=current_node_name)
        build_ete3_tree(n, depth, parent_node=root)
        return root

    if depth > 0:
        predecessors = reverse_collatz_step(n)
        for pred, operation in predecessors:
            child_node = parent_node.add_child(name=f"{pred} ({operation})")
            build_ete3_tree(pred, depth - 1, parent_node=child_node)

    return parent_node

# User input
user_number = int(input("Enter a starting number: "))
depth = int(input("Enter the depth of the reverse Collatz tree: "))

# Build the ete3 tree
collatz_tree = build_ete3_tree(user_number, depth)

# Define a TreeStyle for better visualization
ts = TreeStyle()
ts.show_leaf_name = True
ts.layout_fn = lambda node: setattr(node, "img_style", {"size": 10, "shape": "circle"}) # Basic node styling

# Render the tree to an image file
tree_filename = f"reverse_collatz_{user_number}_depth_{depth}.png"
collatz_tree.render(tree_filename, tree_style=ts)

print(f"Reverse Collatz tree saved to {tree_filename}")

# You can also display it in a GUI if you are in an interactive environment
collatz_tree.show(tree_style=ts)
