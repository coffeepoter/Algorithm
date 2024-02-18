#include <iostream>
#include <string>

using namespace std;

int main() {

    while(1){
        string num;
        bool isTrue;

        cin >> num;
        if(num == "0")
            break;
        
        for(int i=0;i<num.length(); i++){
            if(num[i] == num[num.length()-i-1])
                isTrue = true;
            else{
                isTrue = false;
                break;
            }
        }

        if(isTrue)
            cout << "yes\n";
        else
            cout << "no\n";
    }
    

    return 0;
}