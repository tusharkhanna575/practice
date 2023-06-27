#include<bits/stdc++.h>
using namespace std;

int firstUniqChar(string s) {
    int n=s.size();
    unordered_map<char,int> mp;
    for(int i=0;i<n;i++) {
        mp[s[i]]++;
    }
    for(int i=0;i<n;i++) {
        if(mp[s[i]]==1) {
            return i;
        }
    }
    return -1;
}

int main() {
    string s;
    cout<<"Enter the string : ";
    cin>>s;
    cout<<"The index of the first non-repeating character is : "<<firstUniqChar(s)<<endl;
    return 0;
}
