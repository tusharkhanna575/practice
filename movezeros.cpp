#include<bits/stdc++.h>
using namespace std;

void moveZeroes(vector<int>& nums) {
    int k=0;
    for(int i=0;i<nums.size();i++) {
        if(nums[i]!=0) {
            swap(nums[i],nums[k++]);
        }
    }
}

int main() {
    vector<int> nums;
    int n;
    cout<<"Enter the number of elements : ";
    cin>>n;
    cout<<"Enter the elements : ";
    for(int i=0;i<n;i++) {
        int x;
        cin>>x;
        nums.push_back(x);
    }
    cout<<"Resultant array is : ";
    for(int i: nums) {
        cout<<i<<" ";
    }
    return 0;
}