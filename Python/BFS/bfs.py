def bfs(n,node):
    queue=[]
    queue.append(node)
    add_nodes=[]
    visited[node]=1
    while queue:
        k=queue.pop(0)
        add_nodes.append(k)
        for j in graph[k]:
            if visited[j]==0:
                visited[j]=1
                queue.append(j)
    return add_nodes
if __name__=="__main__":
    n=int(input("Enter number of nodes"))
    graph={}
    visited={}
    for i in range(n):
        nodes=[]
        base_node=input(("Enter base node :"))
        connected_node=input("Enter the node connected with base node in space ex a is conncected with b c d: ").split()
        graph[base_node]=connected_node
        visited[base_node]=0
    print(graph)
    node_name=input("Enter the node from where you want to start BFS: ")
    print("hello")
    print(bfs(n, node_name))
    count=1
    for k in visited:
        if visited[k]==0:
            count=count+1
            print(bfs(n,k))
    print("Number of connected components are :",count)
    if count>1:
        print("The graph is disconnected")


