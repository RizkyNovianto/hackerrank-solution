# problem url : https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

import sys;

class Node(object):
    
    def __init__(self, name):
        self.name = name;
        self.visited = False;
        self.adjacencies_list = [];
        self.min_distance = sys.maxsize;

class Edge(object):
    
    def __init__(self, weight, start_node, target_node):     
        self.weight = weight;
        self.start_node = start_node;
        self.target_node = target_node;

class Graph(object):
    
    def __init__(self, n):      
        self.number_of_nodes = n;     
        self.nodes = [None] * n;    
        for i in range(n):  
            self.nodes[i] = Node(i);    
        self.node_queue = [];
    
    def connect(self, node_x, node_y):
        new_edge_x = Edge(6, self.nodes[node_x], self.nodes[node_y]);
        new_edge_y = Edge(6, self.nodes[node_y], self.nodes[node_x]);    
        self.nodes[node_x].adjacencies_list.append(new_edge_x);
        self.nodes[node_y].adjacencies_list.append(new_edge_y);
	
    def get_distance(self, target_node):
        if self.nodes[target_node].min_distance == sys.maxsize:           
            return -1;    
        return self.nodes[target_node].min_distance;
	
    def print_distance(self, actual_start_node):        
        for i in range(self.number_of_nodes):          
            if i == actual_start_node.name:            
                continue;        
            print(self.get_distance(i), end=" ");  
        print();
		
    def find_all_distances(self, start_node):       
        actual_start_node = self.nodes[start_node];     
        actual_start_node.min_distance = 0;  
        actual_start_node.visited = True;
        self.node_queue.append(actual_start_node);
        while self.node_queue:
            node = self.node_queue.pop(0);
            for edge in node.adjacencies_list:
                if not self.nodes[edge.target_node.name].visited:            
                    u = self.nodes[edge.start_node.name];
                    v = self.nodes[edge.target_node.name];         
                    new_distance = u.min_distance + edge.weight;
                    if new_distance < v.min_distance:   
                        v.min_distance = new_distance;                      
                        v.visited = True;                    
                        self.node_queue.append(v);
        self.print_distance(actual_start_node);

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,m = [int(value) for value in input().split()]
        graph = Graph(n) 
        for i in range(m):
            x,y = [int(x) for x in input().split()]
            graph.connect(x-1,y-1) 
        s = int(input())
        graph.find_all_distances(s-1)


    

    
