//   author: Chris Eddy
#include <iostream>
#include <cmath>
using namespace std;

int main(){
    float investment;
    float interestRate;
    float years;
    float value;

    cout << "Enter investment amount: ";
    cin >> investment;

    cout << "Enter annual interest rate in percentage: ";
    cin >> interestRate; 

    cout << "Enter number of years: ";
    cin >> years;

    float a = 1.0 + ((interestRate * 0.01) / 12.0);
    float b = years * 12.0;

    value = investment * powf(a, b);

    cout << "Accumalated value is: " << value << "\n";

    return 0;
}