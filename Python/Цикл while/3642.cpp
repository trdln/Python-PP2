#include <bits\stdc++.h>
using namespace std;
int main(){
    int n; cin>>n;
    vector<int> v;
    for (int i = 0; i <= n; i++) 
        for (int j = 1; j * j <= i; j++) 
            if (j * j == i) 
                v.push_back(i); 
    for(int i=0;i<v.size();++i)cout<<v[i]<<" ";
}