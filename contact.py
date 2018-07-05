# problem url : https://www.hackerrank.com/challenges/ctci-contacts/problem

class Node:
    
    def __init__(self):
        self.counter = 0;
        self.nodes_ref = {};
        self.is_end_word = False;
        
class Tries:
    
    def __init__(self):        
        self.root = None;
    
    def add(self, contact):        
        self.root = self.add_node(self.root, contact, 0);
    
    def add_node(self, node, contact, index):       
        if index < len(contact): 
            c = contact[index];               
            if node is None:
                node = Node();   
            if c not in node.nodes_ref :               
                node.nodes_ref[c] = self.add_node(Node(), contact, index+1);               
            else:
                self.add_node(node.nodes_ref[c], contact, index+1);            
            node.nodes_ref[c].counter += 1;    
        return node;
    
    def find(self, contact):   
        return self.find_node(self.root, contact, 0);
    
    def find_node(self, node, contact, index):
        if index < len(contact):
            c = contact[index];           
            if (node is None) or (c not in node.nodes_ref):       
                 return 0;        
            return self.find_node(node.nodes_ref[c], contact, index+1);    
        else:        
            return node.counter;
    

if __name__ == '__main__':   
    t = Tries();
    n = int(input().strip())
    for a0 in range(n):
        op, contact = input().strip().split(' ')     
        if op == "add":    
            t.add(contact);
        elif op == "find":  
            print(t.find(contact));
        
