#include<bits/stdc++.h>

using namespace std;

void insertion_sort (vector<int>& arr){
    int n=arr.size();
    for(int i=0;i<n;i++){
        int key=arr[i];
        int j=i-1;
        while(j>=0 && arr[j]>key){
            arr[j+1]=arr[j];
            j=j-1;
        }
        arr[j+1]=key;
    }
}
void print_array(vector<int>& arr){
    int n=arr.size();
    cout<<"Sorted array: ";
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}
void read_array(vector<int>& arr,int n){
    cout<<"Unsorted array: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<endl;
}
int main(){
    int n;
    cout<<"Number of elements: ";
    cin>>n;
    vector<int> array(n);
    read_array(array,n);
    insertion_sort(array);
    print_array(array);
}