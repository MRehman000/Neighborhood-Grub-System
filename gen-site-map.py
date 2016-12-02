import json

import pydot

edges = (
    ("home", "login"),
    ("home", "logout"),
    ("home", "dish posts"),
    ("home", "dish requests"),
    ("home", "account"),
    ("home", "suggestion"),
    ("login", "signup"),
    ("login", "home"),
    ("dish posts", "post detail"),
    ("dish posts", "orders-requests"),
    ("dish posts", "create post"),
    ("dish requests", "request detail"),
    ("dish requests", "create request"),
    ("post detail", "chef profile"),
    ("orders-requests", "cancel order"),
    ("orders-requests", "create request"),
    ("orders-requests", "edit request"),
    ("orders-requests", "cancel request"),
    ("orders-requests", "create post"),
    ("account", "orders-requests"),
    ("account", "manage posts"),
    ("manage posts", "cancel post"),
    ("manage posts", "edit post"),
    ("edit post", "manage posts"),
    ("cancel post", "manage posts"),
    ("create request", "orders-requests"),
    ("edit request", "orders-requests"),
    ("cancel request", "orders-requests"),
    ("create post", "orders-requests"),
)

def main():

    graph = pydot.Dot(graph_type="digraph")

    for u, v in edges:
        edge = pydot.Edge(u, v)
        graph.add_edge(edge)
    else:
        graph.write_png("site-map.png")

if __name__ == "__main__":
    main()
