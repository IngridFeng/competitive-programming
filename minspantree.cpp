#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<string.h>
using namespace std;

//a structure to store v1, v2, w of an edge
struct edge{
  int v1, v2, weight;
  bool operator < (edge e1) const{
    return weight > e1.weight;
  }
};

int main(){
  int n, m;
  while (scanf("%d %d \n", &n, &m) == 2 && n){
    vector<edge> graph[n];
    //store the graph from input file;
    int v1, v2, w;
    for (int i = 0; i < m; ++i){
      scanf("%d %d %d \n", &v1, &v2, &w);
      edge e1 = {v1, v2, w}; graph[v1].push_back(e1);
      edge e2 = {v2, v1, w}; graph[v2].push_back(e2);
    }

    priority_queue<edge> pq;
    vector<edge> MSTs;//edges in MST
    long long cost = 0;
    bool visited[n];
    memset(visited, false, n);
    visited[0] = true;
    for (int i = 0; i < graph[0].size(); ++i) {pq.push(graph[0][i]);}

    while (MSTs.size() < n-1 && !pq.empty()){
        //loop through the priority queue, if only one of the vertices are in the MST for an edges, choose it
        //prim's algorithm
        edge curr_e = pq.top();
        pq.pop();

        int curr_v1 = curr_e.v1;
        int curr_v2 = curr_e.v2;

        if (visited[curr_v1] && visited[curr_v2]) continue;

        if (visited[curr_v1]) {
          for (int i = 0; i < graph[curr_v2].size(); ++i) {
            pq.push(graph[curr_v2][i]);
          }
        }//mark this vertex as visited
        if (visited[curr_v2]) {
          for (int i = 0; i < graph[curr_v1].size(); ++i) {
            pq.push(graph[curr_v1][i]);
          }
        }
        visited[curr_v2] = true; visited[curr_v1] = true;
        MSTs.push_back(curr_e);//add the current edge into MST
        cost += curr_e.weight;//increment the cost by the weight of the current edge
    }
    if (MSTs.size() == n-1) {
      pair<int, int> tmp[n-1];
      for (int i = 0; i < n - 1; ++i) {
        tmp[i].first = min(MSTs[i].v1, MSTs[i].v2);
        tmp[i].second = max(MSTs[i].v1, MSTs[i].v2);
      }//make sure the first vertex is smaller than the second in an edge
      printf("%lld \n", cost);
      sort(tmp, tmp+n-1);//sort the edges
      for (int i = 0; i < n-1; ++i) {printf("%d %d \n", tmp[i].first, tmp[i].second);}
    }
    else printf("Impossible \n");
  }
  return 0;
}
