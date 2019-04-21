#include<iostream>
using namespace std;

int main(){
  int N, M, SC[10000], DC[10000], SI, DI, tmp1, tmp2;
  while (cin >> N >> M){
    for (int i = 0; i < N; ++i){//take all the inputs of calls
      cin >> tmp1 >> tmp2 >> SC[i] >> DC[i];
    }
    for (int j = 0; j < M; ++j){//take all the inputs of intervals
      cin >> SI >> DI;
      int count = 0;
      for (int i = 0; i < N; ++i){
        if (max(SC[i], SI) < min(DC[i]+SC[i], DI+SI)) count++;//one active phone call in the interval
      }
      cout << count << endl;
    }
  }
  return 0;
}
