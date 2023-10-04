def dfs(node):
    visited[node]=1
    print(node)
    for k in graph[node]:
        if visited[k]==0:
            dfs(k)
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
    dfs(node_name)
    count=1
    for k in visited:
        if visited[k]==0:
            count=count+1
            dfs(k)
    print("Number of connected components are :",count)
    if count>1:
        print("The graph is disconnected")