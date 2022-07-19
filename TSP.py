def solve_tsp(G,s):
    # list to store the nodes already traversed
    visited = []
    src = s
    cost = 0

   
    while s not in visited:
     
        edges = G[s]

      
        MimWeight = -1
        minNode = -1
        visited.append(s)

        for (i, j) in enumerate(edges):

            if (MimWeight == -1) and (i not in visited):
                MimWeight = j
                minNode = i

            elif (MimWeight != -1) and (j < MimWeight) and (i not in visited):
                MimWeight = j
                minNode = i

        if minNode != -1:
            s = minNode

        
        if MimWeight != -1:
            cost += MimWeight

    
    cost += G[s][src]
    print("Output = ", cost)


G = [[0, 1, 3, 7], [1, 0, 2, 3], [3, 2, 0, 1], [7, 3, 1, 0]]


solve_tsp(G,0)