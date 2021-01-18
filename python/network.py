import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import sample

#Erds-Renyi model

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

lK = list(dict(G.degree()).values())
plt.hist(lK,bins=range(0,max(lK)+2))
plt.savefig("/home/remy13127/Documents/ghpages/content/images/erds_renyi_hist.png")
plt.close()

dC = nx.clustering(G)
lC = list(dC.values())
h = plt.hist(lC,bins=10)
plt.savefig("/home/remy13127/Documents/ghpages/content/images/erds_renyi_cluster.png")
plt.close()

x = 2.**np.arange(-12,2,0.5)
h = np.histogram(lC,bins=x,density=True)
plt.loglog(x[:-1],h[0],"ro")
plt.savefig("/home/remy13127/Documents/ghpages/content/images/erds_renyi_log.png")
plt.close()

#barabasi-albert

N=1000
m=2

G = nx.Graph()
G.add_edge(0,1)

for n in range(2,N):
	dK = dict(G.degree())
	lN = G.nodes()
	lK = np.array([dK[p] for p in lN])
	lK = lK/sum(lK)
	lN = list(dK.keys())
	a,b = np.random.choice(lN,size=2,p=lK)
	G.add_edge(n,a)
	G.add_edge(n,b)

nx.draw_spring(G,node_size=10,width=0.5)
plt.savefig("/home/remy13127/Documents/ghpages/content/images/barabasi_albert.png")


