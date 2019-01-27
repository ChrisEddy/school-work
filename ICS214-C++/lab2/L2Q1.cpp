//   author: Chris Eddy
#include <iostream>
#include <string>
using namespace std;

int main(){
    int year;
    int month;
    int day;
    int result;
    string weekDay;

    cout << "Enter year: (e.g, 2012): ";
    cin >> year;

    cout << "Enter month: 1-12: ";
    cin >> month;

    cout << "Enter the day of the month: 1-31: ";
    cin >> day;

    int century = year % 100;
    int centuryYear = year / 100;

    enum class Month {
        JAN,
        FEB,
        MAR,
        APR,
        MAY,
        JUN,
        JUL,
        AUG,
        SEP,
        OCT,
        NOV,
        DEC
    };

    enum class Day {
        Sunday,
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday
    };

    if(month == static_cast<int>(Month::JAN)){
        month = 13;
        year = year - 1;
    }
    
    if(month == static_cast<int>(Month::FEB)){
        month = 14;
        year = year - 1;
    }

    result = (day + ((26 * (month + 1)) / 10) + (century) + (century / 4) + (centuryYear / 4) + (5 * century)) % 7;

    switch(result) {
      case 0:
        cout << "Day of the month is: Saturday" << endl; 
        break;
      case 1:
        cout << "Day of the month is: Sunday" << endl; 
        break;
      case 2:
        cout << "Day of the month is: Monday" << endl;
        break;
      case 3:
        cout << "Day of the month is: Tuesday" << endl;
        break;
      case 4:
        cout << "Day of the month is: Wednesday" << endl;
        break;
      case 5:
        cout << "Day of the month is: Thursday" << endl;
        break;
      case 6:
        cout << "Day of the month is: Friday" << endl;
        break;
      default:
        cout << "error" << endl;
   }

    return 0;
}