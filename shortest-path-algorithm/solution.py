#
class Graph: 
   
    def __init__(self,Nodes): 

        self.nodes = Nodes
        self.adj_list={}
        
        for node in self.nodes:
            self.adj_list[node]=[]
            
            
  
    def addEdge(self, u, v): 
        self.adj_list[u].append(v)
        # self.adj_list[v].append(u)
        
    def print_adj_list(self): 
        for node in self.nodes:
            print(node,"-->",self.adj_list[node])
            
    def lowest_commom_ancestor(self,node1,node2):
        path_node1 = self.adj_list[node1]
        print "path of node-----> {0}   {1}".format(node1,path_node1)
        path_node2 =self. adj_list[node2]
        print "path of node-----> {0}   {1}".format(node2,path_node2)

        if node1==node2:
            print "---------------------------------"            
            return int(node1)
        commom_adj=[]
        diff_adj=[]
        for i,j in zip(path_node1,path_node2):
           
            if i==j:
                
                commom_adj.append(i)
            if i!=j:
                diff_adj.append(i)
          
        if len(commom_adj)==0:
            
            return "0"
        if len(commom_adj)==1:
          
            return commom_adj[0]                      
            
        if len(commom_adj)==2:
            
            return commom_adj[1]  
                            
        if len(commom_adj)==3:
            
            return commom_adj[2]  
         
        if len(commom_adj)==4:
           
            return commom_adj[3]                      
                               
                        
        # i=0
        # while i<len(path_node1) and i<len(path_node2):
        #     # path_node1_pop = path_node1.pop() 
        #     # path_node2_pop = path_node2.pop()
          
        #     if path_node1[i] != path_node2[i]: 
        #         # l=l+1
        #         # leng.append(l)
        #         break
        #     i += 1 
        #     print path_node1[i] 
        #     if len(leng)==len(path_node1):
        #         print "root 0"
        #         return "0"    
        #     return path_node1[i] 
        
            # if path_node1_pop==path_node2_pop:
            #     print "---------------------------------"
                
            #     path_node1_pop=path_node2_pop
          
            #     return int(path_node1_pop)
            # else:
            #     pass

        
def find_common_node(data_set_path, node_a, node_b):  
    
    nodes=[] 
    all_adj=[]
    dataset = open("/home/anilkumar/Desktop/TechQWareLabsPythonTest_Ans/data.txt")
    readdata=dataset.readlines()
    
    #Divide Data Into Parts
    if node_a <= 10000 and node_b <=10000:
        for x in readdata[2:10000]:
            node = x.split()
            adj=x,y=node 
            all_adj.append(adj)
            nodes.append(node[0])
            nodes=list(set(nodes))
            
    if node_a >= 10001 and node_b <=20000:
        for x in readdata[10001:20000]:
            node = x.split()
            adj=x,y=node 
            all_adj.append(adj)
            nodes.append(node[0])
            nodes=list(set(nodes))
                
    if node_a >= 20001 and node_b <=30000:
        for x in readdata[20001:30000]:
            node = x.split()
            adj=x,y=node 
            all_adj.append(adj)
            nodes.append(node[0])
            nodes=list(set(nodes))
                
    if node_a >= 30001 and node_b <=40000:
        for x in readdata[30001:40000]:
            node = x.split()
            adj=x,y=node 
            all_adj.append(adj)
            nodes.append(node[0])
            nodes=list(set(nodes))
                
    if node_a >= 40001 and node_b <=50000:
        for x in readdata[40001:50000]:
            node = x.split()
            adj=x,y=node 
            all_adj.append(adj)
            nodes.append(node[0])
            nodes=list(set(nodes))
                
    if node_a >= 50001 and node_b <=60000:
        for x in readdata[50001:60000]:
            node = x.split()
            adj=x,y=node 
            all_adj.append(adj)
            nodes.append(node[0])
            nodes=list(set(nodes))
                
    if node_a >= 60001 and node_b <=70000:
        for x in readdata[60001:70000]:
            node = x.split()
            adj=x,y=node 
            all_adj.append(adj)
            nodes.append(node[0])
            nodes=list(set(nodes))
    if node_a >= 70001 and node_b <=80000:
        for x in readdata[70001:80000]:
            node = x.split()
            adj=x,y=node 
            all_adj.append(adj)
            nodes.append(node[0])
            nodes=list(set(nodes))
                
    if node_a >= 80001 and node_b <=90000:
        for x in readdata[80001:90000]:
            node = x.split()
            adj=x,y=node 
            all_adj.append(adj)
            nodes.append(node[0])
            nodes=list(set(nodes))
                
                    
        
    gragh = Graph(nodes) 
    for u,v in all_adj:
        gragh.addEdge(u,v)   
    a=gragh.lowest_commom_ancestor(str(node_a),str(node_b))
    print a
    if a is None:
        print "---------------------------------"
        
        return "0"
    return a
