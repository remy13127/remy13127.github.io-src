import networkx as nx
import matplotlib.pyplot as plt
from random import sample

G=nx.Graph()
for i in range(50):
	G.add_node(i)
N=list(G.nodes)
for i in range(150):
	x=sample(N,2)
	G.add_edge(x[0],x[1])

nx.draw(G)
plt.savefig("/home/remy13127/Desktop/Website/content/images/graph.png")