//   author: Chris Eddy
#include <iostream>
#include <string>
using namespace std;

int main(){

    int ISBN;
    int checkSum = 0;
    int numArray [9];

    cout << "Enter the first 9 digits of an ISBN as integer: ";
    cin >> ISBN;

    string string_ISBN = to_string(ISBN);

    int y = 0;

    for(int x = 0; x < 9; x++){
        if(string_ISBN.size() < 9 && x < 9 - string_ISBN.size()){
            checkSum = checkSum + (0 * (x + 1));
        }
        else{
            int num = string_ISBN[y] - '0';
            checkSum = checkSum + (num * (y + 1));
            y++;
        }
    }

    checkSum = checkSum % 11;

    if(checkSum == 10){
        cout << "The ISBN-10 number is: " << ISBN << "X" << "\n";
    }
    else{
        cout << "The ISBN-10 number is: " << ISBN << checkSum << "\n";
    }

    return 0;
}