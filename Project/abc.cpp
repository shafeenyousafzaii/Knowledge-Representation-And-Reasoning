#include <iostream>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    
    int papers[50], hours[50];
    
    
    for(int i = 0; i < n; i++) {
        cin >> papers[i] >> hours[i];
    }
    
    for(int i = 0; i < n - 1; i++) {
        for(int j = 0; j < n - i - 1; j++) {
           
            bool should_swap = false;
            if(papers[j] < papers[j + 1]) {
                should_swap = true;
            }
            else if(papers[j] == papers[j + 1] && hours[j] < hours[j + 1]) {
                should_swap = true;
            }
            
            if(should_swap) {
                swap(papers[j], papers[j + 1]);
                swap(hours[j], hours[j + 1]);
            }
        }
    }
    

    k--; 
    int shared_rank = 0;
    for(int i = 0; i < n; i++) {
        if(papers[i] == papers[k] && hours[i] == hours[k]) {
            shared_rank++;
        }
    }
    
    cout << shared_rank << endl;
    return 0;
}