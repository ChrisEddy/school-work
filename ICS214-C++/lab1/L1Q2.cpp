//   author: Chris Eddy
#include <iostream>
using namespace std;

int main(){
    float subtotal;
    float gratuity;
    float total;

    cout << "Enter the subtotal and gratuity rate: ";
    cin >> subtotal >> gratuity;

    gratuity = subtotal * (gratuity * 0.01);

    total = subtotal + gratuity;

    cout << "The gratuity is $" << gratuity << " and total is $" << total << "\n";

    return 0;
}