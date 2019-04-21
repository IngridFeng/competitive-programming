#include<iostream>
#include<math.h>
using namespace std;

int getPrimeFactorSum(long long num){//a function that get the sum of all the prime factors of a number
  long long sum = 0;
  while (num % 2 == 0){//2 is a special case
    sum += 2;
    num = num / 2;
  }
  long long i = 3;
  long long root = sqrt(num);
  for (long long i = 3; i <= root; i+=2){//all other primes are odds so can increment 2 at a time
    //only need to check up until the root because there is at most one prime factor that is going to be
    //larger than the root
    //proof: suppose not, then p,q > sqrt(num) and p*q <= num, contradiction
    while (num % i == 0){
      sum += i;
      num /= i;
    }
  }

  if (num > 2){//deal with the largest prime factor
    sum += num;
  }
  return sum;
}


int main(){
  ios_base::sync_with_stdio(false);//improve performance of cin
  cin.tie(NULL);
  long long num;
  while (cin >> num && num != 4){
    int count = 0;//count number of times visit first line
    while (true){
      count++;
      long long num_new = getPrimeFactorSum(num);
      if (num_new == num) break;//is prime
      else num = num_new;
    }
    cout << num << ' ' << count << endl;
  }
  return 0;
}
