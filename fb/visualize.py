import networkx as nx
import matplotlib.pyplot as plt
import fb

def build_graph(friends):
    G=nx.Graph() # Create a Graph object
    for friend1 in friends:
        for friend2 in friend1['mutual']:
            G.add_edge(friend1['name'], friend2['name'])
    return G

def draw_graph(label_flag=True, remove_isolated=True, different_size=True, iso_level=10, node_size=40):
    G=build_graph(fb.get_friends_network())
    betweenness=nx.betweenness_centrality(G)
    degree=nx.degree_centrality(G)
    clustering=nx.clustering(G)
    print nx.transitivity(G)
    # Judge whether remove the isolated point from graph
    if remove_isolated is True:
        H = nx.empty_graph()
        for SG in nx.connected_component_subgraphs(G):
            if SG.number_of_nodes() > iso_level:
                H = nx.union(SG, H)
        G = H
    # Ajust graph for better presentation
    if different_size is True:
        L = nx.degree(G)
        G.dot_size = {}
        for k, v in L.items():
            G.dot_size[k] = v
        #node_size = [betweenness[v] *1000 for v in G]
        node_size = [G.dot_size[v] * 10 for v in G]
        node_color= [float(degree[v]) for v in G]
        #edge_width = [getcommonfriends(u,v) for u,v in G.edges()]
    pos = nx.spring_layout(G, iterations=20)
    nx.draw_networkx_edges(G, pos, alpha=0.05)
    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=node_color, vmin=0.0,vmax=1.0, alpha=0.3)
    # Judge whether shows label
    if label_flag is True:
        nx.draw_networkx_labels(G, pos, font_size=6,alpha=0.1)
    #nx.draw_graphviz(G)
    plt.show()
    return G

draw_graph()
