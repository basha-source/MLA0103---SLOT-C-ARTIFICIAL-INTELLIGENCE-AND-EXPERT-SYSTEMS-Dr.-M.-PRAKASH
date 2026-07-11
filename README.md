Algorithm BFS_DFS(Graph, Start)

Create an empty Queue Q
Create an empty Stack S
Create an empty Set Visited

// Breadth-First Search (BFS)

Enqueue(Start) into Q
Mark Start as Visited

While Q is not empty do
    Node ← Dequeue(Q)
    Print Node

    For each Neighbor of Node do
        If Neighbor is not Visited then
            Mark Neighbor as Visited
            Enqueue(Neighbor)
        End If
    End For
End While

Clear Visited

// Depth-First Search (DFS)

Push(Start) onto S

While S is not empty do
    Node ← Pop(S)

    If Node is not Visited then
        Print Node
        Mark Node as Visited

        For each Neighbor of Node in reverse order do
            If Neighbor is not Visited then
                Push(Neighbor)
            End If
        End For
    End If
End While

Stop
