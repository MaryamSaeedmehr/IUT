// C++ program to find out whether a
// given graph is Bipartite or not
#include <iostream>
#include <queue>

int G[200][200]; // in the Q.
using namespace std;

// This function returns true if graph
// G[V][V] is Bipartite, else false
bool isBipartite(int V, int src)
{
    // Create a color array to store colors
    // assigned to all veritces. Vertex
    // number is used as index in this array.
    // The value '-1' of colorArr[i]
    // is used to indicate that no color
    // is assigned to vertex 'i'. The value 1
    // is used to indicate first color
    // is assigned and value 0 indicates
    // second color is assigned.
    int colorArr[V];
    for (int i = 0; i < V; ++i)
        colorArr[i] = -1;

    // Assign first color to source
    colorArr[src] = 1;

    // Create a queue (FIFO) of vertex
    // numbers and enqueue source vertex
    // for BFS traversal
    queue <int> q;
    q.push(src);

    // Run while there are vertices
    // in queue (Similar to BFS)
    while (!q.empty())
    {
        // Dequeue a vertex from queue ( Refer http://goo.gl/35oz8 )
        int u = q.front();
        q.pop();

        // Return false if there is a self-loop
        if (G[u][u] == 1)
            return false;

        // Find all non-colored adjacent vertices
        for (int v = 0; v < V; ++v)
        {
            // An edge from u to v exists and
            // destination v is not colored
            if (G[u][v] && colorArr[v] == -1)
            {
                // Assign alternate color to this adjacent v of u
                colorArr[v] = 1 - colorArr[u];
                q.push(v);
            }

                // An edge from u to v exists and destination
                // v is colored with same color as u
            else if (G[u][v] && colorArr[v] == colorArr[u])
                return false;
        }
    }

    // If we reach here, then all adjacent
    // vertices can be colored with alternate color
    return true;
}

void reset()
{
    for(auto & i : G)
        for(int & j : i)
            j = 0;
}


int main()
{
    int  V, E, u, v;
    cin >> V; // V: vertices
    while(V){
        cin >> E; // E: edge
        for(int j = 0 ; j < E ; j++)
        {
            cin >> u >> v;
            G[u][v] = G[v][u] = 1;
        }
        isBipartite(V,0) ? cout << "BICOLORABLE.\n" : cout << "NOT BICOLORABLE.\n";
        reset();
        cin >> V;
    }
    return 0;
}
