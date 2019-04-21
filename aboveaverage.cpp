#include<iostream>
using namespace std;
int main(){
  int C;
  cin >> C;

  int N;//number of students per class
  while (cin >> N){
    float *students = new float[N];//store all the scores per class
    float sum = 0;
    for (int i = 0; i < N; i++){
      cin >> students[i];
      sum += students[i];//sum up
    }
    float average = sum / N;//calculate average
    float count = 0;
    for (int i = 0; i < N; i++){
      if (students[i] > average) count++;//count number of students above average
    }
    float perc = count / N * 100;//calculate the percentage
    printf("%.3f%%\n", perc);
  }

}
