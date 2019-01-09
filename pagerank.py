import random
from collections import defaultdict

def printdict(dict):
	for k,v in dict.items():
		print(k,v)

class Graph:

	def __init__(self,size,df):
		self.size = size
		self.graph = defaultdict(list)
		self.rgraph = defaultdict(list)
		self.df = df
		self.pagerank = [0]*size
		self.initializePR()

	def addEdge(self,u,v):
		self.graph[int(u)].append(int(v))
		self.rgraph[int(v)].append(int(u))

	def removeEdge(self,u,v):
		self.graph[u].remove(v)

	def initializePR(self):
		self.pagerank = [random.random() for i in range(len(self.pagerank))]

	def updatePR(self):
		for i in range(len(self.pagerank)):
			sumval = 0
			for t1 in self.rgraph[i]:
				# print(t1)
				sumval = sumval + self.pagerank[t1]/len(self.graph[t1])
			self.pagerank[i] = (1 - self.df)/self.size + (self.df)*sumval

	def printPR(self):
		print(*self.pagerank)


df = float(input("Enter the damping factor : "))
size = int(input("Enter the size : "))
noe = int(input("Enter number of edges : "))
g = Graph(size,df)


for _ in range(noe):
	inputedge = input("Enter the edge : ")
	g.addEdge(inputedge.split()[0],inputedge.split()[1])

print('Graph is : ')
printdict(g.graph)
print('Reverse graph is : ')
printdict(g.rgraph)

print('Initialized PR : ')
g.printPR()

for _ in range(10000):
	g.updatePR()

print('Final PR : ')
g.printPR()

print('Average PR : ',sum(g.pagerank)/len(g.pagerank))






