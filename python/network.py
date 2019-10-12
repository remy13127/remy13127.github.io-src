import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import sample


N = 1000
p = 0.01
E = N*(N-1)/2 #number of possible links
nE = int(p*E) #actual number of links in the network

G = nx.Graph()
lNodes = range(N)

for i in range(nE):
	a,b = sample(lNodes,2)
	while G.has_edge(a,b):
		a,b = sample(lNodes,2)
	G.add_edge(a,b)

nx.draw_spring(G,node_size=10,width=0.5)
plt.savefig("/home/remy13127/Documents/ghpages/content/images/erds_renyi.png")

plt.close()
